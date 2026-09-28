from __future__ import annotations

from datetime import UTC, date, datetime
from decimal import Decimal

import pytest

from tests.conftest import load_json, load_text
from weatherbot.data.errors import ParseError, StaleDataError
from weatherbot.data.markets import parse_event
from weatherbot.data.observations import (
    Observation,
    check_coverage,
    daily_high,
    fetch_iem_observations,
    is_hourly_report,
    parse_iem_asos_csv,
    parse_nws_observations,
    t_group_celsius,
)

NY = "America/New_York"
DAY = date(2026, 9, 27)
NWS = "nws/observations_KLGA_2026-09-27.json"
IEM = "iem/asos_LGA_2026-09-27_local.csv"


def obs(hour: int, minute: int, temp: str, metar: str | None = "KLGA ...") -> Observation:
    return Observation(
        time_utc=datetime(2026, 9, 27, hour, minute, tzinfo=UTC),
        temp_f=Decimal(temp),
        raw_metar=metar,
        temp_from_t_group=False,
        source="test",
    )


@pytest.mark.parametrize(
    ("metar", "expected"),
    [
        ("KLGA 271651Z 36012KT 10SM OVC023 18/12 A2970 RMK AO2 T01780117", Decimal("17.8")),
        ("KLGA 271651Z ... RMK AO2 T10121033 $", Decimal("-1.2")),
        ("KLGA 271651Z ... RMK AO2 T0178", Decimal("17.8")),  # No dew point part.
        ("KLGA 271651Z 36012KT 10SM OVC023 18/12 A2970 RMK AO2", None),
        ("KLGA 271651Z ... RMK AO2 T01780117X", None),  # Not a clean group.
    ],
)
def test_t_group_celsius(metar: str, expected: Decimal | None) -> None:
    assert t_group_celsius(metar) == expected


def test_nws_uses_t_group_tenths() -> None:
    observations = parse_nws_observations(load_json(NWS))
    reports = [o for o in observations if o.is_report]
    assert reports, "fixture must contain METAR rows"
    assert all(o.source == "nws" for o in observations)
    assert any(o.temp_from_t_group for o in reports)


def test_nws_daily_high_for_resolved_day() -> None:
    """Resolved market 2026-09-27 paid out on 64-65°F. The NWS reports give 64."""
    high = daily_high(parse_nws_observations(load_json(NWS)), DAY, NY)
    assert high.high_f == 64
    assert high.high_raw_f == Decimal("64.04")  # 17.8 °C


def test_nws_feed_can_miss_hourly_metars_so_day_is_incomplete() -> None:
    """VERIFIED in the fixture: 6 of 24 hourly rows (e.g. 19:51Z, 20:51Z) have no rawMessage.

    The bot must not treat an NWS-only daily high as final when reports are missing.
    """
    high = daily_high(parse_nws_observations(load_json(NWS)), DAY, NY)
    assert high.expected_hourly_reports == 24
    assert high.hourly_reports == 18
    assert not high.complete


def test_iem_daily_high_is_complete_and_matches_nws() -> None:
    """Cross-check rule 5 in CLAUDE.md: two independent sources agree on the KLGA high."""
    iem = daily_high(parse_iem_asos_csv(load_text(IEM), NY), DAY, NY)
    nws = daily_high(parse_nws_observations(load_json(NWS)), DAY, NY)
    assert iem.complete
    assert iem.hourly_reports == 24
    assert iem.high_f == nws.high_f == 64


def test_daily_high_rounds_half_up() -> None:
    # Exactly 64.5 must give 65 (JS Math.round). Python round() would give 64.
    high = daily_high([obs(16, 51, "64.5"), obs(17, 51, "63.9")], DAY, NY)
    assert high.high_f == 65


def test_daily_high_counts_speci_but_not_5_minute_rows_or_other_days() -> None:
    rows = [
        obs(16, 51, "60"),
        obs(16, 40, "70"),  # SPECI outside minute 51-59: counts (see 2026-09-20 test).
        obs(17, 0, "81", metar=None),  # NWS 5-minute row: never counts.
        obs(3, 51, "82"),  # 23:51 EDT on Sep 26: previous local day.
    ]
    high = daily_high(rows, DAY, NY)
    assert high.high_f == 70
    assert high.hourly_reports == 1  # Only the 16:51 report is a routine hourly one.


