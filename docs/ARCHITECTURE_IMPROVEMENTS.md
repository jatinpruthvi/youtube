# Architecture and AI Automation Improvements

> **Purpose:** Convert the 20 highest-impact architecture recommendations into implementation contracts for the Automated
> Data Documentary Network. This document complements `ARCHITECTURE.md`; it does not replace it.

---

## Operating rule

AI proposes candidates and explanations. Deterministic automation calculates facts, validates contracts, changes state,
enforces budgets, gates publication, preserves evidence, and records outcomes.

```text
AI proposal
  -> typed contract validation
  -> deterministic fact/source verification
  -> immutable artifact creation
  -> resumable state transition
  -> QC and human approval
  -> publish and telemetry
  -> measured feedback and reranking
```

No AI model receives authority to mutate the warehouse, publish a video, change policy thresholds, increase spend, or replace
configuration without deterministic validation and explicit approval.

---

## 1. Migration-led warehouse

### Improvement

Use versioned SQLite migrations, WAL mode, foreign-key enforcement, restore tests, retention policy, and a documented migration
path to PostgreSQL.

### AI/automation implementation

- AI generates migration intent and a human-readable rollback description.
- Automation applies migrations, runs integrity checks, validates foreign keys, creates a backup, and executes a restore smoke test.
- CI replays migrations against a fixture warehouse.
- PostgreSQL remains a future scaling option, not a first-release dependency.

---

## 2. Typed contracts at every boundary

### Improvement

Use strict Pydantic v2 contracts for `TopicBrief`, `DataBrief`, `SceneGraph`, `RenderSpec`, `AudioSpec`, `QCReport`,
`ApprovalRecord`, and `PublishReceipt`.

### AI/automation implementation

- AI generates payloads that conform to named schemas.
- Pydantic validates types, required fields, ranges, enum values, source Fact-ID bindings, and schema/prompt versions.
- Automation creates JSON Schema and golden fixtures.
- Invalid payloads create a repair request or a blocked-stage result.

---

## 3. Explicit episode state machine

### Improvement

Represent pipeline progress as durable states:

```text
QUEUED -> FACTS_READY -> SCRIPT_READY -> AUDIO_READY
       -> RENDERED -> QC_PASSED -> APPROVED -> PUBLISHED
```

Failure and pause states are first-class.

### AI/automation implementation

- Workers execute only transitions permitted by the state machine.
- AI requests stages or repairs; it cannot directly mark a state complete.
- Completion requires recorded artifact hashes and validation results.

---

## 4. Immutable, content-addressed artifacts

### Improvement

Store artifacts under:

```text
data/episodes/<episode_id>/<stage>/<content_hash>.<ext>
```

Record the schema, prompt, source snapshot, audio, render preset, QC, and approval versions.

### AI/automation implementation

- Automation hashes inputs before and after generation.
- A stage succeeds only when its declared output exists and matches its hash.
- Downstream stages rerun when an upstream hash changes.
- Editing a completed stage never overwrites its immutable predecessor.

---

## 5. Central source provenance

### Improvement

Every Fact ID carries provider, dataset/indicator, source row, ISO-3/period, unit, currency, PPP/CPI status, license,
retrieval time, snapshot time, and snapshot hash.

### AI/automation implementation

- Connectors write raw normalized observations.
- FastMCP or the repository service exposes only snapshot-backed facts.
- AI receives facts with provenance, never a free-form numeric assertion.
- The fact ledger is signed logically by the episode snapshot hash.

---

## 6. Raw observations separated from derived analysis

### Improvement

Keep source observations separate from rankings, medians, CAGR, regional averages, changes, and outliers.

### AI/automation implementation

- Connectors only write normalized observations.
- Deterministic functions derive statistics and assign Fact IDs.
- AI narrates and chooses presentation; it does not calculate the underlying figures.
- Golden tests cover rounding, units, missing periods, and base-year changes.

---

## 7. Event-driven, resumable orchestration

### Improvement

Use durable stage events rather than one monolithic episode process.

### AI/automation implementation

- SQLite or a queue stores task ID, event type, trace ID, payload hash, attempts, next retry, and result.
- Workers consume idempotent handlers.
- Transient failures use bounded exponential backoff.
- Permanent failures enter a dead-letter or blocked state with diagnostics.

---

## 8. Separate control plane and GPU worker

### Improvement

The CPU control plane owns state, data, queue, configuration, APIs, telemetry, and artifact metadata. GPU capacity is used only
for TTS, alignment, rendering, and optional model workloads.

### AI/automation implementation

- Automation provisions a worker when a GPU batch is ready.
- Artifacts and resume state remain on the control plane or approved object storage.
- Worker teardown and cost confirmation run after success or failure.
- A local/developer-machine fallback is supported.

---

## 9. Resolution-independent rendering

### Improvement

`RenderSpec` describes content and timing, never only a fixed output resolution. Resolution presets supply dimensions,
frame rate, bitrate, color, and encoder settings.

### AI/automation implementation

- The launch preset is 1440p60.
- 1080p30 is a fallback preset.
- 4K60 is a separately registered post-YPP preset.
- The renderer, templates, and fact bindings execute identically across presets.

---

## 10. Scene and asset caching

### Improvement

Cache static maps, flags, fonts, backgrounds, chapter assets, unchanged scenes, and reusable textures.

