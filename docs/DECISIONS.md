# Decision Record — What We Changed Before Writing Pipeline Code

> **Mission (unchanged):** $1,500–$2,000/day of profit from pure platform ad revenue, solo-operated, ~$100/month infrastructure budget.
> **Status: decided and applied.** Every decision below is either already reflected in `tracker/items.json`, in an acceptance criterion, or in a sibling doc named on the row. Nothing here is pending owner input.

The blueprint arrived with an unusually honest financial model — inputs labelled MEASURED vs ASSUMED, one pinned baseline, and doc invariants in `scripts/` that fail CI when a figure drifts. What it did **not** have was a set of operating decisions. Ten ambiguities each had more than one defensible answer, and each one silently changes what gets built first. They are decided
here, once, with the arithmetic that decided them.

---

## Summary of the twelve decisions

| ID | Decision | Consequence in the repo | Evidence class |
| :--- | :--- | :--- | :--- |
| **D-01** | Cadence ramps 30 → 45 → 60 → 75 videos/month; 1/day is a *proof sprint*, not the revenue path | `SPRINT_30_DAYS.md` rhythm + `docs/PROFIT_MULTIPLIERS.md` hit-rate target | derived from the sprint gate's own arithmetic |
| **D-02** | A 6-hour falsification episode (`VAL-01`) ships and is measured **before** any 4K60 render code | `VAL-01` added; `REN-02`, `ORC-02` now depend on it | 0 episodes published today |
| **D-03** | Titles become queries; the topic scorer stops paying for production convenience. **Its 6-pillar spread is superseded by D-11** | `TOP-01` reseeded, `ARCHITECTURE.md` Module 1 reweighted | measured: 21/30 format-label titles, 24 pillars, 4 near-duplicate pairs |
| **D-04** | Tracker grows 51 → 56 items; every priced lever gets an item | `VAL-01`, `DAT-09`, `SHR-01`, `ANC-01`, `CMP-05` added | two of seven multipliers had no item |
| **D-05** | Localized metadata ships only for markets that ship captions in the same commit | `PUB-02` acceptance criterion; localization uplift held as ceiling | `VIEW_OPTIMIZATION.md` §7 |
| **D-06** | Facebook In-Stream is an experiment with an eligibility gate and a kill date, not a revenue line | `PUB-03` gated on confirming eligibility first | eligibility is not under our control |
| **D-07** | The LLM layer is provider-agnostic; docs stop naming retired models | `SCR-02` builds against an adapter + `config/models.yaml` | named models age in weeks |
| **D-08** | Contracts and fixtures land before templates: `RenderSpec`, `schema_version`, artifact layout, record/replay cassettes | `REN-01`, `SCR-01`, `ORC-01`, `DAT-09` acceptance criteria | 8 templates x 7 providers otherwise diverge |
| **D-09** | Anti-demonetization is bought with topical concentration and visible provenance, not with more templates | `D-03` + `ANC-01` dataset page; TTS-vs-human voice decided on `VAL-01` data | the risk is a policy judgement, not a render quality problem |
| **D-10** | Views per video is bought with **queries, concentration and refresh rates**, never with output volume | `TOP-04`, `PUB-04`, `ANA-05` added; the video-30 gate re-scaled to trend | v is a ratio: adding 30 videos to 900 cuts it 3.3% unless demand grows |
| **D-11** | **One cluster, 30 deep** — not six pillars of five | `SPRINT_30_DAYS.md` slate rebuilt (20 salary + 10 cost-of-living); concentration from Day 1, not Day 90 | a 5-video pillar reads 32–118 at 90% confidence: unmeasurable |
| **D-12** | **1440p60 is the launch preset; 4K60 is a post-YPP upgrade.** No Facebook, no dubbing, no 4K engine before Day 45 | `REN-02` rescoped, `REN-10` added, sprint rhythm re-cut | 4K60 is 2.2x the pixels and a cost centre; zero evidence it lifts CTR for static charts on mobile |

Total plan effort moves from 142.0h to **166.5h** (0/60 items). The 22.5h increase buys one falsification episode, one test harness,
three levers that were priced but never scheduled, and the three views-per-video levers in D-10.

---

