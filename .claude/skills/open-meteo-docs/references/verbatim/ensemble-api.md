<!--
Source: https://open-meteo.com/en/docs/ensemble-api
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

![](/images/backgrounds/rocky_coast.webp)

# Ensemble API

Perturbed Weather Forecasts from Hundreds of Members

 

This API offers access to individual ensemble member forecasts from various weather models. You
can retrieve up to three days of historical data. Additionally, we store [ensemble means and spreads](/en/docs/ensemble-mean-api "Ensemble Mean API") with a longer retention period. For more information on ensemble models, see this [blog article](https://openmeteo.substack.com/p/ensemble-weather-forecast-api).

[## API Response](#api_response)

Preview:

Loading...

[Download XLSX](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless_eps&format=xlsx) [Download CSV](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless_eps&format=csv)

API URL ([Open in new tab](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless_eps), copy this URL into your application, or paste an API URL to restore its settings)

Note: This API call is equivalent to **4.0** calls because
of factors like long time intervals, the number of locations, variables, or models involved.

[## Data Sources](#data_sources)

Ensemble models are a type of weather forecasting technique that use multiple members or
versions of a model to produce a range of possible outcomes for a given forecast. Each member
is initialized with slightly different initial conditions and/or model parameters to account
for uncertainties and variations in the atmosphere, resulting in a set of perturbed forecasts.

By combining the perturbed forecasts, the ensemble model generates a probability distribution
of possible outcomes, indicating not only the most likely forecast but also the range of
possible outcomes and their likelihoods. This probabilistic approach provides more
comprehensive and accurate forecast guidance, especially for high-impact weather events where
uncertainties are high.

Different national weather services calculate ensemble models, each with varying resolutions
of weather variables and forecast time-range. For instance, the German weather service DWD's
ICON model provides exceptionally high resolution for Europe but only forecasts up to 7 days.
Meanwhile, the GFS model can forecast up to 35 days, albeit at a lower resolution of 50 km.
The appropriate ensemble model to use would depend on the forecast horizon and region of
interest.

Native, full-resolution ECMWF IFS (O1280 grid) and AIFS (N320 grid) ensemble models are
available for Europe, preserving original model output and offering 1-hourly timesteps for
IFS. Retrieved via ECMWF pre-scheduled delivery, this data arrives significantly earlier than
the standard 0.25° open-data distribution, though IFS ensembles are limited to 0z and 6z runs
with a smaller set of variables.

You can find the update timings in the [model updates documentation](/en/docs/model-updates). To ensure ease of use, all data is interpolated to a 1-hourly time-step resolution. As
the forecast horizon extends further into the future, some ensemble models may reduce the
time resolution to 6-hourly intervals.

| National Weather Service | Weather Model | Region | Resolution | Members | Forecast Length | Update frequency |
| --- | --- | --- | --- | --- | --- | --- |
| Deutscher Wetterdienst (DWD) | ICON-D2-EPS | Germany Switzerland Austria Central Europe | 2 km, hourly | 20 | 2 days | Every 3 hours |
| ICON-EU-EPS | European Union Europe | 13 km, hourly | 40 | 5 days | Every 6 hours |
| ICON-EPS | 🌍 Global | 26 km, hourly | 40 | 7.5 days | Every 12 hours |
| NOAA | GFS Ensemble 0.25° | 🌍 Global | 0.25° (~25km), 3-hourly | 31 | 10 days | Every 6 hours |
| GFS Ensemble 0.5° | 🌍 Global | 50 km, 3-hourly | 31 | 35 days | Every 6 hours |
| AIGFS 0.25° | 🌍 Global | 0.25° (~25km), 6-hourly | 31 | 16 days | Every 6 hours |
| ECMWF | IFS 0.25° | 🌍 Global | 0.25° (~25km), 3-hourly | 51 | 15 days | Every 6 hours |
| AIFS 0.25° | 🌍 Global | 0.25° (~25km), 6-hourly | 51 | 15 days | Every 6 hours |
| IFS Europe (native O1280) | European Union Europe | 9-km, 1-hourly, 3-hourly after 90 hours, 6-hourly after 144 hours | 51 | 15 days | Only 0z and 6z run |
| AIFS Europe (native N320) | European Union Europe | 31 km, 6-hourly | 51 | 15 days | Every 6 hours |
| Canadian Weather Service | GEM | 🌍 Global | 0.25° (~25km), 3-hourly | 21 | 16 days (39 days every Mo+Thu) | Every 12 hours |
| Australian Bureau of Meteorology (BOM) | ACCESS-GE | 🌍 Global | 40 km, 3-hourly | 18 | 10 days | Every 6 hours |
| UK Met Office | MOGREPS-UK | United Kingdom UK | 2 km, 1-hourly | 3 | 5 days | Every hour |
| MOGREPS-G | 🌍 Global | 20 km, 1-hourly | 18 | 8 days | Every 6 hours |
| MeteoSwiss | ICON CH1 | Switzerland Central Europe | 1 km, 1-hourly | 11 | 33 hours | Every 3 hours |
| ICON CH2 | Switzerland Central Europe | 2 km, 1-hourly | 21 | 12 hours | Every 6 hours |
| Google | WeatherNext 2 | 🌍 Global | 0.25° (~25km), 6-hourly | 64 | 15 days | Every 12 hours |

[## API Documentation](#api_documentation)

The API endpoint /v1/ensemble accepts a geographical coordinate, a list of weather
variables and responds with a JSON hourly weather forecast for 7 days for each ensemble member.
Time always starts at 0:00 today. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude, longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| models | String array | Yes |  | Select one or more ensemble weather models as comma-separated list |
| elevation | Floating point | No |  | The elevation used for statistical downscaling. Per default, a [90 meter digital elevation model is used](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated. |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| temperature\_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind\_speed\_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation\_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| past\_days | Integer | No | 0 | If past\_days is set, past weather data can be returned. |
| forecast\_days | Integer (0-35) | No | 7 | Per default, only 7 days are returned. Up to 35 days of forecast are possible. |
| forecast\_hours forecast\_minutely\_15 past\_hours past\_minutely\_15 | Integer (>0) | No |  | Similar to forecast\_days, the number of timesteps of hourly and 15-minutely data can controlled. Instead of using the current day as a reference, the current hour or the current 15-minute time-step is used. |
| start\_date end\_date | String (yyyy-mm-dd) | No |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). |
| start\_hour end\_hour start\_minutely\_15 end\_minutely\_15 | String (yyyy-mm-ddThh:mm) | No |  | The time interval to get weather data for hourly or 15 minutely data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00). |
| cell\_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

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
| wind\_speed\_10m wind\_speed\_80m wind\_speed\_100m  wind\_speed\_120m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 80, 100 or 120 meters above ground. Wind speed on 10 meters is the standard level. |
| wind\_direction\_10m wind\_direction\_80m wind\_direction\_100m wind\_direction\_120m | Instant | ° | Wind direction at 10, 80, 100 or 120 meters above ground |
| wind\_gusts\_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave\_radiation | Preceding hour mean | W/m² | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation |
| direct\_radiation direct\_normal\_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun). HRRR offers direct radiation directly. In GFS it is approximated based on [Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf) |
| diffuse\_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour. HRRR offers diffuse radiation directly. In GFS it is approximated based on [Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf) |
| global\_tilted\_irradiance | Preceding hour mean | W/m² | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west, ±180 north). If azimuth is set to "nan", the calculation assumes a vertical tracker (east-west). If tilt is set to "nan", it is assumed that the panel has a horizontal tracker (up-down). If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine\_duration | Preceding hour sum | Seconds | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| vapour\_pressure\_deficit | Instant | kPa | Vapor Pressure Deficit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases |
| evapotranspiration | Preceding hour sum | mm (inch) | Evapotranspiration from land surface and plants that weather models assumes for this location. Available soil water is considered. 1 mm evapotranspiration per hour equals 1 liter of water per square meter. |
| et0\_fao\_evapotranspiration | Preceding hour sum | mm (inch) | ET₀ Reference Evapotranspiration of a well watered grass field. Based on [FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm) ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants. |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation, snowfall, cape, lifted index and gusts. |
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| rain | Preceding hour sum | mm (inch) | Liquid precipitation of the preceding hour in millimeter |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. |
| snow\_depth | Instant | meters | Snow depth on the ground |
| freezing\_level\_height | Instant | meters | Altitude above sea level of the 0°C level |
| visibility | Instant | meters | Viewing distance in meters. Influenced by low clouds, humidity and aerosols. |
| cape | Instant | J/kg | Convective available potential energy. See [Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy). |
| surface\_temperature | Instant | °C (°F) | Temperature of the top soil level |
| soil\_temperature\_0\_to\_10cm soil\_temperature\_10\_to\_40cm soil\_temperature\_40\_to\_100cm soil\_temperature\_100\_to\_200cm | Instant | °C (°F) | Temperature in the soil as an average on 0-10, 10-40, 40-100 and 100-200 cm depths. |
| soil\_moisture\_0\_to\_10cm soil\_moisture\_10\_to\_40cm soil\_moisture\_40\_to\_100cm soil\_moisture\_100\_to\_200cm | Instant | m³/m³ | Average soil water content as volumetric mixing ratio at 0-10, 10-40, 40-100 and 100-200 cm depths. |

[### Daily Parameter Definition](#daily_parameter_definition)

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable | Unit | Description |
| --- | --- | --- |
| temperature\_2m\_max temperature\_2m\_mean temperature\_2m\_min | °C (°F) | Maximum, mean and minimum daily air temperature at 2 meters above ground |
| apparent\_temperature\_max apparent\_temperature\_mean apparent\_temperature\_min | °C (°F) | Maximum, mean and minimum daily apparent temperature |
| cloud\_cover\_max cloud\_cover\_mean cloud\_cover\_min | % | Maximum, mean and minimum cloud cover as an area fraction |
| relative\_humidity\_2m\_max relative\_humidity\_2m\_mean relative\_humidity\_2m\_min | % | Maximum, mean and minimum relative humidity at 2 meters above ground |
| rain\_sum | mm | Sum of daily rain |
| snowfall\_sum | cm | Sum of daily snowfall |
| precipitation\_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| precipitation\_hours | hours | The number of hours with rain |
| pressure\_msl\_max pressure\_msl\_mean pressure\_msl\_min surface\_pressure\_max surface\_pressure\_mean surface\_pressure\_min | hPa | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation. |
| wind\_speed\_10m\_max wind\_speed\_10m\_mean wind\_speed\_10m\_min wind\_gusts\_10m\_max wind\_gusts\_10m\_mean wind\_gusts\_10m\_min | km/h (mph, m/s, knots) | Maximum, mean and minimum wind speed and gusts on a day |
| wind\_direction\_10m\_dominant wind\_direction\_100m\_dominant | ° | Dominant wind direction |
| dew\_point\_2m\_max dew\_point\_2m\_mean dew\_point\_2m\_min | °C (°F) | Dew point temperature at 2 meters above ground |
| shortwave\_radiation\_sum | MJ/m² | The sum of solar radiation on a given day in Megajoules |
| cape\_max cape\_mean  cape\_min | J/kg | Convective available potential energy. See [Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy). |
| et0\_fao\_evapotranspiration | mm | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field |

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

## Model checkboxes on this page (raw checkbox id -> label)

The id is `<api_name>_<group>_models`. Confirm an API name with a live call before use.

- `icon_seamless_eps_models` -> DWD ICON EPS Seamless
- `icon_global_eps_models` -> DWD ICON EPS Global
- `icon_eu_eps_models` -> DWD ICON EPS EU
- `icon_d2_eps_models` -> DWD ICON EPS D2
- `ncep_gefs_seamless_models` -> GFS Ensemble Seamless
- `ncep_gefs025_models` -> GFS Ensemble 0.25°
- `ncep_gefs05_models` -> GFS Ensemble 0.5°
- `ncep_aigefs025_models` -> AIGEFS 0.25°
- `ecmwf_ifs025_ensemble_models` -> ECMWF IFS 0.25° Ensemble
- `ecmwf_ifs_europe_ensemble_models` -> ECMWF IFS 9 km (O1280) Europe Ensemble
- `ecmwf_aifs025_ensemble_models` -> ECMWF AIFS 0.25° Ensemble
- `ecmwf_aifs_europe_ensemble_models` -> ECMWF AIFS 31 km (N320) Europe Ensemble
- `ukmo_global_ensemble_20km_models` -> UK MetOffice Global 20km
- `ukmo_uk_ensemble_2km_models` -> UK MetOffice UK 2km
- `gem_global_ensemble_models` -> GEM Global Ensemble
- `meteoswiss_icon_ch1_ensemble_models` -> MeteoSwiss ICON CH1
- `meteoswiss_icon_ch2_ensemble_models` -> MeteoSwiss ICON CH2
- `google_weathernext2_ensemble_models` -> Google WeatherNext 2 Ensemble
