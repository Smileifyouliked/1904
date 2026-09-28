from __future__ import annotations

import copy
from datetime import UTC, date, datetime
from decimal import Decimal
from typing import Any

import pytest

from tests.conftest import load_json
from weatherbot.data.errors import ParseError
from weatherbot.data.markets import (
    Bucket,
    event_slug,
    parse_book,
    parse_bucket_label,
    parse_bucket_market,
    parse_event,
    parse_json_string_array,
    parse_price,
    validate_buckets,
)

OPEN = "polymarket/gamma_event_nyc_2026-09-29_open.json"
RESOLVED = "polymarket/gamma_event_nyc_2026-09-27_resolved.json"
BOOK = "polymarket/clob_book_nyc_2026-09-29_70-71F_yes.json"
TOKEN_70_71_YES = "78179706910626809009796901742685091838883513128682988751629628697009519289343"


def open_event() -> dict[str, Any]:
    return load_json(OPEN)


# --- slug ------------------------------------------------------------------


def test_event_slug_has_no_zero_padding() -> None:
    assert event_slug(date(2026, 9, 5)) == "highest-temperature-in-nyc-on-september-5-2026"
    assert event_slug(date(2026, 9, 29)) == "highest-temperature-in-nyc-on-september-29-2026"


# --- bucket labels ---------------------------------------------------------


@pytest.mark.parametrize(
    ("label", "low", "high"),
    [
        ("64-65°F", 64, 65),
        ("63°F or below", None, 63),
        ("82°F or higher", 82, None),
        ("-2--1°F", -2, -1),
    ],
)
def test_parse_bucket_label(label: str, low: int | None, high: int | None) -> None:
    b = parse_bucket_label(label)
    assert (b.low_f, b.high_f) == (low, high)


@pytest.mark.parametrize("label", ["64-65", "64 to 65°F", "65-64°F", "64-65°C", ""])
def test_parse_bucket_label_rejects_unknown(label: str) -> None:
    with pytest.raises(ParseError):
        parse_bucket_label(label)


def test_bucket_contains_is_inclusive_at_both_ends() -> None:
    b = Bucket("64-65°F", 64, 65)
    assert [b.contains(t) for t in (63, 64, 65, 66)] == [False, True, True, False]
    assert Bucket("63°F or below", None, 63).contains(-40)
    assert Bucket("82°F or higher", 82, None).contains(120)


def test_validate_buckets_rejects_gap_and_missing_open_ends() -> None:
    lo, mid, hi = Bucket("a", None, 63), Bucket("b", 64, 65), Bucket("c", 66, None)
    validate_buckets([lo, mid, hi])
    with pytest.raises(ParseError, match="contiguous"):
        validate_buckets([lo, Bucket("b", 65, 66), Bucket("c", 67, None)])
    with pytest.raises(ParseError, match="open-ended below"):
        validate_buckets([mid, hi])
    with pytest.raises(ParseError, match="open-ended above"):
        validate_buckets([lo, mid])


# --- BUG-2 regression: Gamma JSON-in-string fields --------------------------


def test_bug2_outcome_prices_is_a_string_holding_a_json_array() -> None:
    """BUG-2 regression. Never remove or weaken this test (CLAUDE.md)."""
    raw = next(m for m in open_event()["markets"] if m["groupItemTitle"] == "70-71°F")
    # The real API sends a STRING, not a list. Iterating it char by char was the old bug.
    assert isinstance(raw["outcomePrices"], str)
    market = parse_bucket_market(raw)
    # Index 0 is YES, index 1 is NO.
    assert market.yes_price == Decimal("0.58")
    assert market.no_price == Decimal("0.42")
    assert market.yes_token_id == TOKEN_70_71_YES
    assert market.best_bid == Decimal("0.57")
    assert market.best_ask == Decimal("0.59")
    assert market.best_bid <= market.yes_price <= market.best_ask


def test_bug2_rejects_an_already_decoded_list() -> None:
    """BUG-2 regression: if Gamma changes the type, fail closed instead of guessing."""
    raw = copy.deepcopy(open_event()["markets"][0])
    raw["outcomePrices"] = ["0.005", "0.995"]
    with pytest.raises(ParseError, match="must be a JSON string"):
        parse_bucket_market(raw)


def test_bug2_rejects_swapped_outcomes() -> None:
    """BUG-2 regression: if outcomes are not ["Yes", "No"], index 0 is not YES."""
    raw = copy.deepcopy(open_event()["markets"][0])
    raw["outcomes"] = '["No", "Yes"]'
    with pytest.raises(ParseError, match="outcomes must be"):
        parse_bucket_market(raw)


