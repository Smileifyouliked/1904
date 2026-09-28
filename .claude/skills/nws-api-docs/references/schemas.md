# Data Models / Schemas

Component schemas (data models) defined in the API specification.

**Total schemas:** 108

---

## ATSUIdentifier

**Type:** `string`

ATSU Identifier


---

## Alert

**Type:** `object`

An object representing a public alert message.
Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information.
http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://vlab.noaa.gov/web/nws-common-alerting-protocol/cap-documentation


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affectedZones` | `array[string(uri)]` | No | An array of API links for zones affected by the alert. This is an API-specific extension field an... |
| `areaDesc` | `string` | No | A textual description of the area affected by the alert. |
| `category` | `string` | No | The code denoting the category of the subject event of the alert message. Enum: [`Met`, `Geo`, `Safety`, `Security`, `Rescue`, +7 more] |
| `certainty` | `AlertCertainty` | No |  Enum: [`Observed`, `Likely`, `Possible`, `Unlikely`, `Unknown`] |
| `code` | `string` | No | The code denoting the special handling of the alert message. |
| `description` | `string` | No | The text describing the subject event of the alert message. |
| `effective` | `string(date-time)` | No | The effective time of the information of the alert message. |
| `ends` | `['string', 'null'](date-time)` | No | The expected end time of the subject event of the alert message. |
| `event` | `string` | No | The text denoting the type of the subject event of the alert message. |
| `eventCode` | `object` | No | System-specific code identifiying the event type of the alert message The keys in this object cor... |
| `expires` | `string(date-time)` | No | The expiry time of the information of the alert message. |
| `geocode` | `object` | No | Lists of codes for NWS public zones and counties affected by the alert. |
| `headline` | `['string', 'null']` | No | The text headline of the alert message. |
| `id` | `AlertId` | No | The identifier of the alert message. |
| `instruction` | `['string', 'null']` | No | The text describing the recommended action to be taken by recipients of the alert message.  |
| `language` | `string` | No | The code denoting the language of the info sub-element of the alert message. |
| `messageType` | `AlertMessageType` | No |  Enum: [`Alert`, `Update`, `Cancel`, `Ack`, `Error`] |
| `note` | `['string', 'null']` | No | The text note accompanying the alert message. Per CAP spec, this should accompany alerts with a s... |
| `onset` | `['string', 'null'](date-time)` | No | The expected time of the beginning of the subject event of the alert message. |
| `parameters` | `object` | No | System-specific additional parameters associated with the alert message. The keys in this object ... |
| `references` | `array[object]` | No | A list of prior alerts that this alert updates or replaces. |
| `response` | `string` | No | The code denoting the type of action recommended for the target audience. This corresponds to res... Enum: [`Shelter`, `Evacuate`, `Prepare`, `Execute`, `Avoid`, +4 more] |
| `scope` | `string` | No | The code denoting the intended distribution of the alert message. Enum: [`Public`, `Restricted`, `Private`] |
| `sender` | `string` | No | Email address of the NWS webmaster. |
| `senderName` | `string` | No | The text naming the originator of the alert message. |
| `sent` | `string(date-time)` | No | The time of the origination of the alert message. |
| `severity` | `AlertSeverity` | No |  Enum: [`Extreme`, `Severe`, `Moderate`, `Minor`, `Unknown`] |
| `status` | `AlertStatus` | No |  Enum: [`Actual`, `Exercise`, `System`, `Test`, `Draft`] |
| `urgency` | `AlertUrgency` | No |  Enum: [`Immediate`, `Expected`, `Future`, `Past`, `Unknown`] |
| `web` | `string` | No | The identifier of the hyperlink associating additional information within the alert message. |


---

## AlertAtomEntry

**Type:** `object`

An alert entry in an Atom feed

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `areaDesc` | `string` | No |  |
| `author` | `object` | No |  |
| `category` | `string` | No |  |
| `certainty` | `string` | No |  |
| `effective` | `string` | No |  |
| `event` | `string` | No |  |
| `expires` | `string` | No |  |
| `geocode` | `array[AlertXMLParameter]` | No |  |
| `id` | `string` | No |  |
| `msgType` | `string` | No |  |
| `parameter` | `array[AlertXMLParameter]` | No |  |
| `polygon` | `string` | No |  |
| `published` | `string` | No |  |
| `sent` | `string` | No |  |
| `severity` | `string` | No |  |
| `status` | `string` | No |  |
| `summary` | `string` | No |  |
| `updated` | `string` | No |  |
| `urgency` | `string` | No |  |


---

## AlertAtomFeed

**Type:** `object`

An alert feed in Atom format

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `author` | `object` | No |  |
| `entry` | `array[AlertAtomEntry]` | No |  |
| `generator` | `string` | No |  |
| `id` | `string` | No |  |
| `title` | `string` | No |  |
| `updated` | `string` | No |  |


---

## AlertCap

**Type:** `object`


---

## AlertCertainty

**Type:** `string`

**Enum values:**

- `Observed`
- `Likely`
- `Possible`
- `Unlikely`
- `Unknown`


---

## AlertCollection

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |
| `title` | `string` | No | A title describing the alert collection |
| `updated` | `string(date-time)` | No | The last time a change occurred to this collection |


---

## AlertCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[object]` | Yes |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |
| `title` | `string` | No | A title describing the alert collection |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |
| `updated` | `string(date-time)` | No | The last time a change occurred to this collection |


---

## AlertCollectionJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[Alert]` | No |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |
| `title` | `string` | No | A title describing the alert collection |
| `updated` | `string(date-time)` | No | The last time a change occurred to this collection |


---

## AlertGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Alert` | Yes | An object representing a public alert message. Unless otherwise noted, the fields in this object ... |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## AlertId

**Type:** `string`

The identifier of the alert message.


---

## AlertJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@graph` | `array[Alert]` | No |  |


---

## AlertMessageType

**Type:** `string`

**Enum values:**

- `Alert`
- `Update`
- `Cancel`
- `Ack`
- `Error`


---

## AlertSeverity

**Type:** `string`

**Enum values:**

