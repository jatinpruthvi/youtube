# Cost Optimization — AI and Automation Plan

> **Purpose:** Define how to reduce project and operating cost without weakening the $1,500–$2,000/day profit goal,
> factual grounding, or publish quality. Cost optimization is evidence-driven: every saving names the automation, the
> metric, the acceptance limit, and the rollback condition.

**Baseline:** a $100/month infrastructure envelope, with a CPU control plane, on-demand GPU compute, provider calls,
local TTS, public source APIs, and minimal storage. Every cost assumption below is measured or tiered in
`BASELINE.md`; none is a promise of revenue.

---

## 1. Measurement model

Record every episode's unit economics in SQLite:

```text
provider_cost
+ gpu_cost
+ storage_cost
+ transfer_cost
+ model_cost
+ retry_cost
+ human_review_minutes
+ failed_stage_rework_count
+ rebuild_count
= approved_episode_cost
```

The primary dashboard is:

```text
cost per approved episode
cost per published episode
GPU seconds per approved episode
model cost per 1,000 narrative words
retry count per stage
review minutes per approved episode
cost per 1,000 views
cost per incremental view
```

AI may explain anomalies; deterministic code calculates cost and enforces ceilings.

---

## 2. Top 20 cost improvements

### 1. Meter GPU workers instead of reserving time

**AI role:** estimate expected GPU minutes from scene count, resolution, duration, and retry risk.

**Automation:**

- Provision the worker only when a GPU batch is ready.
- Queue TTS/alignment and rendering jobs together.
- Record worker start/stop timestamps and provider invoice lines.
- Destroy the worker after all jobs complete or when the idle timeout expires.
- Maintain a local-machine fallback for development.

**Metric:** GPU cost and idle minutes per approved episode.

**Acceptance:** no idle worker remains online beyond the configured timeout.

**Rollback:** retain one worker if measured batch setup cost or queue delay exceeds the metered savings.

---

### 2. Launch at 1440p60, not 4K60

**AI role:** use scene and template complexity to estimate whether 4K60 is beneficial.

**Automation:**

- Store resolution as a validated preset, not as template code.
- Encode 1440p60 for launch.
- Keep 1080p30 as the fallback.
- Run 4K60 only for a configured post-YPP experiment.

**Metric:** GPU seconds, bitrate, storage, upload time, and incremental watch-time/CTR by resolution.

**Acceptance:** 4K60 remains inactive unless the revenue or retention experiment improves measured outcomes.

**Rollback:** restore 1440p60 immediately if 4K60 exceeds cost or retries without measurable benefit.

---

### 3. Use SQLite until scale proves a database service

**AI role:** none.

**Automation:**

- Use WAL mode, migrations, foreign keys, checkpoints, and regular backups.
- Measure database size, write concurrency, lock waits, and backup duration.
- Promote to PostgreSQL only after an explicit threshold is documented and measured.

**Metric:** database latency, lock failures, and daily backup cost.

**Acceptance:** SQLite remains if all production thresholds are met.

**Rollback:** not applicable until a measured bottleneck is reproduced.

---

### 4. Keep one small control plane

**AI role:** summarize queue, cost, and incident state.

**Automation:**

- Run the queue, warehouse, API adapters, metadata, analytics, and replay fixtures on one CPU control plane.
- Attach GPU workers only for GPU stages.
- Destroy scratch volumes after the batch.

**Metric:** control-plane utilization and idle cost.

**Acceptance:** no paid managed orchestration service is required before the queue genuinely exceeds control-plane capacity.

**Rollback:** split workers or services only after capacity and reliability measurements justify it.

---

### 5. Use local TTS and alignment

**AI role:** diagnose pronunciation failures and propose lexicon corrections.

**Automation:**

- Use the locked local voice first.
- Record voice model/version, synthesis duration, runtime, and ASR mismatch.
- Invoke a paid fallback only for explicit pronunciation or synthesis failures.
- Cache synthesis by scene text, voice, lexicon version, and model version.

**Metric:** marginal narration cost and ASR mismatch rate.

**Acceptance:** local synthesis is reused when the input hash and lexicon are unchanged.

**Rollback:** paid fallback remains available for scenes that fail pronunciation quality or ASR verification.

---

### 6. Cache source observations and release data

**AI role:** identify which sources and indicators are required.

**Automation:**

- Cache normalized observations with source snapshot and fetch time.
- Refresh only when provider data is new or an episode snapshot requires a different period.
- Replay recorded provider cassettes for tests.

**Metric:** provider calls, bytes transferred, and cache hit rate.

**Acceptance:** one episode snapshot is reused across script, overlays, audit, and refresh checks.

**Rollback:** bypass cache only for an explicitly forced fresh snapshot.

---

### 7. Cache prompt prefixes

**AI role:** produce versioned prompt payloads.

**Automation:**

