# Data sources

Checked 2026-09-28 (UTC). Each source here is a lead until it fills a role and
earns its place in backtesting (CLAUDE.md, `<data_sources>` rule 6).

Labels: **VERIFIED** means confirmed this session from the docs, a live call or
a fixture. **UNCLEAR** means I could not find or read the terms.

## Summary

| Role | Source | Commercial use | Status |
|---|---|---|---|
| Market data | Polymarket Gamma API | n/a (it is the venue) | Use |
| Market data, order book | Polymarket CLOB API | n/a | Use |
| Resolution truth (what the market settles on) | NOAA timeseries page, KLGA, Hourly Data | Public page | Not callable directly (see below) |
| Ground-truth observations | NWS API `api.weather.gov` | Yes, "free to use for any purpose" | Use as primary |
| Ground-truth observations, cross-check | AviationWeather Data API | Unclear (US gov; no licence text found) | Backup |
| Ground-truth observations, cross-check | Iowa Environmental Mesonet (IEM) ASOS | Unclear | Cross-check source; approved by the owner 2026-09-28 |
| Ensemble forecasts | ECMWF Open Data | Yes, CC-BY-4.0 with attribution | Preferred, but blocked in this sandbox |
| Ensemble forecasts | Open-Meteo Ensemble API | **No** on the free tier | Free tier, by owner decision 2026-09-28 (see licence risk) |
| NBM (deterministic) | Open-Meteo `ncep_nbm_conus` | **No** on the free tier | Free tier, by owner decision 2026-09-28 (see licence risk) |
| Official NWS forecast | NWS API gridpoint forecast | Yes | Use |
| Ensemble forecasts | Meltema | UNCLEAR (docs unreadable) | Do not use |
| Historical training data | Open-Meteo Historical Forecast / Previous Runs | **No** on the free tier | Free tier, by owner decision 2026-09-28 (see licence risk) |
| Historical training data | Oikolab | UNCLEAR (no terms found) | Do not use |

## Polymarket Gamma API (market metadata and prices)

- Base URL: `https://gamma-api.polymarket.com`. Event by slug: `/events/slug/highest-temperature-in-nyc-on-<month>-<day>-<year>` (VERIFIED, fixtures under `tests/fixtures/polymarket/`).
- Auth: none for reads (VERIFIED, live calls without a key returned 200).
- Rate limits: general 4,000 req / 10 s; `/events` 500 / 10 s; `/markets` 300 / 10 s (VERIFIED, `.claude/skills/polymarket-docs/references/verbatim/polymarket-llms-full.md`, API rate limits page).
- Update latency: not documented. `outcomePrices` matched the CLOB midpoint when I checked (one sample).
- Licence: not applicable (it is the trading venue).
- Format traps (VERIFIED from fixtures):
  - `outcomes`, `outcomePrices`, `clobTokenIds` are **strings holding JSON arrays**, e.g. `"[\"0.58\", \"0.42\"]"`. Parse them with `json.loads`. Index 0 = YES, index 1 = NO.
  - `bestBid`, `bestAsk`, `spread`, `lastTradePrice` are **numbers**, not strings.
  - A resolved market has `outcomePrices` `["1", "0"]` or `["0", "1"]` and `umaResolutionStatus: "resolved"`.
  - The YES `outcomePrices` of the 11 buckets summed to 1.054, not 1.0 (fixture `gamma_event_nyc_2026-09-29_open.json`).

## Polymarket CLOB API (order book, prices)

- Base URL: `https://clob.polymarket.com` (VERIFIED).
- Auth: none for `/book`, `/price`, `/midpoint`; orders need signed auth (not checked yet, Phase 4).
- Rate limits: `/book` 1,500 / 10 s; `/price` 1,500 / 10 s; `/midpoint` 1,500 / 10 s (VERIFIED, same docs page).
- Format traps (VERIFIED from fixtures):
  - `/book` returns `bids` sorted **ascending** (best bid is the **last** item) and `asks` sorted **descending** (best ask is the **last** item). Prices and sizes are strings.
  - `/price?side=BUY` returned **0.57, the best bid**, and `side=SELL` returned **0.59, the best ask**. The API reference says the same thing, but the "Prices and Order Books" guide on the same site says BUY returns the lowest ask. **The docs contradict each other; the live API matches the API reference.**
  - `/book` `last_trade_price` was `0.430` while Gamma `lastTradePrice` was `0.57` for the same token at the same minute. Not explained yet (open question).