## D-01 — Cadence ramps to 75/month; 1/day is a proof sprint, not the revenue path

**Decision.** Publish 1/day for the first 30 days as a *proof* sprint (30 episodes, YPP progress, first retention baseline). Then ramp: 30/month through month 3, 45/month through month 6, 60/month through month 9, and 75/month from month 10, adding one approval/QA hire at roughly $700 of labour cost per month at the ramp point.

**Why.** `SPRINT_30_DAYS.md` already derives the gate honestly: holding $1,500/day of profit at 1/day you must sustain **155** views/video/day for a 24-month path or **103** for a 36-month path, against the plan's own assumption of **61**. Believing you will beat the plan's per-video view rate by 1.7–2.5x is not a plan; it is a hope. Cadence is the variable the operator controls, and the memo already prices it: 1,827 videos is 61 months at 30/month and 24 months at 75/month.

**Consequence.** $1,500/day of profit lands in month 26–32 rather than month 21–24, and only if the ramp holds. The first hire is the **approval and QA** role, not a renderer, because the human review gate — 4–6 hours of judgement per episode — is the throughput bottleneck once rendering is automated.

**Rejected.** Staying at 30/month and assuming the view rate doubles. That converts an engineering risk into a market risk and moves the arrival past five years.

---

## D-02 — The falsification episode ships before the 4K60 factory

**Decision.** `VAL-01` (6h, no dependencies) assembles one 10–14 minute episode **by hand**: a hand-authored `DataBrief` from one indicator across ~40 countries, a single static-slide template at 1080p30, TTS narration mastered to -14 LUFS, QC, three thumbnails, published public on the flagship channel. Fourteen days later the read is recorded as views per video per day. **≥20 keeps the format and unblocks `REN-02`; below 10 kills the topic shape** before a single line of 4K60 render code exists.

**Why.** There are zero episodes, zero uploads and zero revenue rows in this repository. The single largest track (`T06`, 31.5h) is justified entirely by assumption, and the render engine is the most expensive irreversible bet in the plan. A 1080p30 static-slide slice costs 6 hours instead of 31.5 and every asset it produces — warehouse rows, `DataBrief`, script, narration, QC, thumbnails — is reused unchanged by the real pipeline. This is the cheapest falsification available.

**Consequence.** `REN-02` (core render engine) and `ORC-02` (daily cron) now carry `VAL-01` as a dependency, so neither can start on faith. The sprint keeps building the data, script and audio layers in parallel during the 14-day observation window; only the expensive render and the automation wait.

**Rejected.** Building all eight templates, then discovering the format does not retain. That is the standard way automated channels die: 90 hours spent before the first evidence arrives.

---

## D-03 — Six pillars x five query-shaped titles, and the scorer stops paying for convenience

**Decision.** Every title is rewritten as a query a person would type, ≤60 characters, with no format label, and the topic scorer stops paying for production convenience. *(The 6-pillars-x-5 spread this decision originally carried is superseded by D-11 — the title rules below are what survived.)* The topic scorer becomes **50% proven demand + 25% auction value + 25% angle novelty**, with data verifiability demoted from a 25% weight to a **hard filter**.

**Why.** `VIEW_OPTIMIZATION.md` §1 already measured the failure: **21 of 30 titles** were the same "Every Country Ranked by …" template, spread across **24 distinct pillars**, containing **4 near-duplicate thesis pairs**. A format label is not a query, and 24 pillars for 30 videos gives the recommender ~1.25 videos of evidence per topic, which makes every 28-day reading unreadable as a measurement. Paying 25% of the score for "can I make this easily?" is the same error in the ranking layer.

**Consequence.** `TOP-01` seeds the slate; `ARCHITECTURE.md` Module 1 carries the new weights; `SPRINT_30_DAYS.md` carries the rewritten titles. Nothing in the pipeline code changes — this is a text and scoring decision.

**Rejected.** Keeping the slate as written and relying on visual diversity to dodge the repetition signal. Topical concentration is the lever the platform actually rewards.

---

## D-04 — Every priced lever gets an item (51 → 56)

