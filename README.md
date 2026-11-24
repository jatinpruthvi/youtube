# Automated Data Documentary Network

> **Mission:** Build an AI-powered, automated data documentary factory generating **$1,500–$2,000/day ($45,000–$60,000/month) of profit** from pure platform ad revenue (YouTube AdSense + Facebook In-Stream) within 24–36 months — operated by a solo developer on a **~$100/month** pipeline (Hetzner CPU control plane + on-demand RTX 4090).

---

## Repository Navigation

| Document / Tool | Purpose |
| :--- | :--- |
| **[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)** | Full technical architecture blueprint: end-to-end DAG, resolution-independent rendering, fact-grounded data, ~$100/mo unit economics, policy guardrails, and measured scaling model. |
| **[`docs/ARCHITECTURE_IMPROVEMENTS.md`](docs/ARCHITECTURE_IMPROVEMENTS.md)** | 20 architecture improvements with AI/automation implementation rules, contracts, state, provenance, replay, publishing, observability, recovery, and plugin isolation. |
| **[`docs/IMPLEMENTATION_READINESS.md`](docs/IMPLEMENTATION_READINESS.md)** | AI execution playbook: corrected build dependencies, typed contracts, immutable artifacts, state transitions, replay, cost gates, compliance, and the `VAL-01` completion gate. |
| **[`docs/AI_AUTOMATION_PLAYBOOK.md`](docs/AI_AUTOMATION_PLAYBOOK.md)** | 20 view/profit improvements plus the AI proposal and deterministic automation boundaries for each stage. |
| **[`docs/COST_OPTIMIZATION.md`](docs/COST_OPTIMIZATION.md)** | 20 cost reductions with AI/automation controls, cost telemetry, acceptance gates, and rollback rules. |
| **[`docs/PROFIT_MULTIPLIERS.md`](docs/PROFIT_MULTIPLIERS.md)** | Deep implementation guide for the 7 profit multipliers: mid-roll ad pacing, commercial CPM keyword seeding, thumbnail contrast detection, 60s hook Shorts funnel, ancillary revenue, 2-3 videos/day throughput, and W-8BEN tax optimization. |
| **[`docs/VIEW_OPTIMIZATION.md`](docs/VIEW_OPTIMIZATION.md)** | View-optimization specification: topic selection and the stale-result test, query-shaped packaging, per-surface playbooks, localized audio, Shorts as both funnel and topic probe, back-catalogue repackaging, measurement and its noise, and every lever priced in $/day against the plan's own baseline. |
| **[`docs/DECISIONS.md`](docs/DECISIONS.md)** | **Decision record (D-01…D-18)** — operating calls covering capacity-led cadence, first launch inventory, editorial concentration, tracker completeness, captions-before-metadata, Facebook eligibility, provider-neutral LLMs, contracts and fixtures, provenance, views-per-video levers, 1440p60 launch, audio fact-audit, and monetization constraints. |
| **[`docs/BASELINE.md`](docs/BASELINE.md)** | **The baseline register** — every input tiered as measured / derived-with-band / unmeasured, the three data corrections (ad-side RPM naming, metered GPU, σ retired), the `v × RPM` library grid, the YPP and limited-ads findings, and **20 pre-registered decision rules** locked before any data arrives. Enforced by `scripts/check_baseline.py`. |
| **[`docs/DECISION_AUDIT.md`](docs/DECISION_AUDIT.md)** | **Audit of every number in the decision record** — each claim re-derived from first principles, the five defects it found and fixed, and the nine inputs that remain unmeasured. Enforced by `scripts/check_decisions.py` (155 assertions). |
| **[`docs/TRACKER.md`](docs/TRACKER.md)** | Complete **62-item Master Track List** organized across **12 architectural tracks** and **4 execution phases** with dependencies, effort estimates, and acceptance criteria. |
| **[`docs/SPRINT_30_DAYS.md`](docs/SPRINT_30_DAYS.md)** | Capacity-led launch sequence + concentrated API-verifiable episode slate with stage checklists. |
| **[`tracker/items.json`](tracker/items.json)** | Machine-readable single source of truth for all 62 architecture tracker items. |
| **[`scripts/track.py`](scripts/track.py)** | Zero-dependency Python CLI to track progress, list unblocked tasks, update statuses, and auto-sync `docs/TRACKER.md`. |

---

## Core Architecture At A Glance

