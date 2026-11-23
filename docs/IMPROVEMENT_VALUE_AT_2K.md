# Reaching $1,500-$2,000/month: the decision memo

> **What this file is.** The whole improvement-value analysis (308 lines, group bounds, $/hour tables, a 7-item corrections log)
> was committed as **`fdd20d0`** and is deliberately not kept in the working tree: with 0/51 items built and nothing published, it
> prices a revenue base that does not exist. Restore it with `git show fdd20d0:docs/IMPROVEMENT_VALUE_AT_2K.md`.
> **This memo keeps only what changes a decision.** Revisit at 100 published videos, when `ANA-01` can replace percentages with
> measurements.

## 1. The one equation

```
$2,000 profit + $85 cost   = $2,085 revenue/month  =  9,929 views/day at $7 RPM
```

Everything else is a choice of **how many videos** and **how many views each one gets per day**. Those two multiply.

## 2. Where the target already sits in the plan - and it is not month 6

`initialBrainstrom/conversations/01-ai-data-documentary-branches.md`, Month 7-9 row: **450 videos, 10,000 views/day, $7 RPM**.

```
ad revenue   = 10,000 x 30 / 1,000 x $7                = $2,100 / month
+ repurposing $15/day + passive $10/day                = $2,850 / month  (the row's PPM)
ad-only profit after $85 cost                          = $2,015 / month
implied per-video rate = 10,000 / 450                  = 22.22 views/video/day
```

**The target is that row.** $2,100 of ad revenue is $2,085 plus $15 of rounding. So the honest baseline is not "163 videos at the
Month 13-16 rate" (61 views/video/day) - it is **450 videos at the rate the plan itself projects for a 450-video library**
(447 whole videos is the exact threshold for $2,085 at that rate).

## 3. The calendar, which is the only thing that varies

Videos needed for $2,085 of ad revenue, and months at three publishing rates:

| views/video/day | Source | Videos needed | 30/mo (sprint) | 60/mo (2/day) | 90/mo (3/day) |
|---|---|---|---|---|---|
| **22.22** | **plan Month 7-9** | **450** | **15.0 mo** | **7.5 mo** | **5.0 mo** |
| 30 | between rows | 331 | 11.0 | 5.5 | 3.7 |
| 40 | this memo's floor | 249 | 8.3 | 4.1 | 2.8 |
| 61 | plan Month 13-16 | 163 | 5.4 | 2.7 | 1.8 |
| 94 | plan Month 25-28 | 106 | 3.5 | 1.8 | 1.2 |

**$1,500-$2,000/month lands between month 1.2 and month 15 depending on two numbers nobody has measured.** That is the whole
answer, and it is why the next 30 videos matter more than any further document: they measure the first of the two.

## 4. The two contradictions that decide which cell you land in

**(a) The repo contains two different publishing rates.** `SPRINT_30_DAYS.md` says 30 videos in 30 days. The plan's library column
says 450 videos by month 9 - which is 50-64 videos/month - and `REN-02`'s own claim in `PPM_REVIEW.md` is "3 vs 2 episodes/day",
i.e. 60-90/month. The sprint is the conservative one, and at 30/month the plan's Month 7-9 row cannot arrive before month 15.

**(b) The plan's per-video rate is not a constant - it rises 4.25x as the library grows.**

| Plan row | Library | Views/day | Implied views/video/day |
|---|---|---|---|
| Month 7-9 | 450 | 10,000 | 22.22 |
| Month 10-12 | 650 | 25,000 | 38.5 |
| Month 13-16 | 900 | 55,000 | 61.1 |
| Month 17-20 | 1,200 | 95,000 | 79.2 |
| Month 21-24 | 1,500 | 140,000 | 93.3 |
| Month 25-28 | 1,800 | 170,000 | 94.4 |

