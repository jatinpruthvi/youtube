---
name: claude-script-fact-auditor
description: Build prompt-cached Claude API documentary script generators, Pydantic SceneGraph schemas with retention & visual-entropy rules, and automated zero-hallucination numeric fact auditors. Use whenever implementing Track T04 (SCR-01..SCR-04).
---

# Claude Script Engine & Zero-Hallucination Fact Auditor Skill

Use this skill when building or tuning `src/script/` prompts, Pydantic schemas, retention linters, or automated fact-audit loops.

## Architecture Rules
1. **Prompt Caching Always On:** Place the static Documentary Style Guide, Visual Template Catalog, and JSON Schema inside cache-marked system blocks (`cache_control: {"type": "ephemeral"}`) to cut Claude input token spend by ~70% (~$0.15–$0.35/episode).
2. **Strict Data-Only Injection:** Claude receives `DataBrief.json` containing verified facts (`F001..Fxxx`). System instructions explicitly forbid inventing or recalling statistics not present in the brief.
3. **Structured `SceneGraph` Output:** Every episode generates a Pydantic-validated JSON document containing:
   - `episode_id`, `title`, `target_duration_sec` (600–1080s), `chapters[]`, `scenes[]`.
   - Each scene specifies: `scene_id`, `act`, `template` (enum of 8 templates), `narration_text`, `fact_refs[]`, `visual_params`, `highlight_triggers[]` (words that trigger animations), `sfx_cues[]`, `source_citation`.
4. **Retention & Anti-Repetitious Enforcements:**
   - Act 0 (`0:00–0:35`): Immediate contrast hook + open loop (zero "Welcome back to the channel" fluff).
   - Visual Entropy: **No two consecutive scenes may share the same `template`**; max scene length `<= 45s` (~115 words).
   - Causal Depth: Every act explains economic mechanisms (taxation, productivity, PPP, housing, demographics) rather than merely reading numbers aloud.
   - Climax Inversion: Re-ranks countries on a second axis in the final third for maximum retention payoff.
   - End-Screen Bridge: Final 10 seconds bridge directly into a specific related channel topic.

## Automated Fact-Audit Gate (`src/script/fact_auditor.py`)
1. Extract all numeric tokens (currency amounts, percentages, ranks `#1`..`#200`, years, multipliers) from every scene's `narration_text`.
2. Normalize spoken forms (`"eighty-two thousand dollars"` → `82000`, `"4.5%"` → `4.5`).
3. Verify each extracted claim against the values referenced in `scene.fact_refs` within acceptable editorial rounding tolerance (`±0.5%` or nearest thousand for spoken rounded numbers).
4. On mismatch: fail the gate and invoke a targeted Claude repair call with the exact offending sentence + verified `DataBrief` row (max 2 auto-repair loops before escalating to human review).

## Verification Checklist
- [ ] Pydantic schema rejects consecutive duplicate templates and scenes missing `fact_refs` or `source_citation`.
- [ ] Fact-auditor unit tests explicitly verify that a deliberately hallucinated salary/GDP number fails the gate and triggers repair.
