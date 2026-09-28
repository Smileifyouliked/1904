from __future__ import annotations

from typing import Any

import pytest
import requests

from weatherbot.config import Settings
from weatherbot.data.errors import FetchError
from weatherbot.data.http import HttpClient


class FakeResponse:
    def __init__(self, status: int, body: Any = None, text: str = "") -> None:
        self.status_code = status
        self._body = body
        self.text = text

    def json(self) -> Any:
        if isinstance(self._body, Exception):
            raise self._body
        return self._body


class FakeSession:
    """Returns queued responses (or raises queued exceptions) and records each call."""

    def __init__(self, *outcomes: Any) -> None:
        self.outcomes = list(outcomes)
        self.calls: list[dict[str, Any]] = []

    def get(self, url: str, **kwargs: Any) -> FakeResponse:
        self.calls.append({"url": url, **kwargs})
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def make(settings: Settings, *outcomes: Any) -> tuple[HttpClient, FakeSession, list[float]]:
    session = FakeSession(*outcomes)
    sleeps: list[float] = []
    return HttpClient(settings, session=session, sleep=sleeps.append), session, sleeps  # type: ignore[arg-type]


def test_sends_user_agent_and_timeout(settings: Settings) -> None:
    client, session, _ = make(settings, FakeResponse(200, {"ok": 1}))
    assert client.get_json("https://x", headers={"Accept": "application/geo+json"}) == {"ok": 1}
    call = session.calls[0]
    assert call["headers"]["User-Agent"] == settings.user_agent
    assert call["headers"]["Accept"] == "application/geo+json"
    assert call["timeout"] == settings.http_timeout_s


def test_retries_5xx_and_429_with_backoff(settings: Settings) -> None:
    client, session, sleeps = make(
        settings, FakeResponse(503), FakeResponse(429), FakeResponse(200, text="hi")
    )
    assert client.get_text("https://x") == "hi"
    assert len(session.calls) == 3
    assert sleeps == [2.0, 4.0]


def test_retries_network_errors_then_gives_up(settings: Settings) -> None:
    err = requests.ConnectionError("down")
    client, session, sleeps = make(settings, err, err, err)
    with pytest.raises(FetchError, match="after 3 attempts"):
        client.get("https://x")
    assert len(session.calls) == 3
    assert sleeps == [2.0, 4.0]  # No sleep after the last attempt.


def test_client_error_is_not_retried(settings: Settings) -> None:
    client, session, sleeps = make(settings, FakeResponse(404))
    with pytest.raises(FetchError, match="HTTP 404"):
        client.get("https://x")
    assert len(session.calls) == 1
    assert sleeps == []


def test_invalid_json_is_a_fetch_error(settings: Settings) -> None:
    client, _, _ = make(settings, FakeResponse(200, ValueError("bad json")))
    with pytest.raises(FetchError, match="invalid JSON"):
        client.get_json("https://x")
