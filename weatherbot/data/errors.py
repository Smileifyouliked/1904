"""Errors raised by the data layer. Callers catch DataError, log it and skip trading."""

from __future__ import annotations


class DataError(Exception):
    """Base class: the data cannot be trusted, so the bot must not trade on it."""


class FetchError(DataError):
    """A network request failed after all retries."""


class ParseError(DataError):
    """A response did not have the shape or values we verified in Phase 0."""


class StaleDataError(DataError):
    """Data is older than the allowed age, or does not cover the needed period."""
