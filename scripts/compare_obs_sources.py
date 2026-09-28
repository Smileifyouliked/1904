"""Research tool: compare KLGA daily highs from several sources against Polymarket results.

Not part of the trading path. It answers: which observation source reproduces the
bucket Polymarket actually paid out, day after day?

Sources per local (New York) day:
  polymarket   winning bucket of the resolved Gamma event (the ground truth we care about)
  iem_hourly   IEM ASOS METAR/SPECI rows at minute 51-59, max, rounded half up
               (our model of the resolution page)
  iem_all      IEM ASOS max over ALL METAR/SPECI rows of the day, rounded half up
  iem_daily    IEM daily summary `max_tmpf` (IEM's own computation)
  cli          NWS Daily Climate Report (CLILGA) "MAXIMUM", read from the IEM text archive
  nws_hourly   api.weather.gov observations, hourly rows (only the last ~7 days exist)
  awc_hourly   aviationweather.gov METARs, hourly rows (only the last ~15 days exist)

Usage:
  WEATHERBOT_USER_AGENT="..." .venv/bin/python scripts/compare_obs_sources.py \
      --start 2026-08-01 --end 2026-09-27 --out comparison.csv
"""

from __future__ import annotations

import argparse
import csv
import logging
import re
import sys
from collections.abc import Callable
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from weatherbot.config import IEM_ASOS_URL, IEM_STATION_ID, STATION_ID, STATION_TZ, load_settings
from weatherbot.data import markets
from weatherbot.data.errors import DataError
from weatherbot.data.http import HttpClient
from weatherbot.data.markets import fetch_event
from weatherbot.data.observations import (
    Observation,
    daily_high,
    fetch_nws_observations,
    parse_iem_asos_csv,
    t_group_celsius,
)
from weatherbot.units import c_to_f, local_day_bounds_utc, round_half_up

log = logging.getLogger("compare")

IEM_DAILY_URL = "https://mesonet.agron.iastate.edu/api/1/daily.json"
IEM_AFOS_URL = "https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py"
AWC_METAR_URL = "https://aviationweather.gov/api/data/metar"

_CLI_DATE_RE = re.compile(r"CLIMATE SUMMARY FOR (\w+ \d{1,2} \d{4})")
_CLI_MAX_RE = re.compile(r"^\s+MAXIMUM\s+(-?\d+)", re.MULTILINE)


def daterange(start: date, end: date) -> list[date]:
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]


def iem_observations(client: HttpClient, start: date, end: date) -> list[Observation]:
    first, last = start - timedelta(days=1), end + timedelta(days=2)
    text = client.get_text(
        IEM_ASOS_URL,
        params=[
            ("station", IEM_STATION_ID),
            ("data", "tmpf"),
            ("data", "metar"),
            ("year1", first.year),
            ("month1", first.month),
            ("day1", first.day),
            ("year2", last.year),
            ("month2", last.month),
            ("day2", last.day),
            ("tz", "Etc/UTC"),
            ("format", "onlycomma"),
            ("latlon", "no"),
            ("missing", "M"),
            ("trace", "T"),
            ("direct", "no"),
            ("report_type", "3"),
            ("report_type", "4"),
        ],
    )
    return parse_iem_asos_csv(text, "Etc/UTC")


def max_all_reports(observations: list[Observation], day: date) -> int | None:
    start, end = local_day_bounds_utc(day, STATION_TZ)
    temps = [
        o.temp_f
        for o in observations
        if start <= o.time_utc < end and o.is_report and o.temp_f is not None
    ]
    return round_half_up(max(temps)) if temps else None


def iem_daily(client: HttpClient, days: list[date]) -> dict[date, Decimal]:
    result: dict[date, Decimal] = {}
    for year, month in sorted({(d.year, d.month) for d in days}):
        raw = client.get_json(
            IEM_DAILY_URL,
            params={"station": IEM_STATION_ID, "network": "NY_ASOS", "year": year, "month": month},
        )
        for row in raw["data"]:
            if row.get("max_tmpf") is not None:
                result[date.fromisoformat(row["date"])] = Decimal(str(row["max_tmpf"]))
    return result


def cli_reports(client: HttpClient, limit: int) -> dict[date, int]:
    """Latest CLILGA report per climate day. Later reports (corrections) win."""
    text = client.get_text(IEM_AFOS_URL, params={"pil": "CLILGA", "limit": limit, "fmt": "text"})
    result: dict[date, int] = {}
    # Products arrive newest first; walk oldest first so later issues overwrite.
    for product in reversed(text.split("\x01")):
        day_match = _CLI_DATE_RE.search(product)
        max_match = _CLI_MAX_RE.search(product)
        if day_match and max_match:
            day = datetime.strptime(day_match.group(1).title(), "%B %d %Y").date()  # noqa: DTZ007
            result[day] = int(max_match.group(1))
    return result