@pytest.mark.parametrize("value", [5, '{"a": 1}', "[1, 2]", "not json"])
def test_parse_json_string_array_is_strict(value: Any) -> None:
    with pytest.raises(ParseError):
        parse_json_string_array(value, "f")


@pytest.mark.parametrize("value", ["-0.01", "1.01", "nan", "abc", True, None])
def test_parse_price_rejects_bad_values(value: Any) -> None:
    with pytest.raises(ParseError):
        parse_price(value, "p")


def test_parse_price_accepts_bounds_and_floats() -> None:
    assert parse_price("0", "p") == 0
    assert parse_price("1", "p") == 1
    assert parse_price(0.57, "p") == Decimal("0.57")  # str() avoids float noise.


# --- whole events ----------------------------------------------------------


def test_parse_open_event() -> None:
    event = parse_event(open_event(), date(2026, 9, 29))
    labels = [m.bucket.label for m in event.markets]
    assert labels[0] == "63°F or below"
    assert labels[-1] == "82°F or higher"
    assert len(event.markets) == 11
    assert event.neg_risk
    assert event.end_date == datetime(2026, 9, 29, 12, tzinfo=UTC)
    assert event.winning_bucket() is None
    # YES prices of a live event sum near 1, not exactly 1 (VERIFIED: 1.054).
    total = sum(m.yes_price for m in event.markets)
    assert Decimal("0.9") < total < Decimal("1.2")


def test_parse_resolved_event_finds_winner() -> None:
    event = parse_event(load_json(RESOLVED), date(2026, 9, 27))
    winner = event.winning_bucket()
    assert winner is not None
    assert winner.label == "64-65°F"
    assert event.markets[0].bucket.label == "55°F or below"
    assert event.markets[-1].bucket.label == "74°F or higher"


def test_parse_event_sorts_buckets_whatever_the_api_order() -> None:
    raw = open_event()
    raw["markets"] = list(reversed(raw["markets"]))
    event = parse_event(raw, date(2026, 9, 29))
    assert event.markets[0].bucket.label == "63°F or below"


def test_parse_event_rejects_wrong_date() -> None:
    with pytest.raises(ParseError, match="slug"):
        parse_event(open_event(), date(2026, 9, 28))


def test_parse_event_rejects_changed_rules() -> None:
    raw = open_event()
    raw["description"] = raw["description"].replace("LaGuardia Airport Station", "JFK")
    with pytest.raises(ParseError, match="rules changed"):
        parse_event(raw, date(2026, 9, 29))


def test_parse_event_rejects_missing_bucket() -> None:
    raw = open_event()
    raw["markets"] = [m for m in raw["markets"] if m["groupItemTitle"] != "70-71°F"]
    with pytest.raises(ParseError, match="contiguous"):
        parse_event(raw, date(2026, 9, 29))


# --- CLOB order book -------------------------------------------------------


def test_parse_book_best_prices() -> None:
    book = parse_book(load_json(BOOK), TOKEN_70_71_YES)
    assert book.best_bid == Decimal("0.57")
    assert book.best_ask == Decimal("0.59")
    assert book.tick_size == Decimal("0.01")
    assert book.min_order_size == Decimal("5")
    assert book.timestamp == datetime.fromtimestamp(1790596358391 / 1000, tz=UTC)


def test_parse_book_does_not_depend_on_level_order() -> None:
    raw = load_json(BOOK)
    raw["bids"], raw["asks"] = list(reversed(raw["bids"])), list(reversed(raw["asks"]))
    book = parse_book(raw, TOKEN_70_71_YES)
    assert (book.best_bid, book.best_ask) == (Decimal("0.57"), Decimal("0.59"))


def test_parse_book_rejects_crossed_book() -> None:
    raw = load_json(BOOK)
    raw["bids"].append({"price": "0.60", "size": "1"})
    with pytest.raises(ParseError, match="crossed"):
        parse_book(raw, TOKEN_70_71_YES)


def test_parse_book_rejects_other_token() -> None:
    with pytest.raises(ParseError, match="response is for asset"):
        parse_book(load_json(BOOK), "123")


def test_parse_book_rejects_numeric_price() -> None:
    raw = load_json(BOOK)
    raw["asks"][0]["price"] = 0.99
    with pytest.raises(ParseError, match="string price"):
        parse_book(raw, TOKEN_70_71_YES)