- Fees (VERIFIED, docs fees page plus the market's own `feeSchedule`): taker only, `fee = C × feeRate × p × (1 − p)`; weather `feeRate` 0.05, `exponent` 1, `rebateRate` 0.25. The market also carries `makerBaseFee: 1000` and `takerBaseFee: 1000`, which the docs I read do not explain.
- Tick size 0.01 for most NYC buckets, 0.001 for some tail buckets; minimum order size 5 (VERIFIED, `orderPriceMinTickSize`, `orderMinSize`).

## Resolution source: NOAA timeseries page for KLGA

- URL named in the market rules: `https://www.weather.gov/wrh/timeseries?site=klga`, using "Show Hourly Data" and the highest "Temp" for the day (VERIFIED, `docs/sources/polymarket_nyc_high_temp_rules_2026-09-29.md`).
- The page gets its data from the Synoptic API (`api.synopticdata.com/v2/stations/timeseries`) with `units=temp|F` and `obtimezone=local`, using NWS's own token (VERIFIED, `docs/sources/noaa_wrh_timeseries_klga.md`). We must not reuse that token. Synoptic's own licence was not checked.
- The Temp cell is `Math.round(air_temp_in_F)`. JavaScript `Math.round` rounds .5 **up** (64.5 → 65). Python's `round()` rounds .5 to the nearest even number (64.5 → 64). Our code must copy the JavaScript rule.
- "Hourly Data" shows rows with minutes 51-59 for NWS/FAA stations, "to include any SPECI observations" (VERIFIED, page help text). Whether SPECIs at other minutes appear is unclear (open question).
- The fallback source is the Weather Underground daily table. If there is no data by 11:59 PM ET the next day, the market resolves to the **lowest bucket** (VERIFIED, rules text).

## NWS API (`api.weather.gov`)

- Base URL: `https://api.weather.gov` (VERIFIED).
- Auth: a `User-Agent` header is required; contact info is recommended (VERIFIED, `.claude/skills/nws-api-docs/references/verbatim/services-web-api.md`).
- Rate limits: not public. When hit, retry after it clears, "typically within 5 seconds" (VERIFIED, same file).
- Update latency: observations "may be delayed up to 20 minutes" from MADIS (VERIFIED, same file).
- Licence: "open data, free to use for any purpose" (VERIFIED, same file). **Commercial use: yes.**
- KLGA facts (VERIFIED, fixtures under `tests/fixtures/nws/`): station at 40.7792, -73.8800; `/points` maps it to office OKX, grid 37,46.
- Format traps (VERIFIED, `observations_KLGA_2026-09-27.json`):
  - `/stations/KLGA/observations` returned 325 rows for one day (about 13 per hour): 5-minute rows with **whole °C** and an empty `rawMessage`, plus METAR/SPECI rows with **tenths of °C** (from the METAR T-group) and a full `rawMessage`.
  - Temperatures are in `wmoUnit:degC`, not °F.

## AviationWeather Data API

- Base URL: `https://aviationweather.gov/api/data/` (VERIFIED, live call `metar?ids=KLGA&format=json` returned 200). The `aviationweather.gov/dataserver` link in the public-apis list is the old service.
- Auth: none (VERIFIED, live call).
- Rate limits: at most 100 requests per minute (VERIFIED, https://aviationweather.gov/data/api/ via Firecrawl search excerpt).
- Licence: UNCLEAR; no terms text found. US government data, but not confirmed.
- History depth: not checked. Only useful for recent METARs so far.
- Format (VERIFIED, `metar_KLGA_recent.json`): a JSON list; `temp` is °C, `metarType` is `METAR` or `SPECI`, `rawOb` holds the raw text. In this sample every T-group was a whole degree (T0150 = 15.0 °C), so I could not confirm whether `temp` keeps the tenths.

## Iowa Environmental Mesonet (IEM) ASOS archive

- URL: `https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py` (VERIFIED, live call returned CSV with `tmpf` and raw METAR).
- Auth: none. Rate limits and licence: not checked (UNCLEAR).
- Not on the original shortlist. The owner approved it as a cross-check source on 2026-09-28.

## ECMWF Open Data

- Licence: CC-BY-4.0, commercial use allowed with attribution (VERIFIED, https://www.ecmwf.int/en/forecasts/datasets/open-data and the ECMWF news post of 2025, via Firecrawl search excerpts).
- Base URL: `https://data.ecmwf.int/forecasts/` (from the attribution text above). **This host is blocked in this sandbox** (proxy refused CONNECT), so no fixture yet.
- Formats: GRIB2 files, not a point API. Needs `ecCodes`/`cfgrib`, and grids must be handled carefully on a 2 GB server. Not checked yet.

## Open-Meteo (Ensemble, Forecast with NBM, Historical Forecast, Previous Runs)

- Base URLs: `https://ensemble-api.open-meteo.com/v1/ensemble`, `https://api.open-meteo.com/v1/forecast` (VERIFIED, live calls).
- Auth: none on the free tier; `apikey` plus a `customer-` server prefix on paid plans (VERIFIED, `.claude/skills/open-meteo-docs/references/verbatim/ensemble-api.md`).
- Rate limits (free): under 10,000 calls a day, 5,000 an hour, 600 a minute (VERIFIED, `.../verbatim/terms.md`).
- **Licence: free tier is non-commercial only.** "Integrating our service into commercial products" is listed as commercial (VERIFIED, `.../verbatim/terms.md`). A trading bot run for profit is very likely commercial.
- **Owner decision (2026-09-28): use the free tier.** Licence risk, stated plainly: using the free tier for a bot that trades for profit likely breaks Open-Meteo's terms. Open-Meteo can block the bot's IP address or cut off access with no warning, which could stop forecasts in the middle of a trading day. The bot must fail closed when Open-Meteo is unavailable. Before live trading, revisit this decision (paid plan, self-hosting, or ECMWF Open Data directly).
- Models (VERIFIED by live call): `models=ecmwf_ifs025` returns `temperature_2m` plus `_member01` to `_member50` (51 series). `models=ncep_nbm_conus` works on `/v1/forecast`. A bad model name returns `{"error": true, ...}`.
- Grid trap (VERIFIED, fixture): for KLGA (40.7792, -73.8800) the ECMWF 0.25° ensemble answered for the cell at 40.75, -74.0, about 10 km away.
- Update times: ECMWF IFS 0.25° ensemble, 51 members, 15 days, every 6 hours (VERIFIED, ensemble docs table). NBM history in the Historical Forecast API starts 2024-10-08 (VERIFIED, `.../verbatim/historical-forecast-api.md`).

## Meltema

- Listed in the public-apis catalog as "keyless point forecasts" with GFS, ECMWF AIFS/IFS and a 31-member GEFS ensemble.
- Its docs page failed to load through Firecrawl and the host is blocked in this sandbox. Licence, rate limits and reliability: **UNCLEAR. Do not use.**

## Oikolab

- Listed as "70+ years of hourly historical and forecast data from NOAA and ECMWF", API key required.
- Its docs overview loaded but I found no terms or prices. Licence: **UNCLEAR. Do not use** until checked.

## Cross-check: KLGA high on 2026-09-27 (ET)

| Source | Highest hourly reading | Rounded (half up) |
|---|---|---|
| NWS API, METAR rows (`observations_KLGA_2026-09-27.json`) | 17.8 °C at 16:51Z (12:51 EDT), = 64.04 °F | 64 |
| IEM ASOS (`asos_LGA_2026-09-27_local.csv`) | 64.00 °F at 12:51 EDT | 64 |
| Polymarket result (`gamma_event_nyc_2026-09-27_resolved.json`) | "64-65°F" resolved YES | agrees |

The two sources agree. The NWS 5-minute rows peaked at 18 °C (64.4 °F), which also rounds to 64, so this day does not test the hourly-versus-5-minute difference.
