from __future__ import annotations

from datetime import date

from scripts.compare_obs_sources import cli_reports
from tests.conftest import load_text


class TextClient:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self, url, params=None, headers=None):
        return self.text


def test_cli_report_parses_climate_max() -> None:
    """NWS climate report for 2026-09-27 says 65 °F; the paid bucket was 64-65 (reports: 64)."""
    result = cli_reports(TextClient(load_text("iem/cli_LGA_2026-09-27.txt")), limit=1)  # type: ignore[arg-type]
    assert result == {date(2026, 9, 27): 65}