- `Extreme`
- `Severe`
- `Moderate`
- `Minor`
- `Unknown`


---

## AlertStatus

**Type:** `string`

**Enum values:**

- `Actual`
- `Exercise`
- `System`
- `Test`
- `Draft`


---

## AlertUrgency

**Type:** `string`

**Enum values:**

- `Immediate`
- `Expected`
- `Future`
- `Past`
- `Unknown`


---

## AlertXMLParameter

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `string` | No |  |
| `valueName` | `string` | No |  |


---

## AreaCode

**Type:** `object`

State/territory codes and marine area codes

### oneOf

1. `StateTerritoryCode` (StateTerritoryCode)
2. `MarineAreaCode` (MarineAreaCode)


---

## AstronomicalData

**Type:** `object`

An object representing sunrise, sunset, and twilight information for a location.


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `astronomicalTwilightBegin` | `string(date-time)` | No | The timestamp of the onset of astronomical twilight, defined as when the sun angle is 108° from v... |
| `astronomicalTwilightEnd` | `string(date-time)` | No | The timestamp of the end of astronomical twilight, defined as when the sun angle is 108° from ver... |
| `civilTwilightBegin` | `string(date-time)` | No | The timestamp of the onset of civil twilight, defined as when the sun angle is 96° from vertical.... |
| `civilTwilightEnd` | `string(date-time)` | No | The timestamp of the end of civil twilight, defined as when the sun angle is 96° from vertical. T... |
| `nauticalTwilightBegin` | `string(date-time)` | No | The timestamp of the onset of nautical twilight, defined as when the sun angle is 102° from verti... |
| `nauticalTwilightEnd` | `string(date-time)` | No | The timestamp of the end of nautical twilight, defined as when the sun angle is 102° from vertica... |
| `sunrise` | `string(date-time)` | No | The timestamp of sunrise, defined as when the sun angle is 90°35' from vertical.  |
| `sunset` | `string(date-time)` | No | The timestamp of sunset, defined as when the sun angle is 90°35' from vertical.  |
| `transit` | `string(date-time)` | No | The timestamp when the sun reaches its zenith.  |


---

## BinaryFile

**Type:** `string`


---

## CenterWeatherAdvisory

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `cwsu` | `NWSCenterWeatherServiceUnitId` | No | Three-letter identifier for a Center Weather Service Unit (CWSU). Enum: [`ZAB`, `ZAN`, `ZAU`, `ZBW`, `ZDC`, +17 more] |
| `end` | `string(date-time)` | No |  |
| `id` | `string` | No |  |
| `issueTime` | `string(date-time)` | No |  |
| `observedProperty` | `string` | No |  |
| `sequence` | `integer` | No |  |
| `start` | `string(date-time)` | No |  |
| `text` | `string` | No |  |


---

## CenterWeatherAdvisoryCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[object]` | Yes |  |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## CenterWeatherAdvisoryGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `CenterWeatherAdvisory` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## CenterWeatherServiceUnitJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`GovernmentOrganization`] |
| `address` | `object` | No |  |
| `approvedObservationStations` | `array[string(uri)]` | No |  |
| `email` | `string` | No |  |
| `faxNumber` | `string` | No |  |
| `id` | `string` | No |  |
| `name` | `string` | No |  |
| `nwsRegion` | `string` | No |  |
| `parentOrganization` | `string(uri)` | No |  |
| `responsibleCounties` | `array[string(uri)]` | No |  |
| `responsibleFireZones` | `array[string(uri)]` | No |  |
| `responsibleForecastZones` | `array[string(uri)]` | No |  |
| `sameAs` | `string(uri)` | No |  |
| `telephone` | `string` | No |  |


---

## Date

**Type:** `string`

Date (in YYYY-MM-DD format).


---

## GeoJsonBoundingBox

**Type:** `array`

A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format.

**Items type:** `number`


---

## GeoJsonCoordinate

**Type:** `array`

A GeoJSON coordinate. Please refer to IETF RFC 7946 for information on the GeoJSON format.

**Items type:** `number`


---

## GeoJsonFeature

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `object` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## GeoJsonFeatureCollection

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[GeoJsonFeature]` | Yes |  |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## GeoJsonGeometry

**Type:** `object`

A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### oneOf

1. `object`
2. `object`
3. `object`
4. `object`
5. `object`
6. `object`
7. `null`


---

## GeoJsonLineString

**Type:** `array`

A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format.

**Items type:** `array[number]`


---

## GeoJsonPolygon

**Type:** `array`

A GeoJSON polygon. Please refer to IETF RFC 7946 for information on the GeoJSON format.

**Items type:** `array[array[number]]`


---

## GeometryString

**Type:** `['string', 'null']`

A geometry represented in Well-Known Text (WKT) format.


---

## Gridpoint

**Type:** `object`

Raw forecast data for a 2.5km grid square.
This is a list of all potential data layers that may appear. Some layers may not be present in all areas.
* temperature
* dewpoint
* maxTemperature
* minTemperature
* relativeHumidity
* apparentTemperature
* heatIndex
* windChill
* wetBulbGlobeTemperature
* skyCover
* windDirection
* windSpeed
* windGust
* weather
* hazards: Watch and advisory products in effect
* heatRisk
* probabilityOfPrecipitation
* quantitativePrecipitation
* iceAccumulation
* snowfallAmount
* snowLevel
* ceilingHeight
* visibility
* transportWindSpeed
* transportWindDirection
* mixingHeight
* hainesIndex
* lightningActivityLevel
* twentyFootWindSpeed
* twentyFootWindDirection
* waveHeight
* wavePeriod
* waveDirection
* primarySwellHeight
* primarySwellDirection
* secondarySwellHeight
* secondarySwellDirection
* wavePeriod2
* windWaveHeight
* dispersionIndex
* pressure: Barometric pressure
* probabilityOfTropicalStormWinds
* probabilityOfHurricaneWinds
* potentialOf15mphWinds
* potentialOf25mphWinds
* potentialOf35mphWinds
* potentialOf45mphWinds
* potentialOf20mphWindGusts
* potentialOf30mphWindGusts
* potentialOf40mphWindGusts
* potentialOf50mphWindGusts
* potentialOf60mphWindGusts
* grasslandFireDangerIndex
* probabilityOfThunder
* davisStabilityIndex
* atmosphericDispersionIndex
* lowVisibilityOccurrenceRiskIndex
* stability
* redFlagThreatIndex


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Gridpoint`] |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastOffice` | `string(uri)` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `gridId` | `string` | No |  |
| `gridX` | `integer` | No |  |
| `gridY` | `integer` | No |  |
| `hazards` | `object` | No |  |
| `updateTime` | `string(date-time)` | No |  |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |
| `weather` | `object` | No |  |

**Additional properties:** `GridpointQuantitativeValueLayer`


---

## Gridpoint12hForecast

**Type:** `object`

A multi-day forecast for a 2.5km grid square.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastGenerator` | `string` | No | The internal generator class used to create the forecast text (used for NWS debugging). |
| `generatedAt` | `string(date-time)` | No | The time this forecast data was generated. |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[Gridpoint12hForecastPeriod]` | No | An array of forecast periods. |
| `units` | `GridpointForecastUnits` | No | Denotes the units used in the textual portions of the forecast. Enum: [`us`, `si`] |
| `updateTime` | `string(date-time)` | No | The last update time of the data this forecast was generated from. |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |


---

## Gridpoint12hForecastGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Gridpoint12hForecast` | Yes | A multi-day forecast for a 2.5km grid square. |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## Gridpoint12hForecastJsonLd

