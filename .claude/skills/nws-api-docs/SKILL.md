---
name: nws-api-docs
description: Official NWS API (api.weather.gov) OpenAPI spec: endpoints, parameters, response schemas. Use when writing or checking code that calls api.weather.gov.
---

> **Provenance (generated doc skill, do not hand-edit; rebuild instead)**
> - Source: https://api.weather.gov/openapi.json (OpenAPI 3.1.2, API version 3.11.0) and https://www.weather.gov/documentation/services-web-api
> - Built: 2026-09-28 (UTC)
> - Tool: Skill Seekers 3.9.1, enhance level 0 (no AI rewriting); built with `skill-seekers create nws-openapi.yaml` (the openapi.json above converted to YAML, since Skill Seekers reads .json files as its own config)
> - Verbatim copies: references/verbatim/services-web-api.md is the official docs page (User-Agent rule, rate limits, known issues). Skill Seekers got no content from that page, so it is saved separately.
> - Rebuild steps: docs/skill-configs/README.md

# weather.gov API

Official NWS API (api.weather.gov) OpenAPI spec: endpoints, parameters, response schemas. Use when writing or checking code that calls api.weather.gov.

**API Version:** 3.11.0

weather.gov API

## When to Use This Skill

Use this skill when you need to:

- Understand the weather.gov API endpoints and operations
- Look up request/response schemas for weather.gov API
- Find authentication and authorization requirements
- Construct API requests with correct parameters
- Review available data models and their properties
- Check endpoint paths, methods, and status codes

## Servers

- `https://api.weather.gov` - Production server

## Authentication

- **userAgent**: API Key in `header` (parameter: `User-Agent`)
- **apiKeyAuth**: API Key in `header` (parameter: `API-Key`)

## API Endpoints Overview

**Total endpoints:** 69

### alerts

- `GET /alerts`
- `GET /alerts/active`
- `GET /alerts/active/count`
- `GET /alerts/active/zone/{zoneId}`
- `GET /alerts/active/area/{area}`
- `GET /alerts/active/region/{region}`
- `GET /alerts/types`
- `GET /alerts/{id}`

### aviation

- `GET /aviation/cwsus/{cwsuId}`
- `GET /aviation/cwsus/{cwsuId}/cwas`
- `GET /aviation/cwsus/{cwsuId}/cwas/{date}/{sequence}`
- `GET /aviation/sigmets`
- `GET /aviation/sigmets/{atsu}`
- `GET /aviation/sigmets/{atsu}/{date}`
- `GET /aviation/sigmets/{atsu}/{date}/{time}`

### glossary

- `GET /glossary`

### gridpoints

- `GET /gridpoints/{wfo}/{x},{y}`
- `GET /gridpoints/{wfo}/{x},{y}/forecast`
- `GET /gridpoints/{wfo}/{x},{y}/forecast/hourly`
- `GET /gridpoints/{wfo}/{x},{y}/stations`

### icons

- `GET /icons/{set}/{timeOfDay}/{first}` *(deprecated)*
- `GET /icons/{set}/{timeOfDay}/{first}/{second}` *(deprecated)*
- `GET /icons` *(deprecated)*

### offices

- `GET /offices/{officeId}`
- `GET /offices/{officeId}/briefing`
- `GET /offices/{officeId}/briefing/download/latest`
- `GET /offices/{officeId}/briefing/download/{briefingId}`
- `GET /offices/{officeId}/headlines/{headlineId}`
- `GET /offices/{officeId}/headlines`
- `GET /offices/{officeId}/weatherstories`
- `GET /offices/{officeId}/weatherstories/download/{imageId}`

### points

- `GET /points/{latitude},{longitude}`
- `GET /points/{latitude},{longitude}/radio`
- `GET /points/{latitude},{longitude}/stations` *(deprecated)*

### products

- `GET /products`
- `GET /products/locations`
- `GET /products/types`
- `GET /products/{productId}`
- `GET /products/types/{typeId}`
- `GET /products/types/{typeId}/locations`
- `GET /products/locations/{locationId}/types`
- `GET /products/types/{typeId}/locations/{locationId}`
- `GET /products/types/{typeId}/locations/{locationId}/latest`

### radar

- `GET /radar/servers`
- `GET /radar/servers/{id}`
- `GET /radar/spgds`
- `GET /radar/stations`
- `GET /radar/stations/{stationId}`
- `GET /radar/stations/{stationId}/alarms`
- `GET /radar/queues/{host}`
- `GET /radar/profilers/{stationId}`

