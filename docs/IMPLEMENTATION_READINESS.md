# Implementation Readiness and AI Execution Playbook

> **Purpose:** Turn the project architecture into an executable, AI-friendly build sequence. This document resolves the
> remaining implementation-readiness risks identified after the architecture, tracker, view/profit, and cost reviews.
>
> **Scope:** This is an execution contract for the first deterministic factory, not another business forecast. The mission
> remains **$1,500-$2,000/day of profit**; views, effective RPM, platform eligibility, and operator capacity must be measured
> rather than assumed.

This document is the operating handoff for an AI coding agent. An agent should read it together with
[`AGENTS.md`](../AGENTS.md), [`ARCHITECTURE.md`](ARCHITECTURE.md), [`ARCHITECTURE_IMPROVEMENTS.md`](ARCHITECTURE_IMPROVEMENTS.md),
[`COST_OPTIMIZATION.md`](COST_OPTIMIZATION.md), [`DECISIONS.md`](DECISIONS.md), and [`tracker/items.json`](../tracker/items.json).

## 1. The highest-priority correction

`VAL-01` is currently displayed as unblocked, but it requires nearly every factory subsystem. This is a tracker defect, not
an implementation shortcut. An agent following `python3 scripts/track.py next` could attempt to produce the first episode
before the warehouse, contracts, audio, renderer, QC, and publishing path exist.

The correct execution dependency is:

```text
INF-01 -> INF-02 -> INF-03
                         ├-> DAT-01 -> DAT-02/DAT-03/DAT-04 -> DAT-06
                         │                                      ├-> DAT-07
                         │                                      └-> DAT-08
                         ├-> TOP-01 -> TOP-02 -> TOP-03
                         ├-> SCR-01 -> SCR-02 -> SCR-03
                         ├-> AUD-01 -> AUD-02/AUD-03 -> AUD-05
                         ├-> REN-01 -> REN-02 -> REN-03/REN-04/REN-05/REN-06 -> REN-09
                         ├-> THM-01 -> THM-02
                         ├-> QAG-01 -> QAG-02
                         ├-> PUB-01 -> PUB-02 -> PUB-03
                         └-> ORC-01 -> ORC-02

DAT-07 + SCR-03 + AUD-05 + REN-09 + THM-02 + QAG-02 + PUB-03 + ORC-02 -> VAL-01
```

The exact tracker IDs are authoritative. The diagram communicates the intended shape; it does not replace the dependency
graph. `VAL-01` must remain a terminal integration item, not a parallel task.

## 2. Definition of implementation-ready

The project is implementation-ready when all of the following are true:

1. A clean checkout can install the Python project from its manifest without undocumented local steps.
2. A fixture warehouse can be created from migrations and restored from a backup.
3. Every pipeline boundary has a strict Pydantic contract and a versioned JSON fixture.
4. Every numeric claim has a Fact ID that resolves to a frozen source snapshot.
5. Every stage produces an immutable, content-addressed artifact and a durable result record.
6. A failed stage can be retried, resumed, quarantined, or repaired without corrupting completed work.
7. The first episode can run offline against fixtures and can be replayed to the same artifact hashes.
8. Live providers are adapters around the same interfaces used by the offline replay.
9. QA can block publication for factual, audio, visual, policy, rights, or budget failures.
10. The operator can see cost, time, retries, review effort, and the reason for every blocked episode.

If any item is false, the work is still foundation work. Do not compensate by adding more templates, channels, languages, or
publishing cadence.

## 3. AI implementation contract

### 3.1 What an AI agent may do

An AI coding or pipeline agent may:

- propose module boundaries, schemas, migrations, tests, prompts, repairs, and provider adapters;
- generate candidate topics, titles, hooks, scripts, SceneGraphs, metadata, localization, and diagnostics;
- create code, fixtures, documentation, and deterministic test cases;
- request a retry or a bounded repair when a validator returns a repairable error;
- recommend a lower-cost provider or render preset when a policy allows it.

### 3.2 What an AI agent may not do

An AI agent may not:

