<!--
Source: https://open-meteo.com/en/docs/model-updates
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/mountain_road.webp)

# Model Updates and Data Availability

Overview of Model Timings and Data Availability via Open-Meteo API

 

[## Model Updates](#model_updates)

This page offers a brief overview of all models integrated into Open-Meteo. These models are
typically updated every few hours. Open-Meteo aims to download and process the data as soon as
it becomes available, immediately after it is released by national weather services.

Open-Meteo operates with geographically distributed and redundant servers. Data across all
Open-Meteo servers is [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency "Wikipedia: Eventual consistency"), meaning there may be instances where the API indicates a weather model has been updated,
but not all servers have been fully updated yet. If you need access to the most recent
forecast, it's recommended to wait an additional 10 minutes after the forecast update has been
applied.

Models with a delay exceeding 20 minutes are highlighted in yellow. If multiple weather model
updates are missed, the model is marked in red. Minor delays are fairly common.

To report a model issue, please open a ticket on [GitHub](https://github.com/open-meteo/open-meteo/issues "GitHub Open-Meteo Repository"). Commercial clients can contact us directly via email.

The free and commercial API services of Open-Meteo operate on different servers, leading to
slight variations in update times. Please choose the appropriate type below. Note that API
calls to the metadata API are not counted toward daily or monthly request limits.

Usage licence:

Global Weather Models

🌍

Local European Models ![european_union](/images/country-flags/european_union.svg)

Local North American Models ![us](/images/country-flags/us.svg) ![ca](/images/country-flags/ca.svg)

Local Asian Models ![jp](/images/country-flags/jp.svg)

[Refresh](/en/docs/model-updates#refresh) Last refresh: 00:00

[## Metadata API Documentation](#metadata_api_documentation)

You can retrieve the update times for each individual model via the API. However, these
times do not directly correlate with the update times in the Forecast API, as Open-Meteo
automatically selects the most appropriate weather model for each location (referred to as
"Best Match"). The table above provides an API link for each model, returning a JSON object
with the following fields:

* **last\_run\_initialisation\_time:** The model's initialization time or reference
  time represented as a Unix timestamp (e.g., 1724796000 for Tue Aug 27, 2024, 22:00:00 GMT+0000).
* **last\_run\_modification\_time:** The time when the data download and conversion
  were completed, which does not indicate when the data became available on the API.
* **last\_run\_availability\_time:** The time when the data is actually accessible on
  the API server. Important: Open-Meteo utilises multiple redundant API servers, so there may
  be slight differences between them while the data is being copied. To ensure all API calls use
  the most recent data, please wait 10 minutes after the availability time.
* **temporal\_resolution\_seconds:** The temporal resolution of the model in seconds.
  By default, the API interpolates the data to a 1-hour resolution. However, the underlying model
  may only provide data in 3 or 6-hourly steps. A value of 3600 indicates that the data is 1-hourly.
* **update\_interval\_seconds:** The typical time interval between model updates, such
  as 3600 seconds for a model that updates every hour.

Additional attributes, such as spatial resolution, area, grid systems, and more, will be
added in the future.