def test_speci_set_the_high_on_2026_09_20() -> None:
    """Regression: a 21:04 EDT SPECI (T0222 = 71.96 °F -> 72) set the high and Polymarket
    paid 72-73 °F. The minute-51-59 reports alone peak at 71 (wrong bucket)."""
    iem = parse_iem_asos_csv(load_text("iem/asos_LGA_2026-09-20_utc.csv"), "Etc/UTC")
    high = daily_high(iem, date(2026, 9, 20), NY)
    assert high.high_f == 72
    assert high.observed_at_utc == datetime(2026, 9, 21, 1, 4, tzinfo=UTC)
    assert high.complete
    event = parse_event(
        load_json("polymarket/gamma_event_nyc_2026-09-20_resolved.json"), date(2026, 9, 20)
    )
    winner = event.winning_bucket()
    assert winner is not None
    assert winner.contains(high.high_f)
    hourly_only = [o for o in iem if is_hourly_report(o, NY)]
    assert not winner.contains(daily_high(hourly_only, date(2026, 9, 20), NY).high_f)


def test_iem_fetch_requests_through_next_local_midnight(settings) -> None:
    """IEM's end date is exclusive; the New York day ends at 04:00 UTC the next date."""
    seen = {}

    class Client:
        def get_text(self, url, params=None, headers=None):
            seen.update(dict(params))
            return "station,valid,tmpf,metar\n"

    fetch_iem_observations(Client(), "LGA", date(2026, 9, 20))  # type: ignore[arg-type]
    assert (seen["year2"], seen["month2"], seen["day2"]) == (2026, 9, 22)
    assert (seen["year1"], seen["month1"], seen["day1"]) == (2026, 9, 19)


def test_daily_high_fails_closed_without_reports() -> None:
    with pytest.raises(StaleDataError):
        daily_high([obs(17, 0, "70", metar=None)], DAY, NY)


def test_is_hourly_report_minutes() -> None:
    assert is_hourly_report(obs(16, 51, "1"), NY)
    assert is_hourly_report(obs(16, 59, "1"), NY)
    assert not is_hourly_report(obs(16, 50, "1"), NY)
    assert not is_hourly_report(obs(16, 51, "1", metar=None), NY)


def test_nws_rejects_unit_change() -> None:
    raw = load_json(NWS)
    raw["features"][0]["properties"]["temperature"]["unitCode"] = "wmoUnit:degF"
    with pytest.raises(ParseError, match="unit changed"):
        parse_nws_observations(raw)


def test_nws_rejects_non_collection() -> None:
    with pytest.raises(ParseError):
        parse_nws_observations({"type": "Feature"})


def test_check_coverage_fails_when_first_page_is_short() -> None:
    start = datetime(2026, 9, 27, 4, tzinfo=UTC)
    check_coverage([obs(4, 5, "60")], start, "x")
    with pytest.raises(StaleDataError):
        check_coverage([obs(5, 0, "60")], start, "x")
    with pytest.raises(StaleDataError):
        check_coverage([], start, "x")


def test_iem_rejects_changed_columns() -> None:
    with pytest.raises(ParseError, match="columns"):
        parse_iem_asos_csv("station,valid,temp\nLGA,2026-09-27 00:51,59\n", NY)


def test_iem_rejects_ambiguous_local_time() -> None:
    text = "station,valid,tmpf,metar\nLGA,2026-11-01 01:51,50.00,KLGA 010551Z\n"
    with pytest.raises(ParseError, match="ambiguous"):
        parse_iem_asos_csv(text, NY)


def test_iem_utc_times_and_missing_values() -> None:
    text = (
        "station,valid,tmpf,metar\n"
        "LGA,2026-11-01 05:51,50.00,KLGA 010551Z 00000KT RMK AO2 T01000050\n"
        "LGA,2026-11-01 06:51,M,\n"
    )
    rows = parse_iem_asos_csv(text, "Etc/UTC")
    assert rows[0].time_utc == datetime(2026, 11, 1, 5, 51, tzinfo=UTC)
    assert rows[0].temp_f == Decimal("50.0")
    assert rows[0].temp_from_t_group
    assert rows[1].temp_f is None
    assert not rows[1].is_report
