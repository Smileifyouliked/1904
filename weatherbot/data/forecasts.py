"""Forecast fetchers: Open-Meteo (ECMWF ensemble, NBM), NWS gridpoint forecast, ECMWF index.

Formats VERIFIED against tests/fixtures/ (see docs/data_sources.md):
- Open-Meteo is requested with timezone=GMT, so `time` values are UTC. We refuse any
  other zone: local-time strings are ambiguous on the autumn DST night.
- The ensemble returns `temperature_2m` (control) plus `temperature_2m_member01..50`.
- Model run times come from https://<host>/data/<model>/static/meta.json.
- ECMWF IFS 0.25° ensemble output is 3-hourly (meta `temporal_resolution_seconds`
  10800); Open-Meteo interpolates it to hourly, so a daily max from it can miss the peak.

Licence: Open-Meteo's free tier is non-commercial. Owner decision 2026-09-28: use it
anyway, and fail closed if it is cut off (docs/data_sources.md).
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal
from typing import Any

from weatherbot.config import (
    ECMWF_OPEN_DATA_URL,
    NWS_BASE_URL,
    OPEN_METEO_ENSEMBLE_META_MODEL,
    OPEN_METEO_ENSEMBLE_META_URL,
    OPEN_METEO_ENSEMBLE_MODEL,
    OPEN_METEO_ENSEMBLE_URL,
    OPEN_METEO_FORECAST_META_URL,
    OPEN_METEO_FORECAST_URL,
    OPEN_METEO_NBM_MODEL,
)
from weatherbot.data.errors import ParseError, StaleDataError
from weatherbot.data.http import HttpClient
from weatherbot.units import local_day_bounds_utc, require_utc

log = logging.getLogger(__name__)

TEMP_UNIT_F = "°F"
CONTROL_KEY = "temperature_2m"
_MEMBER_KEY_RE = re.compile(r"^temperature_2m_member(\d{2})$")
_ONE_HOUR = timedelta(hours=1)


@dataclass(frozen=True)
class HourlyForecast:
    model: str
    grid_lat: float
    grid_lon: float
    times_utc: tuple[datetime, ...]
    # "control" or "member01".."member50" (NBM has only "control").
    members: dict[str, tuple[Decimal | None, ...]]


@dataclass(frozen=True)
class ModelRunInfo:
    model: str
    init_time: datetime
    available_time: datetime
    temporal_resolution_s: int
    update_interval_s: int


@dataclass(frozen=True)
class NwsPeriod:
    start: datetime
    end: datetime
    is_daytime: bool
    temperature_f: int


@dataclass(frozen=True)
class NwsForecast:
    generated_at: datetime
    update_time: datetime
    periods: tuple[NwsPeriod, ...]


@dataclass(frozen=True)
class EcmwfIndexEntry:
    param: str
    type: str  # "cf" control or "pf" perturbed member
    number: int | None
    step: int
    offset: int
    length: int


# --- Open-Meteo ------------------------------------------------------------


def _number_or_none(value: Any, where: str) -> Decimal | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ParseError(f"{where}: expected a number, got {value!r}")
    return Decimal(str(value))


def parse_open_meteo_hourly(raw: Any, model: str) -> HourlyForecast:
    if not isinstance(raw, dict):
        raise ParseError("Open-Meteo: expected an object")
    if raw.get("error"):
        raise ParseError(f"Open-Meteo error: {raw.get('reason')!r}")
    if raw.get("timezone") != "GMT" or raw.get("utc_offset_seconds") != 0:
        raise ParseError(
            f"Open-Meteo times must be GMT, got {raw.get('timezone')!r}; request timezone=GMT"
        )
    units = raw.get("hourly_units") or {}
    if units.get(CONTROL_KEY) != TEMP_UNIT_F:
        raise ParseError(f"Open-Meteo temperature unit must be °F, got {units.get(CONTROL_KEY)!r}")
    hourly = raw.get("hourly")
    if not isinstance(hourly, dict) or not isinstance(hourly.get("time"), list):
        raise ParseError("Open-Meteo: missing hourly.time")
    try:
        times = tuple(datetime.fromisoformat(t).replace(tzinfo=UTC) for t in hourly["time"])
    except (TypeError, ValueError) as exc:
        raise ParseError("Open-Meteo: bad hourly.time value") from exc
    members: dict[str, tuple[Decimal | None, ...]] = {}
    for key, values in hourly.items():
        if key == "time":
            continue
        if key == CONTROL_KEY:
            name = "control"
        elif m := _MEMBER_KEY_RE.match(key):
            name = f"member{m.group(1)}"
        else:
            continue
        if not isinstance(values, list) or len(values) != len(times):
            raise ParseError(f"Open-Meteo: {key} length does not match time")
        members[name] = tuple(_number_or_none(v, key) for v in values)
    if "control" not in members:
        raise ParseError("Open-Meteo: no temperature_2m series")
    return HourlyForecast(
        model=model,
        grid_lat=float(raw.get("latitude", "nan")),
        grid_lon=float(raw.get("longitude", "nan")),
        times_utc=times,
        members=members,
    )


def member_daily_max(forecast: HourlyForecast, day: date, tz_name: str) -> dict[str, Decimal]:
    """Max hourly temperature per member over the local day.

    Fails closed (StaleDataError) unless every local hour of the day is present and non-null.
    """
    start, end = local_day_bounds_utc(day, tz_name)
    index = {t: i for i, t in enumerate(forecast.times_utc)}
    needed = []
    moment = start
    while moment < end:
        if moment not in index:
            raise StaleDataError(f"{forecast.model}: forecast does not cover {moment} for {day}")
        needed.append(index[moment])
        moment += _ONE_HOUR
    result = {}
    for name, series in forecast.members.items():
        values = [series[i] for i in needed]
        if any(v is None for v in values):
            raise StaleDataError(f"{forecast.model} {name}: missing values on {day}")
        result[name] = max(v for v in values if v is not None)
    return result


def parse_open_meteo_meta(raw: Any, model: str) -> ModelRunInfo:
    if not isinstance(raw, dict):
        raise ParseError(f"{model} meta: expected an object")
    try:
        return ModelRunInfo(
            model=model,
            init_time=datetime.fromtimestamp(int(raw["last_run_initialisation_time"]), tz=UTC),
            available_time=datetime.fromtimestamp(int(raw["last_run_availability_time"]), tz=UTC),
            temporal_resolution_s=int(raw["temporal_resolution_seconds"]),
            update_interval_s=int(raw["update_interval_seconds"]),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise ParseError(f"{model} meta: missing or bad field") from exc


def fetch_ensemble(
    client: HttpClient, lat: float, lon: float, forecast_days: int
) -> HourlyForecast:
    raw = client.get_json(
        OPEN_METEO_ENSEMBLE_URL,
        params={
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "models": OPEN_METEO_ENSEMBLE_MODEL,
            "temperature_unit": "fahrenheit",
            "timezone": "GMT",
            "forecast_days": forecast_days,
        },
    )
    return parse_open_meteo_hourly(raw, OPEN_METEO_ENSEMBLE_MODEL)


def fetch_nbm(client: HttpClient, lat: float, lon: float, forecast_days: int) -> HourlyForecast:
    raw = client.get_json(
        OPEN_METEO_FORECAST_URL,
        params={
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "models": OPEN_METEO_NBM_MODEL,
            "temperature_unit": "fahrenheit",
            "timezone": "GMT",
            "forecast_days": forecast_days,
        },
    )
    return parse_open_meteo_hourly(raw, OPEN_METEO_NBM_MODEL)


def fetch_ensemble_run_info(client: HttpClient) -> ModelRunInfo:
    url = OPEN_METEO_ENSEMBLE_META_URL.format(model=OPEN_METEO_ENSEMBLE_META_MODEL)
    return parse_open_meteo_meta(client.get_json(url), OPEN_METEO_ENSEMBLE_META_MODEL)


def fetch_nbm_run_info(client: HttpClient) -> ModelRunInfo:
    url = OPEN_METEO_FORECAST_META_URL.format(model=OPEN_METEO_NBM_MODEL)
    return parse_open_meteo_meta(client.get_json(url), OPEN_METEO_NBM_MODEL)


# --- NWS gridpoint forecast (official deterministic forecast) --------------


def _iso(value: Any, where: str) -> datetime:
    if not isinstance(value, str):
        raise ParseError(f"{where}: expected an ISO timestamp string")
    try:
        return require_utc(datetime.fromisoformat(value), where)
    except ValueError as exc:
        raise ParseError(f"{where}: bad timestamp {value!r}") from exc


def parse_nws_forecast(raw: Any) -> NwsForecast:
    props = raw.get("properties") if isinstance(raw, dict) else None
    if not isinstance(props, dict) or not isinstance(props.get("periods"), list):
        raise ParseError("NWS forecast: missing properties.periods")
    periods = []
    for i, p in enumerate(props["periods"]):
        if p.get("temperatureUnit") != "F":
            raise ParseError(f"NWS forecast period {i}: unit {p.get('temperatureUnit')!r}")
        temp = p.get("temperature")
        if isinstance(temp, bool) or not isinstance(temp, int):
            raise ParseError(f"NWS forecast period {i}: temperature must be an integer")
        periods.append(
            NwsPeriod(
                start=_iso(p.get("startTime"), f"period {i} start"),
                end=_iso(p.get("endTime"), f"period {i} end"),
                is_daytime=bool(p.get("isDaytime")),
                temperature_f=temp,
            )
        )
    return NwsForecast(
        generated_at=_iso(props.get("generatedAt"), "generatedAt"),
        update_time=_iso(props.get("updateTime"), "updateTime"),
        periods=tuple(periods),
    )


def fetch_nws_forecast(client: HttpClient, office: str, grid_x: int, grid_y: int) -> NwsForecast:
    raw = client.get_json(
        f"{NWS_BASE_URL}/gridpoints/{office}/{grid_x},{grid_y}/forecast",
        headers={"Accept": "application/geo+json"},
    )
    return parse_nws_forecast(raw)


# --- ECMWF Open Data index -------------------------------------------------
# GRIB decoding needs ecCodes and is not part of Phase 1. The index tells us which
# byte ranges hold 2 m temperature, so we never download the 6.6 GB file.


def ecmwf_enfo_url(run: datetime, step_h: int, suffix: str) -> str:
    """URL of an IFS 0.25° ensemble file.

    Example: .../20260928/00z/ifs/0p25/enfo/20260928000000-24h-enfo-ef.index
    """
    run = require_utc(run, "run")
    if run.hour % 6 or run.minute or run.second:
        raise ValueError(f"ECMWF runs start at 00/06/12/18 UTC, got {run}")
    stamp = run.strftime("%Y%m%d%H0000")
    return (
        f"{ECMWF_OPEN_DATA_URL}/{run:%Y%m%d}/{run:%H}z/ifs/0p25/enfo/"
        f"{stamp}-{step_h}h-enfo-ef.{suffix}"
    )


def parse_ecmwf_index(text: str) -> list[EcmwfIndexEntry]:
    entries = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            number = item.get("number")
            entries.append(
                EcmwfIndexEntry(
                    param=str(item["param"]),
                    type=str(item["type"]),
                    number=None if number is None else int(number),
                    step=int(item["step"]),
                    offset=int(item["_offset"]),
                    length=int(item["_length"]),
                )
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise ParseError(f"ECMWF index line {line_no} is malformed") from exc
    return entries


def select_param(entries: list[EcmwfIndexEntry], param: str) -> list[EcmwfIndexEntry]:
    """Entries for one parameter, sorted by member number (control first)."""
    chosen = [e for e in entries if e.param == param]
    return sorted(chosen, key=lambda e: (e.type != "cf", e.number or 0))


def fetch_ecmwf_index(client: HttpClient, run: datetime, step_h: int) -> list[EcmwfIndexEntry]:
    return parse_ecmwf_index(client.get_text(ecmwf_enfo_url(run, step_h, "index")))
