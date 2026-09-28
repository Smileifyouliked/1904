<!--
Source: https://open-meteo.com/en/docs/historical-weather-api
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/mountains2.webp)

# Historical Weather API

Discover how weather has shaped our world from 1940 until now

 

Gap-free and consistent historical weather data using weather reanalysis from ERA5 (0.25°, from
1940) and ERA5-Land (0.1°, from 1950) and ECMWF IFS (9 km, from 2017). For data that matches the
live Forecast API format exactly, use the [Historical Forecast API](/en/docs/historical-forecast-api). To access the full forecast horizon of individual model runs, use the [Single Runs API](/en/docs/single-runs-api). To analyse
forecast accuracy at fixed lead times of 1–7 days, use the [Previous Model Runs API](/en/docs/previous-runs-api).

[## API Response](#api_response)

Preview:

Loading...

[Download XLSX](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m&format=xlsx) [Download CSV](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m&format=csv)

API URL ([Open in new tab](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2026-09-08&end_date=2026-09-22&hourly=temperature_2m), copy this URL into your application, or paste an API URL to restore its settings)

[## Data Sources](#data_sources)

The Historical Weather API is based on reanalysis datasets and uses a combination of weather
station, aircraft, buoy, radar, and satellite observations to create a comprehensive record
of past weather conditions. These datasets are able to fill in gaps by using mathematical
models to estimate the values of various weather variables. As a result, reanalysis datasets
are able to provide detailed historical weather information for locations that may not have
had weather stations nearby, such as rural areas or the open ocean.

The models for historical weather data use a spatial resolution of 9 km to resolve fine
details close to coasts or complex mountain terrain. In general, a higher spatial resolution
means that the data is more detailed and represents the weather conditions more accurately
at smaller scales.

The ECMWF IFS dataset has been meticulously assembled by Open-Meteo using simulation runs
daily at 0z, 6z, 12z and 18z, employing the most up-to-date version of IFS. This dataset
offers the highest resolution and precision for global historical weather conditions.

However, when studying climate change over decades, it is advisable to exclusively utilise
ERA5 or ERA5-Land. This choice ensures data consistency and prevents unintentional
alterations that could arise from the adoption of different weather model upgrades.

You can access data dating back to 1940. If you're looking for weather information from the
previous day, our [Forecast API](/en/docs "Weather Forecast API documentation") offers the &past\_days= feature for your convenience.

You can find the update timings in the [model updates documentation](/en/docs/model-updates).

| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
| --- | --- | --- | --- | --- | --- |
| [ECMWF IFS](https://www.ecmwf.int/en/forecasts/documentation-and-support/changes-ecmwf-model) | 🌍 Global | 9 km | Hourly | 2017 to present | Every 6 hours with no delay |
| [ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | 🌍 Global | 0.25° (~25 km) | Hourly | 1940 to present | Daily with 5 days delay |
| [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview) | 🌍 Global | 0.1° (~11 km) | Hourly | 1950 to present | Daily with 5 days delay |
| [ERA5-Ensemble](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | 🌍 Global | 0.5° (~55 km) | 3-Hourly | 1940 to present | Daily with 5 days delay |
| [CERRA](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-single-levels?tab=overview) | European Union Europe | 5 km | Hourly | 1985 to June 2021 | - |
| [ECMWF IFS Assimilation Long-Window](https://confluence.ecmwf.int/display/FUG/Section+2.6+Model+Data+Assimilation%2C+4D-Var) | 🌍 Global | 9 km | 6-Hourly | 2024 to present | Daily with 2 days delay |

Different reanalysis models may include different sets of weather variables. For instance, ERA5
offers a full range of variables but only at 0.25° resolution, whereas ERA5-Land focuses on
surface conditions like temperature, humidity, soil temperature, and soil moisture. CERRA covers
most variables but excludes soil temperature and moisture. IFS includes nearly all variables
except snow depth, while IFA Assimilation omits precipitation, snowfall, and solar radiation.

1 ERA5-Land is driven by atmospheric variables from ERA5 as its "forcing," meaning
it relies on the same data as ERA5.

2 Only with model “ERA5-Seamless” merging temperature and humidity from ERA5-Land
with wind and solar radiation from ERA5.

| Variable | ERA5 0.25° | ERA5-Land 0.1° | CERRA | IFS 9-km | IFS 9-km Assimilation |
| --- | --- | --- | --- | --- | --- |
| Temperature, Relative Humidity, Dew-point, Vapour Pressure Deficit | x | x | x | x | x |
| Soil Temperature & Moisture | x | x | - | x | x |
| Precipitation, Rain, Snowfall | x | -\*1 | x | x | - |
| Solar Radiation | x | -\*1 | x | x | x |
| Snow Depth | - | x | x | - | - |
| Wind Speed & Direction | x | -\*1 | x | x | x |
| Wind Gusts | - | x | x | x | - |
| Apparent Temperature, Reference Evapotranspiration (ET₀) | x\*2 | x | x | x | - |

[## API Documentation](#api_documentation)

The API endpoint /v1/archive allows users to retrieve historical weather data for a
specific location and time period. To use this endpoint, you can specify a geographical coordinate,
a time interval, and a list of weather variables that they are interested in. The endpoint will
then return the requested data in a format that can be easily accessed and used by applications
or other software. This endpoint can be very useful for researchers and other users who need to
access detailed historical weather data for specific locations and time periods.

All URL parameters are listed below:

Additional optional URL parameters will be added. For API stability, no required
parameters will be added in the future.

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| elevation | Floating point | No |  | The elevation used for statistical downscaling. Per default, a [90 meter digital elevation model is used](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated. |
| start\_date end\_date | String (yyyy-mm-dd) | Yes |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-12-31). |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| daily | String array | No |  | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required. |
| temperature\_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind\_speed\_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation\_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! For daily values with unix timestamp, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| cell\_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

[### Hourly Parameter Definition](#hourly_parameter_definition)

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as and average or sum.

| Variable | Valid time | Unit | Description |
| --- | --- | --- | --- |
| temperature\_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative\_humidity\_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew\_point\_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent\_temperature | Instant | °C (°F) | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation |
| pressure\_msl surface\_pressure | Instant | hPa | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation. |
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount. |
| rain | Preceding hour sum | mm (inch) | Only liquid precipitation of the preceding hour including local showers and rain from large scale systems. |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| cloud\_cover | Instant | % | Total cloud cover as an area fraction |
| cloud\_cover\_low | Instant | % | Low level clouds and fog up to 2 km altitude |
| cloud\_cover\_mid | Instant | % | Mid level clouds from 2 to 6 km altitude |
| cloud\_cover\_high | Instant | % | High level clouds from 6 km altitude |
| shortwave\_radiation | Preceding hour mean | W/m² | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation |
| direct\_radiation direct\_normal\_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun) |
| diffuse\_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour |
| global\_tilted\_irradiance | Preceding hour mean | W/m² | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west, ±180 north). If azimuth is set to "nan", the calculation assumes a vertical tracker (east-west). If tilt is set to "nan", it is assumed that the panel has a horizontal tracker (up-down). If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine\_duration | Preceding hour sum | Seconds | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| wind\_speed\_10m wind\_speed\_100m | Instant | km/h (mph, m/s, knots) | Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level. |
| wind\_direction\_10m wind\_direction\_100m | Instant | ° | Wind direction at 10 or 100 meters above ground |
| wind\_gusts\_10m | Instant | km/h (mph, m/s, knots) | Gusts at 10 meters above ground of the indicated hour. Wind gusts in CERRA are defined as the maximum wind gusts of the preceding hour. Please consult the [ECMWF IFS documentation](https://www.ecmwf.int/en/elibrary/81271-ifs-documentation-cy47r3-part-iv-physical-processes) for more information on how wind gusts are parameterized in weather models. |
| et0\_fao\_evapotranspiration | Preceding hour sum | mm (inch) | ET₀ Reference Evapotranspiration of a well watered grass field. Based on [FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm) ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants. |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation and snowfall. As barely no information about atmospheric stability is available, estimation about thunderstorms is not possible. |
| snow\_depth | Instant | meters | Snow depth on the ground. Snow depth in ERA5-Land tends to be overestimated. As the spatial resolution for snow depth is limited, please use it with care. |
| vapour\_pressure\_deficit | Instant | kPa | Vapor Pressure Deficit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases |
| soil\_temperature\_0\_to\_7cm soil\_temperature\_7\_to\_28cm soil\_temperature\_28\_to\_100cm soil\_temperature\_100\_to\_255cm | Instant | °C (°F) | Average temperature of different soil levels below ground. |
| soil\_moisture\_0\_to\_7cm soil\_moisture\_7\_to\_28cm soil\_moisture\_28\_to\_100cm soil\_moisture\_100\_to\_255cm | Instant | m³/m³ | Average soil water content as volumetric mixing ratio at 0-7, 7-28, 28-100 and 100-255 cm depths. |

[### Daily Parameter Definition](#daily_parameter_definition)

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable | Unit | Description |
| --- | --- | --- |
| weather\_code | WMO code | The most severe weather condition on a given day |
| temperature\_2m\_max temperature\_2m\_min | °C (°F) | Maximum and minimum daily air temperature at 2 meters above ground |
| apparent\_temperature\_max apparent\_temperature\_min | °C (°F) | Maximum and minimum daily apparent temperature |
| precipitation\_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| rain\_sum | mm | Sum of daily rain |
| snowfall\_sum | cm | Sum of daily snowfall |
| precipitation\_hours | hours | The number of hours with rain |
| sunrise sunset | iso8601 | Sun rise and set times |
| sunshine\_duration | seconds | The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk. |
| daylight\_duration | seconds | Number of seconds of daylight per day |
| wind\_speed\_10m\_max wind\_gusts\_10m\_max | km/h (mph, m/s, knots) | Maximum wind speed and gusts on a day |
| wind\_direction\_10m\_dominant | ° | Dominant wind direction |
| shortwave\_radiation\_sum | MJ/m² | The sum of solar radiaion on a given day in Megajoules |
| et0\_fao\_evapotranspiration | mm | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field |

[### JSON Return Object](#json_return_object)

On success a JSON object will be returned.

```
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

| Parameter | Format | Description |
| --- | --- | --- |
| latitude, longitude | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometres away from the requested coordinate. |
| elevation | Floating point | The elevation from a 90 meter digital elevation model. This effects which grid-cell is selected (see parameter cell\_selection). Statistical downscaling is used to adapt weather conditions for this elevation. This elevation can also be controlled with the query parameter elevation. If &elevation=nan is specified, all downscaling is disabled and the average grid-cell elevation is used. |
| generationtime\_ms | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements. |
| utc\_offset\_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone\_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| hourly\_units | Object | For each selected weather variable, the unit will be listed here. |
| daily | Object | For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| daily\_units | Object | For each selected daily weather variable, the unit will be listed here. |

[### Errors](#errors)

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```
{
    "error": true, 
    "reason": "Cannot initialize WeatherVariable from invalid String value
	    tempeture_2m for key hourly" 
}
```

[## Weather variable documentation](#weather_variable_documentation)

### WMO Weather interpretation codes (WW)

| Code | Description |
| --- | --- |
| 0 | Clear sky |
| 1 | Mainly clear |
| 2 | Partly cloudy |
| 3 | Overcast |
| 45 | Fog |
| 48 | Depositing rime fog |
| 51 | Light drizzle |
| 53 | Moderate drizzle |
| 55 | Dense drizzle |
| 56 | Light freezing drizzle |
| 57 | Dense freezing drizzle |
| 61 | Slight rain |
| 63 | Moderate rain |
| 65 | Heavy rain |
| 66 | Light freezing rain |
| 67 | Heavy freezing rain |
| 71 | Slight snowfall |
| 73 | Moderate snowfall |
| 75 | Heavy snowfall |
| 77 | Snow grains |
| 80 | Slight rain showers |
| 81 | Moderate rain showers |
| 82 | Violent rain showers |
| 85 | Slight snow showers |
| 86 | Heavy snow showers |
| 95 | Thunderstorm |
| 96 | Thunderstorm with slight hail \* |
| 97 | Heavy thunderstorm |
| 99 | Thunderstorm with heavy hail \* |

(\*) Codes 96 and 99 are only reported by models with an explicit hail forecast, such as DWD ICON
or UKMO. All other models derive thunderstorms from instability parameters and report codes 95
and 97.

#### Weather code descriptions as JSON

The API only returns numeric weather codes. To display descriptions, map the codes on the
client. The mapping below can be copied directly.

```
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

[## Citation & Acknowledgement](#citation)

We encourage researchers in the field of meteorology and related disciplines to cite
Open-Meteo and its sources in their work. Citing not only gives proper credit but also
promotes transparency, reproducibility, and collaboration within the scientific community.
Together, let's foster a culture of recognition and support for open-data initiatives like
Open-Meteo, ensuring that future researchers can benefit from the valuable resources it
provides.

Citation:

Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. [https://doi.org/10.5281/ZENODO.7970649](https://doi.org/10.5281/ZENODO.7970649 "zenodo publication")

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C.,
Dee, D., Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present
[Data set]. ECMWF. [https://doi.org/10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47 "era5-land")

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set].
ECMWF. [https://doi.org/10.24381/CDS.E2161BAC](https://doi.org/10.24381/CDS.E2161BAC "era5-land")

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R.,
Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said
A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q.
(2021). CERRA sub-daily regional reanalysis data for Europe on single levels from 1984
to present [Data set]. ECMWF. [https://doi.org/10.24381/CDS.622A565A](https://doi.org/10.24381/CDS.622A565A "cerra")

Generated using Copernicus Climate Change Service information 2022.
