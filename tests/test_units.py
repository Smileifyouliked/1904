from __future__ import annotations

from datetime import UTC, date, datetime, timedelta, timezone
from decimal import Decimal

import pytest

from weatherbot.units import (
    c_to_f,
    local_day_bounds_utc,
    local_hours_in_day,
    require_utc,
    round_half_up,
)

NY = "America/New_York"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("64.5", 65),  # Python round() would give 64: the reason this helper exists.
        ("65.5", 66),
        ("64.49", 64),
        ("64.04", 64),
        ("0.5", 1),
        ("-0.5", 0),  # JS Math.round(-0.5) is -0.
        ("-2.5", -2),  # JS Math.round(-2.5) is -2.
        ("-2.51", -3),
        ("64", 64),
    ],
)
def test_round_half_up_matches_js_math_round(value: str, expected: int) -> None:
    assert round_half_up(Decimal(value)) == expected


def test_c_to_f_is_exact() -> None:
    assert c_to_f(Decimal("17.8")) == Decimal("64.04")
    assert c_to_f(Decimal("18.1")) == Decimal("64.58")  # Rounds to 65, not 64.
    assert c_to_f(Decimal("-40")) == Decimal("-40")
    assert c_to_f(Decimal("0")) == Decimal("32")


def test_local_day_bounds_normal_day() -> None:
    start, end = local_day_bounds_utc(date(2026, 9, 27), NY)
    assert start == datetime(2026, 9, 27, 4, tzinfo=UTC)  # EDT = UTC-4
    assert end == datetime(2026, 9, 28, 4, tzinfo=UTC)


@pytest.mark.parametrize(
    ("day", "hours"),
    [
        (date(2026, 3, 8), 23),  # Spring forward.
        (date(2026, 11, 1), 25),  # Fall back.
        (date(2026, 9, 27), 24),
        (date(2026, 1, 15), 24),
    ],
)
def test_local_hours_in_day_handles_dst(day: date, hours: int) -> None:
    assert local_hours_in_day(day, NY) == hours


def test_local_day_bounds_winter_uses_est() -> None:
    start, _ = local_day_bounds_utc(date(2026, 1, 15), NY)
    assert start == datetime(2026, 1, 15, 5, tzinfo=UTC)


def test_require_utc_rejects_naive_and_converts() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        require_utc(datetime(2026, 9, 27, 12), "x")  # noqa: DTZ001
    eastern = timezone(timedelta(hours=-4))
    assert require_utc(datetime(2026, 9, 27, 8, tzinfo=eastern), "x") == datetime(
        2026, 9, 27, 12, tzinfo=UTC
    )
