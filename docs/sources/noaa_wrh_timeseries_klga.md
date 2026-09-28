<!--
Source: https://www.weather.gov/source/wrh/timeseries/obs.js?v202601121730 (script behind https://www.weather.gov/wrh/timeseries?site=klga)
and https://www.weather.gov/wrh/timeseries?site=klga (help text)
Fetched: 2026-09-28 (UTC). Excerpts copied verbatim; the API token variable is not reproduced.
-->

# NOAA timeseries page: how the "Temp" column is built

## Data request (obs.js lines 300-304; the page uses a Synoptic API token we must not reuse)

```js
      var InfoToGet = 'https://api.synopticdata.com/v2/stations/timeseries?STID='+SITE+'&showemptystations=1&units=temp|F,speed|mph,english&start='+start+'0000&end='+end+'2359&complete=1&token=<NWS token>&obtimezone=local';
```

## Temp cell (obs.js lines 378-379)

```js
            if (DATA.STATION[0].OBSERVATIONS.air_temp_set_1[j] !== null) {
              var TEMP_F = '<td>'+Math.round(DATA.STATION[0].OBSERVATIONS.air_temp_set_1[j])+'</td>';
```

## Hourly Data definition (page help text)

Hourly Data: By default, the page will display all data for a given time period. If "Yes" is checked, the page will only display data where the observation time stamp has between "51" and "59" in the minutes field for NWS/FAA observation platforms (to include any "SPECI" observations/data - with the date&time stamp highlighted in yellow), and between "56" and "04" for all other platforms.