**Type:** `object`

A multi-day forecast for a 2.5km grid square.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | Yes |  |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastGenerator` | `string` | No | The internal generator class used to create the forecast text (used for NWS debugging). |
| `generatedAt` | `string(date-time)` | No | The time this forecast data was generated. |
| `geometry` | `GeometryString` | Yes | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[Gridpoint12hForecastPeriod]` | No | An array of forecast periods. |
| `units` | `GridpointForecastUnits` | No | Denotes the units used in the textual portions of the forecast. Enum: [`us`, `si`] |
| `updateTime` | `string(date-time)` | No | The last update time of the data this forecast was generated from. |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |


---

## Gridpoint12hForecastPeriod

**Type:** `object`

An object containing forecast information for a specific time period (generally 12-hour or 1-hour).


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `detailedForecast` | `string` | No | A detailed textual forecast for the period. |
| `endTime` | `string(date-time)` | No | The ending time that this forecast period is valid for. |
| `icon` | `string(uri)` | No | A link to an icon representing the forecast summary. |
| `isDaytime` | `boolean` | No | Indicates whether this period is daytime or nighttime. |
| `name` | `string` | No | A textual identifier for the period. This value will not be present for hourly forecasts.  |
| `number` | `integer` | No | Sequential period number. |
| `probabilityOfPrecipitation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `shortForecast` | `string` | No | A brief textual forecast summary for the period. |
| `startTime` | `string(date-time)` | No | The starting time that this forecast period is valid for. |
| `temperature` | `QuantitativeValue | integer` | No | High/low temperature for the period, depending on whether the period is day or night. This proper... |
| `temperatureTrend` | `['string', 'null']` | No | If not null, indicates a non-diurnal temperature trend for the period (either rising temperature ... Enum: [`rising`, `falling`] |
| `temperatureUnit` | `string` | No | The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future ve... Enum: [`F`, `C`] |
| `windDirection` | `string` | No | The prevailing direction of the wind for the period, using a 16-point compass. Enum: [`N`, `NNE`, `NE`, `ENE`, `E`, +11 more] |
| `windGust` | `QuantitativeValue | string | null` | No | Peak wind gust for the period. This property as an string value is deprecated. Future versions wi... |
| `windSpeed` | `QuantitativeValue | string` | No | Wind speed for the period. This property as an string value is deprecated. Future versions will e... |


---

## GridpointForecastUnits

**Type:** `string`

Denotes the units used in the textual portions of the forecast.

**Enum values:**

- `us`
- `si`


---

## GridpointGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Gridpoint` | Yes | Raw forecast data for a 2.5km grid square. This is a list of all potential data layers that may a... |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## GridpointHourlyForecast

**Type:** `object`

An hourly forecast for a 2.5km grid square.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastGenerator` | `string` | No | The internal generator class used to create the forecast text (used for NWS debugging). |
| `generatedAt` | `string(date-time)` | No | The time this forecast data was generated. |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[GridpointHourlyForecastPeriod]` | No | An array of forecast periods. |
| `units` | `GridpointForecastUnits` | No | Denotes the units used in the textual portions of the forecast. Enum: [`us`, `si`] |
| `updateTime` | `string(date-time)` | No | The last update time of the data this forecast was generated from. |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |


---

## GridpointHourlyForecastGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `GridpointHourlyForecast` | Yes | An hourly forecast for a 2.5km grid square. |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## GridpointHourlyForecastJsonLd

**Type:** `object`

An hourly forecast for a 2.5km grid square.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | Yes |  |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastGenerator` | `string` | No | The internal generator class used to create the forecast text (used for NWS debugging). |
| `generatedAt` | `string(date-time)` | No | The time this forecast data was generated. |
| `geometry` | `GeometryString` | Yes | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[GridpointHourlyForecastPeriod]` | No | An array of forecast periods. |
| `units` | `GridpointForecastUnits` | No | Denotes the units used in the textual portions of the forecast. Enum: [`us`, `si`] |
| `updateTime` | `string(date-time)` | No | The last update time of the data this forecast was generated from. |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |


---

## GridpointHourlyForecastPeriod

**Type:** `object`

