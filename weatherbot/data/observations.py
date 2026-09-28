"""KLGA observations and the resolution-style daily high.

How the market resolves (VERIFIED, docs/phase0_verification.md facts 1-10):
the highest "Temp" on the NOAA timeseries page with "Show Hourly Data" on, for the
local (New York) day. The page shows Math.round(temp_F).

Which reports count (VERIFIED empirically, docs/obs_source_comparison.md): the max over
ALL METAR and SPECI reports of the local day matched Polymarket's paid bucket on 177 of
177 resolved days (2026-04-01..2026-09-27). Using only the minute-51-59 reports missed 4
days, e.g. 2026-09-20, when a 21:04 EDT SPECI (72 °F) set the high and 72-73 °F won.

Sources:
- NWS API /stations/KLGA/observations: mixes 5-minute rows (whole °C, no rawMessage)
  with METAR/SPECI rows (rawMessage present). We use only METAR/SPECI rows and take
  the temperature from the METAR T-group (tenths of °C) when present.
- IEM ASOS CSV: approved cross-check source. Same METAR text, independent pipeline.
"""

from __future__ import annotations

import csv
import io
import logging
import re
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any
from zoneinfo import ZoneInfo

from weatherbot.config import (
    HOURLY_MINUTE_MAX,
    HOURLY_MINUTE_MIN,
    IEM_ASOS_URL,
    NWS_BASE_URL,
)
from weatherbot.data.errors import ParseError, StaleDataError
from weatherbot.data.http import HttpClient
from weatherbot.units import (
    c_to_f,
    local_day_bounds_utc,
    local_hours_in_day,
    require_utc,
    round_half_up,
)

log = logging.getLogger(__name__)

NWS_TEMP_UNIT = "wmoUnit:degC"
# METAR remark T-group: T + sign(0/1) + 3 digits tenths °C, optionally dew point after.
_T_GROUP_RE = re.compile(r"\sT([01])(\d{3})(?:[01]\d{3})?(?:\s|$)")
# The first page of /observations covered a whole day (325 rows) in the fixture.
# If the earliest row is later than this after `start`, the day is treated as incomplete.
_COVERAGE_TOLERANCE = timedelta(minutes=10)


@dataclass(frozen=True)
class Observation:
    time_utc: datetime
    temp_f: Decimal | None
    raw_metar: str | None  # None for NWS 5-minute rows.
    temp_from_t_group: bool
    source: str

    @property
    def is_report(self) -> bool:
        """True for METAR/SPECI rows (the rows the NOAA Hourly view can show)."""
        return bool(self.raw_metar)


@dataclass(frozen=True)
class DailyHigh:
    day: date
    high_f: int  # Rounded half up, as the NOAA page shows it.
    high_raw_f: Decimal
    observed_at_utc: datetime
    hourly_reports: int
    expected_hourly_reports: int  # Local clock hours: 23, 24 or 25 on DST days.

    @property
    def complete(self) -> bool:
        return self.hourly_reports >= self.expected_hourly_reports


def t_group_celsius(raw_metar: str) -> Decimal | None:
    """Temperature in °C from the METAR T-group, e.g. 'T01780167' -> 17.8, 'T1012' -> -1.2."""
    match = _T_GROUP_RE.search(raw_metar)
    if not match:
        return None
    sign = -1 if match.group(1) == "1" else 1
    return sign * Decimal(match.group(2)) / 10


def is_hourly_report(obs: Observation, tz_name: str) -> bool:
    """Is this the routine hourly report (minute 51-59)? Used to measure completeness.

    The minute is the same in UTC and in New York.
    """
    minute = obs.time_utc.astimezone(ZoneInfo(tz_name)).minute
    return obs.is_report and HOURLY_MINUTE_MIN <= minute <= HOURLY_MINUTE_MAX


def daily_high(observations: Iterable[Observation], day: date, tz_name: str) -> DailyHigh:
    """Resolution-style high for the local day: max over all METAR/SPECI reports.

    `hourly_reports` counts clock hours that have a minute-51-59 report, so callers can
    tell a complete day from one with gaps. Raises StaleDataError if there are no reports.
    """
    start, end = local_day_bounds_utc(day, tz_name)
    reports = [
        o
        for o in observations
        if start <= o.time_utc < end and o.temp_f is not None and o.is_report
    ]
    if not reports:
        raise StaleDataError(f"no METAR/SPECI reports with a temperature for {day}")
    # One routine report per clock hour; a SPECI inside 51-59 can share the hour.
    hours = {
        o.time_utc.replace(minute=0, second=0, microsecond=0)
        for o in reports
        if is_hourly_report(o, tz_name)
    }
    top = max(reports, key=lambda o: (o.temp_f, o.time_utc))
    top_temp = top.temp_f
    if top_temp is None:  # Unreachable: filtered above. Explicit so -O cannot remove it.
        raise StaleDataError(f"no temperature in the top report for {day}")
    return DailyHigh(
        day=day,
        high_f=round_half_up(top_temp),
        high_raw_f=top_temp,
        observed_at_utc=top.time_utc,
        hourly_reports=len(hours),
        expected_hourly_reports=local_hours_in_day(day, tz_name),
    )


# --- NWS -------------------------------------------------------------------


