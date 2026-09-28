from __future__ import annotations

from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from weatherbot.config import Settings
from weatherbot.data.errors import StaleDataError
from weatherbot.data.forecasts import ModelRunInfo
from weatherbot.data.markets import OrderBook
from weatherbot.data.observations import Observation
from weatherbot.data.staleness import (
    check_age,
    check_book_fresh,
    check_observations_fresh,
    check_run_fresh,
)

NOW = datetime(2026, 9, 28, 12, tzinfo=UTC)


def test_check_age_limits() -> None:
    limit = timedelta(minutes=10)
    assert check_age(NOW - timedelta(minutes=10), NOW, limit, "x") == limit
    with pytest.raises(StaleDataError, match="old"):
        check_age(NOW - timedelta(minutes=10, seconds=1), NOW, limit, "x")
    check_age(NOW + timedelta(minutes=4), NOW, limit, "x")  # Within clock skew.
    with pytest.raises(StaleDataError, match="future"):
        check_age(NOW + timedelta(minutes=6), NOW, limit, "x")


def test_check_age_rejects_naive() -> None:
    with pytest.raises(ValueError):
        check_age(datetime(2026, 9, 28, 12), NOW, timedelta(1), "x")  # noqa: DTZ001


def _obs(minutes_ago: int, metar: str | None) -> Observation:
    return Observation(NOW - timedelta(minutes=minutes_ago), Decimal(60), metar, False, "t")


def test_observations_fresh_ignores_five_minute_rows(settings: Settings) -> None:
    check_observations_fresh([_obs(89, "KLGA")], NOW, settings)
    with pytest.raises(StaleDataError):
        check_observations_fresh([_obs(91, "KLGA"), _obs(1, None)], NOW, settings)
    with pytest.raises(StaleDataError, match="no METAR"):
        check_observations_fresh([_obs(1, None)], NOW, settings)


def test_book_fresh(settings: Settings) -> None:
    book = OrderBook("t", NOW - timedelta(seconds=121), (), (), Decimal("0.01"), Decimal(5))
    with pytest.raises(StaleDataError, match="book t"):
        check_book_fresh(book, NOW, settings)


def test_run_fresh(settings: Settings) -> None:
    run = ModelRunInfo("m", NOW - timedelta(hours=12), NOW, 10800, 21600)
    check_run_fresh(run, NOW, settings)
    old = ModelRunInfo("m", NOW - timedelta(hours=19), NOW, 10800, 21600)
    with pytest.raises(StaleDataError):
        check_run_fresh(old, NOW, settings)
