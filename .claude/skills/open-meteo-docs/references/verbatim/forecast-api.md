<!--
Source: https://open-meteo.com/en/docs
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/partly_cloudy.webp)

# Weather Forecast API

Seamless integration of high-resolution weather models with up 16 days forecast

 

[## API Response](#api_response)

Preview:

Loading...

[Download XLSX](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&format=xlsx) [Download CSV](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&format=csv)

API URL ([Open in new tab](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m), copy this URL into your application, or paste an API URL to restore its settings)

[## Data Sources](#data_sources)

Open-Meteo combines weather model output from multiple national weather services into a
continuous, seamlessly updated timeseries. Each time a model run is ingested, the forecast
data are stitched to the previous run without gaps or discontinuities, so the hourly
timeseries always reflects the latest available initialisation. For each location, the
highest-resolution applicable model is selected automatically.

Weather models cover different geographic areas at different resolutions and provide
different weather variables. Depending on the model, data have been interpolated to hourly
values or not all weather variables are available. Use the Weather models dropdown (just below the hourly variables) to select and compare individual models. To access
the full archive of past forecast runs as issued, useful for forecast verification or training
ML models, see the [Historical Forecast API](/en/docs/historical-forecast-api) and the [Single Runs API](/en/docs/single-runs-api).

You can find the update timings in the [model updates documentation](/en/docs/model-updates).

| Weather Model | Region | National Weather Provider | Origin Country | Resolution | Forecast Length | Update frequency |
| --- | --- | --- | --- | --- | --- | --- |
| [ICON](/en/docs/dwd-api) | 🌍 European Union Global & Europe | Deutscher Wetterdienst (DWD) | Germany | 2 - 11 km | 7.5 days | Every 3 hours |
| [GFS & HRRR](/en/docs/gfs-api) | 🌍 United States Canada Global & North America | NOAA | United States | 3 - 25 km | 16 days | Every hour |
| [ARPEGE & AROME](/en/docs/meteofrance-api) | 🌍 European Union France Global, Europe & France | Météo-France | France | 1 - 25 km | 4 days | Every hour |
| [IFS & AIFS](/en/docs/ecmwf-api) | 🌍 Global | ECMWF | European Union | 9 - 25km | 15 days | Every 6 hours |
| [UKMO](/en/docs/ukmo-api) | 🌍 United Kingdom Global & UK | UK Met Office | United Kingdom | 2 - 10 km | 7 days | Every hour |
| [KMA](/en/docs/kma-api) | 🌍 South Korea Global & South Korea | KMA Korea | Korea | 1.5 - 13 km | 12 days | Every 6 hours |
| [MSM & GSM](/en/docs/jma-api) | 🌍 Japan Global & Japan | JMA | Japan | 5 - 55 km | 11 days | Every 3 hours |
| [ICON CH](/en/docs/meteoswiss-api) | Switzerland Central Europe | MeteoSwiss | Switzerland | 1 - 2 km | 5 days | Every 3 hours |
| [MET Nordic](/en/docs/metno-api) | Norway Sweden Denmark Nordic | MET Norway | Norway | 1 km | 2.5 days | Every hour |
| [GEM](/en/docs/gem-api) | 🌍 Canada Global & Canada | Canadian Weather Service | Canada | 2.5 km | 10 days | Every 6 hours |
| [ACCESS-G](/en/docs/bom-api) | 🌍 Global | Australian Bureau of Meteorology (BOM) | Australia | 15 km | 10 days | Every 6 hours |
| [GFS GRAPES](/en/docs/cma-api) | 🌍 Global | China Meteorological Administration (CMA) | China | 15 km | 10 days | Every 6 hours |
| [HARMONIE](/en/docs/knmi-api) | European Union Netherlands Europe & Netherlands | KNMI | Netherlands | 2 km | 2.5 days | Every hour |
| [HARMONIE](/en/docs/dmi-api) | European Union Europe | DMI | Denmark | 2 km | 2.5 days | Every 3 hours |
| [ARPAE](/en/docs/italia-meteo-arpae-api) | Italy Italy | ItaliaMeteo | Italy | 2 km | 3 days | Every 12 hours |
| [AROME](/en/docs/geosphere-austria-api) | Austria Central Europe | GeoSphere Austria | Austria | 2.5 km | 2.5 days | Every 3 hours |
| [ALADIN](/en/docs/chmi-api) | European Union Czech Republic Central Europe | CHMI | Czech Republic | 1 - 2.3 km | 3 days | Every 6 hours |

[## API Documentation](#api_documentation)

The API endpoint /v1/forecast accepts a geographical coordinate, a list of
weather variables and responds with a JSON hourly weather forecast for 7 days. Time always
starts at 0:00 today and contains 168 hours. If &forecast\_days=16 is set, up to 16 days of forecast can be returned. All URL parameters
are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude, longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. For North and South America locations use negative longitudes, because they lie west of Greenwich. |
| elevation | Floating point | No |  | The elevation used for statistical downscaling. Per default, a [90 meter digital elevation model is used](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated. |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| daily | String array | No |  | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required. |
| current | String array | No |  | A list of weather variables to get current conditions. |
| temperature\_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind\_speed\_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation\_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| past\_days | Integer (0-92) | No | 0 | If past\_days is set, yesterday or the day before yesterday data are also returned. |
| forecast\_days | Integer (0-16) | No | 7 | Per default, only 7 days are returned. Up to 16 days of forecast are possible. |
| forecast\_hours forecast\_minutely\_15 past\_hours past\_minutely\_15 | Integer (>0) | No |  | Similar to forecast\_days, the number of timesteps of hourly and 15-minutely data can controlled. Instead of using the current day as a reference, the current hour or the current 15-minute time-step is used. |
| start\_date end\_date | String (yyyy-mm-dd) | No |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). |
| start\_hour end\_hour start\_minutely\_15 end\_minutely\_15 | String (yyyy-mm-ddThh:mm) | No |  | The time interval to get weather data for hourly or 15 minutely data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00). |
| models | String array | No | auto | Manually select one or more weather models. Per default, the best suitable weather models will be combined. |
| cell\_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters
will be added in the future!

[### Hourly Parameter Definition](#hourly_parameter_definition)

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as an average or sum.

| Variable | Valid time | Unit | Description |
| --- | --- | --- | --- |
| temperature\_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative\_humidity\_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew\_point\_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent\_temperature | Instant | °C (°F) | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation |
| pressure\_msl surface\_pressure | Instant | hPa | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation. |
| cloud\_cover | Instant | % | Total cloud cover as an area fraction |
| cloud\_cover\_low | Instant | % | Low level clouds and fog up to 3 km altitude |
| cloud\_cover\_mid | Instant | % | Mid level clouds from 3 to 8 km altitude |
| cloud\_cover\_high | Instant | % | High level clouds from 8 km altitude |
| wind\_speed\_10m wind\_speed\_80m wind\_speed\_120m wind\_speed\_180m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 80, 120 or 180 meters above ground. Wind speed on 10 meters is the standard level. |
| wind\_direction\_10m wind\_direction\_80m wind\_direction\_120m wind\_direction\_180m | Instant | ° | Wind direction at 10, 80, 120 or 180 meters above ground |
| wind\_gusts\_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave\_radiation | Preceding hour mean | W/m² | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation |
| direct\_radiation direct\_normal\_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun) |
| diffuse\_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour |
| global\_tilted\_irradiance | Preceding hour mean | W/m² | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west, ±180 north). If azimuth is set to "nan", the calculation assumes a vertical tracker (east-west). If tilt is set to "nan", it is assumed that the panel has a horizontal tracker (up-down). If both are set to "nan", a bi-axial tracker is assumed. |
| vapour\_pressure\_deficit | Instant | kPa | Vapour Pressure Deficit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases |
| cape | Instant | J/kg | Convective available potential energy. See [Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy). |
| evapotranspiration | Preceding hour sum | mm (inch) | Evapotranspiration from land surface and plants that weather models assumes for this location. Available soil water is considered. 1 mm evapotranspiration per hour equals 1 liter of water per square meter. |
| et0\_fao\_evapotranspiration | Preceding hour sum | mm (inch) | ET₀ Reference Evapotranspiration of a well watered grass field. Based on [FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm) ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants. |
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| precipitation\_probability | Preceding hour probability | % | Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution. 30 different simulations are computed to better represent future weather conditions. |
| rain | Preceding hour sum | mm (inch) | Rain from large scale weather systems of the preceding hour in millimeter |
| showers | Preceding hour sum | mm (inch) | Showers from convective precipitation in millimeters from the preceding hour |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. |
| snow\_depth | Instant | meters | Snow depth on the ground |
| freezing\_level\_height | Instant | meters | Altitude above sea level of the 0°C level |
| visibility | Instant | meters | Viewing distance in meters. Influenced by low clouds, humidity and aerosols. |
| soil\_temperature\_0cm soil\_temperature\_6cm soil\_temperature\_18cm soil\_temperature\_54cm | Instant | °C (°F) | Temperature in the soil at 0, 6, 18 and 54 cm depths. 0 cm is the surface temperature on land or water surface temperature on water. |
| soil\_moisture\_0\_to\_1cm soil\_moisture\_1\_to\_3cm soil\_moisture\_3\_to\_9cm soil\_moisture\_9\_to\_27cm soil\_moisture\_27\_to\_81cm | Instant | m³/m³ | Average soil water content as volumetric mixing ratio at 0-1, 1-3, 3-9, 9-27 and 27-81 cm depths. |
| is\_day | Instant | Dimensionless | 1 if the current time step has daylight, 0 at night. |

[### 15-Minutely Parameter Definition](#15_minutely_parameter_definition)

The parameter &minutely\_15= can be used to get 15-minutely data. This data is based
on NOAA HRRR model for North America and DWD ICON-D2 and Météo-France AROME model for Central Europe.
If 15-minutely data is requested for other regions data is interpolated from 1-hourly to 15-minutely.

15-minutely data can be requested for other weather variables that are available for hourly
data, but will use interpolation.

| Variable | Valid time | Unit | HRRR | ICON-D2 | AROME |
| --- | --- | --- | --- | --- | --- |
| temperature\_2m | Instant | °C (°F) | x |  | x |
| relative\_humidity\_2m | Instant | % | x |  | x |
| dew\_point\_2m | Instant | °C (°F) | x |  | x |
| apparent\_temperature | Instant | °C (°F) | x |  | x |
| shortwave\_radiation | Preceding 15 minutes mean | W/m² | x | x |  |
| direct\_radiation direct\_normal\_irradiance | Preceding 15 minutes mean | W/m² | x | x |  |
| global\_tilted\_irradiance global\_tilted\_irradiance\_instant | Preceding 15 minutes mean | W/m² | x | x |  |
| diffuse\_radiation | Preceding 15 minutes mean | W/m² | x | x |  |
| sunshine\_duration | Preceding 15 minutes sum | seconds | x | x |  |
| lightning\_potential | Instant | J/kg |  | x |  |
| precipitation | Preceding 15 minutes sum | mm (inch) | x | x | x |
| snowfall | Preceding 15 minutes sum | cm (inch) | x | x | x |
| rain | Preceding 15 minutes sum | mm (inch) | x | x | x |
| showers | Preceding 15 minutes sum | mm (inch) |  | x |  |
| snowfall\_height | Instant | meters |  | x |  |
| freezing\_level\_height | Instant | meters |  | x |  |
| cape | Instant | J/kg | x | x | x |
| wind\_speed\_10m wind\_speed\_80m | Instant | km/h (mph, m/s, knots) | x |  | x |
| wind\_direction\_10m wind\_direction\_80m | Instant | ° | x |  | x |
| wind\_gusts\_10m | Preceding 15 min max | km/h (mph, m/s, knots) | x |  |  |
| visibility | Instant | meters | x |  | x |
| weather\_code | Instant | WMO code | x | x |  |

[### Pressure Level Variables](#pressure_level_variables)

Pressure level variables do not have fixed altitudes. Altitude varies with atmospheric
pressure. 1000 hPa is roughly between 60 and 160 meters above sea level. Estimated altitudes
are given below. Altitudes are in meters above sea level (not above ground). For precise
altitudes, geopotential\_height can be used.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Level (hPa) | 1000 | 975 | 950 | 925 | 900 | 850 | 800 | 700 | 600 | 500 | 400 | 300 | 250 | 200 | 150 | 100 | 70 | 50 | 30 |
| Altitude | 110 m | 320 m | 500 m | 800 m | 1000 m | 1500 m | 1900 m | 3 km | 4.2 km | 5.6 km | 7.2 km | 9.2 km | 10.4 km | 11.8 km | 13.5 km | 15.8 km | 17.7 km | 19.3 km | 22 km |

All pressure levels have valid times of the indicated hour (instant).

| Variable | Unit | Description |
| --- | --- | --- |
| temperature\_1000hPa temperature\_975hPa, ... | °C (°F) | Air temperature at the specified pressure level. Air temperatures decrease linearly with pressure. |
| relative\_humidity\_1000hPa relative\_humidity\_975hPa, ... | % | Relative humidity at the specified pressure level. |
| dew\_point\_1000hPa dew\_point\_975hPa, ... | °C (°F) | Dew point temperature at the specified pressure level. |
| cloud\_cover\_1000hPa cloud\_cover\_975hPa, ... | % | Cloud cover at the specified pressure level. Cloud cover is approximated based on relative humidity using [Sundqvist et al. (1989)](https://www.ecmwf.int/sites/default/files/elibrary/2005/16958-parametrization-cloud-cover.pdf). It may not match perfectly with low, mid and high cloud cover variables. |
| wind\_speed\_1000hPa wind\_speed\_975hPa, ... | km/h (mph, m/s, knots) | Wind speed at the specified pressure level. |
| wind\_direction\_1000hPa wind\_direction\_975hPa, ... | ° | Wind direction at the specified pressure level. |
| geopotential\_height\_1000hPa geopotential\_height\_975hPa, ... | meter | Geopotential height at the specified pressure level. This can be used to get the correct altitude in meter above sea level of each pressure level. Be careful not to mistake it with altitude above ground. |

[### Daily Parameter Definition](#daily_parameter_definition)

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable | Unit | Description |
| --- | --- | --- |
| temperature\_2m\_max temperature\_2m\_mean temperature\_2m\_min | °C (°F) | Maximum and minimum daily air temperature at 2 meters above ground |
| apparent\_temperature\_max apparent\_temperature\_mean apparent\_temperature\_min | °C (°F) | Maximum and minimum daily apparent temperature |
| precipitation\_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| rain\_sum | mm | Sum of daily rain |
| showers\_sum | mm | Sum of daily showers |
| snowfall\_sum | cm | Sum of daily snowfall |
| precipitation\_hours | hours | The number of hours with rain |
| precipitation\_probability\_max precipitation\_probability\_mean precipitation\_probability\_min | % | Probability of precipitation |
| weather\_code | WMO code | The most severe weather condition on a given day |
| sunrise sunset | iso8601 | Sun rise and set times |
| sunshine\_duration | seconds | The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk. |
| daylight\_duration | seconds | Number of seconds of daylight per day |
| wind\_speed\_10m\_max wind\_gusts\_10m\_max | km/h (mph, m/s, knots) | Maximum wind speed and gusts on a day |
| wind\_direction\_10m\_dominant | ° | Dominant wind direction |
| shortwave\_radiation\_sum | MJ/m² | The sum of solar radiation on a given day in Megajoules |
| et0\_fao\_evapotranspiration | mm | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field |
| uv\_index\_max uv\_index\_clear\_sky\_max | Index | Daily maximum in UV Index starting from 0. uv\_index\_clear\_sky\_max assumes cloud free conditions. Please follow the [official WMO guidelines](https://www.who.int/news-room/questions-and-answers/item/radiation-the-ultraviolet-(uv)-index) for ultraviolet index. |

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
| current | Object | For every chosen current weather variable, the data is provided as a numeric value. In addition, time specifies the moment at which the data is valid. The interval represents the duration in seconds used for calculating backward-looking sums or averages. For instance, an interval of 900 seconds (15 minutes) means that aggregated metrics such as precipitation reflect the total from the previous 15 minutes. |
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
