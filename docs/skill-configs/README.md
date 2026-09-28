# Doc skill build configs

These files rebuild the generated doc skills in `.claude/skills/*-docs/`.
Each skill has two parts:

1. The Skill Seekers output (`SKILL.md` plus `references/*.md`), built with
   `--enhance-level 0` so no AI rewrites the docs.
2. `references/verbatim/`: unedited official text saved by `fetch_verbatim.py`.
   Skill Seekers 3.9.1 loses content on these sites: code blocks inside tabs and
   tables on Polymarket and Open-Meteo, and the whole NWS docs page. When the two
   parts disagree, the verbatim copy wins.

Built 2026-09-28 with Skill Seekers 3.9.1. Rebuild a skill whenever the real API
behaves differently from what its skill says.

## Setup (once, on a laptop or dev box, never on the EC2 trading server)

```bash
python3 -m venv .venv-tools
.venv-tools/bin/pip install skill-seekers==3.9.1 requests beautifulsoup4 markdownify
```

## Polymarket

`polymarket-docs.json` lists the English `.md` page URLs from
https://docs.polymarket.com/llms.txt and its nested `_llms/` index files.
The `.md` URLs are used because the HTML pages hide tab content. To refresh the
URL list, re-collect every `https://docs.polymarket.com/...md` link from llms.txt
and the `_llms/en/...` files it links, drop `/cn/` and `/_llms/` URLs, and put
them in `start_urls`.

```bash
.venv-tools/bin/skill-seekers create docs/skill-configs/polymarket-docs.json --enhance-level 0 -o build/polymarket-docs
.venv-tools/bin/python docs/skill-configs/fetch_verbatim.py docs/skill-configs/polymarket-docs.verbatim.json build/polymarket-docs
```

## NWS (api.weather.gov)

Skill Seekers treats any `.json` file as its own config, so convert the
OpenAPI spec to YAML first.

```bash
curl -sL https://api.weather.gov/openapi.json -o build/nws-openapi.json
.venv-tools/bin/python -c "import json,yaml;yaml.safe_dump(json.load(open('build/nws-openapi.json')),open('build/nws-openapi.yaml','w'),sort_keys=False)"
.venv-tools/bin/skill-seekers create build/nws-openapi.yaml --name nws-api-docs --enhance-level 0 -o build/nws-api-docs \
  --description "Official NWS API (api.weather.gov) OpenAPI spec: endpoints, parameters, response schemas. Use when writing or checking code that calls api.weather.gov."
.venv-tools/bin/python docs/skill-configs/fetch_verbatim.py docs/skill-configs/nws-api-docs.verbatim.json build/nws-api-docs
```

## Open-Meteo

```bash
.venv-tools/bin/skill-seekers create docs/skill-configs/open-meteo-docs.json --enhance-level 0 -o build/open-meteo-docs
.venv-tools/bin/python docs/skill-configs/fetch_verbatim.py docs/skill-configs/open-meteo-docs.verbatim.json build/open-meteo-docs
```

## After any build

1. Delete the duplicate `references/documentation/` folder (move its `index.md`
   up to `references/`) and any empty `assets/` or `scripts/` folders.
2. Add the provenance block under the SKILL.md frontmatter: source URL, build
   date, Skill Seekers version, and where the verbatim copies are.
3. Copy the result to `.claude/skills/<name>/`.
4. Spot-check 3 facts in the skill against the live page with Firecrawl, and
   record them in `docs/doc_skills_spotcheck.md`.
