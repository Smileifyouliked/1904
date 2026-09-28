"""Unit conversion, rounding and local-day helpers shared by the data layer."""

from __future__ import annotations

from datetime import UTC, date, datetime, time, timedelta
from decimal import ROUND_FLOOR, Decimal
from zoneinfo import ZoneInfo

_NINE_FIFTHS = Decimal(9) / Decimal(5)
_HALF = Decimal("0.5")


def c_to_f(celsius: Decimal) -> Decimal:
    """Convert Celsius to Fahrenheit exactly (no float error)."""
    return celsius * _NINE_FIFTHS + 32


def round_half_up(value: Decimal) -> int:
    """Round like JavaScript Math.round: floor(x + 0.5).

    The NOAA resolution page shows Math.round(temp_F) (docs/sources/noaa_wrh_timeseries_klga.md).
    Python's round() rounds .5 to even (64.5 -> 64) and must not be used here.
    Math.round(-2.5) is -2, which floor(x + 0.5) also gives.
    """
    return int((value + _HALF).to_integral_value(rounding=ROUND_FLOOR))


def local_day_bounds_utc(day: date, tz_name: str) -> tuple[datetime, datetime]:
    """Return [start, end) in UTC for midnight-to-midnight local time on `day`.

    Handles DST: the day is 23 hours long in spring and 25 hours in autumn.
    """
    tz = ZoneInfo(tz_name)
    start_local = datetime.combine(day, time(0, 0), tzinfo=tz)
    end_local = datetime.combine(day + timedelta(days=1), time(0, 0), tzinfo=tz)
    return start_local.astimezone(UTC), end_local.astimezone(UTC)


def local_hours_in_day(day: date, tz_name: str) -> int:
    """Number of clock hours in the local day (23, 24 or 25)."""
    start, end = local_day_bounds_utc(day, tz_name)
    return int((end - start).total_seconds() // 3600)


def require_utc(moment: datetime, what: str) -> datetime:
    """Reject naive datetimes; return the moment converted to UTC."""
    if moment.tzinfo is None or moment.utcoffset() is None:
        raise ValueError(f"{what} must be timezone-aware, got naive {moment!r}")
    return moment.astimezone(UTC)
