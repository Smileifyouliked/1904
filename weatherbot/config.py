"""All constants and settings. Values come from the environment where noted.

Every default says where it came from. Facts marked VERIFIED are recorded in
docs/phase0_verification.md or docs/data_sources.md.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal

# --- Station and market facts (VERIFIED, Phase 0) ---------------------------

# KLGA coordinates from GET https://api.weather.gov/stations/KLGA
# (tests/fixtures/nws/station_KLGA.json).
STATION_ID = "KLGA"
STATION_LAT = 40.7792
STATION_LON = -73.8800
# The resolution page requests data with obtimezone=local; KLGA local time is New York.
STATION_TZ = "America/New_York"
# IEM uses the 3-letter FAA id for KLGA (tests/fixtures/iem/asos_LGA_2026-09-27_local.csv).
IEM_STATION_ID = "LGA"

# The "Hourly Data" view keeps NWS/FAA reports whose minute is 51-59
# (docs/sources/noaa_wrh_timeseries_klga.md).
HOURLY_MINUTE_MIN = 51
HOURLY_MINUTE_MAX = 59

# Polymarket event slug prefix, checked live: "...-on-september-5-2026" exists,
# "...-on-september-05-2026" is 404 (no zero padding on the day).
EVENT_SLUG_PREFIX = "highest-temperature-in-nyc-on-"

# Text that must appear in the market rules. If Polymarket changes the station
# or the source, parsing fails closed instead of trading on the wrong rules.
REQUIRED_RULES_PHRASES = ("LaGuardia Airport Station", "weather.gov/wrh/timeseries?site=klga")

# Probabilities and prices must lie in [0, 1].
PRICE_MIN = Decimal("0")
PRICE_MAX = Decimal("1")

# --- Endpoints (VERIFIED by live calls on 2026-09-28) -----------------------

GAMMA_BASE_URL = "https://gamma-api.polymarket.com"
CLOB_BASE_URL = "https://clob.polymarket.com"
NWS_BASE_URL = "https://api.weather.gov"
IEM_ASOS_URL = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
OPEN_METEO_ENSEMBLE_URL = "https://ensemble-api.open-meteo.com/v1/ensemble"
OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
# Model metadata: https://<host>/data/<model>/static/meta.json (URL pattern confirmed by
# live call; fields documented in open-meteo-docs verbatim/model-updates.md).
OPEN_METEO_ENSEMBLE_META_URL = "https://ensemble-api.open-meteo.com/data/{model}/static/meta.json"
OPEN_METEO_FORECAST_META_URL = "https://api.open-meteo.com/data/{model}/static/meta.json"
ECMWF_OPEN_DATA_URL = "https://data.ecmwf.int/forecasts"

# Open-Meteo model names (a wrong name returns {"error": true}; these returned data).
OPEN_METEO_ENSEMBLE_MODEL = "ecmwf_ifs025"
OPEN_METEO_ENSEMBLE_META_MODEL = "ecmwf_ifs025_ensemble"
OPEN_METEO_NBM_MODEL = "ncep_nbm_conus"

# --- Tunable settings --------------------------------------------------------

DEFAULT_HTTP_TIMEOUT_S = 20.0  # Engineering choice: long enough for a 1.5 MB NWS page.
DEFAULT_HTTP_RETRIES = 3  # Attempts per request, including the first.
# NWS: after a rate-limit error, retry "typically within 5 seconds" (NWS API docs).
# Backoff of 2 s then 4 s covers that.
DEFAULT_HTTP_BACKOFF_S = 2.0
# Hourly METARs arrive once an hour, and NWS says observations "may be delayed up to
# 20 minutes" (NWS API docs). 60 + 20 + 10 minutes of margin.
DEFAULT_MAX_OBS_AGE_MIN = 90
# Engineering choice: an order book older than 2 minutes is not trusted for pricing.
DEFAULT_MAX_BOOK_AGE_S = 120
# ECMWF ensemble updates every 6 hours (Open-Meteo ensemble docs). 18 h allows two
# missed runs plus availability delay before the forecast is treated as stale.
DEFAULT_MAX_FORECAST_RUN_AGE_H = 18


class ConfigError(ValueError):
    """A required setting is missing or invalid."""


@dataclass(frozen=True)
class Settings:
    user_agent: str
    http_timeout_s: float = DEFAULT_HTTP_TIMEOUT_S
    http_retries: int = DEFAULT_HTTP_RETRIES
    http_backoff_s: float = DEFAULT_HTTP_BACKOFF_S
    max_obs_age_min: int = DEFAULT_MAX_OBS_AGE_MIN
    max_book_age_s: int = DEFAULT_MAX_BOOK_AGE_S
    max_forecast_run_age_h: int = DEFAULT_MAX_FORECAST_RUN_AGE_H


def _positive_number(env: Mapping[str, str], name: str, default: float, kind: type) -> float:
    raw = env.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        value = kind(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be a {kind.__name__}, got {raw!r}") from exc
    if value <= 0:
        raise ConfigError(f"{name} must be > 0, got {raw!r}")
    return value


def load_settings(env: Mapping[str, str] | None = None) -> Settings:
    """Read settings from the environment. Fails if the NWS User-Agent is missing."""
    env = os.environ if env is None else env
    user_agent = env.get("WEATHERBOT_USER_AGENT", "").strip()
    if not user_agent:
        raise ConfigError(
            "WEATHERBOT_USER_AGENT is required (NWS requires a User-Agent that identifies "
            "the app). See .env.example."
        )
    return Settings(
        user_agent=user_agent,
        http_timeout_s=_positive_number(
            env, "WEATHERBOT_HTTP_TIMEOUT_S", DEFAULT_HTTP_TIMEOUT_S, float
        ),
        http_retries=int(
            _positive_number(env, "WEATHERBOT_HTTP_RETRIES", DEFAULT_HTTP_RETRIES, int)
        ),
        http_backoff_s=_positive_number(
            env, "WEATHERBOT_HTTP_BACKOFF_S", DEFAULT_HTTP_BACKOFF_S, float
        ),
        max_obs_age_min=int(
            _positive_number(env, "WEATHERBOT_MAX_OBS_AGE_MIN", DEFAULT_MAX_OBS_AGE_MIN, int)
        ),
        max_book_age_s=int(
            _positive_number(env, "WEATHERBOT_MAX_BOOK_AGE_S", DEFAULT_MAX_BOOK_AGE_S, int)
        ),
        max_forecast_run_age_h=int(
            _positive_number(
                env, "WEATHERBOT_MAX_FORECAST_RUN_AGE_H", DEFAULT_MAX_FORECAST_RUN_AGE_H, int
            )
        ),
    )