An object containing forecast information for a specific time period (generally 12-hour or 1-hour).


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `detailedForecast` | `string` | No | A detailed textual forecast for the period. |
| `dewpoint` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `endTime` | `string(date-time)` | No | The ending time that this forecast period is valid for. |
| `icon` | `string(uri)` | No | A link to an icon representing the forecast summary. |
| `isDaytime` | `boolean` | No | Indicates whether this period is daytime or nighttime. |
| `name` | `string` | No | A textual identifier for the period. This value will not be present for hourly forecasts.  |
| `number` | `integer` | No | Sequential period number. |
| `probabilityOfPrecipitation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `relativeHumidity` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `shortForecast` | `string` | No | A brief textual forecast summary for the period. |
| `startTime` | `string(date-time)` | No | The starting time that this forecast period is valid for. |
| `temperature` | `QuantitativeValue | integer` | No | High/low temperature for the period, depending on whether the period is day or night. This proper... |
| `temperatureTrend` | `['string', 'null']` | No | If not null, indicates a non-diurnal temperature trend for the period (either rising temperature ... Enum: [`rising`, `falling`] |
| `temperatureUnit` | `string` | No | The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future ve... Enum: [`F`, `C`] |
| `windDirection` | `string` | No | The prevailing direction of the wind for the period, using a 16-point compass. Enum: [`N`, `NNE`, `NE`, `ENE`, `E`, +11 more] |
| `windGust` | `QuantitativeValue | string | null` | No | Peak wind gust for the period. This property as an string value is deprecated. Future versions wi... |
| `windSpeed` | `QuantitativeValue | string` | No | Wind speed for the period. This property as an string value is deprecated. Future versions will e... |


---

## GridpointJsonLd

**Type:** `object`

Raw forecast data for a 2.5km grid square.
This is a list of all potential data layers that may appear. Some layers may not be present in all areas.
* temperature
* dewpoint
* maxTemperature
* minTemperature
* relativeHumidity
* apparentTemperature
* heatIndex
* windChill
* wetBulbGlobeTemperature
* skyCover
* windDirection
* windSpeed
* windGust
* weather
* hazards: Watch and advisory products in effect
* heatRisk
* probabilityOfPrecipitation
* quantitativePrecipitation
* iceAccumulation
* snowfallAmount
* snowLevel
* ceilingHeight
* visibility
* transportWindSpeed
* transportWindDirection
* mixingHeight
* hainesIndex
* lightningActivityLevel
* twentyFootWindSpeed
* twentyFootWindDirection
* waveHeight
* wavePeriod
* waveDirection
* primarySwellHeight
* primarySwellDirection
* secondarySwellHeight
* secondarySwellDirection
* wavePeriod2
* windWaveHeight
* dispersionIndex
* pressure: Barometric pressure
* probabilityOfTropicalStormWinds
* probabilityOfHurricaneWinds
* potentialOf15mphWinds
* potentialOf25mphWinds
* potentialOf35mphWinds
* potentialOf45mphWinds
* potentialOf20mphWindGusts
* potentialOf30mphWindGusts
* potentialOf40mphWindGusts
* potentialOf50mphWindGusts
* potentialOf60mphWindGusts
* grasslandFireDangerIndex
* probabilityOfThunder
* davisStabilityIndex
* atmosphericDispersionIndex
* lowVisibilityOccurrenceRiskIndex
* stability
* redFlagThreatIndex


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Gridpoint`] |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `forecastOffice` | `string(uri)` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `gridId` | `string` | No |  |
| `gridX` | `integer` | No |  |
| `gridY` | `integer` | No |  |
| `hazards` | `object` | No |  |
| `updateTime` | `string(date-time)` | No |  |
| `validTimes` | `ISO8601Interval` | No | A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start t... |
| `weather` | `object` | No |  |

**Additional properties:** `GridpointQuantitativeValueLayer`


---

## GridpointQuantitativeValueLayer

**Type:** `object`

A gridpoint layer consisting of quantitative values (numeric values with associated units of measure).


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uom` | `UnitOfMeasure` | No | A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Un... |
| `values` | `array[object]` | Yes |  |


---

## ISO8601Duration

**Type:** `string`

A time duration in ISO 8601 format.


---

## ISO8601Interval

**Type:** `object`

A time interval in ISO 8601 format. This can be one of:

    1. Start and end time
    2. Start time and duration
    3. Duration and end time
The string "NOW" can also be used in place of a start/end time.


### oneOf

1. `string`
2. `string`
3. `string`


---

## JsonLdContext

**Type:** `object`

### anyOf

1. `array[any]`
2. `object`


---

## LandRegionCode

**Type:** `string`

Land region code. These correspond to the six NWS regional headquarters:
* AR: Alaska Region
* CR: Central Region
* ER: Eastern Region
* PR: Pacific Region
* SR: Southern Region
* WR: Western Region


**Enum values:**

- `AR`
- `CR`
- `ER`
- `PR`
- `SR`
- `WR`


---

## MarineAreaCode

**Type:** `string`

Marine area code as defined in NWS Directive 10-302:
* AM: Western North Atlantic Ocean and along U.S. East Coast south of Currituck Beach Light NC following the coastline into Gulf of Mexico to Ocean Reef FL including the Caribbean
* AN: Western North Atlantic Ocean and along U.S. East Coast from Canadian border south to Currituck Beach Light NC
* GM: Gulf of Mexico and along the U.S. Gulf Coast from the Mexican border to Ocean Reef FL
* LC: Lake St. Clair
* LE: Lake Erie
* LH: Lake Huron
* LM: Lake Michigan
* LO: Lake Ontario
* LS: Lake Superior
* PH: Central Pacific Ocean including Hawaiian waters
* PK: North Pacific Ocean near Alaska and along Alaska coastline including the Bering Sea and the Gulf of Alaska
* PM: Western Pacific Ocean including Mariana Island waters
* PS: South Central Pacific Ocean including American Samoa waters
* PZ: Eastern North Pacific Ocean and along U.S. West Coast from Canadian border to Mexican border
* SL: St. Lawrence River above St. Regis


**Enum values:**

- `AM`
- `AN`
- `GM`
- `LC`
- `LE`
- `LH`
- `LM`
- `LO`
- `LS`
- `PH`
- `PK`
- `PM`
- `PS`
- `PZ`
- `SL`


---

## MarineRegionCode

**Type:** `string`

Marine region code. These are groups of marine areas combined.
* AL: Alaska waters (PK)
* AT: Atlantic Ocean (AM, AN)
* GL: Great Lakes (LC, LE, LH, LM, LO, LS, SL)
* GM: Gulf of Mexico (GM)
* PA: Eastern Pacific Ocean and U.S. West Coast (PZ)
* PI: Central and Western Pacific (PH, PM, PS)


**Enum values:**

- `AL`
- `AT`
- `GL`
- `GM`
- `PA`
- `PI`


---

## MetarPhenomenon

**Type:** `object`

An object representing a decoded METAR phenomenon string.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inVicinity` | `boolean` | No |  |
| `intensity` | `['string', 'null']` | Yes |  Enum: [`light`, `heavy`] |
| `modifier` | `['string', 'null']` | Yes |  Enum: [`patches`, `blowing`, `low_drifting`, `freezing`, `shallow`, +2 more] |
| `rawString` | `string` | Yes |  |
| `weather` | `string` | Yes |  Enum: [`fog_mist`, `dust_storm`, `dust`, `drizzle`, `funnel_cloud`, +18 more] |


