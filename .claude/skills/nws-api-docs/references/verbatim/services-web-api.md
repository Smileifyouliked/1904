<!--
Source: https://www.weather.gov/documentation/services-web-api
Fetched: 2026-09-28 (UTC)
Mode: html (verbatim official text, not edited)
-->

[![National Weather Service](/bundles/templating/images/header/header.png)](https://www.weather.gov)
[![United States Department of Commerce](/bundles/templating/images/header/header_doc.png)](http://www.commerce.gov)

* [HOME](#)
* [FORECAST](https://www.weather.gov/forecastmaps/)

  + [Local](https://www.weather.gov)
  + [Graphical](https://digital.weather.gov)
  + [Aviation](https://aviationweather.gov)
  + [Marine](https://www.weather.gov/marine/)
  + [Rivers and Lakes](https://water.noaa.gov)
  + [Hurricanes](https://www.nhc.noaa.gov)
  + [Severe Weather](https://www.spc.noaa.gov)
  + [Fire Weather](https://www.weather.gov/fire/)
  + [Sunrise/Sunset](https://gml.noaa.gov/grad/solcalc/)
  + [Long Range Forecasts](https://www.cpc.ncep.noaa.gov)
  + [Climate Prediction](https://www.cpc.ncep.noaa.gov)
  + [Space Weather](https://www.swpc.noaa.gov)
* [PAST WEATHER](https://www.weather.gov/wrh/climate)

  + [Past Weather](https://www.weather.gov/wrh/climate)
  + [Astronomical Data](https://gml.noaa.gov/grad/solcalc/)
  + [Certified Weather Data](https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table)
* [SAFETY](https://www.weather.gov/safety/)
* [INFORMATION](https://www.weather.gov/informationcenter)

  + [Wireless Emergency Alerts](https://www.weather.gov/wrn/wea)
  + [Weather-Ready Nation](https://www.weather.gov/wrn/)
  + [Brochures](https://www.weather.gov/owlie/publication_brochures)
  + [Cooperative Observers](https://www.weather.gov/coop/)
  + [Daily Briefing](https://www.weather.gov/briefing/)
  + [Damage/Fatality/Injury Statistics](https://www.weather.gov/hazstat)
  + [Forecast Models](http://mag.ncep.noaa.gov)
  + [GIS Data Portal](https://www.weather.gov/gis/)
  + [NOAA Weather Radio](https://www.weather.gov/nwr)
  + [Publications](https://www.weather.gov/publications/)
  + [SKYWARN Storm Spotters](https://www.weather.gov/skywarn/)
  + [StormReady](https://www.weather.gov/stormready)
  + [TsunamiReady](https://www.weather.gov/tsunamiready/)
  + [Service Change Notices](https://www.weather.gov/notification/)
* [EDUCATION](https://www.weather.gov/education/)
* [NEWS](https://www.weather.gov/news)
* [SEARCH](https://www.weather.gov/search/)
* [ABOUT](https://www.weather.gov/about/)

  + [About NWS](https://www.weather.gov/about/)
  + [Organization](https://www.weather.gov/organization)
  + [For NWS Employees](https://sites.google.com/a/noaa.gov/nws-insider/)
  + [National Centers](https://www.weather.gov/ncep/)
  + [Careers](https://www.noaa.gov/nws-careers)
  + [Contact Us](https://www.weather.gov/contact)
  + [Glossary](https://forecast.weather.gov/glossary.php)
  + [Social Media](https://www.weather.gov/socialmedia)
  + [NWS Transformation](https://www.noaa.gov/NWStransformation)

![](/bundles/templating/images/top_news/important.png)

# Nor'Easter Continues to Bring Heavy Rain and Coastal Impacts; Nolo Continues to Impact Hawaii

The nor’easter will weaken tonight, easing beach conditions and coastal flooding, though locally heavy rain will continue in parts of the Mid-Atlantic and New England into Monday. Hurricane Nolo continues to bring strong winds and large waves to Hawaii. A multi-day rain event will return to the Four Corners region Monday and expand to the south-central U.S. by midweek.
[Read More >](http://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=pmdspd)

LOADING...

Documentation

National Headquarters

# API Web Service

[Weather.gov](https://www.weather.gov)
> [Documentation](https://www.weather.gov/documentation)
> API Web Service

* [Services](/documentation/services-web-api)

  + [API Web Service](/documentation/services-web-api)
  + [Alerts Web Service](/documentation/services-web-alerts)
* [Technical Bulletins](/documentation/tb)

Overview

Examples

Updates

Specification

## Overview

The National Weather Service (NWS) API allows developers access to critical forecasts, alerts, and observations, along with other weather data. The API was designed with a cache-friendly approach that expires content based upon the information life cycle. The API is based upon of [JSON-LD](http://json-ld.org/) to promote machine data discovery.

The API is located at: <https://api.weather.gov>

Operational issues should be reported to [nco.ops@noaa.gov](mailto:nco.ops@noaa.gov).

General use questions can be asked on [the API github site](https://weather-gov.github.io/api/).

### Pricing

All of the information presented via the API is intended to be open data, free to use for any purpose. As a public service of the United States Government, we do not charge any fees for the usage of this service, although there are reasonable rate limits in place to prevent abuse and help ensure that everyone has access. The rate limit is not public information, but allows a generous amount for typical use. If the rate limit is execeed a request will return with an error, and may be retried after the limit clears (typically within 5 seconds). Proxies are more likely to reach the limit, whereas requests directly from clients are not likely.

### Content Negotiation

The new API will use headers to modify the version and format of the response. Every request, either by browser or application, sends header information every time you visit any website. For example, a commonly used header called "UserAgent" tells a website what type of device you are using so it can tailor the best experience for you. No private information is shared in a header, and this is a standard practice for all government and private sites. Developers can override these headers for specific purposes (see the "API Specifications" tab for more information). You can get full details by visiting the header field definitions page at the [World Wide Web Consortium](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html) site.

* Authentication
* Format the response
* Request new features

### Authentication

A User Agent is required to identify your application. This string can be anything, and the more unique to your application the less likely it will be affected by a security event. If you include contact information (website or email), we can contact you if your string is associated to a security event. This will be replaced with an API key in the future.

```
User-Agent: (myweatherapp.com, contact@myweatherapp.com)
```

### Formats

Endpoints typically have a GeoJSON default format, given the inclusion of geometry data. See the Specification tab for details on each endpoint. Below are common formats available by the API.

* **GeoJSON:** application/geo+json
* **JSON-LD:** application/ld+json
* **DWML:** application/vnd.noaa.dwml+xml
* **OXML:** application/vnd.noaa.obs+xml
* **CAP:** application/cap+xml
* **ATOM:** application/atom+xml

```
Accept: application/cap+xml
```

### Features

The API will use feature flags to make new features available to consumers. The available feature flags will be noted on the "Updates" and "Specification" tabs on this page. The feature flag will be communicated through a Service Change Notice (SCN) allowing developers a period to adopt the flag if the change impacts their applications. Once the adoption window expires, the feature will be made default. Developers can then remove the flag at their convenience.

```
Feature-Flags: forecast_temperature_qv
```

### Outage Information

Information on outages is generally [communicated through Administrative messages sent by National Center of Environmental Prediction's (NCEP's) Senior Duty Meteorologist (SDM)](https://www.nco.ncep.noaa.gov/status/messages/). These are sent via WMO id NOUS42 KWNO and product identifier ADASDM.

## Questions & Examples

The API uses linked data to allow applications to discover content. Similar to a web site that provides HTML links to help users navigate to each page, linked data helps applications navigate to each endpoint. You may also review the OPEN API specification on the "Specification" tab on this page, or directly using the specification endpoint (that is also used to create the tab presentation): <https://api.weather.gov/openapi.json>.

### How do I get the forecast?

Forecasts are created at each [NWS Weather Forecast Office (WFO)](/srh/nwsoffices) on their own grid definition, at a resolution of about 2.5km x 2.5km. The API endpoint for the 12h forecast periods at a specific grid location is formatted as:

```
	https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
```

For example: https://api.weather.gov/gridpoints/TOP/31,80/forecast

To obtain the grid forecast for a point location, use the /points endpoint to retrieve the current grid forecast endpoint by coordinates:

```
	https://api.weather.gov/points/{latitude},{longitude}
```

For example: https://api.weather.gov/points/39.7456,-97.0892

This will provide the grid forecast endpoints for three format options in these properties:

* forecast - forecast for 12h periods over the next seven days
* forecastHourly - forecast for hourly periods over the next seven days
* forecastGridData - raw forecast data over the next seven days

Note: at this time coastal marine grid forecasts are only available from the forecastGridData property.

Applications may cache the grid for a location to improve latency and reduce the additional lookup request; however, it is important to note that while it generally does not occur often, the gridX and gridY values (and even the office) for a given coordinate may occasionally change. For this reason, it is necessary to check back to the /points endpoint periodically for the latest office/grid mapping.

The /points endpoint also contains information about the issuing office, observation stations, and zones for a given point location.

### How do I get the forecast as DWML?

The forecast can be formatted as DWML for the /forecast and /forecast/hourly endpoints. There is no DWML specification for point lookups, so you first need to use the JSON-only /point endpoint described in the previous question to convert the location to a grid. Once you know the full gridpoint url for the forecast or hourly forecast, you can set the Accept header described in the overview to request the DWML format.

* application/vnd.noaa.dwml+xml

For example: https://api.weather.gov/gridpoints/TOP/31,80/forecast

### How do I get alerts?

The API has a robust selection of filters for alerts. A common request is all active alerts for a state:

```
	https://api.weather.gov/alerts/active?area={state}
```

For example: https://api.weather.gov/alerts/active?area=KS

The /alerts/active endpoint redirects internally to the root /alerts endpoint with the "active=true" parameter. Please review the "Specification" tab above for all the filter options. For important details about filtered alerts requests according to county or zone UGC, please review our [Alerts Geolocation Guide](https://www.weather.gov/media/documentation/docs/NWS_Geolocation.pdf).

For additional details on the format of an alert's content, please see the [CAP documentation](https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation).

The /alerts endpoint contains alerts issued over the past seven days. For an official archive of NWS CAP alerts, please reach out to the [National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov).

Note: The `/alerts` and `/alerts/active` endpoints *do NOT* contain [SPC's SEL product](https://api.weather.gov/products/types/SEL) language for Tornado Watches. Tornado Watch alerts are derived directly from the [local WFO's WCN product](https://api.weather.gov/products/types/WCN).

### Can I retrieve radar display data?

No. The radar endpoints in api.weather.gov are used for radar status data and do not contain the radar data used for display. For radar display data, consider these options:

* [RIDGE2 NWS Radar Display](https://radar.weather.gov)
* [RIDGE2 NWS Radar Data as OGC Web Services](https://opengeo.ncep.noaa.gov)
* [Other NWS OGC Web Services](/gis/cloudgiswebservices)
* [MRMS Data](https://mrms.ncep.noaa.gov)
* [NODD MRMS Archive Data](https://registry.opendata.aws/noaa-mrms-pds)

## Updates

The information on this page is updated regularly. All official NWS Service Change Notices, including an email subscription option, can be found at [weather.gov/notification](/notification).

### Feature Flags

Feature flags are endpoint specific. See Specification tab for details.

#### /gridpoints/{wfo}/{x},{y}/forecast and /gridpoints/{wfo}/{x},{y}/forecast/hourly

* forecast\_temperature\_qv: Represent temperature as QuantitativeValue
* forecast\_wind\_speed\_qv: Represent wind speed as QuantitativeValue

#### /stations, /stations/{stationId}, and /gridpoints/{wfo}/{x},{y}/stations

* obs\_station\_provider: Show provider and subProvider MADIS details

### Known Issues

Before contacting us, please review the following list of issues that have been identified for a future update.

* No significant known issues.

Updated 3/24/2026

### Upstream Issues/Changes

The following issues are related to upstream sources of the API, and are not an API bug.

* Station observations endpoints always show missing (null) 24h max/min temperatures for stations outside the central time zone due to MADIS ingest bug.
* **Delayed observations**

  Observations may be delayed up to 20 minutes from [MADIS](https://madis-data.ncep.noaa.gov), the upstream source, due to QC processing.

### Resolutions

The following issues have been recently resolved:

* 17 Mar 2026: The /radar/queues/rds and /radar/queues/tds endpoints are limited by default so that they no longer return a 503 error from too many results.
* 7 Jan 2026: The /forecast and /forecast/hourly endpoints no longer contain data that has past (ex. previous hours in an hourly forecast or the words "Overnight" during the early part of the day).
* 15 Dec 2025: Precipitation values in the observations endpoints are rounded down to the nearest centimeter (less than 0.4" may be improperly rounded down to 0).
* 2 Oct 2025: Upstream MADIS bug resolved so that station observations endpoints no longer always show missing (null) wind gust values.
* 4 Aug 2025:
  + Station observations should no longer be routinely delayed more than about the 20 minutes it takes the upstream MADIS source to QC and ingest for API.
  + Station observations should no longer have missing (null) values for weather properties (temperature, wind, precipitation, etc.) when the MADIS source has data and [passed all QC levels](https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml).
* 22 May 2025:
  + XML data requests to the stations/<station id>/observations/latest endpoint no longer fail when observation site reports variable (VRB) winds.
  + [/alerts/types](https://api.weather.gov/alerts/types) have been updated to correct "Evacuation Immediate" and add/remove types to align with what appears in the [Hazards Map](https://www.weather.gov/help-map).
  + PoP values less than 20% in the 12h forecast endpoints (/gridpoints/{office}/{gridX},{gridY}/forecast) no longer display as null values.
  + Periods with extra ellipses (...) in the WFO's forecast zone text product (ZFP) are now properly displayed in the /zones/{type}/{zoneId}/forecast endpoint.
  + For more details on other changes with this upgrade, please see [SCN 25-44](https://www.weather.gov/media/notification/pdf_2025/scn25-44_API_latest_changesmay22_2025.pdf).

## Specification

**Note:** All times generated by the API are in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime).

[![usa.gov](/bundles/templating/images/footer/usa_gov.png)](http://www.usa.gov)

[US Dept of Commerce](http://www.commerce.gov)  
[National Oceanic and Atmospheric Administration](http://www.noaa.gov)  
[National Weather Service](https://www.weather.gov)  
Documentation  
   
,
  
  
  
[Comments? Questions? Please Contact Us.](mailto:idp-support@noaa.gov)

[Disclaimer](https://www.weather.gov/disclaimer)  
[Information Quality](http://www.cio.noaa.gov/services_programs/info_quality.html)  
[Help](https://www.weather.gov/help)  
[Glossary](/glossary)

[Privacy Policy](https://www.weather.gov/privacy)  
[Freedom of Information Act (FOIA)](https://www.noaa.gov/foia-freedom-of-information-act)  
[About Us](https://www.weather.gov/about)  
[Career Opportunities](https://www.weather.gov/careers)
