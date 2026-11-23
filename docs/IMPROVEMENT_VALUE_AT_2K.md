# Improvement value at $1,500-$2,000/month

Mission question: *do the tracker's improvement items help reach **$1,500-$2,000 profit per month**, and by how much?*

This document re-prices the twelve revenue-moving items from `docs/PPM_REVIEW.md` against the **$1,500-$2,000/month profit target**
instead of that review's 900-video base, and then sequences the cheap ones onto the 30-in-30 spine in `docs/SPRINT_30_DAYS.md`.

> **This document prices nothing that has been built.** No item has been started or edited, `tracker/items.json` is untouched at
> 51/51 `todo`, and none of the levers below is implemented. Every dollar here is a percentage of a revenue base that does not
> exist yet.

---

## 0. Inputs: what is measured, what is assumed, and what changed from the review

The measured state is unchanged and unchanged by this document: **0 episodes published, $0 revenue, 0/51 items done.**

| Input | Value used here | Status | Source | Note |
|---|---|---|---|---|
| Profit target | $1,500 - $2,000 / month | **GIVEN** | mission statement | the target this doc prices against |
| Monthly cost | $85 | ASSUMED | `ARCHITECTURE.md` §4, Topology A low end | same $85 as `PPM_REVIEW.md` §0 |
| RPM | **$7** | ASSUMED, **below the repo's own band** | `PPM_REVIEW.md` §0 | `ARCHITECTURE.md` §6 states **$8-$16 RPM, $10 blended baseline**; $7 is deliberately below the floor of that band, so every figure here is conservative against the plan's own numbers |
| Views per video per day | **40 / 61 / 94** | ASSUMED | `PPM_REVIEW.md` §0, from the branches projection rows (61 at Month 13-16, 94 at Month 25-28) | unmeasured - nothing is published |
| Videos per month | 30 | **GIVEN** | `SPRINT_30_DAYS.md` ("30 videos in 30 days") | linear from month 1 |
| US share of revenue (for withholding) | 40% | ASSUMED | `PPM_REVIEW.md` §0 | `ARCHITECTURE.md` §3 states the 30%→15% W-8BEN effect on *US-origin views only*; the 40% share is nowhere in the repo |
| Non-EN RPM | $3.00 / $2.33 | ASSUMED | `PPM_REVIEW.md` §0 | used only by `PUB-02` and `ANA-04` |
| Non-YouTube revenue (repurposing) | $15/day | ASSUMED | branches projection table, Month 7-9 row | **not in any tracker item** - see §8 |

Cost is ~4% of the target at $85/$2,085, so the cost side stays second-order here; only the four negligible cost items move it, by
a flat **+$21/month**.

---

## 1. The base: $2,000 profit is $2,088 of revenue, 9,929 views/day, 163 videos

Shown hop by hop because every table below is a percentage of the last line:

```
profit target              = $2,000 / month
revenue needed             = $2,000 + $85 cost                          = $2,085 / month
views/day at $7 RPM        = $2,085 x 1,000 / (30 days x $7)            = 9,928.6 views/day
videos at 61 views/vid/day = 9,928.6 / 61                               = 162.8  -> 163 videos
revenue at 163 videos      = 163 x 61 x 30 / 1,000 x $7                 = $2,088.03 / month
profit at 163 videos       = $2,088.03 - $85                            = $2,003 / month
videos at 30/month         = 163 / 30                                    = 5.43 months
```

**Two numbers are in play and they differ by $3.03.** `$2,085` is the exact requirement; `$2,088` is what 163 whole videos
actually earn, because 162.8 rounds up. Every dollar figure in this document is a percentage of **$2,088**.

The same hops for the other two rates, which is why the 40-94 range decides the calendar rather than the dollars:

| views/video/day | $1,500 profit needs | $2,000 profit needs |
|---|---|---|
| 40 | 189 videos ($1,588 at 189) | 249 videos |
| **61 (likely)** | **124 videos** | **163 videos** |
| 94 | 81 videos | 106 videos |