- Cache system instructions, JSON contracts, style guides, and Fact-ID rules.
- Include only the episode-specific DataBrief and scene requirements in the variable prefix.
- Report cache reads, misses, input/output tokens, retries, and provider cost.

**Metric:** cache hit rate, tokens, and cost per script.

**Acceptance:** stable instructions are not repeated across every script call.

**Rollback:** disable provider caching only if measured quality or cost is worse.

---

### 8. Use a provider registry and cost-aware fallback

**AI role:** evaluate factual and pacing quality.

**Automation:**

- Store provider capabilities, context limit, cost, success rate, and fallback order.
- Use the lowest-cost provider that meets quality and fact-audit gates.
- Fall back only after a bounded retry or explicit provider failure.

**Metric:** provider cost, fact-audit pass rate, repair count, and latency.

**Acceptance:** provider selection is configuration, not a source-code vendor lock.

**Rollback:** restore the known provider if measured fact-audit or quality regressions appear.

---

### 9. Bound script repair retries

**AI role:** perform a targeted repair from the deterministic mismatch report.

**Automation:**

- Allow a configured maximum of two grounded repair passes.
- After the limit, mark the episode blocked for human or fixed-template review.
- Never use an open-ended regeneration loop.

**Metric:** repair count and model cost per script.

**Acceptance:** no episode consumes unbounded model calls.

**Rollback:** increase the repair limit only with a measured quality and cost budget.

---

### 10. Render only changed scenes

**AI role:** explain which narrative or scene states changed.

**Automation:**

- Hash scene spec, audio, data bindings, assets, font set, and render preset.
- Re-render only changed scenes and downstream scenes whose inputs depend on them.
- Cache and concatenate immutable scene outputs.

**Metric:** render GPU seconds and cache hit ratio.

**Acceptance:** equivalent edits reuse unchanged scenes.

**Rollback:** full render remains available for validation or cache corruption.

---

### 11. Cache static visual assets

**AI role:** none.

**Automation:**

- Cache maps, flag atlases, fonts, backgrounds, texture loops, and chapter cards.
- Store resolution-specific variants.
- Verify asset hash and license on cache restore.

**Metric:** asset build time and GPU/CPU parsing per episode.

**Acceptance:** static assets are not re-generated or re-read per frame.

**Rollback:** regenerate assets after license or rendering drift is detected.

---

### 12. Stream directly to NVENC

**AI role:** none.

**Automation:**

- Stream raw frame buffers to FFmpeg/NVENC.
- Remove PNG intermediary scene renders.
- Clean scratch files only after QC and archive confirmation.

**Metric:** NVMe writes, scratch bytes, encode duration, and storage cost.

**Acceptance:** no temporary PNG pipeline is used for normal renders.

**Rollback:** keep an emergency frame dump for a reproducible encoder failure.

---

### 13. Preserve 1080p30 only as fallback

**AI role:** none.

**Automation:**

- Register 1080p30 as an operational compatibility preset.
- Do not use it for normal launch output unless the 1440p60 worker or encoder is unavailable.
- Test fallback rendering through an explicit command.

**Metric:** fallback use, retry count, and 1440p/1080p output cost.

**Acceptance:** fallback activation is measured and temporary.

**Rollback:** return to 1440p60 once GPU availability and QC are restored.

---

### 14. Apply scoped object-storage retention

**AI role:** summarize archive exceptions.

**Automation:**

- Archive masters, source snapshots, manifests, thumbnails, and license records.
- Delete raw scene scratch, failed outputs, and temporary frames after the retention rule.
- Keep the episode index and replay manifest independent of media cleanup.

**Metric:** storage cost and retained bytes per approved episode.

**Acceptance:** scratch data has an automatic expiry and archive data has a restore test.

**Rollback:** restore from source and rerender if an approved master is missing.

---

### 15. Enforce retry budgets

**AI role:** classify provider or model errors only if a structured error exists.

**Automation:**

- Configure maximum attempts for data, model, TTS, render, QC, and upload stages.
- Exponential backoff applies only to transient failures.
- Permanent failures enter blocked/dead-letter state.
- Record retry cost and no-retry reason.

**Metric:** retry count and retry cost per approved episode.

**Acceptance:** no stage retries indefinitely.

**Rollback:** retry limits are lowered, not raised, after a cost incident.

---

### 16. Delay Facebook implementation until eligibility

**AI role:** none.

**Automation:**

- Confirm eligibility on the actual Page.
- Block Graph/FB render code while eligibility is unknown.
- If rejected, close PUB-03 and remove Facebook revenue assumptions.
- If approved, compare upload, encoding, and incremental revenue separately.

**Metric:** engineering cost and eligible-page revenue.

**Acceptance:** no Facebook implementation spend before eligibility confirmation.

**Rollback:** disable the Facebook stage when it remains ineligible or unprofitable.

---

