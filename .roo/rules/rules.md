# Project Engineering & Coding Rules (Automated Data Documentary Network)

1. **Architecture & Tracker Alignment**
   - `docs/ARCHITECTURE.md` is the canonical system blueprint.
   - `tracker/items.json` is the source of truth for implementation items; run `python3 scripts/track.py next` to pick unblocked work and `python3 scripts/track.py set <ID> done` when acceptance criteria are verified.

2. **Zero-Hallucination Fact Grounding (Non-Negotiable)**
   - LLMs must **never** emit economic statistics from parametric memory.
   - Every number rendered or spoken must trace to a verified `DataBrief` Fact ID (`F001..Fxxx`) backed by an immutable Parquet/DuckDB snapshot from a real API (World Bank, FRED, OECD, IMF, OWID).
   - Every data visual frame must include a bottom-left source attribution overlay (`Source: <Org> (<Year>)`).

3. **4K 60FPS Performance & Budget Guardrails (~$100/mo)**
   - Never write full-length uncompressed 4K PNG frame sequences to disk; always stream `rawvideo` directly into FFmpeg hardware NVENC (`hevc_nvenc` / `h264_nvenc`).
   - Split every episode into atomic 15–35s scenes so renders are parallelizable and crash-resumable.
   - Enable Anthropic Prompt Caching on Claude API calls and default to local GPU TTS (Kokoro-82M / Chatterbox / F5-TTS) to protect the ~$100/mo operating budget.

4. **Python Code Quality & Testing**
   - Target Python 3.11+ with strict type annotations (`from __future__ import annotations`, Pydantic v2 models for all stage boundaries).
   - Every new module in `src/` must ship with `pytest` unit tests using deterministic local fixtures (no live external network calls inside unit tests).
   - Never hardcode secrets, API keys, or machine-specific absolute paths; load secrets from `.env` and resolve paths relative to repository root.
   - Run `pytest` and `ruff check` before marking any tracker item `done`.