**Decision.** Add five items: `VAL-01` (falsification episode), `DAT-09` (record/replay fixture harness), `SHR-01` (60s Shorts extractor), `ANC-01` (dataset page, SVG exports, syndication feed), `CMP-05` (the `W8BEN_CHECKLIST.md` artifact).

**Why.** `PROFIT_MULTIPLIERS.md` prices seven levers, and **two of them had no tracker item at all**: multiplier 4 (Shorts funnel, worth $4.20–$10.50 per episode at $10.50 RPM) and multiplier 5 (the $330–$440/day ancillary line at the goal). Multiplier 7 depends on a compliance file that no item produced. `AGENTS.md` §5 mandates offline deterministic tests while four connectors talk to seven live APIs, and no item funded the harness. A tracker that presents 51 items as the complete plan while three priced levers sit outside it is not the source of truth.

**Consequence.** 142.0h → 157.5h, 51 → 56 items, `docs/TRACKER.md` regenerated, `PPM_REVIEW.md` extended to 56 rows. The five new items are all `todo` and carry no claimed revenue of their own.

---

## D-05 — No localized metadata without captions in that market

**Decision.** `PUB-02` may only ship a localized title and description for a market that ships captions in the same commit. `de`, `fr` and `ja` keep their revenue-set status; `es-419`, `pt-BR` and `hi` remain captions-only; `ar` stays dropped. The localization uplift priced in `PPM_REVIEW.md` at +$202 / $307 / $474 per month (PPM arithmetic) is treated as a **ceiling, never as a plan input**.

**Why.** `VIEW_OPTIMIZATION.md` §7 is right: a German title over English narration delivers a German click into an English video, and the bounce feeds the satisfaction signal that decides future impressions. That is negative expected value, and the plan's own doc says so — the metadata line then contradicted it.

**Consequence.** The revenue model keeps no localization credit until captions ship, which is nearly free and nearly immediate. Adding a market stays a config edit (`config/languages.json`) plus a margin test.

**Rejected.** Shipping metadata first because it is cheaper and shows up in search. Cheap and negative is still negative.

---

## D-06 — Facebook In-Stream is an experiment with a kill date

**Decision.** `PUB-03` begins with an **eligibility check on the actual Page**. If In-Stream monetization is not open to it, the item is closed as not-applicable and the Facebook line leaves the model. Until approval exists, Facebook contributes **$0** and the base case is YouTube-only; the plan's +15% Facebook lift is upside, not baseline.

**Why.** The plan leaned roughly 15% of revenue on a program whose eligibility requirements are set by a third party and have changed more than once. Building a burned-caption render path before the gate is confirmed is spending engineering on a business-development unknown.

**Consequence.** `PUB-03`'s acceptance criterion now starts with the eligibility check. Nothing else in the plan changes, because the model was already built at 78% ad / 22% ancillary on the YouTube side.

---

## D-07 — Provider-agnostic LLM layer, current pricing

**Decision.** `SCR-02` builds against a thin adapter with a `config/models.yaml` registry (capability flags, context window, cost per 1M tokens, fallback order). Primary is whatever the current Sonnet-class model is at build time; one alternate provider is the fallback. Documentation stops naming specific retired models. Script generation is budgeted at **$0.15–$0.30 of cost per episode** rather than $0.05, which is what the fact-audit retry loop actually costs at a 2,000-word script.

**Why.** Named models age in weeks — "Claude 3.5 Sonnet / GPT-4o" was already stale on arrival, and a doc that names a retired model invites a build against one. The retry loop is the point of the fact-audit gate: `SCR-03` explicitly regenerates on failure, sometimes twice.

**Consequence.** Changing model is a config edit, not a release. The ~$100/month budget still holds: 30 episodes at $0.30 of cost each is still inside the plan's own LLM line.

---

## D-08 — Contracts and fixtures before templates

**Decision.** Four contracts land before the eight templates do: the `RenderSpec` Pydantic model plus one golden fixture (in `REN-01`), a `schema_version` and `prompt_version` on the `SceneGraph` (`SCR-01`), one artifact layout — `data/episodes/<episode_id>/<stage>/<content_hash>.<ext>` — that defines resume and retry (`ORC-01`), and a record/replay cassette layer so every connector test runs offline (`DAT-09`).

