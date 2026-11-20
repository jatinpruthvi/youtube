# Automated Data Documentary Network

> **Mission:** Build an AI-powered, automated data documentary factory generating **$1,000–$2,000+/day ($30,000–$60,000+/month)** in pure platform ad revenue (YouTube AdSense + Facebook In-Stream) within 24–36 months — operated by a solo developer on a **~$100/month** pipeline (Hetzner CPU control plane + on-demand RTX 4090).

---

## Repository Navigation

| Document / Tool | Purpose |
| :--- | :--- |
| **[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)** | Full technical architecture blueprint: end-to-end DAG, 4K60 GPU rendering solution, zero-hallucination data grounding, ~$100/mo unit economics, anti-demonetization guardrails, and 36-month scaling model. |
| **[`docs/TRACKER.md`](docs/TRACKER.md)** | Complete **50-item Master Track List** organized across **12 architectural tracks** and **4 execution phases** with dependencies, effort estimates, and acceptance criteria. |
| **[`docs/SPRINT_30_DAYS.md`](docs/SPRINT_30_DAYS.md)** | **30 Videos in 30 Days** execution schedule + 30 high-CPM, API-verifiable documentary episode specs with stage checklists. |
| **[`tracker/items.json`](tracker/items.json)** | Machine-readable single source of truth for all 50 architecture tracker items. |
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
Claude API (Prompt Cached) ──► SceneGraph JSON ──► Automated Fact-Audit Gate (0 Hallucinations)
        │
        ▼
Local GPU TTS (MeloTTS/Kokoro, Azure fallback) + WhisperX Word Timestamps ──► FFmpeg -14 LUFS Master + Ducking/SFX
        │
        ▼
Parallel 4K 60FPS GPU Renderer (25–45 Atomic Scenes + Direct NVENC Pipe) ──► Master MP4
        │
        ▼
Automated QC + 3-Variant Playwright Thumbnails ──► Telegram 3-Min Mobile Approval Gate
        │
        ├──► YouTube Data API v3 (English 4K60 + ES/PT/HI/AR Metadata & SRT Subtitles)
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

* **Target Output Spec:** 10–18 min · 4K (`3840×2160`) · `60 FPS` · `-14 LUFS` · `100% API-verified facts`
* **Target Render Time:** ~20–35 min per 15-min episode via scene-level parallelism + direct NVENC piping
* **Monthly Operating Budget:** ~$72–$105/month (GPU compute + prompt-cached Claude API + Cloudflare R2 + free public APIs + local GPU TTS)
* **Immediate Launch Goal:** **30 videos in 30 days. One flagship channel.**

---

## Installed AI Coding Agent Stack & Skills (Model-Agnostic)

This repository is pre-configured using the open **`.agents/` + `AGENTS.md`** standard so **any AI model or coding agent** (Claude, GPT/Codex, Gemini, Grok, Kimi, Qwen, DeepSeek, Roo Code, OpenCode, Cursor, Windsurf, Copilot, Amp, Cline) can use every workflow and skill without `.claude/` vendor lock-in (see [`AGENTS.md`](AGENTS.md)):

| Framework / Repo | Installed Location | Purpose |
| :--- | :--- | :--- |
| **GSD Core (`@opengsd/gsd-core` v1.22.0)** *(successor to `get-shit-done`)* | `.agents/` (`skills/gsd-*`, `agents/`, `commands/`, `gsd-core/`) | Spec-driven phase loop (`gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-code-review`, etc.) in portable open `SKILL.md` format |
| **Multi-Model Ralph (`snarktank/ralph`)** | `scripts/ralph/` + `.agents/skills/{prd,ralph}/` | Autonomous coding loop supporting `--tool codex\|opencode\|gemini\|claude\|amp` or `--cmd "<cli>"` via `scripts/ralph/prompt.md` |
| **Roo Code (`RooCodeInc/Roo-Code`)** | `.roomodes`, `.roo/rules/`, `.roo/commands/`, `.roo/skills/`, `.rooignore` | Custom specialist modes (`pipeline-architect`, `data-etl-engineer`, `manim-4k-renderer`, `issue-fixer`, `merge-resolver`, `translate`) usable with any model provider |
| **31 Universal Agent Skills (`SKILL.md`)** | `.agents/skills/` (8 core skills also mirrored in `.roo/skills/`) | 23 GSD skills + `prd`, `ralph`, `roo-conflict-resolution`, `economic-data-etl`, `claude-script-fact-auditor`, `audio-tts-lufs-mastering`, `manim-4k60-gpu-renderer`, `youtube-fb-distribution-qa` |

