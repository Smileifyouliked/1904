"""Shared test helpers: load saved real API responses from tests/fixtures/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from weatherbot.config import Settings

FIXTURES = Path(__file__).parent / "fixtures"


def load_json(relative: str) -> Any:
    return json.loads((FIXTURES / relative).read_text(encoding="utf-8"))


def load_text(relative: str) -> str:
    return (FIXTURES / relative).read_text(encoding="utf-8")


@pytest.fixture
def settings() -> Settings:
    return Settings(user_agent="weatherbot-tests (test@example.com)")