- invent, alter, or silently round a number outside the declared Fact-ID rules;
- write directly to production warehouse rows without a connector or migration contract;
- mark a stage complete without its artifact, hash, validator result, and provenance record;
- bypass a failed fact, audio, visual, rights, policy, QC, or budget gate;
- publish, increase a spend cap, change a policy threshold, or replace a provider without explicit deterministic approval;
- delete an immutable artifact or overwrite a prior successful run;
- treat a successful API response as proof that the resulting content is correct.

### 3.3 Required agent response shape

Every implementation task should require the agent to report:

```text
Scope:
  Files and contracts changed.
Inputs:
  Fixtures, schemas, configuration, and provider assumptions.
Deterministic behavior:
  State transitions, validations, hashes, retry and failure behavior.
Tests:
  Offline fixtures and commands executed.
Evidence:
  Artifact paths, result IDs, metrics, and remaining limitations.
```

An agent that cannot provide this evidence has produced a proposal, not a completed implementation.

## 4. Foundation-first build order

### Phase A — repository and runtime foundation

Build `INF-01` through `INF-03` first.

Required outputs:

- `pyproject.toml` with Python 3.11+ constraints, pinned production dependencies, and test/lint commands;
- `.env.example` containing names only, never secrets;
- configuration loading with typed settings and explicit environment validation;
- structured JSON logging with `episode_id`, `stage`, `run_id`, `trace_id`, `attempt`, and `artifact_hash`;
- a local fallback profile that does not require the cloud GPU worker;
- deterministic clock and temporary-directory helpers for tests.

The first implementation should be runnable on a developer machine. Cloud provisioning is a deployment adapter, not a
requirement for unit tests.

### Phase B — contracts, migrations, and artifacts

Before any live connector or model call, create:

- migration-managed SQLite schema with WAL and foreign keys;
- typed contracts for `TopicBrief`, `DataBrief`, `FactRecord`, `SceneGraph`, `AudioSpec`, `RenderSpec`, `QCReport`,
  `ApprovalRecord`, `PublishReceipt`, `CostEvent`, and `StageResult`;
- schema version fields and compatibility checks;
- content-addressed artifact storage;
- stage result and event tables;
- fixture builders and golden JSON files;
- backup, restore, and replay commands.

The contract package must not import provider SDKs. Providers depend on contracts; contracts do not depend on providers.

### Phase C — fact and provenance path

Implement `DAT-01`, `DAT-06`, `DAT-07`, `DAT-08`, and `DAT-09` before script generation.

The minimum vertical slice is one indicator, one country mapping path, one derived ranking, and one frozen episode snapshot.
It must demonstrate:

```text
provider fixture
  -> normalized observation
  -> frozen snapshot
  -> deterministic statistic
  -> FactRecord(F001...)
  -> DataBrief
  -> provenance lookup
```

A missing unit, source row, period, currency, PPP flag, or snapshot hash is a hard failure. Do not fill missing values with
LLM text or an unlabelled default.

### Phase D — topic, narrative, and audit path

Implement topic scoring and packaging before requesting a script. The script agent receives only a validated `DataBrief` and
the approved editorial brief.

The narrative path must be:

```text
TopicBrief
  -> approved title/hook/thumbnail concepts
  -> DataBrief with Fact IDs
  -> structured SceneGraph
  -> schema validation
  -> text/overlay fact audit
  -> bounded repair or blocked result
```

The repair loop must create a new SceneGraph and new hash. It must not patch a completed script in place.

### Phase E — audio and render path

Implement the local TTS, pronunciation lexicon, alignment, spoken-number back-check, audio mastering, and launch renderer.
The canonical launch preset is 1440p60. 1080p30 is an explicit fallback. 4K60 is a registered post-YPP preset and must not
become an accidental default.

Audio is part of factual correctness. Text fact-audit alone is insufficient: the spoken-number back-check must compare ASR
output with the scene Fact IDs before rendering.

### Phase F — QA, approval, and publishing path

QA must run before any external upload. At minimum it checks:

- fact and provenance completeness;
- spoken-number agreement;
- duration, frame rate, resolution, codec, and AV drift;
- black frames, frozen frames, clipping, loudness, true peak, and subtitle overlap;
- visual source footers, mobile legibility, and safe zones;
- asset license and Content ID manifest;
- title, thumbnail, captions, metadata, privacy state, and platform eligibility;
- budget cap and operator approval requirements.

