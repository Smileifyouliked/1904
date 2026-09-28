# 1904: Weatherbot

A forecasting and paper-trading bot for Polymarket's daily "Highest temperature in NYC"
markets, which resolve on LaGuardia (KLGA) readings. It is built in phases (see CLAUDE.md).
Live trading is off by default.

Status: Phase 1 (data layer) is in progress. The bot does not trade yet.

## Run the tests

Needs Python 3.11 or newer.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pytest
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

The tests read saved real API responses from `tests/fixtures/` and make no network calls.

## Settings

Copy `.env.example` to `.env` and set `WEATHERBOT_USER_AGENT`. The NWS API requires a
User-Agent header that identifies the app and a contact. Never commit `.env`.

## Where things are

- `weatherbot/data/`: fetchers and parsers for Polymarket, NWS, IEM, Open-Meteo and ECMWF
- `docs/data_sources.md`: each source's terms, limits and licence
- `docs/phase0_verification.md`: market rules and verified facts
