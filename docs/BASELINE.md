# Baseline Register — the inputs every decision rests on

> **Purpose.** `DECISION_AUDIT.md` proved the arithmetic is sound. This register fixes the *other* half: which inputs are
> measured, which are derived with a band, and which are still guesses — and what decision each one triggers. No number in this
> repository is allowed to be a naked point estimate any more.
>
> **Tier key:** **M** = measured in this repository · **D** = derived here, with a band and a formula · **U** = unmeasured, with a
> retirement instrument and a pre-registered rule.

Checked by `python3 scripts/check_baseline.py` (wired into `scripts/check_docs.py`).

---

## 1. The register

| Input | Symbol | Used as | Band | Tier | Derivation or retirement |
| :--- | :--- | :--- | :--- | :---: | :--- |
| Published episodes | — | 0 | 0 | **M** | `tracker/items.json`: 60/60 items `todo` |
| Revenue earned | — | $0 | $0 | **M** | no channel exists (`CMP-01` todo) |
| Plan effort | — | 166.5h | 166.5h | **M** | sum of `effort_hours` over 60 items |
| Docs arithmetic | — | all checks green | 7 check scripts | **M** | `check_docs.py` runs the band and decision checks on every push (the count is deliberately not written here: it drifts) |
| Views per video per day | v | 61 | 22–94 | **D** | the plan's own projection rows: 10,000/450 = 22 … 170,000/1,800 = 94; projected, not measured. Retired by `ANA-01` |
| Ad-side RPM | **RPM_ad** | $10.50 | $6.24–$12.48 | **D** | the plan's stated total-RPM band is $8–$16; at a 78% ad share the ad-side band is 0.78 × that. $10.50 sits at the **68th percentile**, so the base is *not* conservative. Retired by the AdSense report |
| Total RPM (the same word, other meaning) | RPM_total | $13.46 | $8–$16 | **D** | `RPM_ad / 0.78`. Naming fixed by this register — see §2 |
| Ad share of revenue | a | 78% | 78–100% | **D** | the plan's own Month 25–28 row: $510 of $2,295 = 22.2% ancillary. If ancillary never ships, ad revenue rises 1.28x |
| US-origin share | — | 40% | 25–55% | **U** | appears nowhere in the repo as a measured value. Retired by Analytics geography |
| Withholding rate | — | 15% under DTAA | 15–30% | **U** | statutory, conditional on `CMP-05` filing. Retired by the first payout statement |
| Facebook lift | — | 0 (base) | 0–30% | **U** | removed from the base by `D-06`. Retired by the `PUB-03` eligibility answer |
| GPU hours per month | — | 5.4–9.8h at 1440p | 5.4–29h | **D** | 30 episodes × 11–20 GPU-min (render 9–16 + TTS/alignment 2–4). See §3 |
| GPU rate | — | $0.40/h | $0.33–$0.58 | **D** | the plan's own GPU line: $20–35 for ~60h |
| Script cost per episode | — | $0.15–$0.30 | $0.15–$0.30 | **D** | `D-07`; 30 episodes = $9 of cost against the plan's $10 line |
| Word rate for hired voice | — | $0.02–$0.05 | $0.02–$0.10 | **U** | market band, no quote. Retired by one quote |
| Approval/QA hire | — | $700 of cost per month | $400–$1,000 | **U** | India part-time VA band, no offer. Retired by one offer |
| Log-normal view spread | σ | **retired** | — | — | replaced by the distribution-free bound in §4 |
| 4K60 render minutes | — | 20–35 min | 20–35 min | **U** | architecture target, no benchmark. Retired by `REN-02` |
| CTR lift from packaging | — | 0 (base) | 0–20% | **U** | `PPM_REVIEW` calls it the weakest claim. Retired by Test & Compare |

**Nothing in the revenue line is Tier M.** That is the honest state of the business, and it is why `VAL-01` exists.

---

## 2. Correction 1 — "RPM" was doing two jobs

`IMPROVEMENT_VALUE_AT_2K.md` computes `ad revenue = views × RPM / 1000` and then divides by 0.78 to reach total revenue, so its
$10.50 is an **ad-side** RPM. `ARCHITECTURE.md` Module 1 advertises **"$8–$16 RPM"** for Tier-1 finance, which reads as a **total**
RPM. Same word, two meanings, and the difference is 28%.