### 17. Ship captions before paid localization

**AI role:** generate accurate captions and translation candidates.

**Automation:**

- Upload and validate captions first.
- Compare localized engagement and effective RPM.
- Enable paid dubbing only for a measured positive result.
- Ship de/fr/ja metadata only with same-commit verified language content.

**Metric:** incremental views, watch-time cost, effective RPM, and localization cost.

**Acceptance:** population alone does not trigger paid audio or dubbing.

**Rollback:** reduce the localization set or remain captions-only.

---

### 18. Reuse winning topic and data families

**AI role:** create controlled variants from proven data and query families.

**Automation:**

- Reject duplicate thesis and over-wide topic spread.
- Prefer refreshes and country/occupation/year variants.
- Reuse approved prompt, asset, and SceneGraph structures.

**Metric:** cost to produce a variant, views, RPM, and rework.

**Acceptance:** unrelated high-cost topics require the same demand and source gate.

**Rollback:** stop variants that reduce cluster authority or raise rework.

---

### 19. Hire only after a measured bottleneck

**AI role:** summarize approval or QC bottlenecks.

**Automation:**

- Measure review minutes, approval delay, rework reason, and operator idle time.
- Identify whether rendering, data, QA, or approval is the actual limit.
- Trigger a hire proposal only after automated fixes cannot reduce the bottleneck.

**Metric:** operator cost per approved episode and bottleneck time.

**Acceptance:** no planned hire is treated as a guaranteed cost-saving.

**Rollback:** stop or change labor scope if throughput and quality do not improve.

---

### 20. Track cost from input to approved output

**AI role:** explain the top cost drivers and propose experiments.

**Automation:**

- Join provider, GPU, storage, transfer, retry, rebuild, review, and publication costs by episode.
- Store a cost snapshot before and after human approval.
- Rank cost per approved episode and cost per 1,000 measured views.

**Metric:** approved episode cost, cost per published view, rework cost, and cost ceiling.

**Acceptance:** no optimization is claimed complete without a measured before/after row.

**Rollback:** revert an optimization if it increases final approved cost or quality risk.

---

## 3. Cost telemetry schema

| Table or view | Required fields |
| :--- | :--- |
| `cost_events` | episode_id, stage, provider, operation, units, unit_cost, currency, timestamp, trace_id |
| `gpu_sessions` | worker_id, provider, start, stop, idle_minutes, GPU-type, seconds, billed_cost |
| `model_usage` | episode_id, prompt_version, model, input_tokens, cached_tokens, output_tokens, cost |
| `provider_retries` | stage, provider, attempt, transient, error_class, retry_cost |
| `storage_usage` | episode_id, bytes, retention_class, provider, archive_cost |
| `operator_time` | episode_id, review_action, minutes, operator, decision |
| `episode_costs` | episode_id, provider, GPU, storage, transfer, model, retry, operator, approved_cost |
| `cost_experiment` | episode_id, experiment, before_cost, after_cost, before_quality, after_quality |

---

## 4. AI and automation implementation loop

```text
1. Read approved cost ceiling and measured baseline
2. Estimate stage cost before execution
3. Fetch provider/model/GPU prices
4. Choose the lowest-cost validated adapter
5. Cache source, prompt, asset, and scene inputs
6. Enforce retries and worker idle timeout
7. Stream and encode without scratch PNGs
8. Run fact, audio, visual, and license checks
9. Ask for human approval
10. Publish only from the approved artifact set
11. Reconcile provider invoices and actual utilization
12. Record cost per approved episode
13. Rank the next optimization by measured net saving
```

AI proposes the optimization, explains the anomaly, or drafts a prompt/cache change. Automation calculates, caps, hashes,
enforces, invoices, and rolls back.

---

## 5. Implementation sequence

1. Add cost event and episode cost tables.
2. Add provider, model, GPU, storage, retry, and operator telemetry.
3. Add provider/model/preset configuration with hard ceilings.
4. Add bounded retry and idle-worker shutdown.
5. Add source/prompt/asset/scene caches.
6. Add direct NVENC piping and scratch cleanup.
7. Add resolution presets and 4K gate.
8. Add paid-localization and Facebook eligibility gates.
9. Add cost per approved episode and cost-per-measured-view reports.
10. Run four-week cost experiments and keep only net-positive changes.

---

## 6. Stop and rollback rules

Stop an optimization if it:

- lowers factual or ASR verification,
- reduces average percentage viewed or subscriber conversion,
- increases final approval/rework time,
- exceeds source/license obligations,
- creates unbounded retries,
- blocks publication,
- exceeds the daily or monthly budget,
- reduces measured effective RPM,
- or makes the episode unreproducible.

Roll back a cost change when the measured saving is smaller than:

```text
added rework cost
+ added quality-risk cost
+ added operator time
+ added retry cost
+ added storage/recovery cost
```