### radio

- `GET /radio`
- `GET /radio/{callSign}`
- `GET /radio/{callSign}/broadcast`

### stations

- `GET /stations/{stationId}/observations`
- `GET /stations/{stationId}/observations/latest`
- `GET /stations/{stationId}/observations/{time}`
- `GET /stations/{stationId}/tafs`
- `GET /stations/{stationId}/tafs/{date}/{time}`
- `GET /stations`
- `GET /stations/{stationId}`

### thumbnails

- `GET /thumbnails/satellite/{area}` *(deprecated)*

### zones

- `GET /zones`
- `GET /zones/{type}`
- `GET /zones/{type}/{zoneId}`
- `GET /zones/{type}/{zoneId}/forecast`
- `GET /zones/{type}/{zoneId}/radio`
- `GET /zones/forecast/{zoneId}/observations`
- `GET /zones/forecast/{zoneId}/stations`

## Data Models

**Total schemas:** 108

- **ATSUIdentifier** (`string`) - ATSU Identifier
- **Alert** (`object`) - An object representing a public alert message.
Unless otherwise noted, the fi...
- **AlertAtomEntry** (`object`) - An alert entry in an Atom feed
- **AlertAtomFeed** (`object`) - An alert feed in Atom format
- **AlertCap** (`object`)
- **AlertCertainty** (`string`)
- **AlertCollection** (`object`)
- **AlertCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **AlertCollectionJsonLd** (`object`)
- **AlertGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **AlertId** (`string`) - The identifier of the alert message.
- **AlertJsonLd** (`object`)
- **AlertMessageType** (`string`)
- **AlertSeverity** (`string`)
- **AlertStatus** (`string`)
- **AlertUrgency** (`string`)
- **AlertXMLParameter** (`object`)
- **AreaCode** (`object`) - State/territory codes and marine area codes
- **AstronomicalData** (`object`) - An object representing sunrise, sunset, and twilight information for a locati...
- **BinaryFile** (`string`)
- **CenterWeatherAdvisory** (`object`)
- **CenterWeatherAdvisoryCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **CenterWeatherAdvisoryGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **CenterWeatherServiceUnitJsonLd** (`object`)
- **Date** (`string`) - Date (in YYYY-MM-DD format).
- **GeoJsonBoundingBox** (`array`) - A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the ...
- **GeoJsonCoordinate** (`array`) - A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the Ge...
- **GeoJsonFeature** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **GeoJsonFeatureCollection** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **GeoJsonGeometry** (`object`) - A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on t...
- **GeoJsonLineString** (`array`) - A GeoJSON line string. Please refer to IETF RFC 7946 for information on the G...
- **GeoJsonPolygon** (`array`) - A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJS...
- **GeometryString** (`['string', 'null']`) - A geometry represented in Well-Known Text (WKT) format.
- **Gridpoint** (`object`) - Raw forecast data for a 2.5km grid square.
This is a list of all potential da...
- **Gridpoint12hForecast** (`object`) - A multi-day forecast for a 2.5km grid square.
- **Gridpoint12hForecastGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **Gridpoint12hForecastJsonLd** (`object`) - A multi-day forecast for a 2.5km grid square.
- **Gridpoint12hForecastPeriod** (`object`) - An object containing forecast information for a specific time period (general...
- **GridpointForecastUnits** (`string`) - Denotes the units used in the textual portions of the forecast.
- **GridpointGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **GridpointHourlyForecast** (`object`) - An hourly forecast for a 2.5km grid square.
- **GridpointHourlyForecastGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **GridpointHourlyForecastJsonLd** (`object`) - An hourly forecast for a 2.5km grid square.
- **GridpointHourlyForecastPeriod** (`object`) - An object containing forecast information for a specific time period (general...
- **GridpointJsonLd** (`object`) - Raw forecast data for a 2.5km grid square.
This is a list of all potential da...
- **GridpointQuantitativeValueLayer** (`object`) - A gridpoint layer consisting of quantitative values (numeric values with asso...
- **ISO8601Duration** (`string`) - A time duration in ISO 8601 format.
- **ISO8601Interval** (`object`) - A time interval in ISO 8601 format. This can be one of:

    1. Start and end...
- **JsonLdContext** (`object`)
- **LandRegionCode** (`string`) - Land region code. These correspond to the six NWS regional headquarters:
* AR...
- **MarineAreaCode** (`string`) - Marine area code as defined in NWS Directive 10-302:
* AM: Western North Atla...
- **MarineRegionCode** (`string`) - Marine region code. These are groups of marine areas combined.
* AL: Alaska w...
- **MetarPhenomenon** (`object`) - An object representing a decoded METAR phenomenon string.
- **MetarSkyCoverage** (`string`)
- **NWSCenterWeatherServiceUnitId** (`string`) - Three-letter identifier for a Center Weather Service Unit (CWSU).
- **NWSConnectDocumentMetadata** (`object`) - Metadata for an NWS Connect document.
- **NWSForecastOfficeId** (`string`) - Three-letter identifier for a NWS office.
- **NWSNationalHQId** (`string`) - Three-letter identifier for NWS National HQ.
- **NWSOfficeId** (`object`)
- **NWSRegionalHQId** (`string`) - Three-letter identifier for a NWS Regional HQ.
- **NWSZoneID** (`string`) - UGC identifier for a NWS forecast zone or county.
The first two letters will ...
- **NWSZoneType** (`string`)
- **Observation** (`object`)
- **ObservationCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **ObservationCollectionJsonLd** (`object`)
- **ObservationGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **ObservationJsonLd** (`object`)
- **ObservationStation** (`object`)
- **ObservationStationCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **ObservationStationCollectionJsonLd** (`object`)
- **ObservationStationGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **ObservationStationJsonLd** (`object`)
- **Office** (`object`)
- **OfficeBriefing** (`object`) - Metadata for an NWS Connect document.
- **OfficeHeadline** (`object`)
- **OfficeHeadlineCollection** (`object`)
- **OfficeWeatherStory** (`object`) - Metadata for an NWS Connect document.
- **OfficeWeatherStoryCollection** (`array`)
- **PaginationInfo** (`object`) - Links for retrieving more data from paged data sets
- **Point** (`object`)
- **PointGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **PointJsonLd** (`object`)
- **PointString** (`string`)
- **ProblemDetail** (`object`) - Detail about an error. This document conforms to RFC 7807 (Problem Details fo...
- **QuantitativeValue** (`object`) - A structured value representing a measurement and its unit of measure. This o...
- **RegionCode** (`object`)
- **RelativeLocation** (`object`)
- **RelativeLocationGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **RelativeLocationJsonLd** (`object`)
- **Sigmet** (`object`)
- **SigmetCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **SigmetGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **SigmetSequenceNumber** (`string`)
- **StateTerritoryCode** (`string`)
- **TextProduct** (`object`)
- **TextProductCollection** (`object`)
- **TextProductLocationCollection** (`object`)
- **TextProductTypeCollection** (`object`)
- **Time** (`string`) - A time (in HHMM format). This is always specified in UTC (Zulu) time.
- **UnitOfMeasure** (`string`) - A string denoting a unit of measure, expressed in the format "{unit}" or "{na...
- **Zone** (`object`)
- **ZoneCollectionGeoJson** (`object`) - A GeoJSON feature collection. Please refer to IETF RFC 7946 for information o...
- **ZoneCollectionJsonLd** (`object`)
- **ZoneForecast** (`object`) - An object representing a zone area forecast.
- **ZoneForecastGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **ZoneForecastJsonLd** (`object`) - An object representing a zone area forecast.
- **ZoneGeoJson** (`object`) - A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJS...
- **ZoneJsonLd** (`object`)

## Quick Reference

### Common Operations

**GET:**

- `/alerts`
- `/alerts/active`
- `/alerts/active/count`
- `/alerts/active/zone/{zoneId}`
- `/alerts/active/area/{area}`
- *...and 64 more*

## Reference Files

Detailed API documentation is organized in `references/`:

- `references/index.md` - Complete reference index
- `references/alerts.md` - alerts (8 endpoints)
- `references/aviation.md` - aviation (7 endpoints)
- `references/glossary.md` - glossary (1 endpoints)
- `references/gridpoints.md` - gridpoints (4 endpoints)
- `references/icons.md` - icons (3 endpoints)
- `references/offices.md` - offices (8 endpoints)
- `references/points.md` - points (3 endpoints)
- `references/products.md` - products (9 endpoints)
- `references/radar.md` - radar (8 endpoints)
- `references/radio.md` - radio (3 endpoints)
- `references/stations.md` - stations (7 endpoints)
- `references/thumbnails.md` - thumbnails (1 endpoints)
- `references/zones.md` - zones (7 endpoints)
- `references/schemas.md` - Data models (108 schemas)
- `references/security.md` - Security schemes (2 schemes)

---

**Generated by Skill Seekers** | OpenAPI/Swagger Specification Scraper
