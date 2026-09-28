"""Polymarket market data: Gamma events (buckets, prices) and CLOB order books.

Formats VERIFIED against tests/fixtures/polymarket/ (see docs/data_sources.md):
- Gamma `outcomes`, `outcomePrices`, `clobTokenIds` are STRINGS holding JSON arrays.
  Index 0 is YES, index 1 is NO. Misreading this was BUG-2.
- Gamma `bestBid`, `bestAsk` are JSON numbers.
- CLOB /book `bids` come sorted ascending and `asks` descending. We do not rely on
  either order: best bid is the max bid price, best ask is the min ask price.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import UTC, date, datetime
from decimal import Decimal, InvalidOperation
from itertools import pairwise
from typing import Any

from weatherbot.config import (
    CLOB_BASE_URL,
    EVENT_SLUG_PREFIX,
    GAMMA_BASE_URL,
    PRICE_MAX,
    PRICE_MIN,
    REQUIRED_RULES_PHRASES,
)
from weatherbot.data.errors import ParseError
from weatherbot.data.http import HttpClient

log = logging.getLogger(__name__)

EXPECTED_OUTCOMES = ["Yes", "No"]

_RANGE_RE = re.compile(r"^(?P<low>-?\d+)-(?P<high>-?\d+)°F$")
_BELOW_RE = re.compile(r"^(?P<high>-?\d+)°F or below$")
_ABOVE_RE = re.compile(r"^(?P<low>-?\d+)°F or higher$")


@dataclass(frozen=True)
class Bucket:
    """Whole-degree °F range, both ends inclusive. None means open-ended."""

    label: str
    low_f: int | None
    high_f: int | None

    def contains(self, temp_f: int) -> bool:
        if self.low_f is not None and temp_f < self.low_f:
            return False
        return not (self.high_f is not None and temp_f > self.high_f)


@dataclass(frozen=True)
class BucketMarket:
    bucket: Bucket
    market_id: str
    condition_id: str
    yes_token_id: str
    no_token_id: str
    yes_price: Decimal  # From outcomePrices[0]. Matched the CLOB midpoint when checked.
    no_price: Decimal
    best_bid: Decimal | None  # YES side, from Gamma.
    best_ask: Decimal | None
    tick_size: Decimal
    min_order_size: Decimal
    accepting_orders: bool
    closed: bool


@dataclass(frozen=True)
class MarketEvent:
    slug: str
    title: str
    observation_date: date
    end_date: datetime
    closed: bool
    neg_risk: bool
    resolution_source: str
    markets: tuple[BucketMarket, ...]  # Sorted from coldest to warmest bucket.

    def winning_bucket(self) -> Bucket | None:
        """The resolved bucket, or None if the event has not resolved to exactly one YES."""
        winners = [m for m in self.markets if m.closed and m.yes_price == 1 and m.no_price == 0]
        return winners[0].bucket if len(winners) == 1 else None


@dataclass(frozen=True)
class BookLevel:
    price: Decimal
    size: Decimal


@dataclass(frozen=True)
class OrderBook:
    token_id: str
    timestamp: datetime
    bids: tuple[BookLevel, ...]  # Best (highest) first.
    asks: tuple[BookLevel, ...]  # Best (lowest) first.
    tick_size: Decimal
    min_order_size: Decimal

    @property
    def best_bid(self) -> Decimal | None:
        return self.bids[0].price if self.bids else None

    @property
    def best_ask(self) -> Decimal | None:
        return self.asks[0].price if self.asks else None


# --- helpers ---------------------------------------------------------------


def event_slug(observation_date: date) -> str:
    """Slug for the NYC high-temperature event, e.g. ...-on-september-5-2026."""
    month = observation_date.strftime("%B").lower()
    return f"{EVENT_SLUG_PREFIX}{month}-{observation_date.day}-{observation_date.year}"


def parse_bucket_label(label: str) -> Bucket:
    text = label.strip()
    if m := _RANGE_RE.match(text):
        low, high = int(m["low"]), int(m["high"])
        if low > high:
            raise ParseError(f"bucket {label!r} has low > high")
        return Bucket(label, low, high)
    if m := _BELOW_RE.match(text):
        return Bucket(label, None, int(m["high"]))
    if m := _ABOVE_RE.match(text):
        return Bucket(label, int(m["low"]), None)
    raise ParseError(f"unknown bucket label format: {label!r}")


def parse_json_string_array(value: Any, field: str) -> list[str]:
    """Parse a Gamma field that is a string containing a JSON array of strings (BUG-2)."""
    if not isinstance(value, str):
        raise ParseError(f"{field} must be a JSON string, got {type(value).__name__}")
    try:
        items = json.loads(value)
    except json.JSONDecodeError as exc:
        raise ParseError(f"{field} is not valid JSON: {value!r}") from exc
    if not isinstance(items, list) or not all(isinstance(i, str) for i in items):
        raise ParseError(f"{field} must be a JSON array of strings, got {value!r}")
    return items


def parse_price(value: Any, field: str) -> Decimal:
    """Price from a string or number. Must be within [0, 1]."""
    if isinstance(value, bool) or not isinstance(value, (str, int, float)):
        raise ParseError(f"{field} has unexpected type {type(value).__name__}")
    try:
        price = Decimal(str(value))
    except InvalidOperation as exc:
        raise ParseError(f"{field} is not a number: {value!r}") from exc
    if not price.is_finite() or price < PRICE_MIN or price > PRICE_MAX:
        raise ParseError(f"{field} out of range [0, 1]: {value!r}")
    return price


def _optional_price(value: Any, field: str) -> Decimal | None:
    return None if value is None else parse_price(value, field)


def _parse_decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (str, int, float)):
        raise ParseError(f"{field} has unexpected type {type(value).__name__}")
    try:
        number = Decimal(str(value))
    except InvalidOperation as exc:
        raise ParseError(f"{field} is not a number: {value!r}") from exc
    if not number.is_finite() or number < 0:
        raise ParseError(f"{field} must be a finite number >= 0: {value!r}")
    return number


def _parse_iso_utc(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise ParseError(f"{field} must be an ISO timestamp string")
    try:
        moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ParseError(f"{field} is not an ISO timestamp: {value!r}") from exc
    if moment.tzinfo is None:
        raise ParseError(f"{field} has no time zone: {value!r}")
    return moment.astimezone(UTC)


def _require(obj: dict[str, Any], key: str, where: str) -> Any:
    if key not in obj:
        raise ParseError(f"{where}: missing field {key!r}")
    return obj[key]


# --- Gamma -----------------------------------------------------------------


def parse_bucket_market(raw: dict[str, Any]) -> BucketMarket:
    where = f"market {raw.get('id', '?')}"
    outcomes = parse_json_string_array(_require(raw, "outcomes", where), "outcomes")
    if outcomes != EXPECTED_OUTCOMES:
        raise ParseError(f"{where}: outcomes must be {EXPECTED_OUTCOMES}, got {outcomes}")
    prices = parse_json_string_array(_require(raw, "outcomePrices", where), "outcomePrices")
    token_ids = parse_json_string_array(_require(raw, "clobTokenIds", where), "clobTokenIds")
    if len(prices) != 2 or len(token_ids) != 2:
        raise ParseError(f"{where}: expected 2 prices and 2 token ids")
    return BucketMarket(
        bucket=parse_bucket_label(_require(raw, "groupItemTitle", where)),
        market_id=str(_require(raw, "id", where)),
        condition_id=str(_require(raw, "conditionId", where)),
        yes_token_id=token_ids[0],
        no_token_id=token_ids[1],
        yes_price=parse_price(prices[0], "outcomePrices[0]"),
        no_price=parse_price(prices[1], "outcomePrices[1]"),
        best_bid=_optional_price(raw.get("bestBid"), "bestBid"),
        best_ask=_optional_price(raw.get("bestAsk"), "bestAsk"),
        tick_size=_parse_decimal(_require(raw, "orderPriceMinTickSize", where), "tick size"),
        min_order_size=_parse_decimal(_require(raw, "orderMinSize", where), "orderMinSize"),
        accepting_orders=bool(raw.get("acceptingOrders", False)),
        closed=bool(raw.get("closed", False)),
    )


def validate_buckets(buckets: list[Bucket]) -> None:
    """Buckets must tile all temperatures once: open bottom, contiguous, open top."""
    if len(buckets) < 2:
        raise ParseError("an event needs at least 2 buckets")
    if buckets[0].low_f is not None or buckets[0].high_f is None:
        raise ParseError(f"first bucket must be open-ended below: {buckets[0].label!r}")
    if buckets[-1].high_f is not None or buckets[-1].low_f is None:
        raise ParseError(f"last bucket must be open-ended above: {buckets[-1].label!r}")
    for prev, cur in pairwise(buckets):
        if prev.high_f is None or cur.low_f is None or cur.low_f != prev.high_f + 1:
            raise ParseError(f"buckets {prev.label!r} and {cur.label!r} are not contiguous")


def _bucket_sort_key(market: BucketMarket) -> float:
    b = market.bucket
    return float("-inf") if b.low_f is None else float(b.low_f)


def parse_event(raw: dict[str, Any], observation_date: date) -> MarketEvent:
    where = f"event {raw.get('slug', '?')}"
    slug = _require(raw, "slug", where)
    if slug != event_slug(observation_date):
        raise ParseError(f"{where}: slug does not match date {observation_date}")
    description = _require(raw, "description", where)
    missing = [p for p in REQUIRED_RULES_PHRASES if p not in description]
    if missing:
        raise ParseError(f"{where}: market rules changed, missing {missing}")
    raw_markets = _require(raw, "markets", where)
    if not isinstance(raw_markets, list):
        raise ParseError(f"{where}: markets must be a list")
    markets = sorted((parse_bucket_market(m) for m in raw_markets), key=_bucket_sort_key)
    validate_buckets([m.bucket for m in markets])
    return MarketEvent(
        slug=slug,
        title=str(_require(raw, "title", where)),
        observation_date=observation_date,
        end_date=_parse_iso_utc(_require(raw, "endDate", where), "endDate"),
        closed=bool(raw.get("closed", False)),
        neg_risk=bool(raw.get("negRisk", False)),
        resolution_source=str(raw.get("resolutionSource", "")),
        markets=tuple(markets),
    )


def fetch_event(client: HttpClient, observation_date: date) -> MarketEvent:
    slug = event_slug(observation_date)
    raw = client.get_json(f"{GAMMA_BASE_URL}/events/slug/{slug}")
    if not isinstance(raw, dict):
        raise ParseError(f"Gamma event {slug}: expected an object")
    return parse_event(raw, observation_date)


# --- CLOB ------------------------------------------------------------------


def _parse_levels(raw: Any, field: str) -> list[BookLevel]:
    if not isinstance(raw, list):
        raise ParseError(f"book {field} must be a list")
    levels = []
    for i, level in enumerate(raw):
        if not isinstance(level, dict) or not isinstance(level.get("price"), str):
            raise ParseError(f"book {field}[{i}] must have a string price")
        if not isinstance(level.get("size"), str):
            raise ParseError(f"book {field}[{i}] must have a string size")
        levels.append(
            BookLevel(
                price=parse_price(level["price"], f"{field}[{i}].price"),
                size=_parse_decimal(level["size"], f"{field}[{i}].size"),
            )
        )
    return levels


def parse_book(raw: dict[str, Any], token_id: str) -> OrderBook:
    where = f"book {token_id}"
    asset_id = _require(raw, "asset_id", where)
    if asset_id != token_id:
        raise ParseError(f"{where}: response is for asset {asset_id}")
    stamp = _require(raw, "timestamp", where)
    if not isinstance(stamp, str) or not stamp.isdigit():
        raise ParseError(f"{where}: timestamp must be a string of milliseconds")
    bids = sorted(_parse_levels(_require(raw, "bids", where), "bids"), key=lambda lv: -lv.price)
    asks = sorted(_parse_levels(_require(raw, "asks", where), "asks"), key=lambda lv: lv.price)
    if bids and asks and bids[0].price >= asks[0].price:
        raise ParseError(f"{where}: crossed book (bid {bids[0].price} >= ask {asks[0].price})")
    return OrderBook(
        token_id=token_id,
        timestamp=datetime.fromtimestamp(int(stamp) / 1000, tz=UTC),
        bids=tuple(bids),
        asks=tuple(asks),
        tick_size=_parse_decimal(_require(raw, "tick_size", where), "tick_size"),
        min_order_size=_parse_decimal(_require(raw, "min_order_size", where), "min_order_size"),
    )


def fetch_book(client: HttpClient, token_id: str) -> OrderBook:
    raw = client.get_json(f"{CLOB_BASE_URL}/book", params={"token_id": token_id})
    if not isinstance(raw, dict):
        raise ParseError(f"book {token_id}: expected an object")
    return parse_book(raw, token_id)
