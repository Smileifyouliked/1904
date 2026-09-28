# Open-Meteo-Docs_Docs - Api

**Pages:** 4

---

## Previous Runs API | Open-Meteo.com

**URL:** https://open-meteo.com/en/docs/previous-runs-api

**Contents:**
- Previous Model Runs API
- Location and Time
- Hourly Weather Variables
- Additional Options
- Solar Radiation Variables
- Wind on 80, 120 and 180 meter
- Weather models
- Settings
- API Response
- Data Availability

Weather Forecasts from Previous Days to Compare Run-To-Run Performance

By default, we provide forecasts for 1 day, but you can access forecasts for up to 16 days. If you're interested in past weather data, you can use the Past Days feature to access archived forecasts.

Most models are archived from January 2024. Some models were added to the archive later in 2024 or 2025 and have correspondingly shorter coverage. Exceptions with longer history:

Additional historical coverage can be reconstructed on request, subject to upstream availability from the originating weather service.

The Previous Runs API exposes forecast data at fixed lead-time offsets rather than as a seamless time-series. _previous_day0 is the current model run (equivalent to the live Forecast API). _previous_day1 is the value that was predicted 24 hours before valid time, _previous_day2 48 hours before, and so on up to day 7. For local models with shorter forecast horizons (2–5 days), only offsets within that horizon are populated.

This structure is suited to aggregated skill analysis — for example, computing the mean absolute error of all _previous_day3 forecasts against ERA5 over a calendar year. For workflows that need the complete output of a specific model run (initialisation datetime, all forecast hours, multiple variables), use the Single Runs API instead, which stores each run independently and is queryable by its UTC initialisation time via the &run= parameter.

Models: The Previous Runs API supports the same models as the Weather Forecast API. See the Forecast API documentation for the full model and variable list.

Update cadence: Global models update every 6 hours; regional models (e.g. ICON-D2, HRRR, AROME) update every 1–3 hours. The available lead-time window for each model is limited to its forecast horizon, so a model with a 3-day horizon will have at most _previous_day3 populated.

---

## Ensemble API | Open-Meteo.com

**URL:** https://open-meteo.com/en/docs/ensemble-api

**Contents:**
- Ensemble API
- Location and Time
- Ensemble Models
- Hourly Weather Variables
- Additional Variables And Options
- Solar Radiation Variables
- Pressure Level Variables
- Daily Weather Variables
- Settings
- API Response

Perturbed Weather Forecasts from Hundreds of Members

By default, we provide forecasts for 7 days, but you can access forecasts for up to 36 days. If you're interested in past weather data, you can use the Past Days feature to access archived forecasts.

Note: This API call is equivalent to 4.0 calls because of factors like long time intervals, the number of locations, variables, or models involved.

Ensemble models are a type of weather forecasting technique that use multiple members or versions of a model to produce a range of possible outcomes for a given forecast. Each member is initialized with slightly different initial conditions and/or model parameters to account for uncertainties and variations in the atmosphere, resulting in a set of perturbed forecasts.

By combining the perturbed forecasts, the ensemble model generates a probability distribution of possible outcomes, indicating not only the most likely forecast but also the range of possible outcomes and their likelihoods. This probabilistic approach provides more comprehensive and accurate forecast guidance, especially for high-impact weather events where uncertainties are high.

Different national weather services calculate ensemble models, each with varying resolutions of weather variables and forecast time-range. For instance, the German weather service DWD's ICON model provides exceptionally high resolution for Europe but only forecasts up to 7 days. Meanwhile, the GFS model can forecast up to 35 days, albeit at a lower resolution of 50 km. The appropriate ensemble model to use would depend on the forecast horizon and region of interest.

Native, full-resolution ECMWF IFS (O1280 grid) and AIFS (N320 grid) ensemble models are available for Europe, preserving original model output and offering 1-hourly timesteps for IFS. Retrieved via ECMWF pre-scheduled delivery, this data arrives significantly earlier than the standard 0.25° open-data distribution, though IFS ensembles are limited to 0z and 6z runs with a smaller set of variables.

The API endpoint /v1/ensemble accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days for each ensemble member. Time always starts at 0:00 today. All URL parameters are listed below:

Additional optional URL parameters will be added. For API stability, no required parameters will be added in the future!

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as an average or sum.

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

(*) Codes 96 and 99 are only reported by models with an explicit hail forecast, such as DWD ICON or UKMO. All other models derive thunderstorms from instability parameters and report codes 95 and 97.

The API only returns numeric weather codes. To display descriptions, map the codes on the client. The mapping below can be copied directly.

**Examples:**

Example 1 (json):
```json
{
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
	"45": "Fog",
	"48": "Depositing rime fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"
}
```

---

## Historical Forecast API | Open-Meteo.com

**URL:** https://open-meteo.com/en/docs/historical-forecast-api

**Contents:**
- Historical Forecast API
- Location and Time
- Hourly Weather Variables
- Additional Variables And Options
- Solar Radiation Variables
- Pressure Level Variables
- Weather models
- 15-Minutely Weather Variables
- Daily Weather Variables
- Additional Daily Variables

Archived High-Resolution Weather Forecasts

Past weather forecasts from 2022 onwards are available.

The weather data precisely aligns with the weather forecast API, created by continuously integrating weather forecast model data. Each update from the weather models' initial hours is compiled into a seamless time series. This extensive dataset is ideal for training machine learning models and combining them with forecast data to generate optimised predictions.