```text
Free Economic APIs (World Bank / FRED / OECD / IMF / OWID)
        │
        ▼
SQLite Warehouse + FastMCP Grounding + Deterministic Stats Analyzer ──► Verified DataBrief JSON (Fact IDs)
        │
        ▼
Front-tier LLM API (Prompt Cached) ──► SceneGraph JSON ──► Automated Fact-Audit Gate (0 Hallucinations)
        │
        ▼
Local GPU TTS (MeloTTS/Kokoro, Azure fallback) + WhisperX Word Timestamps ──► FFmpeg -14 LUFS Master + Ducking/SFX
        │
        ▼
Parallel 1440p60 GPU Renderer (25–45 Atomic Scenes + Direct NVENC Pipe) ──► Master MP4
        │
        ▼
Automated QC + 3-Variant Playwright Thumbnails ──► Telegram 3-Min Mobile Approval Gate
        │
        ├──► YouTube Data API v3 (1440p60 English + de/fr/ja Metadata & SRT + es-419/pt-BR/hi Captions)
        └──► Facebook Graph API (In-Stream Cut + Burned Captions)
                │
                ▼
     YouTube/FB Analytics ETL ──► Retention & RPM Feedback Loop
```

---

## Using the Live Item Tracker CLI

```bash
# 1. View live progress across all 12 tracks and 4 phases
python3 scripts/track.py summary

# 2. See what unblocked items you should build right now
python3 scripts/track.py next

# 3. Filter items by track, phase, or status
python3 scripts/track.py list --track T06
python3 scripts/track.py list --phase P0_MVP_DAYS_1_7 --status todo

# 4. Update an item's status (automatically syncs docs/TRACKER.md)
python3 scripts/track.py set INF-01 in_progress
python3 scripts/track.py set INF-01 done
```

---

## Key Numbers & Guardrails

* **Target Output Spec:** 10–18 min · **1440p60 at launch, 4K (`3840×2160`) 60 FPS from the first post-YPP upgrade** · `-14 LUFS` · `100% API-verified facts` (`docs/DECISIONS.md` D-12)
* **Target Render Time:** measured per launch preset; scene-level 1440p60 output uses direct NVENC piping
* **Monthly Operating Budget:** ~$72–$105/month of cost (GPU compute + prompt-cached front-tier LLM API + Cloudflare R2 + free public APIs + local GPU TTS)
* **Launch Goal:** publish the first episode through the complete factory and continue a concentrated editorial queue at a capacity-safe cadence, replacing assumptions with measured output and operating telemetry.

---

## Installed AI Coding Agent Stack & Skills (Model-Agnostic)

This repository is pre-configured using the open **`.agents/` + `AGENTS.md`** standard so **any AI model or coding agent** (Claude, GPT/Codex, Gemini, Grok, Kimi, Qwen, DeepSeek, Roo Code, OpenCode, Cursor, Windsurf, Copilot, Amp, Cline) can use every workflow and skill without `.claude/` vendor lock-in (see [`AGENTS.md`](AGENTS.md)):

| Framework / Repo | Installed Location | Purpose |
| :--- | :--- | :--- |
| **GSD Core (`@opengsd/gsd-core` v1.22.0)** *(successor to `get-shit-done`)* | `.agents/` (`skills/gsd-*`, `agents/`, `commands/`, `gsd-core/`) | Spec-driven phase loop (`gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-code-review`, etc.) in portable open `SKILL.md` format |
| **Multi-Model Ralph (`snarktank/ralph`)** | `scripts/ralph/` + `.agents/skills/{prd,ralph}/` | Autonomous coding loop supporting `--tool codex\|opencode\|gemini\|claude\|amp` or `--cmd "<cli>"` via `scripts/ralph/prompt.md` |
| **Roo Code (`RooCodeInc/Roo-Code`)** | `.roomodes`, `.roo/rules/`, `.roo/commands/`, `.roo/skills/`, `.rooignore` | Custom specialist modes (`pipeline-architect`, `data-etl-engineer`, `manim-4k-renderer`, `issue-fixer`, `merge-resolver`, `translate`) usable with any model provider |
| **31 Universal Agent Skills (`SKILL.md`)** | `.agents/skills/` (8 core skills also mirrored in `.roo/skills/`) | 23 GSD skills + `prd`, `ralph`, `roo-conflict-resolution`, `economic-data-etl`, `claude-script-fact-auditor`, `audio-tts-lufs-mastering`, `manim-4k60-gpu-renderer`, `youtube-fb-distribution-qa` |