def awc_observations(client: HttpClient) -> list[Observation]:
    raw = client.get_json(AWC_METAR_URL, params={"ids": STATION_ID, "format": "json", "hours": 720})
    observations = []
    for row in raw:
        celsius = t_group_celsius(row["rawOb"])
        if celsius is None and row.get("temp") is not None:
            celsius = Decimal(str(row["temp"]))
        observations.append(
            Observation(
                time_utc=datetime.fromtimestamp(int(row["obsTime"]), tz=UTC),
                temp_f=None if celsius is None else c_to_f(celsius),
                raw_metar=row["rawOb"],
                temp_from_t_group=t_group_celsius(row["rawOb"]) is not None,
                source="awc",
            )
        )
    return sorted(observations, key=lambda o: o.time_utc)


def hourly_high(observations: list[Observation], day: date) -> tuple[int | None, str]:
    try:
        high = daily_high(observations, day, STATION_TZ)
    except DataError:
        return None, ""
    return high.high_f, f"{high.hourly_reports}/{high.expected_hourly_reports}"


def safe(label: str, func: Callable[[], Any], default: Any) -> Any:
    try:
        return func()
    except DataError as exc:
        log.warning("%s unavailable: %s", label, exc)
        return default


def bucket_of(temp: int | None, buckets: list[Any]) -> str:
    if temp is None:
        return ""
    for b in buckets:
        if b.contains(temp):
            return b.label
    return "?"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=date.fromisoformat, required=True)
    parser.add_argument("--end", type=date.fromisoformat, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    client = HttpClient(load_settings())
    days = daterange(args.start, args.end)
    iem = iem_observations(client, args.start, args.end)
    daily = safe("iem daily", lambda: iem_daily(client, days), {})
    cli = safe("cli", lambda: cli_reports(client, limit=2 * len(days) + 20), {})
    awc = safe("awc", lambda: awc_observations(client), [])
    # NWS keeps about 7 days, and one page holds about one day, so fetch day by day.
    nws: list[Observation] = []
    for day in days[-8:]:
        start, end = local_day_bounds_utc(day, STATION_TZ)
        nws += safe(
            f"nws {day}",
            lambda s=start, e=end: fetch_nws_observations(client, STATION_ID, s, e),
            [],
        )
    # Research only: also read events resolved under the older Weather Underground rules.
    # The trading path keeps the strict check in weatherbot.config.
    markets.REQUIRED_RULES_PHRASES = ("LaGuardia Airport Station",)

    fields = [
        "date", "rules", "polymarket", "iem_hourly", "iem_hourly_n", "iem_all", "iem_daily", "cli",
        "nws_hourly", "nws_hourly_n", "awc_hourly", "awc_hourly_n",
        "b_iem_hourly", "b_iem_all", "b_iem_daily", "b_cli", "b_nws_hourly", "b_awc_hourly",
    ]  # fmt: skip
    rows = []
    for day in days:
        event = safe(f"polymarket {day}", lambda d=day: fetch_event(client, d), None)
        winner = event.winning_bucket() if event else None
        buckets = [m.bucket for m in event.markets] if event else []
        rules = ""
        if event:
            rules = "noaa" if "weather.gov/wrh" in event.resolution_source else "wunderground"
        row: dict[str, Any] = {
            "date": day.isoformat(),
            "rules": rules,
            "polymarket": winner.label if winner else "",
        }
        row["iem_hourly"], row["iem_hourly_n"] = hourly_high(iem, day)
        row["iem_all"] = max_all_reports(iem, day)
        row["iem_daily"] = daily.get(day, "")
        row["cli"] = cli.get(day, "")
        row["nws_hourly"], row["nws_hourly_n"] = hourly_high(nws, day)
        row["awc_hourly"], row["awc_hourly_n"] = hourly_high(awc, day)
        for key in ("iem_hourly", "iem_all", "cli", "nws_hourly", "awc_hourly"):
            value = row[key]
            row[f"b_{key}"] = bucket_of(value if value != "" else None, buckets)
        iem_d = row["iem_daily"]
        row["b_iem_daily"] = bucket_of(round_half_up(iem_d) if iem_d != "" else None, buckets)
        rows.append(row)

    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} days to {args.out}")
    for rules in ("noaa", "wunderground"):
        print(f"-- days resolved under {rules} rules")
        for key in ("iem_hourly", "iem_all", "iem_daily", "cli", "nws_hourly", "awc_hourly"):
            scored = [r for r in rows if r["rules"] == rules and r["polymarket"] and r[f"b_{key}"]]
            hits = sum(r[f"b_{key}"] == r["polymarket"] for r in scored)
            print(f"{key:12s} matches Polymarket on {hits}/{len(scored)} resolved days")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