---

## 2. The percentage levers, priced at the $2,088 base

Same seven claims as `PPM_REVIEW.md` §1, same groups, re-multiplied against $2,088 instead of $11,529. The arithmetic column is the
whole derivation - nothing is blended and nothing is hand-picked.

| Item | Group | Claim (from `PPM_REVIEW.md`) | Arithmetic at $2,088 | $/month | $/day |
|---|---|---|---|---|---|
| `THM-01` | G1 packaging | CTR 3.0%→3.6% = **+20% views** | 20% x $2,088 | **$417.61** | $13.92 |
| `PUB-03` | G4 platform | FB In-Stream **+15%** (plan floor) | 15% x $2,088 | **$313.20** | $10.44 |
| `CMP-04` | T withholding | 40% US x (30%→15%) = **6%** | 6% x $2,088 | **$125.28** | $4.18 |
| `TOP-03` | G2 topics | **+5% views** | 5% x $2,088 | **$104.40** | $3.48 |
| `ANA-04` | G5 non-EN | +15% views at $2.33/1,000 | 15% x 2.33/7 x $2,088 | **$104.25** | $3.48 |
| `SCR-04` | G3 retention | **+4% views** | 4% x $2,088 | **$83.52** | $2.78 |
| `PUB-02` | G5 non-EN | +5% views at $3.00/1,000 | 5% x 3/7 x $2,088 | **$44.74** | $1.49 |
| cost lines | C | `INF-01` $12 + `INF-04` $2 + `SCR-02` $2 + `AUD-01` $5 | flat, cost - not revenue | **$21.00** | - |

---

## 3. Group bounds and the sum - the one total that is allowed to exist

`PPM_REVIEW.md` §2: items inside a group move the same variable and cannot be added to each other; only groups are added. That rule
is applied here unchanged, and it is what makes the sum **$1,169** rather than the $1,193 a naive row-sum produces (see §7,
correction 3).

| Group | Variable it owns | Members | Low | Likely | High |
|---|---|---|---|---|---|
| **G1** | packaging / CTR | `THM-01`, `THM-02` | $41.76 (+2%) | **$417.61** | $459.37 (+22%) |
| **G2** | topic selection | `TOP-02`, `TOP-03` | $104.40 (+5%) | **$104.40** | $208.80 (+10%) |
| **G3** | retention / AVD | `SCR-04`, `ANA-02` | $83.52 (+4%) | **$83.52** | $167.04 (+8%) |
| **G4** | second platform | `PUB-03` | $313.20 (+15%) | **$313.20** | $626.41 (+30%) |
| **G5** | non-EN audience | `PUB-02`, `ANA-04` | $44.74 (+5% @ $3) | **$104.25** (`ANA-04`) | $149.00 (both) |
| **G6** | library refresh | `ANA-03` | $0 | **$0** | $0 |
| **G7** | throughput | `REN-02` | $0 | **$0** | $0 |
| **T** | withholding | `CMP-04` | $78.30 (25% US) | **$125.28** (40%) | $172.26 (55%) |
| **C** | cost lines | 4 items | $21.00 | **$21.00** | $21.00 |
| | | **Sum of group gains** | **$686.93** | **$1,169.27** | **$1,803.88** |
| | | as % of $2,088 | 32.9% | **56.0%** | 86.4% |
| | | **Resulting revenue** | $2,774.96 | **$3,257.30** | $3,891.91 |
| | | **Resulting profit** | **$2,690** | **$3,172** | **$3,807** |
| | | vs the $2,000 target | 134% | **159%** | 190% |

Three things this table says, and they are the answer to the question:

1. **Yes, the improvements help - 56% of the target, at the same library.** The target arrives with 56% headroom instead of exactly
   meeting it: 163 videos becomes 105 (see §4).
2. **Even the low case clears both targets** ($2,690 profit), because the low case still credits the withholding fix and the FB cut.
   The spread between the three cases is 2.6x and almost all of it is the G1 +20% claim, which is the weakest assumption in the
   review (`PPM_REVIEW.md` §3, "weakest remaining assumption").