def _parse_nws_feature(feature: Any) -> Observation:
    if not isinstance(feature, dict) or not isinstance(feature.get("properties"), dict):
        raise ParseError("NWS observation feature has no properties")
    props = feature["properties"]
    stamp = props.get("timestamp")
    if not isinstance(stamp, str):
        raise ParseError("NWS observation has no timestamp")
    try:
        time_utc = require_utc(datetime.fromisoformat(stamp), "NWS timestamp")
    except ValueError as exc:
        raise ParseError(f"bad NWS timestamp {stamp!r}") from exc
    temperature = props.get("temperature")
    if not isinstance(temperature, dict):
        raise ParseError(f"NWS observation {stamp} has no temperature object")
    if temperature.get("unitCode") != NWS_TEMP_UNIT:
        raise ParseError(f"NWS temperature unit changed: {temperature.get('unitCode')!r}")
    raw_metar = props.get("rawMessage") or None
    celsius: Decimal | None = None
    from_t_group = False
    if raw_metar:
        celsius = t_group_celsius(raw_metar)
        from_t_group = celsius is not None
    if celsius is None and temperature.get("value") is not None:
        value = temperature["value"]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ParseError(f"NWS temperature at {stamp} is not a number: {value!r}")
        celsius = Decimal(str(value))
    return Observation(
        time_utc=time_utc,
        temp_f=None if celsius is None else c_to_f(celsius),
        raw_metar=raw_metar,
        temp_from_t_group=from_t_group,
        source="nws",
    )


def parse_nws_observations(raw: Any) -> list[Observation]:
    if not isinstance(raw, dict) or not isinstance(raw.get("features"), list):
        raise ParseError("NWS observations: expected a GeoJSON FeatureCollection")
    return sorted((_parse_nws_feature(f) for f in raw["features"]), key=lambda o: o.time_utc)


def check_coverage(observations: list[Observation], start: datetime, what: str) -> None:
    """Fail closed if the response does not reach back to `start` (pagination not followed)."""
    if not observations or observations[0].time_utc > start + _COVERAGE_TOLERANCE:
        first = observations[0].time_utc if observations else None
        raise StaleDataError(f"{what}: data starts at {first}, needed from {start}")


def fetch_nws_observations(
    client: HttpClient, station_id: str, start: datetime, end: datetime
) -> list[Observation]:
    start, end = require_utc(start, "start"), require_utc(end, "end")
    raw = client.get_json(
        f"{NWS_BASE_URL}/stations/{station_id}/observations",
        params={"start": start.isoformat(), "end": end.isoformat()},
        headers={"Accept": "application/geo+json"},
    )
    observations = parse_nws_observations(raw)
    check_coverage(observations, start, f"NWS {station_id}")
    return observations


# --- IEM -------------------------------------------------------------------


def _local_to_utc(text: str, tz_name: str) -> datetime:
    naive = datetime.strptime(text, "%Y-%m-%d %H:%M")  # noqa: DTZ007 - zone added below
    tz = ZoneInfo(tz_name)
    first, second = naive.replace(tzinfo=tz, fold=0), naive.replace(tzinfo=tz, fold=1)
    if first.utcoffset() != second.utcoffset():
        raise ParseError(f"IEM time {text!r} is ambiguous in {tz_name}; request tz=Etc/UTC")
    utc = first.astimezone(UTC)
    if utc.astimezone(tz).replace(tzinfo=None) != naive:
        raise ParseError(f"IEM time {text!r} does not exist in {tz_name}")
    return utc


def parse_iem_asos_csv(text: str, tz_name: str) -> list[Observation]:
    """Parse IEM ASOS CSV with columns station,valid,tmpf,metar. `valid` is in tz_name."""
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None or not {"valid", "tmpf", "metar"} <= set(reader.fieldnames):
        raise ParseError(f"IEM CSV columns changed: {reader.fieldnames}")
    observations = []
    for row in reader:
        raw_metar = row["metar"].strip() or None
        temp_f: Decimal | None = None
        from_t_group = False
        if raw_metar and (celsius := t_group_celsius(raw_metar)) is not None:
            temp_f, from_t_group = c_to_f(celsius), True
        elif row["tmpf"] not in ("M", ""):
            try:
                temp_f = Decimal(row["tmpf"])
            except InvalidOperation as exc:
                raise ParseError(f"IEM tmpf is not a number: {row['tmpf']!r}") from exc
        observations.append(
            Observation(
                time_utc=_local_to_utc(row["valid"], tz_name),
                temp_f=temp_f,
                raw_metar=raw_metar,
                temp_from_t_group=from_t_group,
                source="iem",
            )
        )
    return sorted(observations, key=lambda o: o.time_utc)


def fetch_iem_observations(client: HttpClient, iem_station: str, day: date) -> list[Observation]:
    """Fetch one UTC-dated range covering the local day; times requested in UTC.

    The end date is EXCLUSIVE (VERIFIED by live call: day2=21 stopped at 2026-09-20 23:51Z),
    and the New York day runs to 04:00 or 05:00 UTC of the next date, so end at day + 2.
    """
    first, last = day - timedelta(days=1), day + timedelta(days=2)
    text = client.get_text(
        IEM_ASOS_URL,
        params=[
            ("station", iem_station),
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
