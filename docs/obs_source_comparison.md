# KLGA daily high: six sources compared with Polymarket results

Run on 2026-09-28 with `scripts/compare_obs_sources.py --start 2026-04-01 --end 2026-09-27`.
Raw output: `docs/data/obs_source_comparison_2026-04-01_to_2026-09-27.csv` (one row per day).

## Result

A "match" means the source's daily high (rounded half up to whole °F) falls in the bucket that
Polymarket paid out. 177 days had a resolved event. 2026-05-17 and 05-18 had no event (404), and
2026-06-18 had a market with no `outcomePrices`.

| Source | What it is | NOAA-rules days (from 2026-08-23) | Wunderground-rules days (before) |
|---|---|---|---|
| `iem_all` | IEM ASOS: max of all METAR + SPECI reports in the New York day | **36/36** | **141/141** |
| `iem_hourly` | IEM ASOS: max of minute-51-59 reports only | 35/36 | 138/141 |
| `awc_hourly` | aviationweather.gov METARs, minute 51-59 only (about 15 days of history) | 14/15 | none |
| `nws_hourly` | api.weather.gov observations, minute 51-59 only (about 7 days of history) | 6/6 | none |
| `cli` | NWS Daily Climate Report CLILGA "MAXIMUM" (from the IEM text archive) | 23/36 | 92/141 |
| `iem_daily` | IEM daily summary `max_tmpf` | 23/36 | 92/141 |

## What this tells us

1. **The market pays on the max of every METAR and SPECI report in the day.** The four misses
   for "hourly only" (2026-06-09, 06-14, 08-17, 09-20) were all days when a SPECI between the
   hourly reports was warmest. Example: on 2026-09-20 a 21:04 EDT SPECI read 22.2 °C (71.96 °F,
   shown as 72). The routine reports peaked at 71. Polymarket paid 72-73 °F. This answers open
   question 5 in `docs/phase0_verification.md`. The bot now uses all reports.
2. **The official climate-report high is the wrong number for this market.** CLI and IEM's
   daily max run 1-2 °F above the reports (they include readings between reports). They missed
   the paid bucket on about 1 day in 3. Do not use them as training labels. NOAA GHCN `TMAX`
   is probably the same kind of number (ASSUMED: NCEI is blocked here, so it was not tested).
3. **The NWS API feed has gaps.** For the 6 days it still holds (09-22 to 09-27), it had only
   16 to 22 of the 24 routine hourly reports. The METAR text was missing on the other rows.
   It matched on all 6 days by luck, not by design.
4. **The market rules changed on 2026-08-23.** Before that date, events resolved on the Weather
   Underground "Daily Observations" table. From that date they resolve on the NOAA timeseries
   page. The same "all reports" max matched both eras. The trading code still rejects any event
   whose rules text is not the current NOAA wording.
5. **IEM's `asos.py` end date is exclusive.** Asking for `day2=21` stopped at 2026-09-20 23:51
   UTC. The New York day runs to 04:00 UTC, so the bot now requests through `day + 2`.

## Not compared

- The NOAA page's own data API (`api.synopticdata.com`) and NCEI are blocked by this
  environment's network allowlist (HTTP 403 from the proxy).
- Weather Underground was not scraped. It is the fallback source in the rules.

## Limits

177 days is one spring and summer. No DST-change day and no winter day was tested yet. The
comparison uses IEM as the observation archive for all six IEM/CLI rows, so it is not fully
independent of IEM.