3. **The high case is not a forecast.** 86.4% requires every group's members to be genuinely additive, which `PPM_REVIEW.md` §2
   says they are not. It is shown to bound the table, not to be quoted.

---

## 4. The part that matters: videos and months, not dollars

Dollars at a level not yet reached are hypothetical. Videos and calendar months are not, and this is where the improvements earn
their keep - because they are largest exactly where the plan is weakest.

Lift applied: **x1.560** (the 56.0% likely case). Videos = revenue needed x 1,000 / ($7 x 30 x views/video/day x 1.560); months =
videos / 30.

| views/video/day | $1,500 base | $1,500 with lifts | saved | $2,000 base | $2,000 with lifts | saved |
|---|---|---|---|---|---|---|
| **40** (floor) | 189 vids · 6.29 mo | 121 vids · 4.03 mo | **2.26 mo** | 249 vids · 8.27 mo | 160 vids · 5.30 mo | **2.97 mo** |
| **61** (likely) | 124 vids · 4.12 mo | 80 vids · 2.64 mo | **1.48 mo** | 163 vids · 5.43 mo | 105 vids · 3.48 mo | **1.95 mo** |
| **94** (high) | 81 vids · 2.68 mo | 52 vids · 1.72 mo | **0.96 mo** | 106 vids · 3.52 mo | 68 vids · 2.26 mo | **1.26 mo** |

In calendar months (partial months paid in full, i.e. ceiling):

| views/video/day | $1,500: month | $2,000: month |
|---|---|---|
| 40 | 7 → **5** | 9 → **6** |
| 61 | 5 → **3** | 6 → **4** |
| 94 | 3 → **2** | 4 → **3** |

**Read the "saved" column, not the "with lifts" column.** At 94 views/video/day the twelve items buy one month; at 40 they buy three.
Since views/video/day is the single unmeasured number in the whole plan (0 episodes published), the items are not a growth engine at
this scale - they are **insurance on the unmeasured variable**, and insurance is worth most in the state you are actually in, which
is the state where you know least.

---

## 5. The $/hour collapse: 128 -> 125 hours of spine, and a fifth of the money

`PPM_REVIEW.md` §4 ranked these items at its Base M ($11,529/month revenue). At the target they are worth 18.1% as much
($2,088 / $11,529) for identical effort, and the ranking is unchanged because every revenue item scales with revenue together.

| Item | Hours | $/mo at target | **$/hour at target** | $/hour at Base M (`PPM_REVIEW.md`) | Blended at target |
|---|---|---|---|---|---|
| `THM-01` | 3.0 | $417.61 | **$139/h** | $769/h | |
| `PUB-03` | 3.5 | $313.20 | **$89/h** | $494/h | |
| `CMP-04` | 2.0 | $125.28 | **$63/h** | $346/h | |
| `TOP-03` | 2.0 | $104.40 | **$52/h** | $288/h | |
| `SCR-04` | 2.0 | $83.52 | **$42/h** | $231/h | |
| `ANA-04` | 5.0 | $104.25 | **$21/h** | $115/h | |
| `PUB-02` | 3.0 | $44.74 | **$15/h** | $82/h | |

**The cheap five vs the expensive seven.** The set of five that can be scheduled inside the sprint (`THM-01`, `PUB-03`, `CMP-04`,
`TOP-03`, `PUB-02`) is **13.5h** and delivers **$1,026/month (49.1% of the target) = $76/hour blended**. The other seven priced
items (`THM-02`, `TOP-02`, `SCR-04`, `ANA-02`, `ANA-03`, `ANA-04`, `REN-02`) are **22.5h** and add only **$188 of credited value**
($8/hour) - because five of them are capped by a group leader already counted, and two are worth $0 here (§6). All twelve together
are 36.0h.

That split is the practical conclusion: **13.5 hours buys 88% of the improvement money; the remaining 22.5 hours buys 12%.**