**Why.** Eight templates and seven providers will each invent their own binding logic unless one contract exists to bind against, and retrofitting a contract after 56 items is the classic rewrite. The artifact layout is also the mechanism that makes `ORC-01`'s "resume from any crash" cheap: a stage is skipped when its key file exists.

**Consequence.** No new items — this is written into four acceptance criteria, so `track.py validate` and the acceptance review keep it visible.

---

## D-09 — Anti-demonetization is concentration and provenance, not more templates

**Decision.** The mitigation for "inauthentic / mass-produced content" is (a) topical concentration from D-03, (b) a per-episode public dataset and methodology page from `ANC-01`, and (c) an explicit human-voice decision after `VAL-01`: if the 14-day read shows the synthetic narrator costs retention or satisfaction, `AUD-01` gains a hired-voice path at roughly $15–$40 of cost per episode.

**Why.** The genuine threat to this business is a policy judgement about whether the channel is a person making things or a machine extruding them — not render speed. Visible provenance (dataset, sources, methodology, a real page per episode) is the cheapest credible signal of intentionality, and it doubles as the external-traffic surface from `VIEW_OPTIMIZATION.md` §6.

**Consequence.** `ANC-01` is classified as risk mitigation as well as revenue, so it does not get dropped when the sprint runs late. The voice decision stays open exactly until evidence exists, which is the only honest place for it.

---

## What these decisions deliberately do not change

| Untouched | Why it stays |
| :--- | :--- |
| The $1,500–$2,000/day of profit target | It is the mission in every doc and it is reachable inside the window once cadence ramps (D-01) |
| The ~$100/month infrastructure budget | No decision above needs new infrastructure; D-07 and D-05 reduce spend risk |
| Zero-hallucination grounding (`F001..Fxxx`) | The one non-negotiable that protects the channel asset |
| 4K60 · -14 LUFS · de/fr/ja revenue set | Output standard is a retention and RPM decision, not a scope one |
| The doc invariants in `scripts/` | Every figure changed above was re-checked by `python3 scripts/check_docs.py` |

---

## How each decision is enforced

| Enforced by | Applies to |
| :--- | :--- |
| `tracker/items.json` dependencies (`REN-02`, `ORC-02` → `VAL-01`) | D-02 |
| Acceptance criteria on `TOP-01`, `REN-01`, `SCR-01`, `ORC-01`, `DAT-02`, `PUB-02`, `PUB-03` | D-03, D-05, D-06, D-08 |
| `docs/SPRINT_30_DAYS.md` rhythm table and slate | D-01, D-03 |
| `TOP-04`'s refusal rule in the editorial queue; the cohort-trend gate in `SPRINT_30_DAYS.md` | D-10 |
| `python3 scripts/track.py validate` and `python3 scripts/check_docs.py` | D-04 and every figure in this file |

---

## D-10 — Views per video is bought with queries, concentration and refresh rates, not with volume

**Decision.** Three additions and one rule. `TOP-04` (2h) makes a **demand verdict mandatory before production**: top-3 competitor
results, their age, and their views/day, recorded per episode, with the queue *refusing* an episode that has no query volume or
whose top results are recent. `PUB-04` (2.5h) builds **session bridging** — pillar playlists, an end screen naming one next episode
instead of asking for a subscribe, a pinned comment with chapters and the dataset link. `ANA-05` (2.5h) runs the **first refresh
wave**: the ten best episodes re-mastered and re-released when their datasets update. The rule: **after Day 90, 80% of output goes
to the two best-performing pillars**, because browse and suggested recommend inside a cluster.

**Why.** `v = views / videos` is a **ratio**, and the plan treated cadence as if it raised it. It does the opposite:

```
hold v=61 while adding 30 videos to a 900-video library
    -> total views must rise by 1,830/day every month = +3.3%/month
    -> at 30 videos, one month of publishing doubles the denominator
```

So publishing is not a v lever, it is a **v tax** unless demand grows with it. The mechanisms that do move v are ranked in
`VIEW_OPTIMIZATION.md` §17: query selection first (at zero subscribers, search is the only surface a new channel ranks on), then
topical concentration, then packaging, then satisfaction, then surfaces, then refresh waves. Three of those six were missing from
the tracker, and the two cheapest are research work rather than code.

