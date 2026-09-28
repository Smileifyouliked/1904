# Phase 0: verified facts and open questions

Checked 2026-09-28 (UTC). No bot code was written in this phase. Source
details, licences and rate limits are in `docs/data_sources.md`.

## Market rules (NYC highest temperature, KLGA)

All VERIFIED from the rules text of the Sep 29, 2026 market
(`docs/sources/polymarket_nyc_high_temp_rules_2026-09-29.md`) unless marked.

1. The market resolves on "the highest temperature recorded by NOAA at the LaGuardia Airport Station in degrees Fahrenheit".
2. Source: `https://www.weather.gov/wrh/timeseries?site=klga`, the highest reading in the "Temp" column, using **"Show Hourly Data"**. It is not the NWS daily climate report and not the 6-hour max.
3. Precision: whole °F.
4. Buckets are 2 °F wide (for example `64-65°F`), with an open bottom bucket (`63°F or below`) and an open top bucket (`82°F or higher`). The bucket edges move from day to day: Sep 27 ran `55°F or below` to `74°F or higher`; Sep 29 runs `63°F or below` to `82°F or higher`.
5. Each bucket is its own YES/NO market inside one `negRisk` event.
6. Fallback: if NOAA data is missing by 11:59 PM ET the next day, the Weather Underground daily table is used. If there is no data at all, the market resolves to the **lowest bucket**.
7. Revisions count only until the first data point of the next day is published.
8. The market resolves when the next day's first data point appears, or by 11:59 PM ET the next day, whichever comes first.
9. The Temp cell is `Math.round()` of Synoptic's °F value, with the day in local station time (`obtimezone=local`) (`docs/sources/noaa_wrh_timeseries_klga.md`). Math.round rounds .5 up. Python's `round()` rounds .5 to even, so code must not use it for this.
10. "Hourly Data" shows rows with minutes 51-59 for NWS/FAA stations, including SPECI reports.

## Price and format facts (the BUG-2 area)

All VERIFIED from fixtures in `tests/fixtures/polymarket/`.

11. Gamma `outcomePrices`, `outcomes` and `clobTokenIds` are **strings** that contain JSON arrays. Index 0 = YES, index 1 = NO (also stated in the docs).
12. Gamma `bestBid`, `bestAsk`, `spread` and `lastTradePrice` are **numbers**, not strings.
13. At the moment I checked, YES `outcomePrices` for the 70-71 °F bucket (0.58) equalled the CLOB midpoint (0.58), not the last trade (0.57).
14. The 11 YES `outcomePrices` summed to 1.054. They are not probabilities that add up to 1.
15. CLOB `/book`: `bids` are sorted ascending and `asks` descending, so the best price in each list is the **last** item.
16. CLOB `/price?side=BUY` returned the **best bid** (0.57) and `side=SELL` returned the **best ask** (0.59). One Polymarket guide page says the opposite. The live API and the API reference agree with each other.
17. A resolved market shows `outcomePrices` `["1", "0"]` (won) or `["0", "1"]` (lost), with `umaResolutionStatus: "resolved"`.
18. Weather fee: taker only, `fee = C × 0.05 × p × (1 − p)`, shown on the market as `feeSchedule: {"rate": 0.05, "exponent": 1, "takerOnly": true, "rebateRate": 0.25}`.

## Observation facts

19. NWS `/stations/KLGA/observations` mixes 5-minute rows (whole °C, empty `rawMessage`) with METAR/SPECI rows (tenths of °C from the T-group). Only the METAR/SPECI rows match what the "Hourly Data" view shows.
20. Cross-check for 2026-09-27: NWS API (17.8 °C = 64.04 °F → 64) and IEM (64.00 °F → 64) agree. The market resolved `64-65°F`.
21. KLGA maps to NWS office OKX, grid 37,46.

## Forecast source facts

22. Open-Meteo `models=ecmwf_ifs025` returns 51 series (control plus members 01-50). For KLGA it used the grid cell at 40.75, -74.0.
23. Open-Meteo `models=ncep_nbm_conus` is a valid model name (a made-up name returns an error).
24. ECMWF Open Data is CC-BY-4.0: commercial use allowed with attribution.
25. Open-Meteo's free tier is non-commercial only.

## Open questions

1. **Open-Meteo licence: decided 2026-09-28, use the free tier.** The terms bar commercial use, so this likely breaks them once the bot trades for profit, and access can be cut off. The bot must fail closed without Open-Meteo. Revisit before live trading.
2. **Blocked hosts.** `data.ecmwf.int` is now allowed and works (fixture saved). `api.meltema.com` and `api.oikolab.com` are still blocked, and both stay out anyway. Where the ECMWF control member (`type: cf`) is published is not yet confirmed.
3. **IEM: approved 2026-09-28 as a cross-check source.**
4. **Which day, exactly.** The rules say "on this day" and the page uses local station time. I assume a midnight-to-midnight ET day (EDT in summer, EST in winter), but the rules text does not say so outright. ASSUMED.
5. **SPECI reports at other minutes.** The help text says Hourly Data "includes any SPECI observations", but its filter is minutes 51-59. If a SPECI at 14:19 is the day's peak, does it count? I can't test this without the Synoptic API.
6. **Synoptic versus METAR rounding.** Synoptic converts °C to °F before `Math.round`. I assume it uses the METAR T-group tenths (for example 17.8 °C → 64.04 °F). A day where the whole-°C value and the tenths value round to different °F numbers would test this. ASSUMED.
7. **Two "last trade" numbers.** CLOB `/book` said `last_trade_price` 0.430 while Gamma said `lastTradePrice` 0.57 for the same token at the same minute. Unexplained.
8. **`makerBaseFee` / `takerBaseFee` = 1000.** These sit on each market next to `feeSchedule`, and the docs I read do not explain them. Until this is resolved, the fee from `feeSchedule` is the one I trust.
9. **When trading stops.** `endDate` is 12:00 UTC on the observation day (8 AM EDT), but the market can still take orders after that. The real cut-off is not confirmed.
10. **Meltema and Oikolab terms.** Unreadable or not found. Both stay out.
11. **AviationWeather `temp` tenths.** Not confirmed; the sample had only whole-degree T-groups.
