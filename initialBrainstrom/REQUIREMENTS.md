# Consolidated requirements

Distilled from the main thread. `[NN]` = turn reference.

## Product
* Output: **10-18 min**, **3840×2160**, **60 FPS**, **-14 LUFS**, English-first narration. [60]
* Localisations: metadata + SRT in **ES, PT, HI, AR** (metadata only, not separate channels). [60]
* Secondary cut: **Facebook In-Stream** long-form (10-15 min, burned captions). [60]
* Niche: global economics — salaries, cost of living, purchasing power, rankings. [60]
* Channel 1: **EconomicsByNumbers**. Mix: rankings/comparisons 40%, data documentaries 30%,
  complete guides 20%, trend analysis 10%. [60]
* Channel 2 (`TechByNumbers`) only after channel 1 passes validation gates. [60]

## Non-negotiables
* **0% hallucination**: every spoken/rendered number traces to a real dataset
  (World Bank, OECD, DBnomics, FRED, UN Data) through the MCP grounding layer. [60]
* No clients, no course sales, no affiliate, no sponsorships in phase 1. [10]
* Policy-safe only — engagement fraud was explicitly refused. [6]
* Solo operator, India-based, limited hours (developer already at ~11 h/day). [1],[5]

## Budget
| Line | Amount |
|---|---|
| Orchestration VPS (Hetzner CPX41, 8 vCPU/16GB) | ~$27/mo |
| GPU node (RunPod/Vast RTX 4090, ~2h/day) | ~$40-60/mo |
| Script LLM API | ~$15-30/mo |
| TTS (MeloTTS/Kokoro local + Azure fallback) | ~$5-10/mo |
| Music/audio (YouTube Audio Library, Pixabay) | $0 |
| **Total** | **~$90-130/mo**, ~95% net margin [60] |

## Technical
* Scripts: frontier API, 15s hook formula, contextual CPM keywords, mid-roll markers 3:15/6:45/9:30. [60]
* Visuals: dark theme `#0F1115`, cyan `#00E5FF` accents, ticking counters, progressive line draws,
  bar-chart races, Ken Burns pans. [60]
* Encode: `-movflags +faststart`, ~320 kbps AAC, 4K upscale for premium codecs. [60]
* TTS: MeloTTS / Kokoro local, Azure fallback. [60]
* Data layer: SQLite tables `videos`, `rss_items`, `ats_snapshots`, `hijack_attempts`. [60]
* ATS metrics at T+24h: CTR, first-30s retention, AVD %, Session Lift; auto-swap thumbnail if CTR < 4%. [60]

## Validation gate (day 30)
**Median 30-day views > 500**, **AVD > 45%**, **CTR > 3.5%**, **0 policy strikes**. [60]

## Revenue expectations (honest percentiles)
| Window | Library | Views/day | Net/day |
|---|---|---|---|
| M1-3 | 30-90 | 0-500 | $0 |
| M4-6 | 100-180 | 3-8k | $25-75 |
| M7-12 | 200-350 | 15-35k | $150-350 |
| M13-18 | 400-600 | 50-90k | $500-900 |
| M19-24 | 700-900 | 100-160k | $1,000-1,500 |
| M25-36 | 1,000+ | 200k+ | $2,000+ |

---

## Drift vs the committed repo — reconciled

The repo was written *from* this thread but had drifted from its final stack. Both
`docs/ARCHITECTURE.md` and `tracker/items.json` have now been rewritten to match the plan
(2026-11-20).

| Topic | Conversation (source of truth) | Repo before | Repo now |
|---|---|---|---|
| Data store | **SQLite** (`production.db`, `schema.sql`: `rss_items`, `videos`, `ats_snapshots`, `hijack_attempts`, `hijack_results`) → PostgreSQL at scale [60],[68] | DuckDB + Parquet snapshots | SQLite warehouse + `data/schema.sql`, PostgreSQL at scale |
| Grounding | **FastMCP** server over World Bank / FRED / OECD / DBnomics / UN Data [60],[68] | Direct connectors, no MCP layer | `src/data/mcp_server.py` (FastMCP), DBnomics + UN Data connectors, tracker item `DAT-08` |
| Compute | **Hetzner CPX41** control plane + **on-demand RTX 4090** (~2 h/day) ≈ $85–100/mo [60] | "Single-GPU VPS" recommended | Topology A (CPX41 + 4090) is the Day-1 plan; single box is the fallback |
| Script model | **Claude 3.5 Sonnet** ~$0.05/script, **GPT-4o** fallback, local Ollama 8B for metadata only [60] | Claude + caching only | Claude 3.5 Sonnet + caching + GPT-4o fallback + Ollama for metadata |
| TTS | **MeloTTS** (MIT) / **Kokoro** (Apache 2.0) + **Azure Neural** fallback ≈ $0.20/video [60],[68] | Kokoro / Chatterbox / F5-TTS | MeloTTS primary, Kokoro alternate, Azure fallback |
| Render | Manim Community v0.18+ + FFmpeg, 4K60, `+faststart`, BT.709, -14 LUFS [60],[68] | Manim + direct NVENC pipe | unchanged — NVENC *is* the FFmpeg encoder; kept as the implementation detail |
| Approval | Telegram used for launch notifications; the pipeline is automatic [60] | Telegram 3-minute approval gate | kept as an addition (it does not contradict the plan; it is the anti-demonetisation human check) |
| Alignment | not specified in the thread | WhisperX word timestamps | kept as an addition (drives word-synced animation) |
| Tracker | 30-day hour-level sprint [60],[68] | 50 items / 12 tracks | 51 items (added `DAT-08` FastMCP server) / 12 tracks, `docs/TRACKER.md` regenerated |

Remaining open question: none of the technical drifts are unresolved. The only judgement calls
recorded above are the three "addition" rows, where the repo is stricter than the thread rather
than different from it.