---

## MetarSkyCoverage

**Type:** `string`

**Enum values:**

- `OVC`
- `BKN`
- `SCT`
- `FEW`
- `SKC`
- `CLR`
- `VV`


---

## NWSCenterWeatherServiceUnitId

**Type:** `string`

Three-letter identifier for a Center Weather Service Unit (CWSU).

**Enum values:**

- `ZAB`
- `ZAN`
- `ZAU`
- `ZBW`
- `ZDC`
- `ZDV`
- `ZFA`
- `ZFW`
- `ZHU`
- `ZID`
- `ZJX`
- `ZKC`
- `ZLA`
- `ZLC`
- `ZMA`
- `ZME`
- `ZMP`
- `ZNY`
- `ZOA`
- `ZOB`
- `ZSE`
- `ZTL`


---

## NWSConnectDocumentMetadata

**Type:** `object`

Metadata for an NWS Connect document.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | A longer description and/or caption. |
| `download` | `string(uri)` | No | The URL of the media content for the weather story. |
| `endTime` | `string(date-time)` | No | The time when the document becomes inactive. ISO8601 datetime. |
| `id` | `string(uuid)` | No |  |
| `priority` | `boolean` | No | An indicator that a weather story should be emphasized. |
| `startTime` | `string(date-time)` | No | The time when the document becomes active. ISO8601 datetime. |
| `title` | `string` | No | A short title. |
| `updateTime` | `string(date-time)` | No | When the document was last updated. ISO8601 datetime. |


---

## NWSForecastOfficeId

**Type:** `string`

Three-letter identifier for a NWS office.

**Enum values:**

- `AKQ`
- `ALY`
- `BGM`
- `BOX`
- `BTV`
- `BUF`
- `CAE`
- `CAR`
- `CHS`
- `CLE`
- `CTP`
- `GSP`
- `GYX`
- `ILM`
- `ILN`
- `LWX`
- `MHX`
- `OKX`
- `PBZ`
- `PHI`
- `RAH`
- `RLX`
- `RNK`
- `ABQ`
- `AMA`
- `BMX`
- `BRO`
- `CRP`
- `EPZ`
- `EWX`
- `FFC`
- `FWD`
- `HGX`
- `HUN`
- `JAN`
- `JAX`
- `KEY`
- `LCH`
- `LIX`
- `LUB`
- `LZK`
- `MAF`
- `MEG`
- `MFL`
- `MLB`
- `MOB`
- `MRX`
- `OHX`
- `OUN`
- `SHV`
- `SJT`
- `SJU`
- `TAE`
- `TBW`
- `TSA`
- `ABR`
- `APX`
- `ARX`
- `BIS`
- `BOU`
- `CYS`
- `DDC`
- `DLH`
- `DMX`
- `DTX`
- `DVN`
- `EAX`
- `FGF`
- `FSD`
- `GID`
- `GJT`
- `GLD`
- `GRB`
- `GRR`
- `ICT`
- `ILX`
- `IND`
- `IWX`
- `JKL`
- `LBF`
- `LMK`
- `LOT`
- `LSX`
- `MKX`
- `MPX`
- `MQT`
- `OAX`
- `PAH`
- `PUB`
- `RIW`
- `SGF`
- `TOP`
- `UNR`
- `BOI`
- `BYZ`
- `EKA`
- `FGZ`
- `GGW`
- `HNX`
- `LKN`
- `LOX`
- `MFR`
- `MSO`
- `MTR`
- `OTX`
- `PDT`
- `PIH`
- `PQR`
- `PSR`
- `REV`
- `SEW`
- `SGX`
- `SLC`
- `STO`
- `TFX`
- `TWC`
- `VEF`
- `AER`
- `AFC`
- `AFG`
- `AJK`
- `ALU`
- `GUM`
- `HPA`
- `HFO`
- `PPG`
- `PQE`
- `PQW`
- `STU`
- `NH1`
- `NH2`
- `ONA`
- `ONP`


---

## NWSNationalHQId

**Type:** `string`

Three-letter identifier for NWS National HQ.

**Enum values:**

- `NWS`


---

## NWSOfficeId

**Type:** `object`

### oneOf

1. `NWSForecastOfficeId` (NWSForecastOfficeId)
2. `NWSRegionalHQId` (NWSRegionalHQId)
3. `NWSNationalHQId` (NWSNationalHQId)


---

## NWSRegionalHQId

**Type:** `string`

Three-letter identifier for a NWS Regional HQ.

**Enum values:**

- `ARH`
- `CRH`
- `ERH`
- `PRH`
- `SRH`
- `WRH`


---

## NWSZoneID

**Type:** `string`

UGC identifier for a NWS forecast zone or county.
The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations).
The third letter will be Z for public/fire zone or C for county.



---

## NWSZoneType

**Type:** `string`

**Enum values:**

- `land`
- `marine`
- `forecast`
- `public`
- `coastal`
- `offshore`
- `fire`
- `county`


---

