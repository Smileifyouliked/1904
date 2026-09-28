"""Freshness checks. Each raises StaleDataError so the caller skips trading and logs why."""

from __future__ import annotations

from datetime import datetime, timedelta

from weatherbot.config import Settings
from weatherbot.data.errors import StaleDataError
from weatherbot.data.forecasts import ModelRunInfo, NwsForecast
from weatherbot.data.markets import OrderBook
from weatherbot.data.observations import Observation
from weatherbot.units import require_utc

# Engineering choice: allow this much clock difference between us and the data source
# before a "future" timestamp is treated as an error.
MAX_CLOCK_SKEW = timedelta(minutes=5)


def check_age(stamp: datetime, now: datetime, max_age: timedelta, what: str) -> timedelta:
    """Return the age of `stamp`; raise if it is older than max_age or in the future."""
    stamp, now = require_utc(stamp, what), require_utc(now, "now")
    age = now - stamp
    if age < -MAX_CLOCK_SKEW:
        raise StaleDataError(f"{what} is {-age} in the future; check the clock")
    if age > max_age:
        raise StaleDataError(f"{what} is {age} old (limit {max_age})")
    return age


def check_observations_fresh(
    observations: list[Observation], now: datetime, settings: Settings
) -> timedelta:
    """The latest METAR/SPECI report must be recent. 5-minute rows do not count."""
    reports = [o for o in observations if o.is_report and o.temp_f is not None]
    if not reports:
        raise StaleDataError("no METAR/SPECI reports with a temperature")
    latest = max(o.time_utc for o in reports)
    return check_age(latest, now, timedelta(minutes=settings.max_obs_age_min), "latest observation")


def check_book_fresh(book: OrderBook, now: datetime, settings: Settings) -> timedelta:
    return check_age(
        book.timestamp, now, timedelta(seconds=settings.max_book_age_s), f"book {book.token_id}"
    )


def check_run_fresh(run: ModelRunInfo, now: datetime, settings: Settings) -> timedelta:
    return check_age(
        run.init_time,
        now,
        timedelta(hours=settings.max_forecast_run_age_h),
        f"{run.model} run initialised",
    )


def check_nws_forecast_fresh(forecast: NwsForecast, now: datetime, settings: Settings) -> timedelta:
    return check_age(
        forecast.update_time,
        now,
        timedelta(hours=settings.max_forecast_run_age_h),
        "NWS forecast update",
    )
