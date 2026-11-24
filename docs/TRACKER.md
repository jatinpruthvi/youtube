# Master Architecture Track List

> **Project:** Automated Data Documentary Network  
> **Mission:** $1,500-$2,000/day ($45k-$60k/month) of profit from pure platform ad revenue in 24-36 months  
> **Progress:** **0/60 items (0%)** · **166.5h remaining** of **166.5h total**

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
| **Phase 0: Pipeline MVP (Days 1–10)** | 0 / 36 | 103.0h |
| **Phase 1: Launch Sprint, 30 episodes (Days 11–33)** | 0 / 16 | 38.5h |
| **Phase 2: Monetization & Retention Optimization (Months 2–6)** | 0 / 6 | 16.0h |
| **Phase 3: Multi-Channel Network Scale (Months 7–36)** | 0 / 2 | 9.0h |

### By Architecture Track
| Track | Component | Items Done | Effort |
| :--- | :--- | :---: | :---: |
| **T01** | [Infrastructure, Compute & Cost Guardrails](#t01-infrastructure-compute--cost-guardrails) | 0 / 5 | 8.0h |
| **T02** | [Fact-Grounded Economic Data Layer (SQLite + FastMCP)](#t02-fact-grounded-economic-data-layer-sqlite--fastmcp) | 0 / 9 | 25.0h |
| **T03** | [Topic Intelligence & Editorial Queue](#t03-topic-intelligence--editorial-queue) | 0 / 4 | 9.0h |
| **T04** | [Claude Narrative Script & Fact-Audit Engine](#t04-claude-narrative-script--fact-audit-engine) | 0 / 4 | 12.0h |
| **T05** | [Voiceover, Forced Alignment & Audio Mastering](#t05-voiceover-forced-alignment--audio-mastering) | 0 / 5 | 12.0h |
| **T06** | [4K 60FPS GPU Rendering & Visual Template Library](#t06-4k-60fps-gpu-rendering--visual-template-library) | 0 / 11 | 36.0h |
| **T07** | [Thumbnail Factory & A/B Packaging](#t07-thumbnail-factory--ab-packaging) | 0 / 2 | 4.5h |
| **T08** | [Automated QA Gate & Mobile Approval Bot](#t08-automated-qa-gate--mobile-approval-bot) | 0 / 2 | 5.5h |
| **T09** | [Localization & Multi-Platform Publishing](#t09-localization--multi-platform-publishing) | 0 / 5 | 15.5h |
| **T10** | [Pipeline Orchestrator & Crash-Resumable DAG](#t10-pipeline-orchestrator--crash-resumable-dag) | 0 / 3 | 11.5h |
| **T11** | [Compliance, Monetization & India Payout Setup](#t11-compliance-monetization--india-payout-setup) | 0 / 5 | 10.0h |
| **T12** | [Analytics Feedback Loop & Multi-Channel Scale](#t12-analytics-feedback-loop--multi-channel-scale) | 0 / 5 | 17.5h |

---

## T01: Infrastructure, Compute & Cost Guardrails
*Hetzner CPX41 control plane + on-demand RTX 4090 worker, CUDA/NVENC runtime, storage, secrets, and ~$100/mo budget controls.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `INF-01` | `P0` | `P0` | 2h | — | **Provision Hetzner CPX41 control plane + on-demand RTX 4090 worker within ~$100/mo budget**<br/><sub>✓ CPX41 reachable over SSH with the cron/SQLite/FastMCP stack installed; an on-demand RTX 4090 worker provisions and destroys cleanly via API for a 2-hour render window; >=200GB NVMe free.</sub> |
| ⬜ Todo | `INF-02` | `P0` | `P0` | 2h | `INF-01` | **Install Python 3.11+, CUDA Toolkit, FFmpeg with NVENC (hevc_nvenc/h264_nvenc), and ManimGL/Cairo deps**<br/><sub>✓ ffmpeg -encoders shows h264_nvenc and hevc_nvenc; test 4K60 5-second GPU encode completes in <3 seconds.</sub> |
| ⬜ Todo | `INF-03` | `P0` | `P0` | 1.5h | `INF-02` | **Initialize Python project skeleton, pyproject.toml, .env secrets template, and logging config**<br/><sub>✓ Virtual environment builds cleanly; structured JSON logging writes to logs/ with secrets loaded strictly from .env.</sub> |
| ⬜ Todo | `INF-04` | `P1` | `P1` | 1.5h | `INF-03` | **Configure Cloudflare R2 (or Backblaze B2) archive sync & NVMe auto-pruning policy**<br/><sub>✓ Published masters and SQLite/JSON snapshots sync to R2; local scratch scene cache auto-cleans after 7 days.</sub> |
| ⬜ Todo | `INF-05` | `P1` | `P1` | 1h | `INF-03` | **Set up API spend guardrails & monthly cost telemetry (Claude API + GPU runtime + R2)**<br/><sub>✓ Hard Anthropic monthly spend cap set; daily cost summary logged to SQLite and sent via Telegram if >$4/day.</sub> |

<details>
<summary>Checklist View — T01 (0/5)</summary>

- [ ] **`INF-01`** (P0, 2h) — Provision Hetzner CPX41 control plane + on-demand RTX 4090 worker within ~$100/mo budget
- [ ] **`INF-02`** (P0, 2h) — Install Python 3.11+, CUDA Toolkit, FFmpeg with NVENC (hevc_nvenc/h264_nvenc), and ManimGL/Cairo deps
- [ ] **`INF-03`** (P0, 1.5h) — Initialize Python project skeleton, pyproject.toml, .env secrets template, and logging config
- [ ] **`INF-04`** (P1, 1.5h) — Configure Cloudflare R2 (or Backblaze B2) archive sync & NVMe auto-pruning policy
- [ ] **`INF-05`** (P1, 1h) — Set up API spend guardrails & monthly cost telemetry (Claude API + GPU runtime + R2)

</details>

## T02: Fact-Grounded Economic Data Layer (SQLite + FastMCP)
*Free public API connectors (World Bank, FRED, OECD, IMF, OWID, DBnomics, UN Data), SQLite warehouse with the production schema, FastMCP grounding server, and deterministic DataBrief generator.* (**0/9 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `DAT-01` | `P0` | `P0` | 2.5h | `INF-03` | **Design SQLite warehouse schema (data/schema.sql: dim_countries, fact_observations, episode_snapshots, rss_items, videos, ats_snapshots, hijack_attempts, hijack_results)**<br/><sub>✓ `sqlite3 data/production.db < data/schema.sql` initializes idempotently in WAL mode with 217 ISO-3 countries, regions, currencies, flag paths and GeoJSON IDs.</sub> |
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
| ⬜ Todo | `TOP-01` | `P0` | `P0` | 2h | `DAT-01` | **Create Editorial Queue DB & seed initial 30-Video Launch Slate mapped to real API indicators**<br/><sub>✓ 30 topics stored with status, target indicator codes, query-shaped title candidates and thumbnail concepts, seeded as ONE cluster 30 deep (20 salary/take-home + 10 adjacent cost-of-living, DECISIONS.md D-11): no format-label titles, no two episodes sharing a thesis, and every title a query a person would type.</sub> |
| ⬜ Todo | `TOP-02` | `P1` | `P1` | 3h | `TOP-01` | **Build YouTube Autocomplete & Outlier Competitor Video Miner**<br/><sub>✓ Discovers high views-to-subscriber outlier videos in economics/rankings niche and extracts title patterns.</sub> |
| ⬜ Todo | `TOP-03` | `P1` | `P1` | 2h | `TOP-02` | **Implement automated Topic Scorer (Tier-1 demand, CPM weight, data completeness, curiosity gap)**<br/><sub>✓ Ranks candidate topics 0-100 and auto-promotes top-scoring unused topics into the daily pipeline queue.</sub> |
| ⬜ Todo | `TOP-04` | `P0` | `P0` | 2h | `TOP-01` | **Build the pre-production demand gate: stale-result test and query-volume rubric recorded per episode**<br/><sub>✓ Every queued episode carries a recorded demand verdict before the ETL stage: the top-3 competitor results for the exact query, their age in years, and their views/day (the stale-result score, VIEW_OPTIMIZATION section 2.2). An episode with no query volume or with recent top results is refused by the queue instead of being produced. Ten minutes of research per episode; this is the only mechanism that removes no-demand videos before they dilute views/video/day (DECISIONS.md D-10).</sub> |

<details>
<summary>Checklist View — T03 (0/4)</summary>

- [ ] **`TOP-01`** (P0, 2h) — Create Editorial Queue DB & seed initial 30-Video Launch Slate mapped to real API indicators
- [ ] **`TOP-02`** (P1, 3h) — Build YouTube Autocomplete & Outlier Competitor Video Miner
- [ ] **`TOP-03`** (P1, 2h) — Implement automated Topic Scorer (Tier-1 demand, CPM weight, data completeness, curiosity gap)
- [ ] **`TOP-04`** (P0, 2h) — Build the pre-production demand gate: stale-result test and query-volume rubric recorded per episode

</details>

## T04: Claude Narrative Script & Fact-Audit Engine
*Prompt-cached Claude API storyboard generation, retention pacing schema, and zero-hallucination numeric audit.* (**0/4 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `SCR-01` | `P0` | `P0` | 3h | `DAT-07` | **Define Pydantic SceneGraph JSON Schema (acts, scenes, visual templates, data bindings, SFX cues)**<br/><sub>✓ Schema validates 10-18 min episodes, enforces visual-template entropy (no consecutive duplicates), and links every scene to fact IDs. The schema carries an explicit schema_version and the prompt_version that produced it, so a later model or prompt change can be re-audited against the episodes it already made.</sub> |
| ⬜ Todo | `SCR-02` | `P0` | `P0` | 4h | `SCR-01` | **Engineer versioned front-tier-model prompts with prompt caching and a registry fallback**<br/><sub>✓ Generates 1,700-2,600 word causal documentary scripts + SceneGraph JSON at a cost of <=$0.30/script with cache hit rate >70%, resolving the model through config/models.yaml and falling back to the registry's alternate provider on repeated fact-audit failure (DECISIONS.md D-07: a retired model is a config edit, not a release).</sub> |
| ⬜ Todo | `SCR-03` | `P0` | `P0` | 3h | `SCR-02` | **Build Zero-Hallucination Automated Fact-Audit Gate & targeted auto-repair loop**<br/><sub>✓ Extracts every number/rank/percentage in narration, cross-checks against DataBrief (+-0.5% tolerance), and auto-repairs mismatches.</sub> |
| ⬜ Todo | `SCR-04` | `P1` | `P1` | 2h | `SCR-03` | **Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts every <=55s, end-screen bridge)**<br/><sub>✓ Scores script retention structure and rejects scripts lacking a hook contrast, mid-video inversion, or bridge.</sub> |

<details>
<summary>Checklist View — T04 (0/4)</summary>

- [ ] **`SCR-01`** (P0, 3h) — Define Pydantic SceneGraph JSON Schema (acts, scenes, visual templates, data bindings, SFX cues)
- [ ] **`SCR-02`** (P0, 4h) — Engineer versioned front-tier-model prompts with prompt caching and a registry fallback
- [ ] **`SCR-03`** (P0, 3h) — Build Zero-Hallucination Automated Fact-Audit Gate & targeted auto-repair loop
- [ ] **`SCR-04`** (P1, 2h) — Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts every <=55s, end-screen bridge)

</details>

## T05: Voiceover, Forced Alignment & Audio Mastering
*Zero-marginal-cost GPU TTS, pronunciation lexicon, WhisperX word timestamps, BGM ducking, SFX sync, and -14 LUFS mastering.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `AUD-01` | `P0` | `P0` | 3h | `INF-02` | **Deploy local GPU TTS (MeloTTS primary, Kokoro-82M alternate, Azure Neural fallback) with a locked narrator voice**<br/><sub>✓ MeloTTS synthesizes clean 48kHz broadcast narration per scene at >10x real-time with $0 marginal API cost; Azure fallback triggers on any flagged pronunciation.</sub> |
| ⬜ Todo | `AUD-02` | `P0` | `P0` | 1.5h | `AUD-01` | **Build Pronunciation Lexicon & SSML/Pause Preprocessor for countries, currencies, and acronyms**<br/><sub>✓ Correctly pronounces 100+ tricky terms (Gini, PPP, OECD, Liechtenstein, Luxembourg, CHF, UAE, etc.) with natural pauses.</sub> |
| ⬜ Todo | `AUD-03` | `P0` | `P0` | 2.5h | `AUD-01` | **Integrate WhisperX / stable-ts Forced Word-Level Alignment**<br/><sub>✓ Outputs per-scene word timestamp JSON (start_ms, end_ms) accurate within +-40ms to drive visual animation triggers.</sub> |
| ⬜ Todo | `AUD-04` | `P0` | `P0` | 2h | `INF-03` | **Curate royalty-free ambient documentary BGM stems & micro-SFX library with license manifest**<br/><sub>✓ At least 6 loopable BGM tracks + 15 crisp SFX stored in assets/ with documented commercial licenses in assets/licenses.json.</sub> |
| ⬜ Todo | `AUD-05` | `P0` | `P0` | 3h | `AUD-03`, `AUD-04` | **Build FFmpeg Audio Mixer (sidechain BGM ducking, timestamped SFX injection, 2-pass -14 LUFS mastering)**<br/><sub>✓ Master audio hits -14.0 +- 0.5 LUFS, <= -1.0 dBTP true peak, smooth BGM ducking, and exact frame-synced SFX hits.</sub> |

<details>
<summary>Checklist View — T05 (0/5)</summary>

- [ ] **`AUD-01`** (P0, 3h) — Deploy local GPU TTS (MeloTTS primary, Kokoro-82M alternate, Azure Neural fallback) with a locked narrator voice
- [ ] **`AUD-02`** (P0, 1.5h) — Build Pronunciation Lexicon & SSML/Pause Preprocessor for countries, currencies, and acronyms
- [ ] **`AUD-03`** (P0, 2.5h) — Integrate WhisperX / stable-ts Forced Word-Level Alignment
- [ ] **`AUD-04`** (P0, 2h) — Curate royalty-free ambient documentary BGM stems & micro-SFX library with license manifest
- [ ] **`AUD-05`** (P0, 3h) — Build FFmpeg Audio Mixer (sidechain BGM ducking, timestamped SFX injection, 2-pass -14 LUFS mastering)

</details>

## T06: 4K 60FPS GPU Rendering & Visual Template Library
*Design system, 8 core animated chart templates, atomic scene parallelism, static caching, and direct NVENC encoding.* (**0/11 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `REN-01` | `P0` | `P0` | 3h | `INF-03` | **Establish 4K 60FPS Documentary Visual Design System (palette, typography, safe margins, source footer)**<br/><sub>✓ style_guide.yaml + font/flag/Natural Earth GeoJSON asset pack verified legible at both 4K TV and 360px mobile sizes. It also publishes the single `RenderSpec` Pydantic contract (scene_id, template, data bindings, camera move, safe zones, SFX cues, duration) plus one golden fixture, so all 8 templates bind data the same way instead of embedding their own binding logic.</sub> |
| ⬜ Todo | `REN-02` | `P0` | `P0` | 4h | `INF-02`, `REN-01`, `VAL-01` | **Build the 1440p60-first render engine (atomic scene worker pool + static texture cache + NVENC pipe)**<br/><sub>✓ Streams raw 2560x1440 60fps RGB frames directly to hevc_nvenc/h264_nvenc with zero intermediate PNG bloat; benchmark >=25fps. The same pipeline renders 4K60 through REN-10's preset, so this item changes resolution, not architecture (DECISIONS.md D-12: 2.2x the pixels for a difference a mobile viewer cannot resolve, held until YPP).</sub> |
| ⬜ Todo | `REN-03` | `P0` | `P0` | 4h | `REN-02` | **Implement Template 1: BarChartRace (interpolated rankings, flags, rolling year counter, spotlight glow)**<br/><sub>✓ Renders buttery-smooth 4K60 Top-15 bar race synchronized to WhisperX word highlights.</sub> |
| ⬜ Todo | `REN-04` | `P0` | `P0` | 4.5h | `REN-02` | **Implement Template 2: WorldChoroplethMap (Natural Earth vectors, camera zoom/pan, animated color scale)**<br/><sub>✓ Renders crisp vector world map with smooth zoom onto target regions and animated country callout pins.</sub> |
| ⬜ Todo | `REN-05` | `P0` | `P0` | 3h | `REN-02` | **Implement Template 3: SpotlightCountryCard & Template 4: ChapterTitleCard**<br/><sub>✓ High-contrast KPI card with animated rolling counters, sparkline, rank badge, plus 3-second kinetic chapter transition.</sub> |
| ⬜ Todo | `REN-06` | `P0` | `P0` | 3.5h | `REN-02` | **Implement Template 5: DualSplitComparison (e.g., Nominal vs PPP or Country A vs Country B)**<br/><sub>✓ Animated split-screen comparison with synced delta callout and zero label overlap.</sub> |
| ⬜ Todo | `REN-07` | `P1` | `P1` | 4h | `REN-02` | **Implement Template 6: HistoricalLineRace & Template 7: AnimatedBubbleScatter**<br/><sub>✓ Multi-line time series with historical event pins + multi-axis animated bubble scatter with trails.</sub> |
| ⬜ Todo | `REN-08` | `P1` | `P1` | 3h | `REN-02` | **Implement Template 8: DistributionHistogram + Pre-Baked 4K60 Ambient Motion Backgrounds**<br/><sub>✓ Bell-curve percentile visualizer + 3 reusable 4K60 subtle dark-mode animated backdrop loops.</sub> |
| ⬜ Todo | `REN-09` | `P0` | `P0` | 2.5h | `AUD-05`, `REN-03`, `REN-04`, `REN-05`, `REN-06` | **Build Scene Concatenator, Master Audio-Video Muxer & YouTube 4K60 Export Preset**<br/><sub>✓ Assembles full 10-18 min 4K60 MP4 with faststart atom, 0ms AV drift, and verified playback in VLC/YouTube. Master export defaults to a 1440p60 preset at ~12-16 Mbps; the 4K60 preset is REN-10 (D-12).</sub> |
| ⬜ Todo | `SHR-01` | `P1` | `P1` | 2.5h | `REN-09` | **Build the 60s Shorts hook extractor (climax clip, burned captions, long-form link)**<br/><sub>✓ Renders a 9:16 60s cut from the episode's strongest DataBrief contrast with burned captions and uploads it as a Short carrying the long-form link in the description; long-form click-through per Short is logged in SQLite. Profit Multiplier 4 is worth $4.20-$10.50 per episode at $10.50 RPM, earned over the Short's lifetime rather than per day.</sub> |
| ⬜ Todo | `REN-10` | `P2` | `P2` | 2h | `REN-09`, `CMP-03` | **Add the 4K60 (3840x2160) preset to the render engine once the channel is monetized**<br/><sub>✓ The engine renders 3840x2160 at 60fps through the same NVENC pipe with no code path change beyond the preset, and the upgrade is applied to the top-performing episodes before new output. Gated behind YPP approval (DECISIONS.md D-12): 4K60 is 2.2x the pixels, render time and bitrate budget of 1440p60, and the repository holds no evidence that resolution moves CTR or retention for static data charts.</sub> |

<details>
<summary>Checklist View — T06 (0/11)</summary>

- [ ] **`REN-01`** (P0, 3h) — Establish 4K 60FPS Documentary Visual Design System (palette, typography, safe margins, source footer)
- [ ] **`REN-02`** (P0, 4h) — Build the 1440p60-first render engine (atomic scene worker pool + static texture cache + NVENC pipe)
- [ ] **`REN-03`** (P0, 4h) — Implement Template 1: BarChartRace (interpolated rankings, flags, rolling year counter, spotlight glow)
- [ ] **`REN-04`** (P0, 4.5h) — Implement Template 2: WorldChoroplethMap (Natural Earth vectors, camera zoom/pan, animated color scale)
- [ ] **`REN-05`** (P0, 3h) — Implement Template 3: SpotlightCountryCard & Template 4: ChapterTitleCard
- [ ] **`REN-06`** (P0, 3.5h) — Implement Template 5: DualSplitComparison (e.g., Nominal vs PPP or Country A vs Country B)
- [ ] **`REN-07`** (P1, 4h) — Implement Template 6: HistoricalLineRace & Template 7: AnimatedBubbleScatter
- [ ] **`REN-08`** (P1, 3h) — Implement Template 8: DistributionHistogram + Pre-Baked 4K60 Ambient Motion Backgrounds
- [ ] **`REN-09`** (P0, 2.5h) — Build Scene Concatenator, Master Audio-Video Muxer & YouTube 4K60 Export Preset
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
| ⬜ Todo | `PUB-01` | `P0` | `P0` | 3h | `QAG-02` | **Configure Google Cloud OAuth & YouTube Data API v3 Resumable Uploader (chapters + scheduling)**<br/><sub>✓ Uploads 4K60 master as scheduled video at optimal Tier-1 UTC slot with chapter timestamps and custom thumbnail.</sub> |
| ⬜ Todo | `PUB-02` | `P0` | `P1` | 3h | `PUB-01`, `AUD-03` | **Build Automated Metadata & SRT Subtitle Localizer (German, French, Japanese revenue set)**<br/><sub>✓ Translates title and description into de, fr and ja and uploads accurate time-coded SRTs for those three via YouTube localizations and captions APIs; ships es-419/pt-BR/hi captions only (reach, no revenue claim) and no ar. A market only receives localized metadata once captions in that language ship in the same commit - a German title over English audio is a negative-EV bounce (DECISIONS.md D-05). The language list is config (config/languages.json), not code.</sub> |
| ⬜ Todo | `PUB-03` | `P1` | `P1` | 3.5h | `REN-09`, `AUD-03` | **Build Facebook In-Stream Cut Generator (3s visual hook + burned captions) & Graph API Uploader**<br/><sub>✓ Eligibility is confirmed on the actual Page before any render code is written (DECISIONS.md D-06); once eligible, renders an FB-ready MP4 with high-contrast burned captions and uploads it on a schedule. If the program is not open to the Page, the item is closed as not-applicable and the Facebook revenue line is dropped from the model rather than assumed.</sub> |
| ⬜ Todo | `ANC-01` | `P1` | `P2` | 3.5h | `PUB-01` | **Build the ancillary revenue lane: per-episode dataset page, SVG chart exports and an embeddable feed**<br/><sub>✓ Every episode publishes a dataset page (CSV, chart SVGs, methodology note, source citation) on a static site plus an embeddable feed, and external-traffic watch-time share is logged in SQLite. Profit Multiplier 5 is the $330-$440/day ancillary line at the goal, so this lane is instrumented from the first episode instead of assumed.</sub> |
| ⬜ Todo | `PUB-04` | `P1` | `P1` | 2.5h | `PUB-01` | **Build session bridging: playlist/series slots, end-screen bridge to one named next video, pinned comment**<br/><sub>✓ Every upload lands in a pillar playlist, its end screen points at one named next episode rather than a subscribe prompt, and the pinned comment carries the chapter list plus the dataset link. Session-time and views-per-viewer from Browse/Suggested are logged in SQLite so the effect is measurable rather than assumed; session duration is the channel-level signal that decides the next upload's impressions (VIEW_OPTIMIZATION sections 5 and 6).</sub> |

<details>
<summary>Checklist View — T09 (0/5)</summary>

- [ ] **`PUB-01`** (P0, 3h) — Configure Google Cloud OAuth & YouTube Data API v3 Resumable Uploader (chapters + scheduling)
- [ ] **`PUB-02`** (P0, 3h) — Build Automated Metadata & SRT Subtitle Localizer (German, French, Japanese revenue set)
- [ ] **`PUB-03`** (P1, 3.5h) — Build Facebook In-Stream Cut Generator (3s visual hook + burned captions) & Graph API Uploader
- [ ] **`ANC-01`** (P1, 3.5h) — Build the ancillary revenue lane: per-episode dataset page, SVG chart exports and an embeddable feed
- [ ] **`PUB-04`** (P1, 2.5h) — Build session bridging: playlist/series slots, end-screen bridge to one named next video, pinned comment

</details>

## T10: Pipeline Orchestrator & Crash-Resumable DAG
*Idempotent scene-level state machine, job retries, disk cleanup, and daily batch runner.* (**0/3 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `VAL-01` | `P0` | `P0` | 6h | — | **Ship the Falsification Episode (hand-built 1080p30 thin slice) and publish it before any 4K60 render work**<br/><sub>✓ One 10-14 min episode assembled by hand from a hand-authored DataBrief (one indicator, ~40 countries), a single static-slide template at 1080p30, TTS narration with a -14 LUFS master, QC pass and 3 thumbnails, published public on the flagship channel. A 14-day read is recorded as views/video/day in SQLite. Go/no-go: >=20 views/video/day keeps the format and unblocks REN-02; below 10 kills the topic shape before any 4K60 work is spent on it.</sub> |
| ⬜ Todo | `ORC-01` | `P0` | `P0` | 3.5h | `DAT-07`, `SCR-03`, `AUD-05`, `REN-09`, `PUB-01` | **Build Resumable Episode DAG Orchestrator (SQLite state machine with scene-level checkpointing)**<br/><sub>✓ Single CLI command `python -m src.orchestrator run <episode_id>` runs end-to-end and resumes cleanly from any crash. Artifacts use one layout, data/episodes/<episode_id>/<stage>/<content_hash>.<ext>, which is what makes resume and retry-after-edit cheap: a stage is skipped when its key file already exists.</sub> |
| ⬜ Todo | `ORC-02` | `P1` | `P1` | 2h | `ORC-01`, `QAG-02`, `VAL-01` | **Configure Daily Autonomous Cron / Systemd Timer for the 1/day production cadence**<br/><sub>✓ Automatically builds next queued episode overnight IST so approval bundle arrives every morning at 08:00 IST. The cron is enabled only after the VAL-01 14-day read, so automation never multiplies an unvalidated format.</sub> |

<details>
<summary>Checklist View — T10 (0/3)</summary>

- [ ] **`VAL-01`** (P0, 6h) — Ship the Falsification Episode (hand-built 1080p30 thin slice) and publish it before any 4K60 render work
- [ ] **`ORC-01`** (P0, 3.5h) — Build Resumable Episode DAG Orchestrator (SQLite state machine with scene-level checkpointing)
- [ ] **`ORC-02`** (P1, 2h) — Configure Daily Autonomous Cron / Systemd Timer for the 1/day production cadence

</details>

## T11: Compliance, Monetization & India Payout Setup
*Anti-demonetization guardrails, Content ID license ledger, YPP/FB monetization, and India USD tax/export setup.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `CMP-01` | `P0` | `P0` | 2h | — | **Create Flagship YouTube Channel & Facebook Page (branding, banner, about, Tier-1 English positioning)**<br/><sub>✓ Channel branded as authoritative global data documentary network; verification enabled for custom thumbnails & >15 min uploads.</sub> |
| ⬜ Todo | `CMP-02` | `P0` | `P0` | 1.5h | `AUD-04`, `SCR-03` | **Implement Anti-Demonetization Policy Checklist & Citation/License Audit Manifest**<br/><sub>✓ Every episode ships with persistent source overlays, >=5 unique visual templates, analytical commentary, and verified asset licenses.</sub> |
| ⬜ Todo | `CMP-03` | `P1` | `P2` | 3h | `CMP-01`, `CMP-02` | **Apply for YouTube Partner Program (1k subs + 4k watch hrs) & Facebook In-Stream Monetization**<br/><sub>✓ Both YouTube AdSense and Facebook In-Stream approved with clean policy standing and mid-roll ads enabled.</sub> |
| ⬜ Todo | `CMP-04` | `P1` | `P2` | 2h | `CMP-03`, `CMP-05` | **Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-8BEN 15% DTAA, GST LUT prep)**<br/><sub>✓ W-8BEN approved (15% US withholding vs 24%/30%), Indian bank SWIFT USD settlement tested, e-FIRA workflow documented.</sub> |
| ⬜ Todo | `CMP-05` | `P1` | `P1` | 1.5h | `CMP-01` | **Write the docs/compliance/W8BEN_CHECKLIST.md filing artifact that CMP-04 executes**<br/><sub>✓ docs/compliance/W8BEN_CHECKLIST.md exists with the step-by-step AdSense tax-info filing for India (W-8BEN, 15% DTAA rate vs 24%/30%), GST registration plus LUT, and the e-FIRA archival workflow. Profit Multiplier 7 is $70/day of AdSense retained at the goal, so the artifact ships before the first payout cycle rather than after it.</sub> |

<details>
<summary>Checklist View — T11 (0/5)</summary>

- [ ] **`CMP-01`** (P0, 2h) — Create Flagship YouTube Channel & Facebook Page (branding, banner, about, Tier-1 English positioning)
- [ ] **`CMP-02`** (P0, 1.5h) — Implement Anti-Demonetization Policy Checklist & Citation/License Audit Manifest
- [ ] **`CMP-03`** (P1, 3h) — Apply for YouTube Partner Program (1k subs + 4k watch hrs) & Facebook In-Stream Monetization
- [ ] **`CMP-04`** (P1, 2h) — Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-8BEN 15% DTAA, GST LUT prep)
- [ ] **`CMP-05`** (P1, 1.5h) — Write the docs/compliance/W8BEN_CHECKLIST.md filing artifact that CMP-04 executes

</details>

## T12: Analytics Feedback Loop & Multi-Channel Scale
*YouTube/FB analytics ETL, retention drop-off diagnostics, RPM optimization, annual refreshes, and multi-channel cloning.* (**0/5 complete**)

| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| ⬜ Todo | `ANA-01` | `P1` | `P1` | 3h | `PUB-01` | **Build YouTube Analytics & Revenue daily ETL into SQLite (CTR, AVD, RPM, retention curves, geo)**<br/><sub>✓ Daily cron ingests video-level performance and geo RPM splits (US/UK/CA/AU share) into SQLite.</sub> |
| ⬜ Todo | `ANA-02` | `P1` | `P2` | 3h | `ANA-01`, `TOP-03` | **Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop**<br/><sub>✓ Weekly Telegram report correlates >3% retention drops to exact scene templates and updates topic scorer weights.</sub> |
| ⬜ Todo | `ANA-03` | `P2` | `P3` | 4h | `ANA-01`, `ORC-01` | **Build Automated Annual Dataset Refresh Trigger ('2027/2028 Edition' re-render pipeline)**<br/><sub>✓ Detects new World Bank / OECD annual releases and queues refreshed sequel episodes for top-earning evergreen videos.</sub> |
| ⬜ Todo | `ANA-04` | `P2` | `P3` | 5h | `ANA-02`, `CMP-03` | **Add Multi-Channel Config Isolation & Multi-Language Audio Dubbing (YouTube MLA for de/fr/ja)**<br/><sub>✓ Single GPU pipeline serves 3+ niche channels via channel_id configs and optional de/fr/ja audio tracks, priced at the PPM_REVIEW.md sec.0 revenue-set blend.</sub> |
| ⬜ Todo | `ANA-05` | `P1` | `P2` | 2.5h | `ANA-01` | **Run the first refresh wave: re-master and re-release the top 10 episodes when their datasets update**<br/><sub>✓ The ten best-performing episodes are re-rendered with refreshed source rows and re-released (same video where YouTube permits an update, new episode where the dataset changed materially), with a recorded views delta at day 28 per episode. A refresh adds views without adding library, so it is the only lever that raises views/video/day with no dilution (DECISIONS.md D-10); ANA-03 automates this trigger later, ANA-05 proves it once by hand.</sub> |

<details>
<summary>Checklist View — T12 (0/5)</summary>

- [ ] **`ANA-01`** (P1, 3h) — Build YouTube Analytics & Revenue daily ETL into SQLite (CTR, AVD, RPM, retention curves, geo)
- [ ] **`ANA-02`** (P1, 3h) — Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop
- [ ] **`ANA-03`** (P2, 4h) — Build Automated Annual Dataset Refresh Trigger ('2027/2028 Edition' re-render pipeline)
- [ ] **`ANA-04`** (P2, 5h) — Add Multi-Channel Config Isolation & Multi-Language Audio Dubbing (YouTube MLA for de/fr/ja)
- [ ] **`ANA-05`** (P1, 2.5h) — Run the first refresh wave: re-master and re-release the top 10 episodes when their datasets update

</details>