---

## 6. Worth exactly $0 at this scale

| Item | Why $0 here | When it stops being $0 |
|---|---|---|
| `ANA-03` annual refresh | The mechanism needs a library old enough to have decayed; "refresh 100 of 900 at +60%" has no meaning when the newest video is weeks old and nothing has gone stale. The tracker already places it in `P3_SCALE_MONTHS_7_36`. | Year 2, once the first cohort is 12 months old |
| `REN-02` **throughput delta** | The *item* is mandatory - it is the render engine and `REN-03`..`REN-09` depend on it. Its *delta* (3 episodes/day instead of 2 = +30 videos/month) is $0 because the sprint already runs 1/day and the target is reached at 163 videos; `PPM_REVIEW.md` §2 states REN-02 "can legitimately be worth $0" | Past ~30 videos/month, if views/video/day holds |
| `ANA-04` dubbing | $104 for 5h ($21/h) **and** it depends on `ANA-02` and `CMP-03`, so it cannot exist before YPP and cannot be measured before retention data exists | Months 2-6, after `ANA-02` |
| `PUB-02` localizer | $44.74 for 3h ($15/h) - not literally $0, but the weakest item in the set; keep it only because it shares `PUB-01`'s pipeline | Most valuable once non-EN impressions are visible in analytics |
| group **G6** | $0 - no stale library | Year 2 |
| group **G7** | $0 - no throughput headroom needed | Past 30 videos/month |
| the other **39** items | `PPM_REVIEW.md` §5: 31 at exactly $0 (gates, risk spine, labour savers, pure mechanism), 4 negligible cost items totalling $21, 4 unpriceable (`DAT-04`, `DAT-05`, `AUD-02`, `REN-07`) | Gates and insurance, not levers |

The 39 are not worthless - `DAT-07` and `SCR-03` are what stops a strike and `CMP-01`/`CMP-03` are what makes revenue possible at
all. They are just **not improvements in the PPM sense**, and at this target the withholding and platform levers are worth more than
many of them.

---

## 7. Sequencing: the five-item set on the 125-hour spine

### 7.1 The spine, counted rather than remembered

`tracker/items.json`, counted this pass:

| Slice | Items | Hours |
|---|---|---|
| Phase 0 (`P0_MVP_DAYS_1_7`) | 33 | 93.0 |
| Phase 1 (`P1_SPRINT_DAYS_8_30`) | 13 | 32.0 |
| **Phase 0 + Phase 1 = the spine** | **46** | **125.0** |
| Phase 2 (`P2_OPT_MONTHS_2_6`) | 3 | 8.0 |
| Phase 3 (`P3_SCALE_MONTHS_7_36`) | 2 | 9.0 |
| **Total** | **51** | **142.0** |

**Correction 1: the spine is 125.0h, not 128.0h.** The 128.0h figure is what you get by adding 96.0h (the 34 `P0`-priority items) to
32.0h (the 13 Phase-1 items) - and `PUB-02` (3.0h) satisfies both descriptions, so it was counted twice. 128.0 - 3.0 = **125.0h
across 46 items**. The number moved **down by 3.0h**; the spine itself is unchanged, only its size was overstated.

### 7.2 Where each of the five slots, what it blocks, and how far it can slip

Dependencies are read from `tracker/items.json`; the windows are the ones `SPRINT_30_DAYS.md` already assigns. The point of this
table is that the *windows were already right* - what the sprint does not state is the precedence and the deferral limits, and those
are what decide which item gets sacrificed when the week overruns.