Weather models are initialized using data from weather stations, satellites, radar, airplanes, soundings, and buoys. With high update frequencies of 1, 3, or 6 hours, the resulting time series is nearly as accurate as direct measurements and offers global coverage. In regions like North America and Central Europe, the difference from local weather stations is minimal. However, for precise values such as precipitation, local measurements are preferable when available.

The Historical Forecast API archives comprehensive data, including atmospheric pressure levels, from all accessible weather forecast models. Depending on the model and public archive availability, data is available starting from 2021 or 2022.

The default Best Match option selects the most suitable high-resolution weather models for any global location, though users can also manually specify the weather model. Open-Meteo utilises the following weather forecast models:

Open-Meteo offers four distinct historical weather datasets, each suited to different use cases. Only a small fraction of the Earth's surface has reliable, continuous weather station coverage; all four datasets use numerical weather models to fill that gap globally.

As the API is identical to the Forecast API, please refer to the Weather Forecast API documentation for all available variables and parameters. The only notable difference is the API host "historical-forecast-api.open-meteo.com" as historical data is moved to a different set of servers with access to a large storage system.

---

## 🏛️ Historical Weather API | Open-Meteo.com

**URL:** https://open-meteo.com/en/docs/historical-weather-api

**Contents:**
- Historical Weather API
- Location and Time
- Hourly Weather Variables
- Additional Variables And Options
- Solar Radiation Variables
- ERA5-Ensemble Spread Variables
- Reanalysis models
- Daily Weather Variables
- Additional Daily Variables
- Settings

Discover how weather has shaped our world from 1940 until now

You can access past weather data dating back to 1940 in 0.1 or 0.25° resolution. Data from 2017 onwards uses newer weather models with 9 km resolution. Select "ERA5" or "ERA5-Land" for consistent data over multiple decades.

The Historical Weather API is based on reanalysis datasets and uses a combination of weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. These datasets are able to fill in gaps by using mathematical models to estimate the values of various weather variables. As a result, reanalysis datasets are able to provide detailed historical weather information for locations that may not have had weather stations nearby, such as rural areas or the open ocean.

The models for historical weather data use a spatial resolution of 9 km to resolve fine details close to coasts or complex mountain terrain. In general, a higher spatial resolution means that the data is more detailed and represents the weather conditions more accurately at smaller scales.

The ECMWF IFS dataset has been meticulously assembled by Open-Meteo using simulation runs daily at 0z, 6z, 12z and 18z, employing the most up-to-date version of IFS. This dataset offers the highest resolution and precision for global historical weather conditions.

However, when studying climate change over decades, it is advisable to exclusively utilise ERA5 or ERA5-Land. This choice ensures data consistency and prevents unintentional alterations that could arise from the adoption of different weather model upgrades.

You can access data dating back to 1940. If you're looking for weather information from the previous day, our Forecast API offers the &past_days= feature for your convenience.

Different reanalysis models may include different sets of weather variables. For instance, ERA5 offers a full range of variables but only at 0.25° resolution, whereas ERA5-Land focuses on surface conditions like temperature, humidity, soil temperature, and soil moisture. CERRA covers most variables but excludes soil temperature and moisture. IFS includes nearly all variables except snow depth, while IFA Assimilation omits precipitation, snowfall, and solar radiation.

1 ERA5-Land is driven by atmospheric variables from ERA5 as its "forcing," meaning it relies on the same data as ERA5.

2 Only with model “ERA5-Seamless” merging temperature and humidity from ERA5-Land with wind and solar radiation from ERA5.

The API endpoint /v1/archive allows users to retrieve historical weather data for a specific location and time period. To use this endpoint, you can specify a geographical coordinate, a time interval, and a list of weather variables that they are interested in. The endpoint will then return the requested data in a format that can be easily accessed and used by applications or other software. This endpoint can be very useful for researchers and other users who need to access detailed historical weather data for specific locations and time periods.

All URL parameters are listed below:

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as and average or sum.

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

On success a JSON object will be returned.

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error object is returned with a HTTP 400 status code.

(*) Codes 96 and 99 are only reported by models with an explicit hail forecast, such as DWD ICON or UKMO. All other models derive thunderstorms from instability parameters and report codes 95 and 97.

The API only returns numeric weather codes. To display descriptions, map the codes on the client. The mapping below can be copied directly.

We encourage researchers in the field of meteorology and related disciplines to cite Open-Meteo and its sources in their work. Citing not only gives proper credit but also promotes transparency, reproducibility, and collaboration within the scientific community. Together, let's foster a culture of recognition and support for open-data initiatives like Open-Meteo, ensuring that future researchers can benefit from the valuable resources it provides.

Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.7970649

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set]. ECMWF. https://doi.org/10.24381/cds.adbb2d47

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.E2161BAC

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021). CERRA sub-daily regional reanalysis data for Europe on single levels from 1984 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.622A565A

Generated using Copernicus Climate Change Service information 2022.

**Examples:**

Example 1 (json):
```json
{
    "latitude": 52.52,
    "longitude": 13.419,
    "elevation": 44.812,
    "generationtime_ms": 2.2119,
    "utc_offset_seconds": 0,
    "timezone": "Europe/Berlin",
    "timezone_abbreviation": "CEST",
    "hourly": {
        "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
        "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
    },
    "hourly_units": {
        "temperature_2m": "°C"
    }
}
```

Example 2 (json):
```json
{
    "error": true, 
    "reason": "Cannot initialize WeatherVariable from invalid String value
	    tempeture_2m for key hourly" 
}
```

Example 3 (json):
```json
{
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
	"45": "Fog",
	"48": "Depositing rime fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"
}
```

---
