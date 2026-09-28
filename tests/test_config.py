from __future__ import annotations

import pytest

from weatherbot.config import DEFAULT_HTTP_RETRIES, ConfigError, load_settings

UA = {"WEATHERBOT_USER_AGENT": "weatherbot (me@example.com)"}


def test_user_agent_is_required() -> None:
    with pytest.raises(ConfigError, match="WEATHERBOT_USER_AGENT"):
        load_settings({})
    with pytest.raises(ConfigError):
        load_settings({"WEATHERBOT_USER_AGENT": "   "})


def test_defaults_apply() -> None:
    s = load_settings(UA)
    assert s.user_agent == "weatherbot (me@example.com)"
    assert s.http_retries == DEFAULT_HTTP_RETRIES


def test_overrides_are_read() -> None:
    s = load_settings({**UA, "WEATHERBOT_HTTP_RETRIES": "5", "WEATHERBOT_MAX_BOOK_AGE_S": "30"})
    assert s.http_retries == 5
    assert s.max_book_age_s == 30


@pytest.mark.parametrize("bad", ["0", "-1", "abc", "2.5"])
def test_bad_numbers_fail(bad: str) -> None:
    with pytest.raises(ConfigError):
        load_settings({**UA, "WEATHERBOT_HTTP_RETRIES": bad})