A growing library normally sees *decaying* per-video performance, because new uploads cannibalise old ones. Here it is assumed to
rise 22.2 -> 94.4 (4.25x) while the library rises 4x. Hold the rate at 22.22 and the Year-3 row (1,800 videos, $10.50 RPM) is
**$12,600/month, not $68,850 - a 5.5x overstatement**. Most of the plan's growth curve is the assumption, not the inventory.

## 5. What that changes in the decisions

| Was | Is now | Why |
|---|---|---|
| `REN-02` throughput is worth **$0** at this scale | **The primary lever.** It is the only thing that moves a cell leftwards in §3 without improving quality | Moving from 30 to 60/month halves the calendar at every rate in the table - at the plan's own 22.22 (447 videos) it is 14.9 -> 7.5 months |
| `THM-01` is worth $418/month | Unchanged, and it is **free** - only 4 items / 8.5h upstream of the start, and 4 items upstream of `PUB-01` | It is already on the critical path to the first upload |
| `CMP-04` is worth $125/month | Unchanged, and it has the **only hard external deadline** in the set: before the first AdSense payment. Nothing in production depends on it | Lost at payout time if the W-8BEN is missing |
| Packaging levers (G1/G2/G3) dominate | They matter **after** the per-video rate is measured, not before | A +20% on an unmeasured 22.22 is worth less than knowing whether it is 22 or 40 |

Cost stays second-order at every rate: 90 videos/month adds ~$105-150 of variable cost against a $2,085 target (~7%).

## 6. The measurement plan - three checkpoints, no new documents

| Checkpoint | What it settles | What it changes |
|---|---|---|
| **Video 10** | CTR and AVD on a real thumbnail/title | Whether `THM-01`'s +20% is real |
| **Video 30** | **views/video/day on a 30-video library** - the first real reading of the number the whole table turns on | Which §3 cell you are in, and therefore whether the answer is month 5 or month 15 |
| **Video 60** | whether the rate is holding as the library doubles | 30/month or 60/month for the rest of the year |

`ANA-01` (3h) is what makes those readings exist. It is worth $0/month in PPM terms and is the most valuable item in the tracker.

## 7. Sequencing: the five value-bearing items on the 125-hour spine

| Item | Hours | Must come after | Blocks | Slot | Deferral limit |
|---|---|---|---|---|---|
| `THM-01` | 3.0 | `REN-01` <- `INF-03` <- `INF-02` <- `INF-01` | `QAG-02` -> `PUB-01` -> every upload | Days 1-5 | **None** |
| `TOP-03` | 2.0 | `TOP-02` <- `TOP-01` <- `DAT-01` | only `ANA-02` | Days 6-7 | Past EP01-EP05, not past EP06 |
| `PUB-02` | 3.0 | `PUB-01` + `AUD-03` | nothing | Days 8-20 | **Unbounded** - retrofittable; designated slip item ($15/h) |
| `PUB-03` | 3.5 | `REN-09` + `AUD-03` | nothing | Days 21-30 | Any published video can be re-cut |
| `CMP-04` | 2.0 | `CMP-03` <- `CMP-01` + `CMP-02` | nothing | Day 30+ | **Before the first AdSense payment** |

**Deferral order:** `PUB-02` -> `PUB-03` -> `CMP-04` -> `TOP-03` -> `THM-01` (never).

**The spine is 125.0h / 46 items** (Phase 0: 33 items / 93.0h; Phase 1: 13 items / 32.0h), not 128.0h - that figure counted
`PUB-02` twice, since it is both `P0`-priority and Phase 1. `SPRINT_30_DAYS.md` assigns all 93.0h of Phase 0 to Days 1-5, which is
**93.0h / 5 days = 18.6 h/day** against 60.0h available at 12h/day - a **33.0h** shortfall, so `TOP-01`/`TOP-02`/`TOP-03` are the
correct overflow into the Day 6-7 buffer.

## 8. The rule

**49.0h of work across 17 items** stands between the current state and the first published video (`PUB-01`). Nothing in this file
reduces that by an hour. No new analysis document until 30 episodes are published; then re-derive §3 from `ANA-01` instead of from
the plan's rows.
