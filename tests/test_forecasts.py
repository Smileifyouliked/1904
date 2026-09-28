from __future__ import annotations

from datetime import UTC, date, datetime
from decimal import Decimal

import pytest

from tests.conftest import load_json, load_text
from weatherbot.data.errors import ParseError, StaleDataError
from weatherbot.data.forecasts import (
    ecmwf_enfo_url,
    member_daily_max,
    parse_ecmwf_index,
    parse_nws_forecast,
    parse_open_meteo_hourly,
    parse_open_meteo_meta,
    select_param,
)

NY = "America/New_York"
ENS = "open_meteo/ensemble_ecmwf_ifs025_KLGA_gmt.json"
NBM = "open_meteo/forecast_nbm_KLGA_gmt.json"


def test_ensemble_has_control_plus_50_members_in_utc() -> None:
    fc = parse_open_meteo_hourly(load_json(ENS), "ecmwf_ifs025")
    assert len(fc.members) == 51
    assert "control" in fc.members
    assert "member01" in fc.members
    assert "member50" in fc.members
    assert fc.times_utc[0] == datetime(2026, 9, 28, 0, tzinfo=UTC)
    assert len(fc.times_utc) == 72


def test_nbm_has_single_series() -> None:
    fc = parse_open_meteo_hourly(load_json(NBM), "ncep_nbm_conus")
    assert list(fc.members) == ["control"]


@pytest.mark.parametrize(
    "path", ["open_meteo/ensemble_ecmwf_ifs025_KLGA.json", "open_meteo/forecast_nbm_KLGA.json"]
)
def test_local_time_responses_are_rejected(path: str) -> None:
    with pytest.raises(ParseError, match="GMT"):
        parse_open_meteo_hourly(load_json(path), "m")


def test_open_meteo_error_and_unit_checks() -> None:
    with pytest.raises(ParseError, match="error"):
        parse_open_meteo_hourly({"error": True, "reason": "bad model"}, "m")
    raw = load_json(NBM)
    raw["hourly_units"]["temperature_2m"] = "°C"
    with pytest.raises(ParseError, match="°F"):
        parse_open_meteo_hourly(raw, "m")


def test_open_meteo_length_mismatch_rejected() -> None:
    raw = load_json(NBM)
    raw["hourly"]["temperature_2m"] = raw["hourly"]["temperature_2m"][:-1]
    with pytest.raises(ParseError, match="length"):
        parse_open_meteo_hourly(raw, "m")


def test_member_daily_max_over_local_day() -> None:
    fc = parse_open_meteo_hourly(load_json(ENS), "ecmwf_ifs025")
    maxima = member_daily_max(fc, date(2026, 9, 28), NY)
    assert len(maxima) == 51
    # Values read from the fixture by hand for 2026-09-28 04:00Z..2026-09-29 03:00Z.
    assert maxima["control"] == Decimal("63.7")
    assert min(maxima.values()) == Decimal("61.0")
    assert max(maxima.values()) == Decimal("65.9")


def test_member_daily_max_fails_when_day_not_covered() -> None:
    fc = parse_open_meteo_hourly(load_json(NBM), "ncep_nbm_conus")
    # Fixture starts 2026-09-28 00Z, so the local Sep 27 is only partly covered.
    with pytest.raises(StaleDataError, match="does not cover"):
        member_daily_max(fc, date(2026, 9, 27), NY)
    # Fixture ends 2026-09-30 23Z; local Sep 30 ends 2026-10-01 04Z.
    with pytest.raises(StaleDataError, match="does not cover"):
        member_daily_max(fc, date(2026, 9, 30), NY)


def test_member_daily_max_fails_on_null_value() -> None:
    raw = load_json(NBM)
    raw["hourly"]["temperature_2m"][10] = None  # 10:00Z = 06:00 EDT on Sep 28.
    fc = parse_open_meteo_hourly(raw, "ncep_nbm_conus")
    with pytest.raises(StaleDataError, match="missing values"):
        member_daily_max(fc, date(2026, 9, 28), NY)


def test_meta_parse() -> None:
    ens = parse_open_meteo_meta(load_json("open_meteo/meta_ecmwf_ifs025_ensemble.json"), "e")
    assert ens.init_time == datetime(2026, 9, 28, 0, tzinfo=UTC)
    assert ens.temporal_resolution_s == 10800  # 3-hourly: daily max can miss the peak.
    assert ens.update_interval_s == 21600
    nbm = parse_open_meteo_meta(load_json("open_meteo/meta_ncep_nbm_conus.json"), "n")
    assert nbm.temporal_resolution_s == 3600
    with pytest.raises(ParseError):
        parse_open_meteo_meta({}, "x")


def test_nws_forecast_parse() -> None:
    fc = parse_nws_forecast(load_json("nws/gridpoint_forecast_KLGA.json"))
    assert fc.update_time == datetime(2026, 9, 28, 8, 52, 9, tzinfo=UTC)
    assert len(fc.periods) == 14
    assert fc.periods[0].is_daytime
    assert fc.periods[0].temperature_f == 64


def test_nws_forecast_rejects_celsius() -> None:
    raw = load_json("nws/gridpoint_forecast_KLGA.json")
    raw["properties"]["periods"][0]["temperatureUnit"] = "C"
    with pytest.raises(ParseError, match="unit"):
        parse_nws_forecast(raw)


def test_ecmwf_index_2t_members() -> None:
    entries = parse_ecmwf_index(load_text("ecmwf/enfo_20260928_00z_24h.index"))
    t2 = select_param(entries, "2t")
    # VERIFIED: this file lists 50 perturbed members and no control for 2t.
    assert len(t2) == 50
    assert {e.type for e in t2} == {"pf"}
    assert [e.number for e in t2] == list(range(1, 51))
    assert all(e.step == 24 and e.length > 0 for e in t2)


def test_ecmwf_index_rejects_bad_line() -> None:
    with pytest.raises(ParseError, match="line 2"):
        parse_ecmwf_index('{"param":"2t","type":"cf","step":"0","_offset":0,"_length":1}\n{bad')


def test_ecmwf_url() -> None:
    url = ecmwf_enfo_url(datetime(2026, 9, 28, tzinfo=UTC), 24, "index")
    assert url == (
        "https://data.ecmwf.int/forecasts/20260928/00z/ifs/0p25/enfo/"
        "20260928000000-24h-enfo-ef.index"
    )
    with pytest.raises(ValueError, match="00/06/12/18"):
        ecmwf_enfo_url(datetime(2026, 9, 28, 3, tzinfo=UTC), 24, "index")
