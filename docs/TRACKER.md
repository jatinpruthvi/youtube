# Master Architecture Track List

> **Project:** Automated Data Documentary Network  
> **Mission:** $1,500-$2,000/day ($45k-$60k/month) of profit from pure platform ad revenue in 24-36 months  
> **Progress:** **0/62 items (0%)** · **170.5h remaining** of **170.5h total**

<!-- Generated from tracker/items.json via `python3 scripts/track.py sync-md` -->

### Quick CLI Commands
```bash
python3 scripts/track.py summary          # Live dashboard by track & phase
python3 scripts/track.py next             # Show unblocked tasks ready to build right now
python3 scripts/track.py set INF-01 done  # Mark item done & auto-sync this Markdown file
```

---

## Executive Progress Summary

### By Phase
| Phase | Items Done | Total Effort |
| :--- | :---: | :---: |
| **Phase 0: Core Factory** | 0 / 38 | 107.5h |
| **Phase 1: Publishing and Early Operations** | 0 / 16 | 38.0h |
| **Phase 2: Monetization and Retention** | 0 / 6 | 16.0h |
| **Phase 3: Scale and Network** | 0 / 2 | 9.0h |

### By Architecture Track
| Track | Component | Items Done | Effort |
| :--- | :--- | :---: | :---: |
| **T01** | [Infrastructure, Compute & Cost Guardrails](#t01-infrastructure-compute--cost-guardrails) | 0 / 5 | 8.0h |
| **T02** | [Fact-Grounded Economic Data Layer (SQLite + FastMCP)](#t02-fact-grounded-economic-data-layer-sqlite--fastmcp) | 0 / 9 | 25.0h |
| **T03** | [Topic Intelligence & Editorial Queue](#t03-topic-intelligence--editorial-queue) | 0 / 4 | 9.0h |
| **T04** | [Claude Narrative Script & Fact-Audit Engine](#t04-claude-narrative-script--fact-audit-engine) | 0 / 4 | 12.0h |
| **T05** | [Voiceover, Forced Alignment & Audio Mastering](#t05-voiceover-forced-alignment--audio-mastering) | 0 / 6 | 14.0h |
| **T06** | [4K 60FPS GPU Rendering & Visual Template Library](#t06-4k-60fps-gpu-rendering--visual-template-library) | 0 / 11 | 36.0h |
| **T07** | [Thumbnail Factory & A/B Packaging](#t07-thumbnail-factory--ab-packaging) | 0 / 2 | 4.5h |
| **T08** | [Automated QA Gate & Mobile Approval Bot](#t08-automated-qa-gate--mobile-approval-bot) | 0 / 2 | 5.5h |
| **T09** | [Localization & Multi-Platform Publishing](#t09-localization--multi-platform-publishing) | 0 / 5 | 15.5h |
| **T10** | [Pipeline Orchestrator & Crash-Resumable DAG](#t10-pipeline-orchestrator--crash-resumable-dag) | 0 / 3 | 11.5h |
| **T11** | [Compliance, Monetization & India Payout Setup](#t11-compliance-monetization--india-payout-setup) | 0 / 5 | 10.0h |
| **T12** | [Analytics Feedback Loop & Multi-Channel Scale](#t12-analytics-feedback-loop--multi-channel-scale) | 0 / 6 | 19.5h |

---

## T01: Infrastructure, Compute & Cost Guardrails
*Hetzner CPX41 control plane + on-demand RTX 4090 worker, CUDA/NVENC runtime, storage, secrets, and ~$100/mo budget controls.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `INF-01` | `P0` | `P0` | 2h | — | **Provision the control plane and a provision-on-demand GPU worker within the monthly cost budget**<br/><sub>✓ The control plane is reachable over SSH with SQLite and the pipeline stack installed; a GPU worker provisions, encodes, and destroys cleanly from a script; at least 200GB NVMe is available; actual monthly spend remains within the approved budget. A local/developer-machine fallback is documented.</sub> |
| ⬜ Todo | `INF-02` | `P0` | `P0` | 2h | `INF-01` | **Install Python 3.11+, CUDA Toolkit, FFmpeg with NVENC (hevc_nvenc/h264_nvenc), and ManimGL/Cairo deps**<br/><sub>✓ ffmpeg -encoders shows h264_nvenc and hevc_nvenc; benchmarked 1080p30, 1440p60, and optional 4K60 5-second encodes report resolution, FPS, bitrate, and elapsed time.</sub> |
| ⬜ Todo | `INF-03` | `P0` | `P0` | 1.5h | `INF-02` | **Initialize Python project skeleton, pyproject.toml, .env secrets template, and logging config**<br/><sub>✓ Virtual environment builds cleanly; structured JSON logging writes to logs/ with secrets loaded strictly from .env.</sub> |
| ⬜ Todo | `INF-04` | `P1` | `P1` | 1.5h | `INF-03` | **Configure Cloudflare R2 (or Backblaze B2) archive sync & NVMe auto-pruning policy**<br/><sub>✓ Published masters and SQLite/JSON snapshots sync to R2; local scratch scene cache auto-cleans after 7 days.</sub> |
| ⬜ Todo | `INF-05` | `P1` | `P1` | 1h | `INF-03` | **Set up provider spend and total operating-cost telemetry**<br/><sub>✓ A configured hard spend cap exists for model and GPU providers; daily source, LLM, GPU, storage, and transfer costs are logged to SQLite and alerted when the configurable budget threshold is exceeded.</sub> |

<details>
<summary>Checklist View — T01 (0/5)</summary>

- [ ] **`INF-01`** (P0, 2h) — Provision the control plane and a provision-on-demand GPU worker within the monthly cost budget
- [ ] **`INF-02`** (P0, 2h) — Install Python 3.11+, CUDA Toolkit, FFmpeg with NVENC (hevc_nvenc/h264_nvenc), and ManimGL/Cairo deps
- [ ] **`INF-03`** (P0, 1.5h) — Initialize Python project skeleton, pyproject.toml, .env secrets template, and logging config
- [ ] **`INF-04`** (P1, 1.5h) — Configure Cloudflare R2 (or Backblaze B2) archive sync & NVMe auto-pruning policy
- [ ] **`INF-05`** (P1, 1h) — Set up provider spend and total operating-cost telemetry

</details>

## T02: Fact-Grounded Economic Data Layer (SQLite + FastMCP)
*Free public API connectors (World Bank, FRED, OECD, IMF, OWID, DBnomics, UN Data), SQLite warehouse with the production schema, FastMCP grounding server, and deterministic DataBrief generator.* (**0/9 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `DAT-01` | `P0` | `P0` | 2.5h | `INF-03` | **Design SQLite warehouse schema (data/schema.sql: dim_countries, fact_observations, episode_snapshots, rss_items, videos, ats_snapshots, hijack_attempts, hijack_results)**<br/><sub>✓ `sqlite3 data/production.db < data/schema.sql` initializes idempotently in WAL mode with migrations, foreign-key enforcement, source/license metadata, 217 ISO-3 countries, regions, currencies, flag paths, GeoJSON IDs, and a backup/restore smoke test.</sub> |
| ⬜ Todo | `DAT-02` | `P0` | `P0` | 3h | `DAT-01` | **Build World Bank API v2 connector with pagination, retry backoff, and indicator caching**<br/><sub>✓ Fetches full multi-decade history for NY.GDP.PCAP.PP.KD and writes clean rows to fact_observations in <10s. Connector tests replay recorded fixtures (DAT-09) rather than calling api.worldbank.org.</sub> |
| ⬜ Todo | `DAT-03` | `P0` | `P0` | 2.5h | `DAT-01` | **Build FRED API connector for US/global macro, CPI, wages, housing, and interest rates**<br/><sub>✓ Fetches FRED series with metadata units and frequency normalization into SQLite.</sub> |
| ⬜ Todo | `DAT-04` | `P0` | `P0` | 3h | `DAT-01` | **Build OECD SDMX API connector for Tier-1 average wages, tax wedge, and hours worked**<br/><sub>✓ Successfully parses OECD SDMX JSON/CSV payloads and maps all OECD members to ISO-3 codes.</sub> |
| ⬜ Todo | `DAT-05` | `P1` | `P1` | 2.5h | `DAT-01` | **Build DBnomics, UN Data, IMF and Our World in Data (OWID) secondary connectors**<br/><sub>✓ Ingests IMF debt-to-GDP / inflation forecasts and OWID long-run historical CSVs into unified schema.</sub> |
| ⬜ Todo | `DAT-06` | `P0` | `P0` | 3h | `DAT-02`, `DAT-03`, `DAT-04` | **Build Data Normalizer (ISO-3 reconciliation, PPP vs Nominal tagging, missing-year handling)**<br/><sub>✓ Zero orphan country names; explicitly flags latest available year per country and rejects unaligned units.</sub> |
| ⬜ Todo | `DAT-07` | `P0` | `P0` | 3.5h | `DAT-06` | **Build Deterministic Statistical Analyzer & DataBrief JSON + Fact-ID Ledger generator**<br/><sub>✓ Generates a frozen episode snapshot (JSON row-set keyed by episode_id) + DataBrief JSON with Top/Bottom N, medians, CAGRs, outliers, and F001..Fxxx IDs.</sub> |
| ⬜ Todo | `DAT-08` | `P0` | `P0` | 3h | `DAT-06` | **Build FastMCP data-grounding server (get_indicator, rank_countries, get_series, search_datasets)**<br/><sub>✓ Claude can call the MCP tools over stdio, receives only warehouse-backed rows with Fact IDs, and never receives a number that is absent from fact_observations.</sub> |
| ⬜ Todo | `DAT-09` | `P0` | `P0` | 2h | `DAT-01` | **Build the record/replay HTTP fixture harness so every connector test runs offline**<br/><sub>✓ A cassette layer records each provider response once into tests/fixtures/<provider>/ and replays it afterwards; the whole connector suite passes with outbound network disabled, which is what AGENTS.md section 5 requires and what 7 live providers otherwise make impossible.</sub> |

<details>
<summary>Checklist View — T02 (0/9)</summary>

- [ ] **`DAT-01`** (P0, 2.5h) — Design SQLite warehouse schema (data/schema.sql: dim_countries, fact_observations, episode_snapshots, rss_items, videos, ats_snapshots, hijack_attempts, hijack_results)
- [ ] **`DAT-02`** (P0, 3h) — Build World Bank API v2 connector with pagination, retry backoff, and indicator caching
- [ ] **`DAT-03`** (P0, 2.5h) — Build FRED API connector for US/global macro, CPI, wages, housing, and interest rates
- [ ] **`DAT-04`** (P0, 3h) — Build OECD SDMX API connector for Tier-1 average wages, tax wedge, and hours worked
- [ ] **`DAT-05`** (P1, 2.5h) — Build DBnomics, UN Data, IMF and Our World in Data (OWID) secondary connectors
- [ ] **`DAT-06`** (P0, 3h) — Build Data Normalizer (ISO-3 reconciliation, PPP vs Nominal tagging, missing-year handling)
- [ ] **`DAT-07`** (P0, 3.5h) — Build Deterministic Statistical Analyzer & DataBrief JSON + Fact-ID Ledger generator
- [ ] **`DAT-08`** (P0, 3h) — Build FastMCP data-grounding server (get_indicator, rank_countries, get_series, search_datasets)
- [ ] **`DAT-09`** (P0, 2h) — Build the record/replay HTTP fixture harness so every connector test runs offline

</details>

## T03: Topic Intelligence & Editorial Queue
*High-CPM niche scoring, YouTube outlier/autocomplete research, and packaging-first episode queue.* (**0/4 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `TOP-01` | `P0` | `P0` | 2h | `DAT-01` | **Create the editorial queue and seed a concentrated launch slate from real API indicators**<br/><sub>✓ A prioritized candidate pool, rather than a fixed publish quota, is stored with status, indicator codes, query-shaped title candidates, thumbnail concepts, source coverage, refresh date, and operator decision history. It begins with salary/take-home and adjacent cost-of-living topics, but weak or duplicate topics are rejected instead of filled to a target count.</sub> |
| ⬜ Todo | `TOP-02` | `P1` | `P1` | 3h | `TOP-01` | **Build YouTube Autocomplete & Outlier Competitor Video Miner**<br/><sub>✓ Discovers high views-to-subscriber outlier videos in economics/rankings niche and extracts title patterns.</sub> |
| ⬜ Todo | `TOP-03` | `P1` | `P1` | 2h | `TOP-02` | **Implement the evidence-based topic scorer**<br/><sub>✓ Ranks 0-100 using 50% measured search demand, 25% auction value, and 25% angle novelty; source verifiability and policy safety are hard filters. It returns a reasoned verdict and never promotes a topic automatically without the configured approval state.</sub> |
| ⬜ Todo | `TOP-04` | `P0` | `P0` | 2h | `TOP-01` | **Build the pre-production demand gate: stale-result test and query-volume rubric recorded per episode**<br/><sub>✓ Every queued episode carries a recorded demand verdict before ETL: exact query, top competitors, publish age, views/day, source coverage, policy risk, snapshot, and operator decision. Episodes with no defensible demand or policy-verifiable source coverage are refused rather than filled to a schedule. The evidence and override reason are retained for later cohort analysis.</sub> |

<details>
<summary>Checklist View — T03 (0/4)</summary>

- [ ] **`TOP-01`** (P0, 2h) — Create the editorial queue and seed a concentrated launch slate from real API indicators
- [ ] **`TOP-02`** (P1, 3h) — Build YouTube Autocomplete & Outlier Competitor Video Miner
- [ ] **`TOP-03`** (P1, 2h) — Implement the evidence-based topic scorer
- [ ] **`TOP-04`** (P0, 2h) — Build the pre-production demand gate: stale-result test and query-volume rubric recorded per episode

</details>

## T04: Claude Narrative Script & Fact-Audit Engine
*Prompt-cached Claude API storyboard generation, retention pacing schema, and zero-hallucination numeric audit.* (**0/4 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `SCR-01` | `P0` | `P0` | 3h | `DAT-07` | **Define Pydantic SceneGraph JSON Schema (acts, scenes, visual templates, data bindings, SFX cues)**<br/><sub>✓ Schema validates 10-18 min episodes, enforces visual-template entropy (no consecutive duplicates), and links every scene to fact IDs. The schema carries an explicit schema_version and the prompt_version that produced it, so a later model or prompt change can be re-audited against the episodes it already made.</sub> |
| ⬜ Todo | `SCR-02` | `P0` | `P0` | 4h | `SCR-01` | **Engineer versioned front-tier-model prompts with prompt caching and a registry fallback**<br/><sub>✓ Generates 1,700-2,600 word causal documentary scripts + SceneGraph JSON at a cost of <=$0.30/script with cache hit rate >70%, resolving the model through config/models.yaml and falling back to the registry's alternate provider on repeated fact-audit failure (DECISIONS.md D-07: a retired model is a config edit, not a release).</sub> |
| ⬜ Todo | `SCR-03` | `P0` | `P0` | 3h | `SCR-02` | **Build Zero-Hallucination Automated Fact-Audit Gate & targeted auto-repair loop**<br/><sub>✓ Extracts every script and visual-overlay number, rank, percentage, year, unit, and range; maps each to a Fact ID or rejects it. Rounding and unit rules are explicit, mismatches are repairable only through a new grounded SceneGraph, and golden fixtures cover currencies, percentages, ranks, dates, and ranges.</sub> |
| ⬜ Todo | `SCR-04` | `P1` | `P1` | 2h | `SCR-03` | **Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts every <=55s, end-screen bridge)**<br/><sub>✓ Scores script retention structure and rejects scripts lacking a hook contrast, mid-video inversion, or bridge.</sub> |

<details>
<summary>Checklist View — T04 (0/4)</summary>

- [ ] **`SCR-01`** (P0, 3h) — Define Pydantic SceneGraph JSON Schema (acts, scenes, visual templates, data bindings, SFX cues)
- [ ] **`SCR-02`** (P0, 4h) — Engineer versioned front-tier-model prompts with prompt caching and a registry fallback
- [ ] **`SCR-03`** (P0, 3h) — Build Zero-Hallucination Automated Fact-Audit Gate & targeted auto-repair loop
- [ ] **`SCR-04`** (P1, 2h) — Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts every <=55s, end-screen bridge)

</details>

## T05: Voiceover, Forced Alignment & Audio Mastering
*Zero-marginal-cost GPU TTS, pronunciation lexicon, WhisperX word timestamps, BGM ducking, SFX sync, and -14 LUFS mastering.* (**0/6 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `AUD-01` | `P0` | `P0` | 3h | `INF-02` | **Deploy local GPU TTS (MeloTTS primary, Kokoro-82M alternate, Azure Neural fallback) with a locked narrator voice**<br/><sub>✓ The locked local voice synthesizes clean 48kHz narration per scene and reports version/hash/runtime data; provider fallback is explicit and priced. Failure, missing voice assets, or flagged pronunciation blocks render rather than silently switching voice.</sub> |
| ⬜ Todo | `AUD-02` | `P0` | `P0` | 1.5h | `AUD-01` | **Build Pronunciation Lexicon & SSML/Pause Preprocessor for countries, currencies, and acronyms**<br/><sub>✓ Correctly pronounces 100+ tricky terms (Gini, PPP, OECD, Liechtenstein, Luxembourg, CHF, UAE, etc.) with natural pauses.</sub> |
| ⬜ Todo | `AUD-03` | `P0` | `P0` | 2.5h | `AUD-01` | **Integrate WhisperX / stable-ts Forced Word-Level Alignment**<br/><sub>✓ Outputs per-scene word timestamp JSON (start_ms, end_ms) accurate within +-40ms to drive visual animation triggers.</sub> |
| ⬜ Todo | `AUD-04` | `P0` | `P0` | 2h | `INF-03` | **Curate royalty-free ambient documentary BGM stems & micro-SFX library with license manifest**<br/><sub>✓ At least 6 loopable BGM tracks + 15 crisp SFX stored in assets/ with documented commercial licenses in assets/licenses.json.</sub> |
| ⬜ Todo | `AUD-05` | `P0` | `P0` | 3h | `AUD-03`, `AUD-04` | **Build FFmpeg Audio Mixer (sidechain BGM ducking, timestamped SFX injection, 2-pass -14 LUFS mastering)**<br/><sub>✓ Master audio hits -14.0 +- 0.5 LUFS, <= -1.0 dBTP true peak, smooth BGM ducking, and exact frame-synced SFX hits.</sub> |
| ⬜ Todo | `AUD-06` | `P0` | `P0` | 2h | `AUD-03` | **Build the spoken-number back-check: ASR the TTS audio and diff the numerals against the fact ledger**<br/><sub>✓ Each scene's synthesised narration is decoded with a local ASR model and every spoken numeral is normalised to a value and diffed against that scene's DataBrief Fact IDs; any mismatch, missing number or extra number fails the episode before render. The script fact-audit (SCR-03) proves the TEXT is grounded and proves nothing about the AUDIO, so a TTS engine can read 82,000 as eighty-two hundred and the channel's 0% hallucination claim is still false on screen. Runs on every episode; golden fixture for the number normaliser included.</sub> |

<details>
<summary>Checklist View — T05 (0/6)</summary>

- [ ] **`AUD-01`** (P0, 3h) — Deploy local GPU TTS (MeloTTS primary, Kokoro-82M alternate, Azure Neural fallback) with a locked narrator voice
- [ ] **`AUD-02`** (P0, 1.5h) — Build Pronunciation Lexicon & SSML/Pause Preprocessor for countries, currencies, and acronyms
- [ ] **`AUD-03`** (P0, 2.5h) — Integrate WhisperX / stable-ts Forced Word-Level Alignment
- [ ] **`AUD-04`** (P0, 2h) — Curate royalty-free ambient documentary BGM stems & micro-SFX library with license manifest
- [ ] **`AUD-05`** (P0, 3h) — Build FFmpeg Audio Mixer (sidechain BGM ducking, timestamped SFX injection, 2-pass -14 LUFS mastering)
- [ ] **`AUD-06`** (P0, 2h) — Build the spoken-number back-check: ASR the TTS audio and diff the numerals against the fact ledger

</details>

## T06: 4K 60FPS GPU Rendering & Visual Template Library
*Design system, 8 core animated chart templates, atomic scene parallelism, static caching, and direct NVENC encoding.* (**0/11 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `REN-01` | `P0` | `P0` | 3h | `INF-03` | **Establish the resolution-independent documentary visual design system**<br/><sub>✓ style_guide.yaml and font/flag/Natural Earth asset packs are verified at 1440p60 and 360px mobile preview. A RenderSpec Pydantic contract binds every template with Fact IDs, resolution preset, source footer, safe zones, timing, camera, and SFX fields; one golden fixture proves the contract.</sub> |
| ⬜ Todo | `REN-02` | `P0` | `P0` | 4h | `INF-02`, `REN-01` | **Build the 1440p60 launch render engine (atomic scenes, cache, and direct NVENC)**<br/><sub>✓ Streams raw 2560x1440 60fps RGB frames directly to NVENC with zero intermediate PNG bloat; benchmark >=25fps. The same pipeline supports 1080p30 fallback and 4K60 as a configuration preset; resolution is not embedded in template code.</sub> |
| ⬜ Todo | `REN-03` | `P0` | `P0` | 4h | `REN-02` | **Implement Template 1: BarChartRace (interpolated rankings, flags, rolling year counter, spotlight glow)**<br/><sub>✓ Renders a smooth launch-preset Top-15 bar race synchronized to WhisperX word highlights at 1440p60. Golden fixtures verify Fact-ID bindings, labels, source footer, mobile legibility, and AV timing.</sub> |
| ⬜ Todo | `REN-04` | `P0` | `P0` | 4.5h | `REN-02` | **Implement Template 2: WorldChoroplethMap (Natural Earth vectors, camera zoom/pan, animated color scale)**<br/><sub>✓ Renders crisp vector world map with smooth zoom onto target regions and animated country callout pins.</sub> |
| ⬜ Todo | `REN-05` | `P0` | `P0` | 3h | `REN-02` | **Implement Template 3: SpotlightCountryCard & Template 4: ChapterTitleCard**<br/><sub>✓ High-contrast KPI card with animated rolling counters, sparkline, rank badge, plus 3-second kinetic chapter transition.</sub> |
| ⬜ Todo | `REN-06` | `P0` | `P0` | 3.5h | `REN-02` | **Implement Template 5: DualSplitComparison (e.g., Nominal vs PPP or Country A vs Country B)**<br/><sub>✓ Animated split-screen comparison with synced delta callout and zero label overlap.</sub> |
| ⬜ Todo | `REN-07` | `P1` | `P1` | 4h | `REN-02` | **Implement Template 6: HistoricalLineRace & Template 7: AnimatedBubbleScatter**<br/><sub>✓ Multi-line time series with historical event pins + multi-axis animated bubble scatter with trails.</sub> |
| ⬜ Todo | `REN-08` | `P1` | `P1` | 3h | `REN-02` | **Implement Template 8: DistributionHistogram + Pre-Baked Ambient Motion Background**<br/><sub>✓ Bell-curve percentile visualizer plus 3 reusable subtle launch-resolution animated backdrop loops, with 1080p30/1440p60 asset variants and no unlicensed visual assets.</sub> |
| ⬜ Todo | `REN-09` | `P0` | `P0` | 2.5h | `AUD-05`, `REN-03`, `REN-04`, `REN-05`, `REN-06` | **Build Scene Concatenator, Master Muxer & Resolution Export Presets**<br/><sub>✓ Assembles a 10-18 minute launch MP4 with faststart atom, <=150ms AV drift, verified playback, and 1440p60 export; 1080p30 fallback and 4K60 presets are separately tested and export metadata is recorded.</sub> |
| ⬜ Todo | `SHR-01` | `P1` | `P1` | 2.5h | `REN-09` | **Build the 60s Shorts hook extractor (climax clip, burned captions, long-form link)**<br/><sub>✓ Renders a 9:16 60s cut from the episode's strongest DataBrief contrast with burned captions and uploads it as a Short carrying the long-form link in the description; long-form click-through per Short is logged in SQLite. Profit Multiplier 4 is worth $4.20-$10.50 per episode at $10.50 RPM, earned over the Short's lifetime rather than per day.</sub> |
| ⬜ Todo | `REN-10` | `P2` | `P2` | 2h | `REN-09`, `CMP-03` | **Add the 4K60 (3840x2160) preset to the render engine once the channel is monetized**<br/><sub>✓ The engine renders 3840x2160 at 60fps through the same NVENC pipe with no code path change beyond the preset, and the upgrade is applied to the top-performing episodes before new output. Gated behind YPP approval (DECISIONS.md D-12): 4K60 is 2.2x the pixels, render time and bitrate budget of 1440p60, and the repository holds no evidence that resolution moves CTR or retention for static data charts.</sub> |

<details>
<summary>Checklist View — T06 (0/11)</summary>

- [ ] **`REN-01`** (P0, 3h) — Establish the resolution-independent documentary visual design system
- [ ] **`REN-02`** (P0, 4h) — Build the 1440p60 launch render engine (atomic scenes, cache, and direct NVENC)
- [ ] **`REN-03`** (P0, 4h) — Implement Template 1: BarChartRace (interpolated rankings, flags, rolling year counter, spotlight glow)
- [ ] **`REN-04`** (P0, 4.5h) — Implement Template 2: WorldChoroplethMap (Natural Earth vectors, camera zoom/pan, animated color scale)
- [ ] **`REN-05`** (P0, 3h) — Implement Template 3: SpotlightCountryCard & Template 4: ChapterTitleCard
- [ ] **`REN-06`** (P0, 3.5h) — Implement Template 5: DualSplitComparison (e.g., Nominal vs PPP or Country A vs Country B)
- [ ] **`REN-07`** (P1, 4h) — Implement Template 6: HistoricalLineRace & Template 7: AnimatedBubbleScatter
- [ ] **`REN-08`** (P1, 3h) — Implement Template 8: DistributionHistogram + Pre-Baked Ambient Motion Background
- [ ] **`REN-09`** (P0, 2.5h) — Build Scene Concatenator, Master Muxer & Resolution Export Presets
- [ ] **`SHR-01`** (P1, 2.5h) — Build the 60s Shorts hook extractor (climax clip, burned captions, long-form link)
- [ ] **`REN-10`** (P2, 2h) — Add the 4K60 (3840x2160) preset to the render engine once the channel is monetized

</details>

## T07: Thumbnail Factory & A/B Packaging
*Programmatic 3-variant 1080p thumbnail generator via Playwright + mobile legibility checks for YouTube Test & Compare.* (**0/2 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `THM-01` | `P0` | `P0` | 3h | `REN-01` | **Build Playwright HTML/SVG -> 1920x1080 PNG Thumbnail Factory (3 distinct CTR templates)**<br/><sub>✓ Generates 3 distinct variants (Map Contrast, Flag Showdown, Outlier Spike) per episode in <10s.</sub> |
| ⬜ Todo | `THM-02` | `P1` | `P1` | 1.5h | `THM-01` | **Add Mobile-Scale Legibility Preview (168x94px grid) & Contrast Ratio Checker**<br/><sub>✓ Produces a 3-variant contact sheet at mobile thumbnail size and flags text contrast below WCAG AA.</sub> |

<details>
<summary>Checklist View — T07 (0/2)</summary>

- [ ] **`THM-01`** (P0, 3h) — Build Playwright HTML/SVG -> 1920x1080 PNG Thumbnail Factory (3 distinct CTR templates)
- [ ] **`THM-02`** (P1, 1.5h) — Add Mobile-Scale Legibility Preview (168x94px grid) & Contrast Ratio Checker

</details>

## T08: Automated QA Gate & Mobile Approval Bot
*Automated ffprobe/blackdetect/loudness/overlap linting and 3-minute Telegram/Discord founder approval workflow.* (**0/2 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `QAG-01` | `P0` | `P0` | 3h | `REN-09` | **Build Automated QC Suite (ffprobe spec check, blackdetect, freezedetect, silence, LUFS, layout overlap)**<br/><sub>✓ Outputs pass/fail QC JSON report; blocks publishing automatically on any spec violation or audio/video defect.</sub> |
| ⬜ Todo | `QAG-02` | `P0` | `P0` | 2.5h | `QAG-01`, `THM-01` | **Build Telegram (or Discord) Mobile Approval Bot with 30s hook clip, thumbnails & one-tap commands**<br/><sub>✓ Sends episode review bundle to phone; supports /approve, /regen_thumb, /fix_scene <n>, and /hold commands.</sub> |

<details>
<summary>Checklist View — T08 (0/2)</summary>

- [ ] **`QAG-01`** (P0, 3h) — Build Automated QC Suite (ffprobe spec check, blackdetect, freezedetect, silence, LUFS, layout overlap)
- [ ] **`QAG-02`** (P0, 2.5h) — Build Telegram (or Discord) Mobile Approval Bot with 30s hook clip, thumbnails & one-tap commands

</details>

## T09: Localization & Multi-Platform Publishing
*YouTube Data API v3 upload, de/fr/ja localized metadata & SRT captions (es-419/pt-BR/hi captions only), and Facebook In-Stream burned-caption cut.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `PUB-01` | `P0` | `P0` | 3h | `QAG-02` | **Configure YouTube OAuth and resumable publishing**<br/><sub>✓ Uploads a launch-preset master privately or as scheduled with chapter timestamps and custom thumbnail; retry, quota, duplicate, and partial-upload behavior are covered by fixtures.</sub> |
| ⬜ Todo | `PUB-02` | `P0` | `P1` | 3h | `PUB-01`, `AUD-03` | **Build Automated Metadata & SRT Subtitle Localizer (German, French, Japanese revenue set)**<br/><sub>✓ Translates title and description into de, fr and ja and uploads accurate time-coded SRTs for those three via YouTube localizations and captions APIs; ships es-419/pt-BR/hi captions only (reach, no revenue claim) and no ar. A market only receives localized metadata once captions in that language ship in the same commit - a German title over English audio is a negative-EV bounce (DECISIONS.md D-05). The language list is config (config/languages.json), not code.</sub> |
| ⬜ Todo | `PUB-03` | `P1` | `P1` | 3.5h | `REN-09`, `AUD-03` | **Build the eligible Facebook In-Stream cut and uploader**<br/><sub>✓ Eligibility is confirmed on the actual Page before any render code is written (DECISIONS.md D-06); once eligible, renders an FB-ready MP4 with high-contrast burned captions and uploads it on a schedule. If the program is not open to the Page, the item is closed as not-applicable and the Facebook revenue line is dropped from the model rather than assumed.</sub> |
| ⬜ Todo | `ANC-01` | `P1` | `P2` | 3.5h | `PUB-01` | **Build per-episode provenance pages and embeddable data assets**<br/><sub>✓ Every episode publishes a dataset page (frozen CSV, chart SVGs, methodology, source citation, snapshot hash, and license) on a static host with embeddable assets. External traffic and watch-time are logged in SQLite, while ancillary revenue remains an instrumented experiment rather than a baseline assumption.</sub> |
| ⬜ Todo | `PUB-04` | `P0` | `P0` | 2.5h | `PUB-01` | **Build subscriber-conversion engineering: series playlists, named-next end screens, pinned 'start here'**<br/><sub>✓ Every upload lands in a series playlist ordered by the intended viewing sequence, its end screen names one next episode rather than a subscribe prompt, and the pinned comment carries the chapter list, the dataset link and a 'start here' pointer. Subscribers gained per 1,000 views and per episode are logged in SQLite, ranked, and reviewed weekly. Subscribers are the YPP gate (1,000 at a 1% subscribe rate implies ~3,333 views/video, BASELINE.md section 8), so conversion is instrumented from EP01 and is a P0 rather than a Days-18-25 nicety.</sub> |

<details>
<summary>Checklist View — T09 (0/5)</summary>

- [ ] **`PUB-01`** (P0, 3h) — Configure YouTube OAuth and resumable publishing
- [ ] **`PUB-02`** (P0, 3h) — Build Automated Metadata & SRT Subtitle Localizer (German, French, Japanese revenue set)
- [ ] **`PUB-03`** (P1, 3.5h) — Build the eligible Facebook In-Stream cut and uploader
- [ ] **`ANC-01`** (P1, 3.5h) — Build per-episode provenance pages and embeddable data assets
- [ ] **`PUB-04`** (P0, 2.5h) — Build subscriber-conversion engineering: series playlists, named-next end screens, pinned 'start here'

</details>

## T10: Pipeline Orchestrator & Crash-Resumable DAG
*Idempotent scene-level state machine, job retries, disk cleanup, and daily batch runner.* (**0/3 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `VAL-01` | `P0` | `P0` | 6h | `INF-03`, `DAT-07`, `DAT-08`, `TOP-03`, `SCR-03`, `AUD-05`, `AUD-06`, `REN-09`, `THM-02`, `QAG-02`, `PUB-03`, `ORC-02` | **Produce and publish the first launch episode through the real end-to-end pipeline**<br/><sub>✓ A 10-14 minute episode uses the real warehouse, frozen DataBrief, SceneGraph, TTS/alignment, 1440p60 render, text/audio/visual fact-audit, QC, thumbnails, approval, and private-or-public YouTube publishing path. One reproducible episode is published; pipeline stage time, cost, operator review time, artifact hashes, replay evidence, and every manual intervention are recorded. The episode is launch inventory and establishes operating telemetry.</sub> |
| ⬜ Todo | `ORC-01` | `P0` | `P0` | 3.5h | `DAT-07`, `SCR-03`, `AUD-05`, `REN-09`, `PUB-01` | **Build Resumable Episode DAG Orchestrator (SQLite state machine with scene-level checkpointing)**<br/><sub>✓ Single CLI command `python -m src.orchestrator run <episode_id>` runs end-to-end and resumes cleanly from any crash. Artifacts use one layout, data/episodes/<episode_id>/<stage>/<content_hash>.<ext>, which is what makes resume and retry-after-edit cheap: a stage is skipped when its key file already exists.</sub> |
| ⬜ Todo | `ORC-02` | `P1` | `P1` | 2h | `ORC-01`, `QAG-02` | **Configure capacity-based batch scheduling**<br/><sub>✓ A systemd timer or cron processes the next approved queue item within configured capacity limits and leaves no autonomous publish without approval. It enforces weekday/weekend, retry, cost, and concurrency limits and produces a review bundle at the configured time.</sub> |

<details>
<summary>Checklist View — T10 (0/3)</summary>

- [ ] **`VAL-01`** (P0, 6h) — Produce and publish the first launch episode through the real end-to-end pipeline
- [ ] **`ORC-01`** (P0, 3.5h) — Build Resumable Episode DAG Orchestrator (SQLite state machine with scene-level checkpointing)
- [ ] **`ORC-02`** (P1, 2h) — Configure capacity-based batch scheduling

</details>

## T11: Compliance, Monetization & India Payout Setup
*Anti-demonetization guardrails, Content ID license ledger, YPP/FB monetization, and India USD tax/export setup.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `CMP-01` | `P0` | `P0` | 2h | — | **Create the flagship YouTube channel and baseline channel identity**<br/><sub>✓ Channel branding clearly identifies its original data-documentary role; custom thumbnail and long-upload eligibility are enabled; the channel name, description, links, and owner/access controls are recorded.</sub> |
| ⬜ Todo | `CMP-02` | `P0` | `P0` | 1.5h | `AUD-04`, `SCR-03` | **Implement Anti-Demonetization Policy Checklist & Citation/License Audit Manifest**<br/><sub>✓ Every episode ships with persistent source overlays, analytical commentary, verified provenance/license manifests, and no unsupported claims or unlicensed commercial assets. The checklist is a published gate report, not a visual-template-count proxy.</sub> |
| ⬜ Todo | `CMP-03` | `P1` | `P2` | 3h | `CMP-01`, `CMP-02` | **Complete platform monetization applications**<br/><sub>✓ YouTube YPP status is recorded after CMP-01/CMP-02; Facebook eligibility is recorded separately and only enables PUB-03 if the actual Page is approved. Neither success is assumed, and policy status is retained with evidence.</sub> |
| ⬜ Todo | `CMP-04` | `P1` | `P2` | 2h | `CMP-03`, `CMP-05` | **Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-8BEN 15% DTAA, GST LUT prep)**<br/><sub>✓ AdSense tax and payout settings are completed using current official guidance; Indian SWIFT settlement is tested and e-FIRA handling is documented. Any withholding result is recorded rather than guaranteed.</sub> |
| ⬜ Todo | `CMP-05` | `P1` | `P1` | 1.5h | `CMP-01` | **Write the docs/compliance/W8BEN_CHECKLIST.md filing artifact that CMP-04 executes**<br/><sub>✓ docs/compliance/W8BEN_CHECKLIST.md exists with the step-by-step AdSense tax-info filing for India (W-8BEN, 15% DTAA rate vs 24%/30%), GST registration plus LUT, and the e-FIRA archival workflow. Profit Multiplier 7 is $70/day of AdSense retained at the goal, so the artifact ships before the first payout cycle rather than after it.</sub> |

<details>
<summary>Checklist View — T11 (0/5)</summary>

- [ ] **`CMP-01`** (P0, 2h) — Create the flagship YouTube channel and baseline channel identity
- [ ] **`CMP-02`** (P0, 1.5h) — Implement Anti-Demonetization Policy Checklist & Citation/License Audit Manifest
- [ ] **`CMP-03`** (P1, 3h) — Complete platform monetization applications
- [ ] **`CMP-04`** (P1, 2h) — Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-8BEN 15% DTAA, GST LUT prep)
- [ ] **`CMP-05`** (P1, 1.5h) — Write the docs/compliance/W8BEN_CHECKLIST.md filing artifact that CMP-04 executes

</details>

## T12: Analytics Feedback Loop & Multi-Channel Scale
*YouTube/FB analytics ETL, retention drop-off diagnostics, RPM optimization, annual refreshes, and multi-channel cloning.* (**0/6 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `ANA-01` | `P1` | `P1` | 3h | `PUB-01` | **Build YouTube Analytics & Revenue daily ETL into SQLite (CTR, AVD, RPM, retention curves, geo)**<br/><sub>✓ Daily cron ingests video-level performance and geo RPM splits (US/UK/CA/AU share) into SQLite. Also records subscribers gained per 1,000 views and per episode, and the estimated-revenue-per-1,000-views figure needed to detect limited ads (BASELINE.md section 8, rule R15).</sub> |
| ⬜ Todo | `ANA-02` | `P1` | `P2` | 3h | `ANA-01`, `TOP-03` | **Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop**<br/><sub>✓ Weekly Telegram report correlates >3% retention drops to exact scene templates and updates topic scorer weights.</sub> |
| ⬜ Todo | `ANA-03` | `P2` | `P3` | 4h | `ANA-01`, `ORC-01` | **Build the automated dataset-refresh trigger**<br/><sub>✓ Detects new source releases, diffs frozen snapshots, identifies meaningful editorial/data changes, and queues refresh candidates only for eligible evergreen episodes. It verifies the output and records source/version changes; it does not append a meaningless year label.</sub> |
| ⬜ Todo | `ANA-04` | `P2` | `P3` | 5h | `ANA-02`, `CMP-03` | **Add multi-channel configuration isolation**<br/><sub>✓ The pipeline isolates channel credentials, branding, queue, warehouse scope, audience, publishing targets, and output assets by channel_id. A run for one channel cannot mutate another. Language/dubbing support remains separately gated because MLA availability is provider/platform controlled.</sub> |
| ⬜ Todo | `ANA-05` | `P1` | `P2` | 2.5h | `ANA-01` | **Run the first refresh wave: re-master and re-release the top 10 episodes when their datasets update**<br/><sub>✓ The ten best-performing episodes are re-rendered with refreshed source rows and re-released (same video where YouTube permits an update, new episode where the dataset changed materially), with a recorded views delta at day 28 per episode. A refresh adds views without adding library, so it is the only lever that raises views/video/day with no dilution (DECISIONS.md D-10); ANA-03 automates this trigger later, ANA-05 proves it once by hand.</sub> |
| ⬜ Todo | `ANA-06` | `P1` | `P1` | 2h | `ANA-01`, `THM-01` | **Build the monthly back-catalogue repackage pass (title + thumbnail refresh on high-impression, low-CTR videos)**<br/><sub>✓ For every video with >=1,000 impressions in the trailing 28 days and CTR below the channel median, two new thumbnails and one query-shaped title variant are generated and applied (title and thumbnail edits are permitted at any time on the Data API), with before/after CTR logged at day 28. Test & Compare has no public API, so the A/B launch happens through the QAG-02 approval bot. This is the only views-per-video lever that costs no new production and no new library (DECISIONS.md D-15).</sub> |

<details>
<summary>Checklist View — T12 (0/6)</summary>

- [ ] **`ANA-01`** (P1, 3h) — Build YouTube Analytics & Revenue daily ETL into SQLite (CTR, AVD, RPM, retention curves, geo)
- [ ] **`ANA-02`** (P1, 3h) — Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop
- [ ] **`ANA-03`** (P2, 4h) — Build the automated dataset-refresh trigger
- [ ] **`ANA-04`** (P2, 5h) — Add multi-channel configuration isolation
- [ ] **`ANA-05`** (P1, 2.5h) — Run the first refresh wave: re-master and re-release the top 10 episodes when their datasets update
- [ ] **`ANA-06`** (P1, 2h) — Build the monthly back-catalogue repackage pass (title + thumbnail refresh on high-impression, low-CTR videos)

</details>