**A second finding, fixed in the same change.** The video-30 gate applied the **library-scale** requirement (155 views/video/day
for 720 videos, i.e. 111,600 views/day) to a **30-video launch cohort**, where a realistic outcome reads 0.6–17.9. That gate would
have failed every honest launch and passed only a viral outlier. It now reads the **cohort trend** (latest five uploads' day-28
views against the previous five) as the pass/fail, and the level only as an extrapolation.

**Consequence.** 56 → 59 items, 157.5h → 164.5h. `TOP-04` costs ten minutes per episode and is the only mechanism in the plan that
prevents a no-demand video from being produced at all — which raises the measured ratio by removing the denominator.

**Rejected.** Publishing more to "give the algorithm more to work with". At this library size that lowers the metric the whole
revenue model is built on, and it spends the scarcest resource — the operator's review time — on the lowest-yield work.

---

## D-11 — One cluster, 30 deep (supersedes D-03's six-pillar spread)

**Decision.** The 30-episode sprint is **one cluster**: 20 episodes in salary and take-home pay, 10 in the adjacent
cost-of-living band. Concentration starts Day 1, not Day 90 (which is what D-10 originally said). A second pillar is only
considered after the Day-45 read, and then as a *second channel*, not as a wider slate.

**Why.** Two numbers decide it.

```
a 5-video pillar, log-normal view spread (sigma 0.9), true value 61 v/day
    -> 90% interval = 32 .. 118       (a 3.7x span)
    -> the plan's whole 61 -> 94 argument fits inside one pillar's error bar
```

Six pillars of five therefore produces **six unreadable numbers**, and it spends the only asset that compounds: cluster
authority. Browse and suggested — the surfaces that carry the volume above search — recommend *within* a cluster, so 30 episodes
on salary data is a channel the recommender can classify, while five videos on taxes is a channel it cannot.

**Consequence.** The slate is re-cut (`SPRINT_30_DAYS.md`), still 30 episodes, still 1/day, still every title a query. `TOP-01`
seeds the single-cluster queue with all 30 query candidates. `TOP-04`'s demand verdict now runs on 30 queries inside one cluster,
which makes the research cumulative instead of scattered across six unrelated subjects.

**Rejected.** Keeping six pillars "for learning". You cannot learn from a five-sample cell, and the leasing cost of that
non-learning is the cluster depth you did not build.

---

## D-12 — 1440p60 at launch; 4K60 is a post-YPP upgrade, and the deferred spend is real

**Decision.** The launch preset is **1440p60** (`3840x2160` stays the standard from the first post-YPP refresh). The 4K60 NVENC
preset becomes `REN-10`, scheduled **after** YouTube Partner Program approval (`CMP-03`). Three further deferrals sit behind the
same Day-45 gate: **no Facebook build** (`PUB-03` eligibility first, D-06), **no multi-language audio dubbing** (`ANA-04` stays in
Phase 3), and **no 4K render engine work** before the cohort trend exists.

**Why.** 4K60 is **8.29M pixels/frame against 3.69M at 1440p — 2.2x the render time, 2.2x the NVENC bitrate budget and 2.2x the
upload**, for a difference the majority of the audience cannot see: mobile viewers are the majority of watch time, and phone
displays are below 1080p. For *static and semi-animated data charts* the visible gain of 4K over 1440p is close to nil, while the
cost — 31.5h of T06 plus GPU hours — is the largest single block in the plan. There is no evidence in this repository that
resolution affects CTR or retention; the claim that "4K clarity" earns views is an assumption, and it is an expensive one.

**Consequence.** `REN-02` is rescoped to a 1440p60-first engine (the pipeline, the templates and the NVENC pipe are identical;
only the preset changes), `REN-10` (2h) holds the 4K60 preset behind YPP, and the sprint rhythm gains a **Days 34–45 gate** in
which nothing new is built. Roughly 30h of the original T06 spend moves behind evidence, and the episodes ship three weeks
earlier than they otherwise would.

**Rejected.** Rendering 4K60 from episode one because the mission line says so. The mission's own economics are views x RPM; a
resolution the viewer cannot resolve is a cost, not a feature. The standard is not abandoned — it is scheduled.
