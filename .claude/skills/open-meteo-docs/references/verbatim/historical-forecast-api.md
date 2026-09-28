<!--
Source: https://open-meteo.com/en/docs/historical-forecast-api
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/andermatt.webp)

# Historical Forecast API

Archived High-Resolution Weather Forecasts

 

Historical forecasts archived from the [Weather Forecast API](/en/docs) — same models, same parameters, same response format. Coverage starts around 2022. Each run's first
few hours are stitched into a continuous hourly timeseries. To access the full forecast horizon of
individual runs, use the [Single Runs API](/en/docs/single-runs-api).

[## API Response](#api_response)

Preview:

Loading...

[Download XLSX](https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m&format=xlsx) [Download CSV](https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m&format=csv)

API URL ([Open in new tab](https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m), copy this URL into your application, or paste an API URL to restore its settings)

[## Data Sources](#data_sources)

The weather data precisely aligns with the weather forecast API, created by continuously
integrating weather forecast model data. Each update from the weather models' initial hours is
compiled into a seamless time series. This extensive dataset is ideal for training machine
learning models and combining them with forecast data to generate optimised predictions.

Weather models are initialized using data from weather stations, satellites, radar, airplanes,
soundings, and buoys. With high update frequencies of 1, 3, or 6 hours, the resulting time
series is nearly as accurate as direct measurements and offers global coverage. In regions
like North America and Central Europe, the difference from local weather stations is minimal.
However, for precise values such as precipitation, local measurements are preferable when
available.

The Historical Forecast API archives comprehensive data, including atmospheric pressure
levels, from all accessible weather forecast models. Depending on the model and public archive
availability, data is available starting from 2021 or 2022.

The default Best Match option selects the most suitable high-resolution weather models
for any global location, though users can also manually specify the weather model. Open-Meteo utilises
the following weather forecast models:

| National Weather Provider | Weather Model | Region | Spatial Resolution | Temporal Resolution | Update Frequency | Available Since |
| --- | --- | --- | --- | --- | --- | --- |
| Deutscher Wetterdienst (DWD) | ICON | 🌍 Global | 0.1° (~11 km) | Hourly | Every 6 hours | 2022-11-24 |
| ICON-EU | European Union Europe | 0.0625° (~7 km) | Hourly | Every 3 hours | 2022-11-24 |
| ICON-D2 | Germany Switzerland Austria Central Europe | 0.02° (~2 km) | Hourly | Every 3 hours | 2022-11-24 |
| NOAA NCEP | GFS | 🌍 Global | 0.11° (~13 km) | Hourly | Every 6 hours | 2021-03-23 |
| GFS Pressure Variables | 🌍 Global | 0.25° (~25 km) | Hourly | Every 6 hours | 2021-03-23 |
| HRRR | United States Canada U.S. Conus | 3 km | Hourly | Every hour | 2018-01-01 |
| NAM | United States Canada U.S. Conus | 3 km | Hourly | Every 6 hours | 2025-09-01 |
| NBM | United States Canada U.S. Conus | 3 km | Hourly | Every hour | 2024-10-08 |
| AIGFS | 🌍 Global | 0.25° (~25 km) | 6-Hourly | Every 6 hours | 2026-01-07 |
| HGEFS | 🌍 Global | 0.25° (~25 km) | 6-Hourly | Every 6 hours | 2026-01-07 |
| Météo-France | ARPEGE World | 🌍 Global | 0.25° (~25 km) | Hourly | Every 6 hours | 2024-01-02 |
| ARPEGE Europe | European Union Europe | 0.1° (~11 km) | Hourly | Every 6 hours | 2022-11-13 |
| AROME France | France France | 0.025° (~2.5 km) | Hourly | Every 3 hours | 2024-01-02 |
| AROME France HD | France France | 0.01° (~1.5 km) | Hourly | Every 3 hours | 2022-11-13 |
| ECMWF | IFS 0.4° | 🌍 Global | 0.4° (~44 km) | 3-Hourly | Every 6 hours | 2022-11-07 |
| IFS 0.25° | 🌍 Global | 0.25° (~25 km) | 3-Hourly | Every 6 hours | 2024-02-03 |
| AIFS 0.25° Single | 🌍 Global | 0.25° (~25 km) | 6-Hourly | Every 6 hours | 2025-02-20 |
| IFS HRES | 🌍 Global | 9 km (O1280 grid) | Hourly | Every 6 hours | 2017-01-01 |
| UK Met Office | UKMO Global | 🌍 Global | 0.09° (~10 km) | Hourly | Every 6 hours | 2022-03-01 |
| UKMO UKV | United Kingdom Ireland UK and Ireland | 2 km | Hourly | Every hour | 2022-03-01 |
| JMA | GSM | 🌍 Global | 0.5° (~55 km) | 6-Hourly | Every 6 hours | 2016-01-01 |
| MSM | Japan Japan | 0.05° (~5 km) | Hourly | Every 3 hours | 2016-01-01 |
| MET Norway | MET Nordic | Norway Sweden Denmark Norway, Denmark, Sweden, Finland | 1 km | Hourly | Every hour | 2022-11-15 |
| Canadian Weather Service | GEM Global | 🌍 Global | 0.15° (~15 km) | 3-Hourly | Every 12 hours | 2022-11-23 |
| GEM Regional | Canada United States North America, North Pole | 10 km | Hourly | Every 6 hours | 2022-11-23 |
| HRDPS Continental | Canada Canada, Nothern US | 2.5 km | Hourly | Every 6 hours | 2023-03-03 |
| China Meteorological Administration (CMA) | GFS GRAPES | 🌍 Global | 0.125° (~15 km) | 3-hourly | Every 6 hours | 2023-12-31 |
| Australian Bureau of Meteorology (BOM) | ACCESS-G | 🌍 Global | 0.15° (~15 km) | Hourly | Every 6 hours | 2024-01-18 |
| ItaliaMeteo ItaliaMeteo-ARPAE | ICON 2I | Italy Southern Europe | 2 km | Hourly | Every 12 hours | 2025-04-13 |
| DMI | HARMONIE AROME DINI | European Union Central & Northern Europe | 2 km | Hourly | Every 3 hours | 2024-07-01 |
| KNMI | HARMONIE AROME Netherlands | Netherlands Belgium Netherlands, Belgium | 2 km | Hourly | Every hour | 2024-07-01 |
| HARMONIE AROME Europe | European Union Central & Northern Europe up to Iceland | 5.5 km | Hourly | Every hour | 2024-07-01 |
| MeteoSwiss | ICON CH1 | Switzerland Central Europe | 1 km | Hourly | Every 3 hours | 2025-07-29 |
| ICON CH2 | Switzerland Central Europe | 2 km | Hourly | Every 6 hours | 2025-07-29 |

[## Which Historical Weather Data to Use?](#which_historical_weather_data_to_use)

Open-Meteo offers four distinct historical weather datasets, each suited to different use
cases. Only a small fraction of the Earth's surface has reliable, continuous weather station
coverage; all four datasets use numerical weather models to fill that gap globally.

* **[Historical Weather API:](/en/docs/historical-weather-api)** ERA5 reanalysis at 0.25° (~25 km) from 1940, ERA5-Land at 0.1° (~9 km) from 1950, and ECMWF
  IFS analysis at 9 km from 2017. Optimised for long-term consistency rather than day-to-day accuracy
  — the right choice for climate trend analysis.
* **[Historical Forecast API:](/en/docs/historical-forecast-api)** A continuous hourly timeseries built by stitching the first hours of each successive model run.
  Closely tracks actual conditions because each run is initialised from real measurements. Coverage
  starts around 2021. Not suitable for long time series due to model version changes over time.
* **[Previous Runs API:](/en/docs/previous-runs-api)** Archives the same high-resolution models as the Historical Forecast API, but provides each variable
  at a fixed lead-time offset: 1, 2, 3, up to 7 days ahead. Useful for evaluating forecast skill
  at specific lead times. Data starts from January 2024 (GFS from March 2021, JMA from 2018).
* **[Single Runs API:](/en/docs/single-runs-api)** Retrieves the complete forecast horizon of any individual model run, selected by initialisation
  time using the run= parameter (e.g. run=2025-09-01T00:00). Unlike the Historical Forecast API — which stitches runs
  into a continuous timeseries — the Single Runs API preserves the original run structure.
  ECMWF IFS HRES at 9 km is archived from March 2024; all other models from 2nd of April 2026.

#### Choosing the Right Dataset:

* For multi-decade climate analysis, use the **Historical Weather API** (ERA5 from
  1940).
* For the most accurate representation of past conditions over the last few years, use the **Historical Forecast API**.
* To assess how forecast accuracy degrades at longer lead times, use the **Previous Runs API**.
* To retrieve the full output of a specific model run — for example to reproduce a forecast
  issued on a given date — use the **Single Runs API**.
* For training machine learning models on consistent weather model output, the **Historical Forecast API** and **Single Runs API** both provide data directly from the operational model runs.

[## API Endpoint](#api_endpoint)

As the API is identical to the Forecast API, please refer to the Weather Forecast API
documentation for all available variables and parameters. The only notable difference is the
API host "historical-forecast-api.open-meteo.com" as historical data is moved to a different
set of servers with access to a large storage system.
