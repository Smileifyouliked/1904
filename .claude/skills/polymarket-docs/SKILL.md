---
name: polymarket-docs
description: Official Polymarket docs (Gamma market-data API, CLOB trading API, fees, resolution). Use when writing or checking code that reads Polymarket markets, prices, or places orders.
---

> **Provenance (generated doc skill, do not hand-edit; rebuild instead)**
> - Source: https://docs.polymarket.com/ (English pages listed in https://docs.polymarket.com/llms.txt; /cn/ pages excluded)
> - Built: 2026-09-28 (UTC)
> - Tool: Skill Seekers 3.9.1, enhance level 0 (no AI rewriting); docs/skill-configs/polymarket-docs.json
> - Verbatim copies: references/verbatim/polymarket-llms-full.md is the official https://docs.polymarket.com/llms-full.txt, saved unedited. Skill Seekers drops code blocks inside tabs and flattens tables on this site (for example the Gamma `outcomePrices` example on the Market Details page is missing from references/market-data.md). For exact field names, types and examples, read the verbatim file.
> - Rebuild steps: docs/skill-configs/README.md

# Polymarket-Docs Skill

Official Polymarket docs (Gamma market-data API, CLOB trading API, fees, resolution). Use when writing or checking code that reads Polymarket markets, prices, or places orders.

## When to Use This Skill

Use this skill when you need to:
- understand polymarket-docs features, APIs, and workflows
- find concrete code examples before implementing or debugging
- navigate the official documentation quickly through categorized references

## Quick Reference

### High-Signal Examples

**Example 1** (text):
```text
`end_timestamp`.** They were previously ignored; they now return
`400` with `invalid start_timestamp` / `invalid end_timestamp`. Use
`date`, `start_date`, and `end_date`.
```

**Example 2** (text):
```text
(boolean, always present) and `settlement` (object with `sequence`,
`timestamp`, `price`, `insurance_debit`; present only after
settlement). Instruments may also carry an optional `display_symbol`;
`symbol` is unchanged.
```

**Example 3** (text):
```text
import os

        from polymarket import AsyncSecureClient

        client = await AsyncSecureClient.create(
            private_key=os.environ["PRIVATE_KEY"],
            wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
        )
```

**Example 4** (text):
```text
The stream yields typed events for each subscription and can be closed when the
live view no longer needs updates.
```

**Example 5** (text):
```text
WorstCaseSize = max(|Position + OpenBuys|, |Position - OpenSells|)
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **api.md** - Api documentation
- **market-data.md** - Market-Data documentation
- **markets.md** - Markets documentation
- **other.md** - Other documentation
- **overview.md.md** - Overview.Md documentation
- **perps.md** - Perps documentation
- **rewards.md** - Rewards documentation
- **trading.md** - Trading documentation

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