| Item | Hours | Phase / priority | Must come after | Blocks | Slot | Deferral limit |
|---|---|---|---|---|---|---|
| `THM-01` | 3.0 | P0 / P0 | `REN-01` ← `INF-03` ← `INF-02` ← `INF-01` | `QAG-02` (needs 3 thumbnails) → `PUB-01` → every upload | **Days 1-5** (already in the sprint's Factory Build window) | **None.** Slips EP01. Highest-value item in the tracker and simultaneously on the critical path - its improvement dollars are free |
| `TOP-03` | 2.0 | Phase 1 / P1 | `TOP-02` ← `TOP-01` ← `DAT-01` (7.0h total behind it) | only `ANA-02` (months 2-6) | **Days 6-7** (Batch Buffer) | Past EP01-EP05, but **not past the render of EP06** - otherwise 24 of 30 episodes are re-scoped after the slate is locked |
| `PUB-02` | 3.0 | Phase 1 / **P0** | `PUB-01` + `AUD-03` | nothing | **Days 8-20** (Daily Cadence window) | **Unbounded for production** - metadata can be back-filled to already-published videos through the API. This is the designated slip item: $15/h, no dependents |
| `PUB-03` | 3.5 | Phase 1 / P1 | `REN-09` + `AUD-03` | nothing | **Days 21-30** (FB Rollout window) | No hard block, and any published video can be re-cut later - but every day it slips is a day the +15% inventory does not exist ($10.44/day at target) |
| `CMP-04` | 2.0 | Phase 2 / P1 | `CMP-03` ← `CMP-01` + `CMP-02` | nothing | **Day 30+** (the sprint does not schedule it, correctly - it is a Phase-2 item) | **Hard external deadline: before the first AdSense payment.** Nothing in production depends on it; the money is lost at payout time if the W-8BEN is not in |

### 7.3 Deferral order when the week overruns (explicit)

1. **`PUB-02`** - nothing depends on it, and it is retrofittable to old uploads. Cost of slipping: $44.74/month, starting whenever
   non-EN traffic exists.
2. **`PUB-03`** - nothing depends on it, and any video can be cut later. Cost of slipping: $10.44/day, but only against a catalogue
   that is worth cutting, so a slip in week 3-4 is nearly free.
3. **`CMP-04`** - nothing depends on it, but it has a hard external deadline. Slips to day 30-60 without harm; **cannot** slip past
   YPP approval, because the withholding starts at the first payment.
4. **`TOP-03`** - nothing depends on it technically, but late arrival mis-scopes the remaining episodes. Slips past EP01-EP05 only.
5. **`THM-01`** - never. `QAG-02` → `PUB-01` → all 30 episodes sit behind it.

### 7.4 The overload the sprint document does not state

`SPRINT_30_DAYS.md` assigns "Complete `P0` MVP items (`INF-01` → `REN-09`, `THM-01`, `PUB-01`)" to **Days 1-5** - that is the whole
93.0h Phase-0 slice in 5 days:

```
93.0h / 5 days            = 18.6 h/day
a 12-hour solo day x 5    = 60.0h
shortfall                 = 33.0h  (about 2.75 working days)
```

So the first week cannot hold the Phase-0 work at a solo pace, and something must overflow into the Day 6-7 buffer. The correct
overflow is exactly the pair the sprint already puts there: `TOP-01`/`TOP-02`/`TOP-03` (the only priced chain that nothing else
depends on) - which is why §7.2 places `TOP-03` in Days 6-7 rather than Days 1-5. **No re-sequencing of the 125.0h spine is
warranted; the sequencing work is choosing the overflow, and it is `TOP-03`.**

### 7.5 What this section does not change

`docs/SPRINT_30_DAYS.md` keeps its windows, its 30-episode slate and its exit KPIs untouched. This document only adds the precedence
and deferral limits that the sprint window table does not express. `tracker/items.json` is untouched: no item was added, moved,
re-prioritised or started.

---

## 8. Reconciliation and corrections log

### 8.1 The $2,088 base, hop by hop

| Hop | Arithmetic | Result |
|---|---|---|
| profit target | given | $2,000 |
| + cost (`ARCHITECTURE.md` §4 low end) | $2,000 + $85 | $2,085 |
| -> views/day | 2,085,000 / (30 x 7) | 9,928.6 |
| -> videos at 61 | 9,928.6 / 61 | 162.8 |
| -> whole videos | ceiling | 163 |
| -> revenue | 163 x 61 x 30 / 1,000 x 7 | **$2,088.03** |
| -> profit | $2,088.03 - $85 | **$2,003.03** |

### 8.2 The group sums, re-added

```
41.76 + 104.40 + 83.52 + 313.20 + 104.25 + 0 + 0 + 125.28 + 21.00 = 1,169.27      (likely)
 1,169.27 / 2,088.03                                              = 0.5599 -> 56.0%
 2,088.03 + 1,169.27 = 3,257.30 revenue  ->  - $85               = 3,172.30 profit
```

### 8.3 Figures from the prior chat analysis that did not survive checking

Each is corrected above; direction of movement stated.

| # | Prior claim | What the files say | Moved |
|---|---|---|---|
| 1 | "128-hour critical path (P0 34 items, 96h + P1 13 items, 32h)" | `items.json`: Phase 0 = 33 items / 93.0h, Phase 1 = 13 items / 32.0h -> **125.0h across 46 items**. The 96.0h and 32.0h slices both contain `PUB-02` (3.0h) | **down 3.0h** |
| 2 | "the ~40-hour do-now set" | `items.json` effort: `THM-01` 3.0 + `PUB-03` 3.5 + `CMP-04` 2.0 + `TOP-03` 2.0 + `PUB-02` 3.0 = **13.5h**. 40h was a rounding of all twelve priced items, which are **36.0h** | **down 26.5h** (vs the five) or 4.0h (vs the twelve) |
| 3 | "twelve items add ~$1,155 / +55%, sum of seven rows $1,193 / 57.1%" | `PPM_REVIEW.md` §2 credits **one member per group**; `PUB-02` sits inside G5 where `ANA-04` is the leader, so summing all seven rows double-counts it. Correct likely sum: **$1,169.27 / 56.0%** | **down $23.73 / 1.1 pp** |
| 4 | "104 videos instead of 163" | follows from #3: 2,085,000 / (7 x 30 x 61 x 1.5599) = 104.4 -> **105** | **up 1 video** |
| 5 | "248 videos for $2,000 at 40 v/v/day" | 2,085,000 / (7 x 30 x 40) = 248.2 -> **249** | **up 1 video** |
| 6 | "80 videos for $1,500 at 94 v/v/day" | 1,585,000 / (7 x 30 x 94) = 80.3 -> **81** | **up 1 video** |
| 7 | "RPM $7" presented alongside `ARCHITECTURE`'s band | correct, but the band is **$8-$16 with a $10 baseline**, so $7 is 12.5% below the floor and every figure here is conservative: at $10 the same 163 videos earn **$2,983**, and $2,000 profit would need **114 videos** | unchanged, now stated |

### 8.4 Not a tracker item at all

The plan's own Month 7-9 projection row (branches table, `$15/day` repurposing + `$10/day` passive streams) is **$750/month of
non-YouTube revenue** that appears in **no tracker item**. That is 36% of the $2,085 requirement - more than `THM-01` + `PUB-03` +
`CMP-04` combined ($856). It is excluded from every total above because it has no owning item and therefore no hours to price, but it
is the largest single gap between "the tracker's improvements" and "the target".

---

## 9. What this does not claim

* **That any of these dollars exist.** 0 episodes, 0 views, $0 revenue, 51/51 items `todo`. **56.0% of $0 is $0.** The items multiply
  a base that does not exist, and no item in the tracker can create that base - only publishing can.
* **That the percentages are measured.** They are `PPM_REVIEW.md` §1's stated claims. The largest (`THM-01` +20%) is that review's
  own weakest assumption: each 10 percentage points of it is +/-$209/month here.
* **That the improvements replace the sprint.** The first 30 videos are worth more than all twelve items combined; §7 exists so the
  items hang off the spine instead of competing with it.
* **That $1,500-$2,000/month is the mission.** `README.md` and `AGENTS.md` still state $1,000-$2,000/day. This document answers the
  smaller target on request and does not revise the mission.
