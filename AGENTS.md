# AGENTS.md — Automated Data Documentary Network

Universal, model-agnostic operating instructions for **all AI coding models and agents** (Claude, GPT/Codex, Gemini, Grok, Kimi, Qwen, DeepSeek, Roo Code, OpenCode, Cursor, Windsurf, Copilot, Amp, Cline, Ralph, GSD Core) working in this repository.

> **Multi-Model Standard:** All shared skills, GSD workflows, commands, and subagent prompts live in the vendor-neutral **`.agents/`** directory (no `.claude/` lock-in). Roo Code project settings live in **`.roo/`** and **`.roomodes`**.

---

## 1. Mission & Non-Negotiable Constraints

* **Mission:** Build an AI-powered, automated data documentary factory generating **$1,500–$2,000/day ($45k–$60k/month) of profit** from pure platform ad revenue (YouTube AdSense + Facebook In-Stream) within 24–36 months.
* **Budget Cap:** **~$100/month** — Hetzner CPX41 control plane always on plus an on-demand RTX 4090 worker for ~2 h/day (single-GPU VPS as fallback) — zero unnecessary paid SaaS, prompt-cached Claude 3.5 Sonnet script generation with GPT-4o fallback, free public economic APIs, self-hosted MeloTTS/Kokoro.
* **Fact Grounding:** **0% hallucination tolerance.** Every number spoken or rendered must trace back to a frozen snapshot row in the SQLite warehouse, fetched from World Bank, FRED, OECD, IMF, OWID, DBnomics or UN Data through the FastMCP server, and carried by a verified `DataBrief` Fact ID (`F001..Fxxx`).
* **Output Standard:** 10–18 min · **4K (`3840×2160`) 60FPS** · `-14 LUFS` · English-first + automated ES/PT/HI/AR metadata & SRTs + Facebook In-Stream cut.

---

## 2. Canonical Project Docs & Live Tracker

Always consult these before planning or writing code:

| File | Role |
| :--- | :--- |
| `docs/ARCHITECTURE.md` | Full system architecture, 10 module specs, 4K60 NVENC strategy, ~$100/mo unit economics (CPX41 + on-demand 4090) |
| `docs/TRACKER.md` | Human-readable 51-item Master Track List across 12 tracks and 4 phases |
| `docs/SPRINT_30_DAYS.md` | 30 Videos in 30 Days production schedule & 30 high-CPM episode specs |
| `tracker/items.json` | Machine-readable task database (validated acyclic DAG) |

### Tracker CLI Workflow
```bash
python3 scripts/track.py summary          # Overall progress by track & phase
python3 scripts/track.py next             # Top unblocked items whose dependencies are done
python3 scripts/track.py set <ID> done    # Update status and auto-sync docs/TRACKER.md
```
CI also runs `summary` on every push, which fails if `tracker/items.json` will not load or is missing a field the CLI reads. It is not a graph check: `track.py` has no cycle, dangling-dependency, duplicate-ID or enum validation, so run `python3 scripts/track.py next` and read the result before trusting a dependency edit.

### Doc Invariant Check (run after editing any `.md`)
```bash
python3 scripts/check_docs.py   # memo arithmetic + table render + per-day goal sweep
```
CI runs this same command on every push (`.github/workflows/doc-invariant.yml`, no install step — the checks are stdlib-only).
Fails loudly if a figure or table drifts from the mission's **$1,500–$2,000 of profit per day**: `scripts/check_memo.py` re-derives the memo's arithmetic, `scripts/check_render.py` checks every table's width, `scripts/check_goal.py` requires every per-month figure to show what it is (and requires a monthly figure under a target noun to carry its own day figure), and `scripts/selftest_goal.py` plants monthly-target violations in a temp copy of the docs and fails if the sweep stops catching them. Shared helpers live in `scripts/doccheck.py`.

---

## 3. Model-Agnostic Agent Tooling & Frameworks

