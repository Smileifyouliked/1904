"""HTTP GET with a timeout, retries with exponential backoff, and a log line per failure."""

from __future__ import annotations

import logging
import time
from collections.abc import Callable, Mapping, Sequence
from typing import Any

import requests

from weatherbot.config import Settings
from weatherbot.data.errors import FetchError

log = logging.getLogger(__name__)

# 429 = rate limited; 5xx = server trouble. Other 4xx mean our request is wrong,
# so retrying would not help.
RETRY_STATUS = frozenset({429, 500, 502, 503, 504})

# A mapping, or a list of pairs when a key repeats (IEM uses data=tmpf&data=metar).
Params = Mapping[str, Any] | Sequence[tuple[str, Any]] | None


class HttpClient:
    """Small wrapper so every call gets the same timeout, retries and User-Agent."""

    def __init__(
        self,
        settings: Settings,
        session: requests.Session | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._settings = settings
        self._session = session or requests.Session()
        self._sleep = sleep

    def get(
        self,
        url: str,
        params: Params = None,
        headers: Mapping[str, str] | None = None,
    ) -> requests.Response:
        merged_headers = {"User-Agent": self._settings.user_agent}
        if headers:
            merged_headers.update(headers)
        attempts = self._settings.http_retries
        last_problem = "no attempt made"
        for attempt in range(1, attempts + 1):
            try:
                response = self._session.get(
                    url,
                    params=params,
                    headers=merged_headers,
                    timeout=self._settings.http_timeout_s,
                )
            except requests.RequestException as exc:
                last_problem = f"{type(exc).__name__}: {exc}"
            else:
                if response.status_code == 200:
                    return response
                last_problem = f"HTTP {response.status_code}"
                if response.status_code not in RETRY_STATUS:
                    log.warning("GET %s failed (%s), not retrying", url, last_problem)
                    raise FetchError(f"GET {url} failed: {last_problem}")
            log.warning("GET %s failed (attempt %d/%d): %s", url, attempt, attempts, last_problem)
            if attempt < attempts:
                self._sleep(self._settings.http_backoff_s * 2 ** (attempt - 1))
        raise FetchError(f"GET {url} failed after {attempts} attempts: {last_problem}")

    def get_json(
        self,
        url: str,
        params: Params = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        response = self.get(url, params=params, headers=headers)
        try:
            return response.json()
        except ValueError as exc:
            log.warning("GET %s returned invalid JSON", url)
            raise FetchError(f"GET {url} returned invalid JSON") from exc

    def get_text(
        self,
        url: str,
        params: Params = None,
        headers: Mapping[str, str] | None = None,
    ) -> str:
        return self.get(url, params=params, headers=headers).text