## Observation

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:ObservationStation`] |
| `barometricPressure` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `cloudLayers` | `['array', 'null']` | No |  |
| `dewpoint` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `heatIndex` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `icon` | `['string', 'null'](uri)` | No |  |
| `maxTemperatureLast24Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `minTemperatureLast24Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLast3Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLast6Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLastHour` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `presentWeather` | `array[MetarPhenomenon]` | No |  |
| `rawMessage` | `string` | No |  |
| `relativeHumidity` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `seaLevelPressure` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `station` | `string(uri)` | No |  |
| `stationId` | `string` | No |  |
| `stationName` | `string` | No |  |
| `temperature` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `textDescription` | `string` | No |  |
| `timestamp` | `string(date-time)` | No |  |
| `visibility` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windChill` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windDirection` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windGust` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windSpeed` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |


---

## ObservationCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[object]` | Yes |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## ObservationCollectionJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[Observation]` | No |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |


---

## ObservationGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Observation` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## ObservationJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:ObservationStation`] |
| `barometricPressure` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `cloudLayers` | `['array', 'null']` | No |  |
| `dewpoint` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `heatIndex` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `icon` | `['string', 'null'](uri)` | No |  |
| `maxTemperatureLast24Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `minTemperatureLast24Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLast3Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLast6Hours` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `precipitationLastHour` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `presentWeather` | `array[MetarPhenomenon]` | No |  |
| `rawMessage` | `string` | No |  |
| `relativeHumidity` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `seaLevelPressure` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `station` | `string(uri)` | No |  |
| `stationId` | `string` | No |  |
| `stationName` | `string` | No |  |
| `temperature` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `textDescription` | `string` | No |  |
| `timestamp` | `string(date-time)` | No |  |
| `visibility` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windChill` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windDirection` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windGust` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `windSpeed` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |


---

## ObservationStation

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:ObservationStation`] |
| `bearing` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `county` | `string(uri)` | No | A link to the NWS county zone containing this station. |
| `distance` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `fireWeatherZone` | `string(uri)` | No | A link to the NWS fire weather forecast zone containing this station. |
| `forecast` | `string(uri)` | No | A link to the NWS public forecast zone containing this station. |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `name` | `string` | No |  |
| `provider` | `string` | No | The data provider for this station. E.g., "ASOS," "MesoWest," etc. |
| `stationIdentifier` | `string` | No |  |
| `subProvider` | `string` | No | The sub-provider of for this station. E.g., "FAA," "DOT," etc. |
| `timeZone` | `string(iana-time-zone-identifier)` | No |  |


---

## ObservationStationCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[object]` | Yes |  |
| `observationStations` | `array[string(uri)]` | No |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## ObservationStationCollectionJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[ObservationStation]` | No |  |
| `observationStations` | `array[string(uri)]` | No |  |
| `pagination` | `PaginationInfo` | No | Links for retrieving more data from paged data sets |


---

## ObservationStationGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `ObservationStation` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## ObservationStationJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | Yes |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:ObservationStation`] |
| `bearing` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `county` | `string(uri)` | No | A link to the NWS county zone containing this station. |
| `distance` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `elevation` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `fireWeatherZone` | `string(uri)` | No | A link to the NWS fire weather forecast zone containing this station. |
| `forecast` | `string(uri)` | No | A link to the NWS public forecast zone containing this station. |
| `geometry` | `GeometryString` | Yes | A geometry represented in Well-Known Text (WKT) format. |
| `name` | `string` | No |  |
| `provider` | `string` | No | The data provider for this station. E.g., "ASOS," "MesoWest," etc. |
| `stationIdentifier` | `string` | No |  |
| `subProvider` | `string` | No | The sub-provider of for this station. E.g., "FAA," "DOT," etc. |
| `timeZone` | `string(iana-time-zone-identifier)` | No |  |


---

## Office

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`GovernmentOrganization`] |
| `address` | `object` | No |  |
| `approvedObservationStations` | `array[string(uri)]` | No |  |
| `email` | `string` | No |  |
| `faxNumber` | `string` | No |  |
| `id` | `string` | No |  |
| `name` | `string` | No |  |
| `nwsRegion` | `string` | No |  |
| `parentOrganization` | `string(uri)` | No |  |
| `responsibleCounties` | `array[string(uri)]` | No |  |
| `responsibleFireZones` | `array[string(uri)]` | No |  |
| `responsibleForecastZones` | `array[string(uri)]` | No |  |
| `sameAs` | `string(uri)` | No |  |
| `telephone` | `string` | No |  |


---

## OfficeBriefing

**Type:** `object`

Metadata for an NWS Connect document.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | A longer description and/or caption. |
| `download` | `string(uri)` | No | The URL of the media content for the weather story. |
| `endTime` | `string(date-time)` | No | The time when the document becomes inactive. ISO8601 datetime. |
| `id` | `string(uuid)` | No |  |
| `priority` | `boolean` | No | An indicator that a weather story should be emphasized. |
| `startTime` | `string(date-time)` | No | The time when the document becomes active. ISO8601 datetime. |
| `title` | `string` | No | A short title. |
| `updateTime` | `string(date-time)` | No | When the document was last updated. ISO8601 datetime. |


---

## OfficeHeadline

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `content` | `string` | No |  |
| `id` | `string` | No |  |
| `important` | `boolean` | No |  |
| `issuanceTime` | `string(date-time)` | No |  |
| `link` | `string(uri)` | No |  |
| `name` | `string` | No |  |
| `office` | `string(uri)` | No |  |
| `summary` | `['string', 'null']` | No |  |
| `title` | `string` | No |  |


---

## OfficeHeadlineCollection

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | Yes |  |
| `@graph` | `array[OfficeHeadline]` | Yes |  |


---

## OfficeWeatherStory

**Type:** `object`