| Reading | Value | Consistent? |
| :--- | :--- | :--- |
| `RPM_ad` $10.50 ÷ 0.78 | $13.46 total | inside $8–$16, at the 68th percentile |
| `RPM_total` $10.50 → `RPM_ad` | $8.19 | inside $6.24–$12.48, at the 33rd percentile |

**Decision taken:** keep $10.50 as `RPM_ad` (the memo's convention, all gates and tables are built on it) and **record it as a
mid-band value, not a conservative one**. The plan's risk is symmetric here; there is no cushion to spend.

---

## 3. Correction 2 — the GPU line pays for a window the pipeline does not use

`ARCHITECTURE.md` provisions **~2h/day = 60 GPU-hours** at $20–35 of cost per month. The pipeline's own SLA implies far less:

| Preset | GPU-min per episode | 30 episodes | Cost at $0.40/h |
| :--- | :---: | :---: | :---: |
| 1440p60 (launch, `D-12`) | 11–20 | **5.4–9.8h** | $2.18–$3.91 |
| 1440p60 with 3x retries | 33–60 | 16.2–29.4h | $6.53–$11.73 |
| 4K60 (post-YPP, `REN-10`) | 22–39 | 11.0–19.5h | $4.40–$7.80 |

**Decision taken:** the GPU line is **metered per episode, not reserved as a daily window**. The provisioned $20–35 was **6–11x**
the implied 1440p need and 3–5x the 4K need, which is what made the on-demand-worker topology look expensive; billed per minute the
launch preset costs $2.18–$3.91 of GPU time per month, and even a 3x retry rate stays under $12. The ~$100/month cap therefore has real headroom — which
should be spent on *(a)* the approval/QA hire at the cadence ramp and *(b)* re-renders after the Day-45 read, not on a bigger GPU
window.

---

## 4. Correction 3 — σ is gone; detectability is now distribution-free

`D-11` argued a five-video pillar cannot be read using a log-normal spread of σ = 0.9, which was itself an assumption. It is not
needed. A Mann-Whitney comparison of 5 videos against 5 videos has an exact null distribution with no distributional assumption at
all:

| Cross-pairs out of order (of 25) | Exact two-sided p | Read at 5%? |
| :---: | :---: | :---: |
| 0 (U ≤ 0) | 0.0079 | yes |
| ≤ 2 (U ≤ 2) | 0.0317 | **yes — the boundary** |
| ≤ 3 (U ≤ 3) | 0.0556 | no |
| ≤ 5 (U ≤ 5) | 0.1508 | no |

**A five-vs-five comparison is only significant when at least 23 of 25 cross-pairs are already ordered correctly** — that is,
when one pillar beats the other almost completely. Any decision that needs to separate two pillars by 20–30% is out of reach at
five episodes each, and that conclusion no longer depends on an assumed view distribution.

---

## 5. The library the goal actually needs — `v` × `RPM_ad` grid

Replacing the single breakeven number with the grid it was hiding. Each cell is the published-video count needed for $1,500/day of
profit at a 78% ad share and $2.64/day of infrastructure cost:

| | v = 40 | v = 61 (plan) | v = 94 |
| :--- | :---: | :---: | :---: |
| **RPM_ad $7** | 4,186 | 2,745 | 1,781 |
| **RPM_ad $10.50** | 2,791 | **1,830** | 1,187 |
| **RPM_ad $14** | 2,093 | 1,372 | 891 |

The plan's **1,827** is correct at exactly one point in this grid — the plan's own (61, $10.50). The reachable cell decides the
calendar, and the corner case (40, $7) needs **2.3x** the library, which at 75 videos a month is 56 months rather than 24.

---

## 6. Pre-registered decision rules

Locked **before** any data arrives, so the reading cannot be rationalised afterwards. Each rule names the input, the threshold,
and the action — including the action that ends the project.

| # | When | Reading | Threshold | Action, fixed in advance |
| :---: | :--- | :--- | :--- | :--- |
| **R1** | Day 3 | `VAL-01` published | live within 3 days of the demand research | If not published, the constraint is production, not demand: cut scope to one template before anything else |
| **R2** | Day 17 | 14-day views on `VAL-01` | ≥ 20 v/day | keep the format, release `REN-02` and the 1/day cadence |
| **R3** | Day 17 | same | 10–20 v/day | keep the format, **hold 4K60 and Facebook**, publish 30 episodes before any further tooling |
| **R4** | Day 17 | same | < 10 v/day | **stop the 33-day sprint**, re-cut the slate with `TOP-04`, and re-run `VAL-01` once — one retry, not two |
| **R5** | Day 45 | cohort trend, latest 5 uploads vs previous 5 | flat or rising | scale: hire the approval/QA role, ramp to 45/month |
| **R6** | Day 45 | same | falling > 25% | stop publishing; the topic shape is wrong, and more episodes cannot fix it |
| **R7** | Day 45 | measured v (30 videos, 28 days) | any value | record it and **replace the 61 in every table** with the measured figure; the calendar is re-derived, not debated |
| **R8** | Day 45 | measured v | < 22 | the plan's own floor is already exceeded downward: reset the goal horizon to 5 years or change the niche, and say which |
| **R9** | YPP approval | AdSense `RPM_ad` | < $6.24 | the ad-side band is broken: cut the localization set, raise price-tier keywords, and re-price the goal before scaling cadence |
| **R10** | YPP approval | AdSense `RPM_ad` | > $12.48 | the band's top is beaten: scale cadence aggressively, and the library requirement falls by up to 40% |
| **R11** | any time | ancillary revenue share | < 5% of total after 60 episodes | `ANC-01` is not working: drop it to a monthly batch job and delete the 22% assumption from the model |
| **R12** | any time | a decision contradicts a rule | — | the rule wins until the register is edited **and** re-audited; an exception is a document change, not a conversation |

**What is *not* pre-registered, deliberately:** the *content* of the re-cut in `R4`. Demand research is the input to that
decision and inventing its answer now would be the same error as inventing a number.

---

## 7. What would make us abandon the plan

Stated once, so it is not negotiated under pressure:

1. **`VAL-01` reads under 10 views/video/day twice** (the original and the one permitted retry) — the format has no demand.
2. **The cohort trend falls at Day 45** and the top-5 pillars cannot be re-cut to fix it — the slate shape is wrong.
3. **`RPM_ad` lands under $6.24 at YPP** while v is under 61 — both terms of `V × v × RPM` miss their band at once, and no
   cadence closes a 2.3x library gap inside four years.
4. **Ancillary stays under 5%** and v is under 40 — the revenue side is then a pure advertising business at the bottom of its band.

Any one of those is a pivot signal. Two together is a stop signal.

---

## 8. Review round 3 — five findings that change what we watch

The register above bands the inputs the plan already had. This section is the domain review: what the plan never modelled at all.

### Finding 1 — the monetization gate needs *more* views than the revenue gate does

YPP requires **1,000 subscribers + 4,000 public watch hours**. Nobody has priced that, and it is the actual revenue switch.

| Gate | At 40% AVD on a 14-min video | Views needed over 30 videos | Per video |
| :--- | :--- | :---: | :---: |
| 4,000 watch hours | 5.6 min per view | 42,857 | **1,429** |
| 1,000 subs at 0.5% conversion | — | 200,000 | 6,667 |
| 1,000 subs at 1% conversion | — | 100,000 | 3,333 |
| 1,000 subs at 2% conversion | — | 50,000 | 1,667 |
| 1,000 subs at 3% conversion | — | 33,333 | 1,111 (hours bind) |

**Watch hours are easy; subscribers are the gate.** At a normal 1% conversion the subscriber requirement is 3,333 views per video,
i.e. **v ≈ 111 over 30 days — 1.8x the plan's assumed 61.** The subscriber gate and the v gate (`SPRINT_30_DAYS.md`) are the same
number, and the plan quoted neither. Subscriber *conversion* is also the most controllable variable in the whole model: end
screens, series structure and the `PUB-04` session bridge move it, whereas v is decided by demand we do not control.

### Finding 2 — the binding constraint is the operator's calendar, not the GPU

| Work | Load |
| :--- | :--- |
| Review at 2–4h per episode, 30 episodes a month | 60–120h of labour per month |
| The 33-day sprint at 1/day | 2–4h per day of review, on top of |
| 170.5h of build across 45 days | 3.8h per day |
| **Sustained total** | **5.8–7.8h per day for 45 days, no days off** |

`D-01` put the first hire at the cadence ramp (month 10). The review load starts on **Day 4**. Every other constraint in this plan
— GPU time, LLM tokens, render throughput — was modelled to the minute; the one resource that cannot be bought back is the
operator's evening, and it is the first thing to break.

### Finding 3 — the two core assumptions are anti-correlated, and nothing says so

| Assumption | What it requires |
| :--- | :--- |
| cost per episode of $1.17–$1.67 | near-zero editorial labour: templated visuals, TTS narration, automated assembly |
| `RPM_ad` $10.50 | advertiser-friendly, brand-safe, *original* finance content — the highest editorial bar on the platform |

The plan assumes **the cost base of mass production and the RPM of editorial content at the same time.** Those pull in opposite
directions, and the mechanism that connects them is measurably unfriendly: YouTube's policy on inauthentic and repetitious content
does not reduce views, it reduces *advertising* — which is precisely the term the model scales.

### Finding 4 — "limited ads" is the failure mode that looks like success

If a share of impressions carry limited or no ads, the views still arrive and the revenue does not:

| Limited-ad share of impressions | Effective `RPM_ad` | Library needed for the goal |
| :---: | :---: | :---: |
| 0% | $10.50 | 1,830 |
| 20% | $8.40 | 2,287 |
| 40% | $6.30 | **3,050** |

The 40% case lands at the **bottom edge of the register's own band** and demands 1.7x the library. This is the single most
plausible way the business misses without anyone noticing: every dashboard looks healthy except the one column nobody pulls.

### Finding 5 — one channel is the whole asset

100% of revenue comes from one channel on one AdSense account until Phase 3, which the plan dates to months 7–36. At 75 videos a
month a single policy strike removes the entire business, not one video. The register's job is to say this out loud once, and the
rule is to seed a second channel — even a small one — before the library is large enough to be worth losing.

### The two gaps this round closed in the tracker

| Gap | Why it was a gap | Item |
| :--- | :--- | :--- |
| The fact-audit covered the **text**, not the **audio** | `SCR-03` proves the script is grounded and proves nothing about what the voice says. A TTS engine reading 82,000 as "eighty-two hundred" leaves a false claim on screen with a green audit | `AUD-06` — ASR back-check of every spoken numeral against the Fact IDs |
| Nothing repackaged the **back catalogue** | Title and thumbnail editing is free and permitted at any time; Test & Compare has no API, so it needs a human in the approval bot. This is the only v lever with no production cost and no library dilution | `ANA-06` — monthly refresh on high-impression, low-CTR videos |

### Rules added (continuing R-series)

| # | When | Reading | Threshold | Action, fixed in advance |
| :---: | :--- | :--- | :--- | :--- |
| **R13** | after 15 episodes | subscribers per view | < 0.5% | the packaging or the series structure is the problem, not the cadence: fix end screens and series order before adding a single episode |
| **R14** | any 5 consecutive days | operator review hours | > 3h per day | drop to 60 videos a month; never skip `QAG-02`, and never let `AUD-06` slide to save time |
| **R15** | YPP approval + 28 days | limited-ad exposure, measured **two ways** | Studio sample > 20% **or** revenue per 1,000 views more than 25% below `playbackBasedCpm` | the mass-production/RPM combination is broken: cut cadence, raise editorial quality, and re-derive the library before scaling. **The instrument has to be honest:** the Analytics API does not return a limited-ads flag per video, so this is a 20-video Studio sample (`Monetization → limited ads`) plus the revenue-per-1,000-views vs CPM divergence, which is the only API-side proxy |
| **R16** | every episode | spoken-numeral mismatches from `AUD-06` | any | blocker. Nothing publishes; fix the pronunciation lexicon or the number formatter first |
| **R17** | monthly, from 10 videos with impressions | back-catalogue CTR after `ANA-06` repackage | < 5% relative gain in 28 days | stop the pass, it is costing an hour for nothing; revisit at 100 videos |
| **R18** | month 6 | channel-loss recovery drill | never rehearsed | run the restore: rebuild one episode end to end from the R2 archive (`INF-04`) and the frozen snapshots alone. A second channel is the expensive insurance and it competes with focus; a rehearsed restore is the cheap one, and it is the only version that survives a strike |
| **R19** | Day 1 | available hours per day | 3 / 5 / 8 | the sprint calendar is set by the profile table in `SPRINT_30_DAYS.md`; every later date derives from it. Nobody negotiates the calendar again |
| **R20** | YPP approval + 90 days | `RPM_ad` and limited-ad exposure together | `RPM_ad` ≥ $8.24 and exposure ≤ 20% | **scale**: cadence goes to 60–75/month and the hire becomes permanent. Below $6.24 **or** exposure above 30%, **switch strategy**: hold at 30/month and spend the marginal hour on editorial quality, not volume — the commodity bet and the $10.50 RPM bet cannot both be true (`D-17`) |
