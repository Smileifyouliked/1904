---
name: public-apis
description: Find free or public APIs for a project from a catalog of about 1,950 APIs in 51 categories (weather, finance, geocoding, games, government, open data, and more), with auth, HTTPS, and CORS details for each. Use when the user asks for an API, a data source, a free alternative to a paid API, or "is there an API for X".
---

# Public APIs

`references/apis.md` is a snapshot of the community-maintained public-apis list. Each category is a `### Heading` followed by a table:

`| [Name](url) | Description | Auth | HTTPS | CORS |`

- **Auth**: `No`, `apiKey`, `OAuth`, `X-Mashape-Key`, or `User-Agent`.
- **HTTPS**: `Yes` or `No`.
- **CORS**: `Yes`, `No`, or `Unknown`. It matters only for calls made from browser JavaScript.

## Finding APIs

The file is about 260 KB, so don't read it top to bottom.

1. Pick the likely categories. The headings are Animals, Anime, Anti-Malware, Art & Design, Authentication & Authorization, Blockchain, Books, Business, Calendar, Cloud Storage & File Sharing, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Development, Dictionaries, Documents & Productivity, Email, Entertainment, Environment, Events, Finance, Food & Drink, Games & Comics, Geocoding, Government, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Phone, Photography, Programming, Science & Math, Security, Shopping, Social, Sports & Fitness, Test Data, Text Analysis, Tracking, Transportation, URL Shorteners, Vehicle, Video, and Weather.
2. Search for that heading or for keywords in descriptions, and read only the matching section or rows. Many APIs fit more than one topic, so also search a keyword across the whole file (for example "air quality" turns up rows under both Environment and Weather).
3. Filter on the user's constraints. Prefer `Auth: No` when they want no signup, `HTTPS: Yes` for anything in production, and `CORS: Yes` for a browser-only app.

## Answering

- Recommend 2 to 5 options, not the whole category. For each, give the name, link, what it provides, and its auth, HTTPS, and CORS values.
- Say which one you'd start with and why.
- The list is a snapshot and entries go stale: services shut down, change pricing, or add keys. Tell the user to check the provider's docs before relying on one. If you have web access, open the link and confirm the API is still up and still free before recommending it.
- The catalog says nothing about rate limits, history depth, or data quality. If those matter to the user (for example "I need 10 years of daily history"), say that the list can't answer it and check the provider's docs.
- If nothing in the catalog fits, say so rather than stretching a weak match.