Metadata for an NWS Connect document.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altText` | `string` | Yes | Alternative text description of the content of the image for assistive technology. |
| `description` | `string` | Yes | A longer description and/or caption. |
| `download` | `string(uri)` | Yes | The URL of the media content for the weather story. |
| `endTime` | `string(date-time)` | Yes | The time when the document becomes inactive. ISO8601 datetime. |
| `id` | `string(uuid)` | No |  |
| `order` | `integer` | Yes | The order in which a weather story should be displayed. Unique for each object. |
| `priority` | `boolean` | Yes | An indicator that a weather story should be emphasized. |
| `startTime` | `string(date-time)` | Yes | The time when the document becomes active. ISO8601 datetime. |
| `title` | `string` | Yes | A short title. |
| `updateTime` | `string(date-time)` | Yes | When the document was last updated. ISO8601 datetime. |


---

## OfficeWeatherStoryCollection

**Type:** `array`

**Items type:** `OfficeWeatherStory`

Schema: `OfficeWeatherStory` (object)
- `altText`: `string` *(required)* - Alternative text description of the content of the image ...
- `description`: `string` *(required)* - A longer description and/or caption.
- `download`: `string(uri)` *(required)* - The URL of the media content for the weather story.
- `endTime`: `string(date-time)` *(required)* - The time when the document becomes inactive. ISO8601 date...
- `id`: `string(uuid)`
- `order`: `integer` *(required)* - The order in which a weather story should be displayed. U...
- `priority`: `boolean` *(required)* - An indicator that a weather story should be emphasized.
- `startTime`: `string(date-time)` *(required)* - The time when the document becomes active. ISO8601 datetime.
- `title`: `string` *(required)* - A short title.
- `updateTime`: `string(date-time)` *(required)* - When the document was last updated. ISO8601 datetime.


---

## PaginationInfo

**Type:** `object`

Links for retrieving more data from paged data sets

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `next` | `string(uri)` | Yes | A link to the next page of records |


---

## Point

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Point`] |
| `astronomicalData` | `AstronomicalData` | No | An object representing sunrise, sunset, and twilight information for a location.  |
| `county` | `string(uri)` | No |  |
| `cwa` | `NWSForecastOfficeId` | No | Three-letter identifier for a NWS office. Enum: [`AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, +128 more] |
| `fireWeatherZone` | `string(uri)` | No |  |
| `forecast` | `string(uri)` | No |  |
| `forecastGridData` | `string(uri)` | No |  |
| `forecastHourly` | `string(uri)` | No |  |
| `forecastOffice` | `string(uri)` | No |  |
| `forecastZone` | `string(uri)` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `gridId` | `NWSForecastOfficeId` | No | Three-letter identifier for a NWS office. Enum: [`AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, +128 more] |
| `gridX` | `integer` | No |  |
| `gridY` | `integer` | No |  |
| `nwr` | `object` | No | NOAA Weather Radio metadata for this point |
| `observationStations` | `string(uri)` | No |  |
| `radarStation` | `string` | No |  |
| `relativeLocation` | `RelativeLocationGeoJson | RelativeLocationJsonLd` | No |  |
| `timeZone` | `string` | No |  |
| `type` | `string` | No | Whether the specific point is on land or marine Enum: [`land`, `marine`] |


---

## PointGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Point` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## PointJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | Yes |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Point`] |
| `astronomicalData` | `AstronomicalData` | No | An object representing sunrise, sunset, and twilight information for a location.  |
| `county` | `string(uri)` | No |  |
| `cwa` | `NWSForecastOfficeId` | No | Three-letter identifier for a NWS office. Enum: [`AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, +128 more] |
| `fireWeatherZone` | `string(uri)` | No |  |
| `forecast` | `string(uri)` | No |  |
| `forecastGridData` | `string(uri)` | No |  |
| `forecastHourly` | `string(uri)` | No |  |
| `forecastOffice` | `string(uri)` | No |  |
| `forecastZone` | `string(uri)` | No |  |
| `geometry` | `GeometryString` | Yes | A geometry represented in Well-Known Text (WKT) format. |
| `gridId` | `NWSForecastOfficeId` | No | Three-letter identifier for a NWS office. Enum: [`AKQ`, `ALY`, `BGM`, `BOX`, `BTV`, +128 more] |
| `gridX` | `integer` | No |  |
| `gridY` | `integer` | No |  |
| `nwr` | `object` | No | NOAA Weather Radio metadata for this point |
| `observationStations` | `string(uri)` | No |  |
| `radarStation` | `string` | No |  |
| `relativeLocation` | `RelativeLocationGeoJson | RelativeLocationJsonLd` | No |  |
| `timeZone` | `string` | No |  |
| `type` | `string` | No | Whether the specific point is on land or marine Enum: [`land`, `marine`] |


---

## PointString

**Type:** `string`


---

## ProblemDetail

**Type:** `object`

Detail about an error. This document conforms to RFC 7807 (Problem Details for HTTP APIs).

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `correlationId` | `string` | Yes | A unique identifier for the request, used for NWS debugging purposes. Please include this identif... |
| `detail` | `string` | Yes | A human-readable explanation specific to this occurrence of the problem. |
| `instance` | `string(uri)` | Yes | A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only a... |
| `status` | `number` | Yes | The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of ... |
| `title` | `string` | Yes | A short, human-readable summary of the problem type. |
| `type` | `string(uri)` | Yes | A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is no... |


---

## QuantitativeValue

**Type:** `object`

A structured value representing a measurement and its unit of measure. This object is a slightly modified version of the schema.org definition at https://schema.org/QuantitativeValue


### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxValue` | `number` | No | The maximum value of a range of measured values |
| `minValue` | `number` | No | The minimum value of a range of measured values |
| `qualityControl` | `string` | No | For values in observation records, the quality control flag from the MADIS system. The definition... Enum: [`Z`, `C`, `S`, `V`, `X`, +4 more] |
| `unitCode` | `UnitOfMeasure` | No | A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}". Un... |
| `value` | `['number', 'null']` | No | A measured value |


---

## RegionCode

**Type:** `object`

### oneOf

1. `LandRegionCode` (LandRegionCode)
2. `MarineRegionCode` (MarineRegionCode)


---

## RelativeLocation

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bearing` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `city` | `string` | No |  |
| `distance` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `state` | `string` | No |  |


---

## RelativeLocationGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `RelativeLocation` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## RelativeLocationJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bearing` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `city` | `string` | No |  |
| `distance` | `QuantitativeValue` | No | A structured value representing a measurement and its unit of measure. This object is a slightly ... |
| `geometry` | `GeometryString` | Yes | A geometry represented in Well-Known Text (WKT) format. |
| `state` | `string` | No |  |