### A. GSD Core (`@opengsd/gsd-core` v1.22.0 — successor to `get-shit-done`)
Installed cleanly in **`.agents/`** (`skills/gsd-*`, `agents/`, `commands/`, `gsd-core/workflows/`, `gsd-core/references/`, `gsd-core/templates/`, `gsd-core/bin/`).
* Works with **any AI model or runtime** that reads `.agents/skills/` or `AGENTS.md`:
  - Core phase loop skills: `gsd-new-project`, `gsd-onboard`, `gsd-discuss-phase`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-progress`, `gsd-quick`, `gsd-review`, `gsd-code-review`, `gsd-map-codebase`.

### B. Multi-Model Ralph Autonomous Loop (`snarktank/ralph`)
Installed in **`scripts/ralph/`** (`ralph.sh`, `prompt.md`, `prd.json.example`) + `prd` & `ralph` skills in `.agents/skills/`.
* Workflow (works with any CLI/model):
  1. Load the `prd` skill (`.agents/skills/prd/SKILL.md`) to generate `tasks/prd-<feature>.md`.
  2. Load the `ralph` skill (`.agents/skills/ralph/SKILL.md`) to generate `scripts/ralph/prd.json`.
  3. Run with any AI model CLI:
     ```bash
     ./scripts/ralph/ralph.sh --tool codex 10
     ./scripts/ralph/ralph.sh --tool opencode 10
     ./scripts/ralph/ralph.sh --tool gemini 10
     ./scripts/ralph/ralph.sh --tool claude 10
     ./scripts/ralph/ralph.sh --tool amp 10
     ./scripts/ralph/ralph.sh --cmd "your-custom-cli" 10
     ```

### C. Roo Code Configuration (`RooCodeInc/Roo-Code`)
Installed in **`.roomodes`**, **`.roo/rules/rules.md`**, **`.roo/commands/commit.md`**, **`.roo/skills/`**, and **`.rooignore`**.
* Specialist modes for Roo Code (usable with any model provider configured in Roo Code — OpenRouter, Anthropic, OpenAI, Gemini, DeepSeek, local Ollama, etc.):
  `pipeline-architect`, `data-etl-engineer`, `manim-4k-renderer`, `issue-fixer`, `merge-resolver`, `translate`.

---

## 4. Universal Agent Skills (`.agents/skills/`)

**31 open-standard `SKILL.md` skills** live in `.agents/skills/` (the 8 core project/workflow skills are also mirrored in `.roo/skills/` for Roo Code):

### Project & Workflow Core Skills (8)
| Skill | Source | When to Load |
| :--- | :--- | :--- |
| `prd` | `snarktank/ralph` | Writing detailed PRDs before building a module or phase |
| `ralph` | `snarktank/ralph` | Converting PRDs into autonomous `prd.json` user stories |
| `roo-conflict-resolution` | `RooCodeInc/Roo-Code` | Resolving git merge/rebase conflicts safely |
| `economic-data-etl` | Project-native | Track T02: World Bank/FRED/OECD/IMF/OWID/DBnomics/UN Data connectors, SQLite warehouse, FastMCP server, `DataBrief` |
| `claude-script-fact-auditor` | Project-native | Track T04: Prompt-cached LLM scripts, `SceneGraph` schema, fact-audit gate |
| `audio-tts-lufs-mastering` | Project-native | Track T05: GPU TTS, pronunciation lexicon, WhisperX alignment, `-14 LUFS` mix |
| `manim-4k60-gpu-renderer` | Project-native | Track T06: Parallel 4K60 GPU templates, static caching, direct NVENC piping |
| `youtube-fb-distribution-qa` | Project-native | Tracks T07–T09/T11: QC gate, Playwright thumbnails, YT/FB publishing & localization |

### GSD Core Spec-Driven Skills (23)
`gsd-new-project`, `gsd-onboard`, `gsd-map-codebase`, `gsd-discuss-phase`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-phase`, `gsd-quick`, `gsd-progress`, `gsd-pause-work`, `gsd-resume-work`, `gsd-review`, `gsd-code-review`, `gsd-manager`, `gsd-workspace`, `gsd-import`, `gsd-ingest-docs`, `gsd-surface`, `gsd-config`, `gsd-settings`, `gsd-update`, `gsd-help`.

---

## 5. Engineering Quality Bar

1. **Python 3.11+** with strict type hints and Pydantic v2 contracts across every pipeline boundary.
2. **Offline Deterministic Tests:** Every `src/` module ships with `pytest` tests using local fixtures (no live external network calls in unit tests).
3. **Zero Temp-PNG Bloat:** Pipe 4K60 raw RGB frames directly into FFmpeg NVENC (`hevc_nvenc` / `h264_nvenc`).
4. **Never Hardcode Secrets:** All credentials (`ANTHROPIC_API_KEY`, `FRED_API_KEY`, Google OAuth, Telegram token, R2 keys) stay in `.env` (gitignored).
5. **Update Tracker On Completion:** After tests pass, mark the corresponding item done via `python3 scripts/track.py set <ID> done`.