### AI/automation implementation

- Hash scene spec, audio, assets, font set, source rows, and render preset.
- Re-render only changed or downstream-dependent scenes.
- Cache the immutable scene output and verify cache hits against the full input hash.

---

## 11. Direct frame piping to the encoder

### Improvement

Avoid PNG intermediate bloat by streaming frame buffers directly to FFmpeg/NVENC.

### AI/automation implementation

- The renderer sends bounded raw frames over a pipe or queue.
- Automation measures FPS, frame count, memory, dropped frames, AV drift, and encoder outcome.
- FFmpeg writes one final launch-preset MP4 plus optional resolution variants.

---

## 12. Adapter-based providers

### Improvement

Use one interface for data sources, LLMs, TTS, ASR, analytics, storage, publishing, and notifications.

### AI/automation implementation

- Provider selection comes from validated configuration.
- Adapters implement capability, cost, timeout, retry, and artifact declarations.
- Provider changes require contract and offline replay tests.
- Fallback providers are explicit and bounded.

---

## 13. End-to-end replay harness

### Improvement

Record provider responses and generated artifacts once, then replay the complete episode pipeline offline.

### AI/automation implementation

- Cassettes include data/API responses, model payloads, TTS/ASR outputs, render specs, upload responses, and analytics fixtures.
- CI disables outbound network access.
- Replay verifies facts, hashes, state transitions, cost accounting, and output contracts.

---

## 14. Publish transaction

### Improvement

Publishing is atomic from the factory's perspective: no partial success without a complete publish receipt.

### AI/automation implementation

The approval package must contain text and audio fact reports, frozen snapshot hash, video hash, thumbnail hash, caption hash,
license/provenance report, approval identity/time, platform target, and quota status.

Automation commits a publish receipt only after successful upload and platform response verification.

---

## 15. Centralized validated configuration

### Improvement

Configuration owns channel settings, provider registry, model versions, languages, resolution presets, thresholds, budgets,
retry limits, and queue limits.

### AI/automation implementation

- Pydantic settings or JSON Schema validates startup configuration.
- AI may propose configuration content.
- CI validates compatibility and tests.
- Production promotion requires explicit approval.

---

## 16. Operational and business metric separation

### Improvement

Operational telemetry is distinct from business performance.

```text
Operational: stage time, cost, retries, GPU hours, review minutes, failures
Business:     views, CTR, AVD, subscribers, RPM, coverage, revenue
```

### AI/automation implementation

- ETL writes both metric domains to separate tables or views.
- AI diagnoses anomalies and recommends experiments.
- Thresholds and formulas remain versioned, deterministic code.
- Re-ranking never changes historical measurements.

---

## 17. Structured observability

### Improvement

Every episode, stage, provider call, artifact, and publish result emits structured diagnostics.

### AI/automation implementation

- Logs contain episode ID, stage, trace ID, provider/model version, artifact hash, cost, retry count, and outcome.
- Automation alerts on spend, fact mismatch, repeated retry, QC failure, upload failure, and stale snapshots.
- AI generates concise incident summaries from machine-recorded events.

---

## 18. Capability and cost budgets

### Improvement

Every stage declares capability, estimated cost, timeout, concurrency, retry, and storage impact.

### AI/automation implementation

- The orchestrator enforces provider, episode, daily, and monthly budgets.
- Low-priority work pauses before a ceiling is crossed.
- Resolution, provider, or concurrency changes require a budget record.
- AI cannot raise a configured ceiling.

---

## 19. Disaster recovery

### Improvement

Back up configuration, SQLite, source snapshots, artifact index, credentials metadata, and license manifests. Test complete
restoration and replay.

### AI/automation implementation

- Scheduled automation verifies backup integrity and restore drills.
- A drill rebuilds one known episode solely from frozen snapshots and artifacts.
- Recovery reports identify missing source, version, or credential data.
- A second channel is optional insurance; a rehearsed restore is the first recovery requirement.

---

## 20. Stable plugin architecture

### Improvement

Core orchestration is independent of data sources, scripts, TTS, renderers, exporters, analytics, and publishers.

### AI/automation implementation

- Plugins implement registered interfaces and declare capabilities, schemas, cost, and license.
- Automation tests plugin compatibility in an isolated environment.
- Core code owns state, provenance, retries, and artifact lifecycle.
- Channel-specific configuration cannot mutate another channel.

---

## Implementation sequencing

1. Warehouse migrations and source provenance
2. Pydantic contracts and immutable artifact layout
3. Episode state machine and resumable stage events
4. Provider adapters and offline replay fixtures
5. Script, text fact-audit, TTS, ASR, and audio mastering
6. 1440p60 render engine and direct NVENC pipeline
7. QC, approval, publishing transaction, and analytics
8. Observability and cost budgets
9. Cache, worker scaling, and plugin isolation
10. Disaster recovery and optional secondary channels

## Acceptance checks

- A clean checkout reproduces a fixture episode offline.
- Every episode can resume after a simulated crash at every state.
- No numeric script/overlay/spoken value maps outside the frozen Fact-ID ledger.
- Replacing a provider or model requires no core contract rewrite.
- Publishing requires an approval and complete publish receipt.
- Worker teardown and spend reconciliation complete after every batch.
- One episode rebuild succeeds from backup and frozen source state.