---

## Sigmet

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `atsu` | `ATSUIdentifier` | No | ATSU Identifier |
| `end` | `string(date-time)` | No |  |
| `fir` | `['string', 'null']` | No |  |
| `id` | `string(uri)` | No |  |
| `issueTime` | `string(date-time)` | No |  |
| `phenomenon` | `['string', 'null'](uri)` | No |  |
| `sequence` | `['string', 'null']` | No |  |
| `start` | `string(date-time)` | No |  |


---

## SigmetCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[SigmetGeoJson]` | Yes |  |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## SigmetGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Sigmet` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## SigmetSequenceNumber

**Type:** `string`


---

## StateTerritoryCode

**Type:** `string`

**Enum values:**

- `AL`
- `AK`
- `AS`
- `AR`
- `AZ`
- `CA`
- `CO`
- `CT`
- `DE`
- `DC`
- `FL`
- `GA`
- `GU`
- `HI`
- `ID`
- `IL`
- `IN`
- `IA`
- `KS`
- `KY`
- `LA`
- `ME`
- `MD`
- `MA`
- `MI`
- `MN`
- `MS`
- `MO`
- `MT`
- `NE`
- `NV`
- `NH`
- `NJ`
- `NM`
- `NY`
- `NC`
- `ND`
- `OH`
- `OK`
- `OR`
- `PA`
- `PR`
- `RI`
- `SC`
- `SD`
- `TN`
- `TX`
- `UT`
- `VT`
- `VI`
- `VA`
- `WA`
- `WV`
- `WI`
- `WY`
- `MP`
- `PW`
- `FM`
- `MH`


---

## TextProduct

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `id` | `string` | No |  |
| `issuanceTime` | `string(date-time)` | No |  |
| `issuingOffice` | `string` | No |  |
| `productCode` | `string` | No |  |
| `productName` | `string` | No |  |
| `productText` | `string` | No |  |
| `wmoCollectiveId` | `string` | No |  |


---

## TextProductCollection

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[TextProduct]` | No |  |


---

## TextProductLocationCollection

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `locations` | `object` | No |  |


---

## TextProductTypeCollection

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[object]` | No |  |


---

## Time

**Type:** `string`

A time (in HHMM format). This is always specified in UTC (Zulu) time.


---

## UnitOfMeasure

**Type:** `string`

A string denoting a unit of measure, expressed in the format "{unit}" or "{namespace}:{unit}".
Units with the namespace "wmo" or "wmoUnit" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}.
Units with the namespace "nwsUnit" are currently custom and do not align to any standard.
Units with no namespace or the namespace "uc" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156).
Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.



---

## Zone

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Zone`] |
| `awipsLocationIdentifier` | `string` | No |  |
| `cwa` | `array[NWSForecastOfficeId]` | No |  |
| `effectiveDate` | `string(date-time)` | No |  |
| `expirationDate` | `string(date-time)` | No |  |
| `forecastOffice` | `string(uri)` | No |  |
| `forecastOffices` | `array[string(uri)]` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `gridIdentifier` | `string` | No |  |
| `id` | `NWSZoneID` | No | UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either... |
| `name` | `string` | No |  |
| `observationStations` | `array[string(uri)]` | No |  |
| `radarStation` | `['string', 'null']` | No |  |
| `state` | `StateTerritoryCode | string | null` | No |  |
| `timeZone` | `array[string(iana-time-zone-identifier)]` | No |  |
| `type` | `NWSZoneType` | No |  Enum: [`land`, `marine`, `forecast`, `public`, `coastal`, +3 more] |


---

## ZoneCollectionGeoJson

**Type:** `object`

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `features` | `array[object]` | Yes |  |
| `type` | `string` | Yes |  Enum: [`FeatureCollection`] |


---

## ZoneCollectionJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@graph` | `array[Zone]` | No |  |


---

## ZoneForecast

**Type:** `object`

An object representing a zone area forecast.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[object]` | No | An array of forecast periods. |
| `updated` | `string(date-time)` | No | The time this zone forecast product was published. |
| `zone` | `string(uri)` | No | An API link to the zone this forecast is for. |


---

## ZoneForecastGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `ZoneForecast` | Yes | An object representing a zone area forecast. |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## ZoneForecastJsonLd

**Type:** `object`

An object representing a zone area forecast.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `periods` | `array[object]` | No | An array of forecast periods. |
| `updated` | `string(date-time)` | No | The time this zone forecast product was published. |
| `zone` | `string(uri)` | No | An API link to the zone this forecast is for. |


---

## ZoneGeoJson

**Type:** `object`

A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `geometry` | `GeoJsonGeometry` | Yes | A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format. |
| `id` | `string(uri)` | No |  |
| `properties` | `Zone` | Yes |  |
| `type` | `string` | Yes |  Enum: [`Feature`] |


---

## ZoneJsonLd

**Type:** `object`

### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `@context` | `JsonLdContext` | No |  |
| `@id` | `string(uri)` | No |  |
| `@type` | `string` | No |  Enum: [`wx:Zone`] |
| `awipsLocationIdentifier` | `string` | No |  |
| `cwa` | `array[NWSForecastOfficeId]` | No |  |
| `effectiveDate` | `string(date-time)` | No |  |
| `expirationDate` | `string(date-time)` | No |  |
| `forecastOffice` | `string(uri)` | No |  |
| `forecastOffices` | `array[string(uri)]` | No |  |
| `geometry` | `GeometryString` | No | A geometry represented in Well-Known Text (WKT) format. |
| `gridIdentifier` | `string` | No |  |
| `id` | `NWSZoneID` | No | UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either... |
| `name` | `string` | No |  |
| `observationStations` | `array[string(uri)]` | No |  |
| `radarStation` | `['string', 'null']` | No |  |
| `state` | `StateTerritoryCode | string | null` | No |  |
| `timeZone` | `array[string(iana-time-zone-identifier)]` | No |  |
| `type` | `NWSZoneType` | No |  Enum: [`land`, `marine`, `forecast`, `public`, `coastal`, +3 more] |


---
