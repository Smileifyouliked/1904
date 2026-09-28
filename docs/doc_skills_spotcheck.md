# Doc skill spot-checks

Checked 2026-09-28 (UTC). Each fact was found in the skill, then compared with the
live page scraped by Firecrawl (maxAge 0, so no cached copy). All 9 matched.

| Skill | Fact | Where in the skill | Live page | Match |
|---|---|---|---|---|
| polymarket-docs | Gamma returns `outcomes`, `outcomePrices`, `clobTokenIds` as JSON-encoded string arrays, e.g. `"outcomePrices": "[\"0.085\", \"0.915\"]"`; parse each and match by index; index 0 is YES, index 1 is NO | references/verbatim/polymarket-llms-full.md (Market Details). Not in the Skill Seekers references. | https://docs.polymarket.com/market-data/market-details | yes |
| polymarket-docs | Weather category: taker fee rate 0.05, maker fee rate 0; fees are applied at match time and are not included in orders | references/trading.md and verbatim | https://docs.polymarket.com/trading/fees | yes |
| polymarket-docs | Gamma API base URL is `https://gamma-api.polymarket.com` | references/api.md | https://docs.polymarket.com/market-data/market-details (curl example) | yes |
| nws-api-docs | A User-Agent header is required to identify the application | references/verbatim/services-web-api.md | https://www.weather.gov/documentation/services-web-api | yes |
| nws-api-docs | Rate limit is not public; after hitting it, retry once it clears, typically within 5 seconds | references/verbatim/services-web-api.md | same page | yes |
| nws-api-docs | Endpoint `GET /stations/{stationId}/observations/latest` exists | references/stations.md | same page (endpoint list) and https://api.weather.gov/openapi.json | yes |
| open-meteo-docs | ECMWF IFS 0.25° ensemble: 51 members, 15 days, updated every 6 hours | references/verbatim/ensemble-api.md | https://open-meteo.com/en/docs/ensemble-api | yes |
| open-meteo-docs | `forecast_days`: integer 0-35, default 7 | references/verbatim/ensemble-api.md | same page | yes |
| open-meteo-docs | Free API: under 10,000 calls/day, 5,000/hour, 600/minute, non-commercial only; "integrating our service into commercial products" counts as commercial | references/verbatim/terms.md | https://open-meteo.com/en/terms | yes |

Also confirmed with a live call: `models=ecmwf_ifs025` is a valid Open-Meteo
ensemble model name (request to ensemble-api.open-meteo.com for 40.7769,-73.874
returned `temperature_2m_member01` and later members in °F).

## Known gaps in the Skill Seekers part (use the verbatim files instead)

- Polymarket: 207 of the 306 English doc pages made it into `references/*.md`;
  the verbatim `llms-full.txt` copy has all of them. Code blocks inside tabs
  (including the `outcomePrices` example) and table line breaks are lost.
- Open-Meteo: model tables, parameter tables and model names are missing from
  `references/*.md`.
- NWS: Skill Seekers returned no content for the docs web page; the API spec part
  is complete (69 paths).