The YouTube upload path should default to private or unlisted until the approval record is valid. A publish receipt must record
the platform ID, request payload hash, response metadata, visibility, and timestamp.

### Phase G — integration and measured operations

Only after the previous phases pass should `VAL-01` run. It must exercise the real interfaces, but it may use fixture-backed
providers when live credentials or external availability would make the run non-reproducible.

The episode run must record:

- wall-clock time per stage;
- CPU/GPU minutes and worker lifecycle;
- model, TTS, storage, transfer, and retry cost;
- operator review and repair time;
- every artifact hash and validator result;
- the final publication state;
- any manual intervention and its reason.

## 5. Artifact and state model

### 5.1 Required stage states

Use durable states, including failure states:

```text
QUEUED
FACTS_READY
SCRIPT_READY
AUDIO_READY
RENDERED
QC_PASSED
APPROVAL_PENDING
APPROVED
PUBLISHED
PAUSED
REPAIR_REQUIRED
BLOCKED
QUARANTINED
```

Only the orchestrator may transition an episode. Workers return a typed `StageResult`; they do not mutate episode state
directly.

Every successful result must include:

- `episode_id`, `run_id`, `stage`, `stage_version`;
- input artifact hashes and output artifact hashes;
- contract/schema version;
- provider and model identifiers;
- start/end timestamps and attempt number;
- validator names and pass/fail results;
- cost events and resource usage;
- a replay reference.

### 5.2 Artifact layout

Use immutable paths similar to:

```text
data/episodes/<episode_id>/
  topic/<hash>/topic_brief.json
  facts/<hash>/snapshot.json
  facts/<hash>/data_brief.json
  script/<hash>/scene_graph.json
  audio/<hash>/<scene_id>.wav
  alignment/<hash>/<scene_id>.json
  render/<preset>/<hash>/<scene_id>.mp4
  master/<hash>/episode.mp4
  qc/<hash>/report.json
  publish/<platform>/<hash>/receipt.json
```

The path is descriptive; the content hash is authoritative. A new input or configuration version creates a new artifact.

### 5.3 Retry and quarantine policy

Classify errors before retrying:

- **Transient:** network timeout, provider rate limit, temporary worker failure. Retry with bounded exponential backoff.
- **Repairable:** schema violation, unsupported phrasing, missing required field. Send targeted repair with the validator error.
- **Permanent:** missing provenance, invalid unit, failed rights check, unsupported codec, budget breach. Block immediately.
- **Suspected corruption:** hash mismatch, partial artifact, database integrity failure. Quarantine the run and require restore
  or operator inspection.

No error may return a success-shaped empty artifact.

## 6. Offline replay and validation strategy

The project requires one comprehensive validation path, not repeated ad-hoc tests.

### 6.1 Fixture layers

Maintain fixtures for:

1. provider payloads and HTTP error responses;
2. normalized warehouse rows;
3. a frozen episode snapshot;
4. a DataBrief with representative Fact IDs;
5. valid and invalid SceneGraphs;
6. TTS text and ASR number variants;
7. render and QC metadata;
8. approval and publish responses.

### 6.2 Required replay commands

The implementation should expose commands with equivalent behavior to:

```bash
python -m factory.migrate
python -m factory.validate-fixtures
python -m factory.replay --episode fixture-ep01
python -m factory.qc --episode fixture-ep01
python -m factory.costs --episode fixture-ep01
```

The exact package name may differ, but each command must be documented and callable in CI.

### 6.3 Replay acceptance criteria

A replay passes only when:

- outbound network is disabled or all providers are fixture-backed;
- the same snapshot hash and contract versions are used;
- every Fact ID resolves;
- no stage silently calls a live provider;
- all expected artifacts exist;
- the final reports are structurally valid;
- rerunning the same inputs produces the same logical output hashes;
- nondeterministic metadata such as timestamps is isolated from content hashes.

## 7. Economics, capacity, and cost controls

The factory must not claim that the mission is achieved because the pipeline rendered one episode. The operational equation is:

```text
profit/day = library videos × views/video/day × effective RPM / 1000
             - operating cost/day
```

