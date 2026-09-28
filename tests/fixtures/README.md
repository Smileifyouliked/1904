# Fixtures

Real API responses saved unedited on 2026-09-28 between about 11:50 and 11:55 UTC.
Parser tests must use these, not hand-written samples. Do not edit them; save a
new file instead if an API changes.

| File | Request |
|---|---|
| `polymarket/gamma_event_nyc_2026-09-29_open.json` | `GET https://gamma-api.polymarket.com/events/slug/highest-temperature-in-nyc-on-september-29-2026` (open market) |
| `polymarket/gamma_event_nyc_2026-09-27_resolved.json` | same endpoint, slug `...-september-27-2026` (resolved: `64-65°F` won) |
| `polymarket/clob_book_nyc_2026-09-29_70-71F_yes.json` | `GET https://clob.polymarket.com/book?token_id=<70-71°F YES token>` |
| `polymarket/clob_price_buy_nyc_2026-09-29_70-71F_yes.json` | `GET https://clob.polymarket.com/price?token_id=<same>&side=BUY` (returned the best bid) |
| `polymarket/clob_price_sell_nyc_2026-09-29_70-71F_yes.json` | same with `side=SELL` (returned the best ask) |
| `polymarket/clob_midpoint_nyc_2026-09-29_70-71F_yes.json` | `GET https://clob.polymarket.com/midpoint?token_id=<same>` |
| `nws/station_KLGA.json` | `GET https://api.weather.gov/stations/KLGA` |
| `nws/points_KLGA.json` | `GET https://api.weather.gov/points/40.7792,-73.8800` |
| `nws/gridpoint_forecast_KLGA.json` | `GET https://api.weather.gov/gridpoints/OKX/37,46/forecast` |
| `nws/observations_KLGA_2026-09-27.json` | `GET https://api.weather.gov/stations/KLGA/observations?start=2026-09-27T04:00:00Z&end=2026-09-28T04:00:00Z` (Sep 27 in EDT) |
| `iem/asos_LGA_2026-09-27_local.csv` | `GET https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=LGA&data=tmpf&data=metar&year1=2026&month1=9&day1=27&year2=2026&month2=9&day2=28&tz=America/New_York&format=onlycomma&latlon=no&missing=M&trace=T&direct=no&report_type=3&report_type=4` |
| `aviationweather/metar_KLGA_recent.json` | `GET https://aviationweather.gov/api/data/metar?ids=KLGA&format=json&hours=3` |
| `open_meteo/ensemble_ecmwf_ifs025_KLGA.json` | `GET https://ensemble-api.open-meteo.com/v1/ensemble?latitude=40.7792&longitude=-73.8800&hourly=temperature_2m&models=ecmwf_ifs025&temperature_unit=fahrenheit&timezone=America%2FNew_York&forecast_days=2` |
| `ecmwf/enfo_20260928_00z_24h.index` | `GET https://data.ecmwf.int/forecasts/20260928/00z/ifs/0p25/enfo/20260928000000-24h-enfo-ef.index` (fetched about 12:05 UTC) |
| `open_meteo/forecast_nbm_KLGA.json` | `GET https://api.open-meteo.com/v1/forecast?latitude=40.7792&longitude=-73.8800&daily=temperature_2m_max&hourly=temperature_2m&models=ncep_nbm_conus&temperature_unit=fahrenheit&timezone=America%2FNew_York&forecast_days=2` |
| `open_meteo/ensemble_ecmwf_ifs025_KLGA_gmt.json` | same as the ensemble request above but `timezone=GMT&forecast_days=3` (fetched about 12:10 UTC). The bot's parser accepts only GMT responses. |
| `open_meteo/forecast_nbm_KLGA_gmt.json` | `GET https://api.open-meteo.com/v1/forecast?latitude=40.7792&longitude=-73.8800&hourly=temperature_2m&models=ncep_nbm_conus&temperature_unit=fahrenheit&timezone=GMT&forecast_days=3` (about 12:10 UTC) |
| `open_meteo/meta_ecmwf_ifs025_ensemble.json` | `GET https://ensemble-api.open-meteo.com/data/ecmwf_ifs025_ensemble/static/meta.json` (about 12:10 UTC) |
| `open_meteo/meta_ncep_nbm_conus.json` | `GET https://api.open-meteo.com/data/ncep_nbm_conus/static/meta.json` (about 12:10 UTC) |
| `iem/asos_LGA_2026-09-20_utc.csv` | IEM `asos.py` as above but `year1=2026&month1=9&day1=19&year2=2026&month2=9&day2=22&tz=Etc/UTC` (about 12:40 UTC). Holds the 21:04 EDT SPECI that set the 2026-09-20 high. |
| `iem/cli_LGA_2026-09-27.txt` | `GET https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=CLILGA&limit=1&fmt=text&sdate=2026-09-28&edate=2026-09-29` (NWS climate report, MAXIMUM 65 for Sep 27) |
| `polymarket/gamma_event_nyc_2026-09-20_resolved.json` | Gamma event slug `...-september-20-2026` (resolved: `72-73°F` won) |

Note found in Phase 1: in `nws/observations_KLGA_2026-09-27.json`, 6 of the 24 hourly
rows (06:51, 07:51, 11:51, 19:51, 20:51 and 00:51 UTC) have no `rawMessage`. The NWS feed
alone therefore gives an incomplete day; the IEM file has all 24.

NWS requests used the header `User-Agent: weatherbot-dev (github.com/Smileifyouliked/1904)`.
None of these responses contain keys, wallet addresses or personal data.
Open-Meteo data here came from the free, non-commercial tier; see `docs/data_sources.md`.
