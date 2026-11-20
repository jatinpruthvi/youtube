---
name: economic-data-etl
description: Build fact-grounded economic data connectors (World Bank API v2, FRED, OECD SDMX, IMF DataMapper, OWID), DuckDB warehouse tables, ISO-3/PPP normalizers, and deterministic DataBrief JSON generators with auditable Fact IDs. Use whenever implementing or debugging Track T02 (DAT-01..DAT-07) or any economic dataset pipeline.
---

# Economic Data ETL & Fact-Grounding Skill

Use this skill when building or modifying `src/data/` connectors, DuckDB schemas, normalizers, or `DataBrief` generators.

## Core Invariants
1. **Zero LLM Memory Stats:** Every figure used in narration or visuals MUST originate from a stored API observation.
2. **ISO-3 Canonical Key:** All country rows MUST normalize to uppercase ISO 3166-1 alpha-3 (`USA`, `IND`, `CHE`, `DEU`). Drop or quarantine regional aggregates (`WLD`, `EAS`, `EUU`) into an explicit `is_aggregate = true` flag so they never pollute country rankings.
3. **Unit & Adjustment Explicitness:** Always store `unit`, `currency`, `is_ppp_adjusted`, and `is_inflation_adjusted`. Never mix nominal USD and PPP-adjusted international dollars in the same ranking without explicit dual-axis comparison.
4. **Immutable Episode Freeze:** Before scripting begins, freeze the exact DuckDB query output to `data/episodes/<episode_id>/snapshot.parquet` and generate `data_brief.json` with deterministic Fact IDs (`F001`, `F002`, ...).

## API Connector Contracts
* **World Bank API v2 (`https://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page=20000`)**
  - Respect pagination (`pages` metadata) and implement exponential backoff with jitter on HTTP 429/5xx.
  - Cache raw JSON responses by `(source, indicator_code, fetched_date)` to avoid redundant calls.
* **FRED API (`https://api.stlouisfed.org/fred/series/observations`)**
  - Require `FRED_API_KEY` from `.env`; handle `"."` missing observation strings cleanly as `None`.
* **OECD SDMX API (`https://sdmx.oecd.org/public/rest/data/...`)**
  - Request CSV/JSON SDMX format with `Accept: application/vnd.sdmx.data+json` or `text/csv`; map OECD country codes to ISO-3.
* **IMF DataMapper (`https://www.imf.org/external/datamapper/api/v1/{indicator}`)**
  - Parse nested `{values: {indicator: {ISO3: {year: value}}}}` structures cleanly; flag forecast years (`year > current_year`).
* **OWID Grapher (`https://ourworldindata.org/grapher/{slug}.csv`)**
  - Use `Code` column for ISO-3 filtering; discard rows with empty `Code`.

## Required DuckDB Tables
* `dim_countries(iso3 PRIMARY KEY, iso2, name, short_name, region, sub_region, currency_code, is_oecd, flag_asset_path)`
* `fact_observations(source, indicator_id, iso3, year, value, unit, is_ppp, is_real, is_forecast, fetched_at, PRIMARY KEY (source, indicator_id, iso3, year))`
* `episode_snapshots(episode_id, dataset_hash, parquet_path, created_at)`

## Verification Checklist
- [ ] Unit tests use local JSON/CSV fixtures (no live internet required during `pytest`).
- [ ] Zero duplicate `(source, indicator_id, iso3, year)` rows on idempotent re-runs (`INSERT OR REPLACE`).
- [ ] `DataBrief.json` validates against Pydantic schema and assigns unique `F001..Fxxx` IDs to Top-10, Bottom-10, median, mean, regional averages, and 10y/20y CAGRs.