Track each input separately:

- views per video per day;
- effective RPM after platform share and geography;
- ad coverage and limited-ads rate;
- Tier-1 audience share;
- library size and active catalogue;
- GPU, model, storage, transfer, retry, and operator costs;
- review and rework minutes.

### 7.1 Hard budget behavior

The system must:

- assign a cost estimate before expensive work;
- reserve budget before a GPU or paid model call;
- stop or downgrade when the remaining budget is insufficient;
- record actual provider and worker cost after completion;
- alert at configurable warning thresholds;
- prevent an AI agent from increasing caps;
- include failed attempts and operator time in episode cost.

### 7.2 Capacity-led cadence

Cadence is calculated from measured throughput:

```text
safe cadence = min(
  build capacity,
  render capacity,
  QA/review capacity,
  provider/platform limits,
  approved budget
)
```

Do not encode “two or three videos per day” as a promise. It is an optimization hypothesis that can be enabled only after
the telemetry shows stable quality, cost, and operator workload.

## 8. Compliance, rights, and publication safety

Before a publish receipt can be created, the episode must have:

- source and dataset license records;
- music and SFX license manifest;
- asset provenance and attribution where required;
- reused-content and repetitious-content checks;
- disclosure and metadata policy checks;
- platform visibility and account eligibility state;
- human approval record with reviewer, timestamp, and artifact hash.

The system should default to private upload for a new integration. Public release is a separate approved transition.
Localization and Facebook distribution remain downstream features until the English YouTube path is stable.

## 9. Missing tracker coverage to add or verify

The following controls must be represented by an existing tracker item or a new explicit item. Documentation alone is not
enough:

- typed contract package and schema fixture generation;
- migration and restore smoke tests;
- content-addressed artifact store;
- durable stage-event and result records;
- deterministic replay command;
- retry classification and quarantine handling;
- backup verification and recovery drill;
- secrets/configuration validation;
- provider and episode cost reservation;
- operator-review telemetry;
- rights and license ledger;
- publish-private-by-default policy;
- reproducibility report for `VAL-01`.

If a control cannot be pointed to by a tracker ID and acceptance criterion, it is not scheduled work.

## 10. AI task template for implementation

Use this prompt shape for every implementation item:

```text
Implement tracker item <ID> only.

Read:
  AGENTS.md
  docs/IMPLEMENTATION_READINESS.md
  docs/ARCHITECTURE.md
  the item's dependencies and acceptance criteria in tracker/items.json

Constraints:
  - use typed contracts and existing repository patterns;
  - keep provider calls behind adapters;
  - use offline fixtures; do not call live APIs in unit tests;
  - preserve immutable artifacts and durable state transitions;
  - never invent numeric facts or silently downgrade a validation failure;
  - do not modify unrelated files.

Before coding:
  - identify the input/output contracts;
  - list the dependency artifacts;
  - define failure, retry, and quarantine behavior.

After coding:
  - add focused fixture-backed tests;
  - run the smallest relevant validation command;
  - report files changed, commands run, artifact hashes, and known limitations;
  - do not mark the tracker item done unless every acceptance criterion is evidenced.
```

## 11. Completion gate for the first episode

`VAL-01` is complete only when all of the following evidence exists:

1. A clean environment installs and initializes the database.
2. The episode uses a frozen snapshot and valid Fact IDs.
3. The SceneGraph passes schema, pacing, text, overlay, and provenance audits.
4. TTS output passes pronunciation and spoken-number back-checks.
5. Audio meets the declared LUFS and true-peak limits.
6. The 1440p60 master passes render and AV-sync checks.
7. Thumbnails pass mobile legibility and contrast checks.
8. The episode passes rights, policy, and automated QC checks.
9. A human approval record exists before publication.
10. The private-or-public YouTube receipt is recorded.
11. A replay produces the same logical results from fixtures.
12. Cost, time, retries, operator effort, and manual interventions are recorded.

Only after this gate passes should the project optimize packaging, localization, Facebook distribution, scale, or additional
channels. This order protects the mission from building an impressive factory that cannot prove factual correctness,
repeatability, sustainable cost, or operator capacity.
