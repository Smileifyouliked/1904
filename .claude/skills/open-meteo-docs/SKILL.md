---
name: open-meteo-docs
description: Official Open-Meteo docs: forecast, ensemble, historical-forecast and previous-runs APIs, plus terms, licence and pricing. Use when writing or checking code that calls Open-Meteo, or deciding if its licence allows our use.
---

> **Provenance (generated doc skill, do not hand-edit; rebuild instead)**
> - Source: https://open-meteo.com/en/docs and the ensemble, historical-forecast, previous-runs, historical-weather, model-updates, terms, licence and pricing pages
> - Built: 2026-09-28 (UTC)
> - Tool: Skill Seekers 3.9.1, enhance level 0 (no AI rewriting); docs/skill-configs/open-meteo-docs.json
> - Verbatim copies: references/verbatim/ holds each page converted from the official HTML. Skill Seekers missed the model tables and parameter tables on these pages, so read the verbatim files for model names, parameters and licence terms.
> - Rebuild steps: docs/skill-configs/README.md

# Open-Meteo-Docs Skill

Official Open-Meteo docs: forecast, ensemble, historical-forecast and previous-runs APIs, plus terms, licence and pricing. Use when writing or checking code that calls Open-Meteo, or deciding if its licence allows our use.

## When to Use This Skill

Use this skill when you need to:
- understand open-meteo-docs features, APIs, and workflows
- find concrete code examples before implementing or debugging
- navigate the official documentation quickly through categorized references

## Quick Reference

### High-Signal Examples

**Example 1** (json):
```json
{
    "error": true, 
    "reason": "Cannot initialize WeatherVariable from invalid String value
	    tempeture_2m for key hourly" 
}
```

**Example 2** (jsx):
```jsx
<a href="https://open-meteo.com/">
	Weather data by Open-Meteo.com
</a>
```

### Key Usage Notes

**Pattern 1:** Data Sources Open-Meteo utilises open-data from various national weather services including: Atmospheric, ensemble and wave forecasts from Deutsche...

```
<a href="https://open-meteo.com/">
	Weather data by Open-Meteo.com
</a>
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **api.md** - Api documentation
- **other.md** - Other documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### Start Here
Start with the getting_started or tutorials reference files for foundational concepts.

### For Specific Features
Use the appropriate category reference file (api, guides, etc.) for detailed information.

### For Code Examples
Use the high-signal examples above first, then open the matching reference file for full context.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference entries are filtered to avoid low-signal placeholders and inline tokens

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
