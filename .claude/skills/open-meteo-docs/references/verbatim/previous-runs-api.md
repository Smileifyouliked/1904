<!--
Source: https://open-meteo.com/en/docs/previous-runs-api
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/clouds.webp)

# Previous Model Runs API

Weather Forecasts from Previous Days to Compare Run-To-Run Performance

 

Data from past model runs is aligned to fixed lead-time offsets of 1–7 days. Requesting temperature\_2m\_previous\_day1 returns the value predicted 24 hours before valid
time; \_previous\_day2 returns 48 hours before, and so on up to day 7. Comparing
these offsets against observations or reanalysis makes it straightforward to measure how
forecast skill degrades with lead time and to train bias-correction models. Most models are
archived from **January 2024**. GFS 2 m temperature extends back to **March 2021**.

[## API Response](#api_response)

Preview:

Loading...

[Download XLSX](https://previous-runs-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,temperature_2m_previous_day1,temperature_2m_previous_day2,temperature_2m_previous_day3,temperature_2m_previous_day4,temperature_2m_previous_day5&past_days=7&forecast_days=1&format=xlsx) [Download CSV](https://previous-runs-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,temperature_2m_previous_day1,temperature_2m_previous_day2,temperature_2m_previous_day3,temperature_2m_previous_day4,temperature_2m_previous_day5&past_days=7&forecast_days=1&format=csv)

API URL ([Open in new tab](https://previous-runs-api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,temperature_2m_previous_day1,temperature_2m_previous_day2,temperature_2m_previous_day3,temperature_2m_previous_day4,temperature_2m_previous_day5&past_days=7&forecast_days=1), copy this URL into your application, or paste an API URL to restore its settings)

[## Data Availability](#data_availability)

Most models are archived from **January 2024**. Some models were added to the
archive later in 2024 or 2025 and have correspondingly shorter coverage. Exceptions with
longer history:

* **GFS 2 m temperature** — available from **March 2021**
* **JMA GSM and MSM** — available from **2018**

Additional historical coverage can be reconstructed on request, subject to upstream
availability from the originating weather service.

[## API Documentation](#api_documentation)

The Previous Runs API exposes forecast data at fixed lead-time offsets rather than as a
seamless time-series. \_previous\_day0 is the current model run (equivalent to the
live Forecast API). \_previous\_day1 is the value that was predicted 24 hours
before valid time, \_previous\_day2 48 hours before, and so on up to day 7. For local
models with shorter forecast horizons (2–5 days), only offsets within that horizon are populated.

This structure is suited to aggregated skill analysis — for example, computing the mean
absolute error of all \_previous\_day3 forecasts against ERA5 over a calendar year.
For workflows that need the *complete* output of a specific model run (initialisation
datetime, all forecast hours, multiple variables), use the [Single Runs API](/en/docs/single-runs-api) instead,
which stores each run independently and is queryable by its UTC initialisation time via the &run= parameter.

**Models:** The Previous Runs API supports the same models as the [Weather Forecast API](/en/docs). See the Forecast API
documentation for the full model and variable list.

**Update cadence:** Global models update every 6 hours; regional models (e.g.
ICON-D2, HRRR, AROME) update every 1–3 hours. The available lead-time window for each model is
limited to its forecast horizon, so a model with a 3-day horizon will have at most \_previous\_day3 populated.
