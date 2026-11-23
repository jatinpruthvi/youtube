# Reaching $1,500-$2,000/day: the decision memo

> **What this file is.** The whole improvement-value analysis (308 lines, group bounds, $/hour tables, a 7-item corrections log)
> was committed as **`fdd20d0`** and is deliberately not kept in the working tree: with 0/51 items built and nothing published, it
> prices a revenue base that does not exist. Restore it with `git show fdd20d0:docs/IMPROVEMENT_VALUE_AT_2K.md`.
> **This memo keeps only what changes a decision.** Revisit at 100 published videos, when `ANA-01` can replace percentages with
> measurements.
>
> **Target correction (this revision).** Earlier versions of this file priced the goal as **$1,500-$2,000 per month**. That was the
> wrong unit: `AGENTS.md` sec.1, `README.md` line 3 and `docs/TRACKER.md` line 4 all state the mission as
> **$1,000-$2,000+ per day ($30k-$60k+/month)**, and `PPM_REVIEW.md` sec.8 already prices it per day. Every figure below is now
> per day. The monthly reading made the goal look like the plan's Month 7-9 row; at the daily reading it is the plan's Month 20-26.
>
> **Revenue or profit, and per day or per month?** Two unit questions sit under this file, and both are answered with arithmetic
> rather than by picking one. The mission's own wording is *"pure platform ad revenue"*, so sections 1.1-1.3 price a **revenue**
> target; **1.4** adds the cost stack ($2.14-$105.14/day depending on whether the 2-3 FTE hires exist) and states **profit/day and
> profit/month for every operating point** under one conversion, `profit/month = profit/day x 30`. The request this file answers asks
> for **$1,500-$2,000 per *month*** while the mission line says **per *day***; **1.5** prices the monthly reading too (64-126 videos
> rather than 1,913-2,564), so the 30x difference is visible instead of implied. No table here mixes the two units.

## 1. The target is per day

```
AGENTS.md sec.1 mission      = $1,000-$2,000+ / day  = $30,000-$60,000+ / month
this memo uses the upper half = $1,500-$2,000 / day  = $45,000-$60,000   / month
```

```
revenue/day = V x v x RPM / 1000  +  ancillary
              V   = videos in the library
              v   = views per video per day
              RPM = dollars per 1,000 views
```

**Ancillary** is the plan's repurposing + passive + refresh lines. Its own Month 25-28 row is
$220 + $140 + $150 = **$510 of $2,295 = 22.2% of the total**, i.e. 28.6% of AdSense. The tables below use **78% ad / 22%
ancillary**. If ancillary never materialises, every ad figure rises by `1 / 0.78 = 1.28x`. **Ancillary has zero tracker items** -
all 51 are ad-side.

**This formula is gross revenue, per day.** Profit is 1.4: subtract $2.14-$2.64/day solo or $70.56-$105.14/day with the 2-3 FTE hires
(4.7-7.0% of a $1,500-$2,000 day), then `x 30` for profit/month. The same goal read as a *monthly* figure is 1.5 - a 30x smaller
business. Infrastructure is second-order at this scale ($2.14-$5.14/day, under 0.4% of the target). Labour is not second-order, and
is not in the repo at all (sec.3).

### 1.1 Ad revenue and views/day required

| Profit goal (per day) | Ad revenue/day (78%) | Views/day at $7 RPM | at $10.50 | at $14 | AdSense-only views/day at $10.50 |
|---|---|---|---|---|---|
| **$1,500/day** | $1,170 | 167,143 | 111,429 | 83,571 | 142,857 |
| **$2,000/day** | $1,560 | 222,857 | 148,571 | 111,429 | 190,476 |

`views/day = ad revenue/day x 1000 / RPM`. RPM band is the plan's own: `$7` is where its projection starts, `$10.50` is its
Month 25-28 blended figure, `$14` is inside the `$10-18` band that `branches.md` itself assigns to EconomicsByNumbers. Both rows are
**revenue** columns of a *profit* goal: `revenue/day = profit goal + $2.14...$105.14` (1.4), so the two rows need $1,570.56-$1,605.14
and $2,070.56-$2,105.14/day of revenue for the full cost stack, or the figures above when the operator is solo. The same two goals read
as a *monthly* figure are 1.5.

### 1.2 Library size required

Videos needed for **$1,500/day of revenue**, by per-video rate (as *profit* at the hired stack it is 1,913-1,955, 1.4):

| RPM | v = 22.22 <br>(plan Month 7-9) | v = 61 <br>(plan Month 13-16) | v = 91 <br>(61 + the twelve items' +49.1%) | v = 94 <br>(plan Month 25-28) |
|---|---|---|---|---|
| **$7** | 7,522 | 2,740 | 1,837 | 1,778 |
| **$10.50** | 5,015 | **1,827** | 1,224 | 1,185 |
| **$14** | 3,761 | 1,370 | **918** | 889 |

Videos needed for **$2,000/day of revenue** (as profit at the hired stack, 2,522-2,564):

| RPM | v = 22.22 | v = 61 | v = 91 | v = 94 |
|---|---|---|---|---|
| **$7** | 10,030 | 3,653 | 2,449 | 2,371 |
| **$10.50** | 6,686 | 2,436 | 1,633 | 1,581 |
| **$14** | 5,015 | **1,827** | 1,224 | 1,185 |

Three readings of the same table:

* **At today's per-video rate (61) and the plan's own Month-25 RPM ($10.50), $1,500/day needs 1,827 videos.** Volume alone clears
  the goal - the packaging improvement is not required, it is the accelerator.
* **At $14 RPM and 91 views/video/day it needs 918** - one quarter of the 22.22-rate requirement, and 12 months at 75/month.
* **The same 1,827 videos deliver either $1,500/day at $10.50 or $2,000/day at $14.** RPM and the per-video rate are worth as much
  as a third of the library; neither is in `tracker/items.json` as a lever in its own right.

### 1.3 The calendar, which is the only thing that varies

| Videos needed | 30/mo (sprint) | 60/mo (2/day) | 75/mo (plan's implied) | 90/mo (3/day) |
|---|---|---|---|---|
| **918** ($14, v=91) | 31 mo | 15 | **12** | 10 |
| **1,224** ($14/$10.50, v=91) | 41 | 20 | **16** | 14 |
| **1,370** ($14, v=61) | 46 | 23 | **18** | 15 |
| **1,827** ($10.50, v=61) | **61** | 30 | **24** | 20 |
| **2,436** ($10.50, v=61, $2,000/day) | 81 | 41 | **32** | 27 |
| **5,015** (22.22, $10.50) | 167 | 84 | **67** | 56 |

**$1,500-$2,000/day lands between month 10 and month 67 (5.6 years) depending on two numbers nobody has measured and one cadence
nobody has committed to.** That is the whole answer, and it is why the next 30 videos matter more than any further document: they
measure the first of the two.

### 1.4 Profit per day, and profit per month

```
profit/day   = revenue/day - cost/day
profit/month = profit/day x 30        <- the only conversion used in this file
```

**One month is 30 days, so a year is 360.** That is not this memo's invention: `PPM_REVIEW.md` sec.8 already fixes the conversion
for this repository - *"PPM is monthly, so the conversion is fixed: $/day = PPM/month / 30."* Stating it also states its cost: a
calendar year has 365 days, so any annual total built by multiplying these months by 12 is **1.4% low** (`365 / 360 = 1.0139`).
Every profit cell below is `revenue/day - cost/day` using the cost figures published in the stack, and every /month cell is that /day
cell `x 30`, so any line can be reproduced with two subtractions and one multiplication. The stack's own monthly source is rounded
before the division, so it can sit up to $0.10 from `30 x` its daily figure - rounding, not a second estimate.

**The cost stack.** Both lines are priced in the repository already; nothing here is new.

| Cost line | Per month (source) | Per day (/30) | Where it comes from |
|---|---|---|---|
| Infrastructure, 30 videos/month | $64.10-$79.10 | **$2.14-$2.64** | `PPM_REVIEW.md` sec.0: CPX41 $27 + R2 $2 fixed, plus 30 x $1.17-$1.67 per episode |
| Infrastructure, 75 videos/month | $116.75-$154.25 | **$3.89-$5.14** | the same line at 75 episodes - the plan's ~$100/month holds only at 30/month |
| Labour, 2-3 FTE from ~Month 3 | $2,000.00-$3,000.00 | **$66.67-$100.00** | sec.3: 75 videos/month needs 300-450 h, i.e. 2-3 people at $600-$1,000/month |
| **Total, solo at 30/month** | **$64.10-$79.10** | **$2.14-$2.64** | the 61-67 month column of 1.3: no hires |
| **Total, 2-3 FTE at 75/month** | **$2,116.75-$3,154.25** | **$70.56-$105.14** | the 24-26 month column of 1.3: the only regime that reaches the goal inside 5 years |
| Flat line used by `PPM_REVIEW.md` sec.8 | $85.00 | $2.83 | infrastructure only, no labour: $5.90-$20.90/month conservative on infrastructure, and $2,031.75-$3,069.25/month short of the hired stack |

**Profit at every operating point.** Three revenue points, each under both regimes. The solo columns are the 30-per-month case
(no hires, 61-81 months per 1.3); the 2-3 FTE columns are the 75-per-month case that reaches the goal at Month 24-26.

| Operating point | Revenue/day | Revenue/month | Profit/day, solo | Profit/month, solo | Profit/day, 2-3 FTE | Profit/month, 2-3 FTE | Margin, 2-3 FTE |
|---|---|---|---|---|---|---|---|
| 900 videos, v=61, $7 (the `PPM_REVIEW.md` base) | $492.69 | $14,780.70 | $490.05-$490.55 | $14,701.50-$14,716.50 | $387.55-$422.13 | $11,626.50-$12,663.90 | 78.7-85.7% |
| 1,827 videos, v=61, $10.50 ($1,500/day) | $1,500.00 | $45,000.00 | $1,497.36-$1,497.86 | $44,920.80-$44,935.80 | $1,394.86-$1,429.44 | $41,845.80-$42,883.20 | 93.0-95.3% |
| 2,436 videos, v=61, $10.50 ($2,000/day) | $2,000.00 | $60,000.00 | $1,997.36-$1,997.86 | $59,920.80-$59,935.80 | $1,894.86-$1,929.44 | $56,845.80-$57,883.20 | 94.7-96.5% |

The base row is the `PPM_REVIEW.md` likely base with this memo's 78% ad share applied: `900 x 61 x $7 / 1000` = **$384.30 ad/day**,
and `$384.30 / 0.78` = **$492.69 total/day** = $11,529/month of ad, which is exactly `PPM_REVIEW.md`'s base.

**Margin is 78.7-85.7% at the base, 93.0-95.3% at $1,500/day and 94.7-96.5% at $2,000/day**, because labour is fixed at
$2,000-$3,000/month while revenue grows 4x. Profit per day is therefore not a different problem from revenue per day - it is the
same problem with a cost floor of $70.56-$105.14/day, i.e. **4.7-7.0% of a $1,500 day**. Only the hired stack has a margin that
moves: at the base it gives up 14-21 points, at the goal 5-7.

**What a profit target costs in inventory.** Solving `profit = goal` instead of `revenue = goal`, on the hired stack, at $10.50 RPM
and 61 views/video/day:

| Profit goal | Revenue/day needed | Revenue/month | Ad revenue/day (78%) | Views/day | Library | vs the revenue target | Calendar cost at 75/month |
|---|---|---|---|---|---|---|---|
| **$1,500/day** | $1,570.56-$1,605.14 | $47,116.80-$48,154.20 | $1,225.04-$1,252.01 | 116,670-119,239 | **1,913-1,955** | 1,827 -> +86 to +128 | +1.1-1.7 months |
| **$2,000/day** | $2,070.56-$2,105.14 | $62,116.80-$63,154.20 | $1,615.04-$1,642.01 | 153,813-156,382 | **2,522-2,564** | 2,436 -> +86 to +128 | +1.1-1.7 months |

The premium is the same +86 to +128 videos at both goals, because it depends only on cost: `$70.56-$105.14/day` divided by
`61 x $10.50 / 1000 / 0.78` = **$0.82/day of total revenue per video**. In calendar terms the profit target arrives **1.1-1.7 months
later at 75/month and 2.9-4.3 months later at 30/month** than the revenue target. **If the owner means net profit, add 86-128 videos
and 1-4 months; nothing else in this memo changes.**

**Cash, withholding, and the one-offs.** None of these is a cost of production, and all three are real. They belong on the page as
lines, not as prose:

| Line | Size | At $1,500/day | Per month (x30) | At $2,000/day | Per month (x30) |
|---|---|---|---|---|---|
| Withholding before `CMP-04` | 12% of revenue (30% x 40% US-origin) | $180.00/day | $5,400.00 | $240.00/day | $7,200.00 |
| Withholding after `CMP-04` | 6% of revenue (15% x 40%) | $90.00/day | $2,700.00 | $120.00/day | $3,600.00 |
| Cash in hand, unfiled | `revenue x 0.88 - cost` | $1,214.86-$1,249.44/day | $36,445.80-$37,483.20 | $1,654.86-$1,689.44/day | $49,645.80-$50,683.20 |
| Cash in hand, filed | `revenue x 0.94 - cost` | $1,304.86-$1,339.44/day | $39,145.80-$40,183.20 | $1,774.86-$1,809.44/day | $53,245.80-$54,283.20 |
| `CMP-04` filing, one-off | 2.0h of owner time, no cash cost | - | - | - | - |
| Runway recoup, one-off | $55,000 of cumulative labour before the first $1,500 day (sec.3) | 38.5-39.4 days | ~1.3 months | 28.5-29.0 days | ~1.0 month |

Withholding is a prepaid tax credit, not a permanent loss, but it is cash that does not arrive on the day it is earned, and the
6-point gap between the two rows is the whole value of a 2-hour filing. The recoup row is the one number profit makes worse: the
first $1,500 day arrives at Month 24-26, and **cumulative profit turns positive about 39 days after it**.

So the chain is: **revenue/day (1.1-1.3) -> minus $2.14-$105.14/day depending on regime -> profit/day -> x30 -> profit/month ->
minus withholding for cash.** The middle step is 4.7-7.0% of the goal; the last is 6-12%. At $1,500/day the cost and withholding
lines together are a **$160.56-$285.14/day** swing - comparable to the whole twelve-item package at the base (sec.5.1) and far
below what cadence is worth at the goal.

### 1.5 The other reading: $1,500-$2,000 per **month**

**The unit discrepancy, stated plainly.** The request this memo answers asks for *"$1,500 to $2,000 profit per month"*. The mission
this repository tracks is *"$1,000-$2,000+ **per day**"* (`AGENTS.md` sec.1, `README.md` line 3, `docs/TRACKER.md` line 4,
`docs/ARCHITECTURE.md` line 3). **The two are 30x apart, and both are priced here.** Sections 1.1-1.4 and 2-8 price the daily
reading, because that is the one the repository states and the one the plan's Month 20-26 rows describe. This section prices the
monthly reading, which is a different and much smaller business.

**Why the monthly reading is the tempting one.** The plan's own Month 7-9 row is **$2,850/month**. As a *monthly profit* target that
row already clears $2,000 with room: `$2,850 - $64.10...$79.10` = **$2,770.90-$2,785.90 of profit per month** for a solo operator.
As a *daily* target the same row is $95/day - **6.3% of the floor** (sec.2). One row, two readings, and the monthly one makes the
goal look eight months away instead of two and a bit years.

**What $1,500-$2,000 of profit per month actually needs** (same method, same conversion):

| Profit goal | Regime | Revenue/month needed | Ad/month (78%) | Views/day at $10.50 | Views/day at $7 | Library at v=61 ($10.50 / $7) | Months at 30/month ($10.50 / $7) |
|---|---|---|---|---|---|---|---|
| $1,500/month | solo (infra only) | $1,564.10-$1,579.10 | $1,220.00-$1,231.70 | 3,873-3,910 | 5,810-5,865 | **64 / 96** | 2.1 / 3.2 |
| $2,000/month | solo (infra only) | $2,064.10-$2,079.10 | $1,610.00-$1,621.70 | 5,111-5,148 | 7,667-7,722 | **84 / 126** | 2.8 / 4.2 |
| $1,500/month | 2-3 FTE | $3,616.75-$4,654.25 | $2,821.07-$3,630.32 | 8,956-11,525 | 13,434-17,287 | 147-189 / 220-283 | 4.9-6.3 / 7.3-9.4 |
| $2,000/month | 2-3 FTE | $4,116.75-$5,154.25 | $3,211.07-$4,020.32 | 10,194-12,763 | 15,291-19,144 | 167-209 / 251-314 | 5.6-7.0 / 8.4-10.5 |

`views/day = revenue/month x 0.78 x 1000 / (30 x RPM)`, and `library = views/day / 61`.

**The monthly reading is solo-only.** The hired stack costs $2,116.75-$3,154.25/month, which is *more than the entire $1,500-$2,000
monthly target*: hiring is not a way to reach a monthly goal, it is a way to miss it. Any monthly plan is a one-person plan, and the
monthly reading therefore never uses 1.3's 75-per-month column at all.

The other cash lines scale down with it. `CMP-04` withholding on $1,564.10-$1,579.10 of revenue is **$93.85-$189.49/month** at 6-12%,
i.e. 6.3-12.6% of the $1,500 target - the same line as 1.4, measured at a monthly scale. The runway recoup does not exist here at all,
because the monthly reading never hires anyone, and neither does the $55,000.

**The two readings side by side**, which is the whole point of this section:

| Reading | Profit target | Equivalent profit/day | Revenue needed/day | Views/day at $10.50 | Library at v=61 | Arrival at 30/month |
|---|---|---|---|---|---|---|
| **per month** | $1,500/month = $18,000/year | **$50.00** | $52.14-$52.64 | 3,873-3,910 | **64** | month 2.1 |
| **per month** | $2,000/month = $24,000/year | **$66.67** | $68.80-$69.30 | 5,111-5,148 | **84** | month 2.8 |
| **per day** | $1,500/day = $45,000/month | **$1,500.00** | $1,570.56-$1,605.14 | 116,670-119,239 | **1,913-1,955** | month 63.8-65.2 |
| **per day** | $2,000/day = $60,000/month | **$2,000.00** | $2,070.56-$2,105.14 | 153,813-156,382 | **2,522-2,564** | month 84.1-85.5 |

The target ratio is exactly 30x (`$1,500 / $50.00`). The views ratio is **30.1x** (`116,670 / 3,873`) and the library ratio
**29.9x-30.0x** (`1,913 / 64`, `2,522 / 84`) - the same 30x, with the published video counts rounded to whole videos. Nothing else
about the two businesses is proportional, though: the monthly reading fits inside the 30-video sprint's second month and needs no
hiring, no second channel, no Facebook cut and no ancillary revenue, while the daily reading is the Month 20-26 network that
sec.2-8 are about.

**Which one is the goal?** The repository's canonical line is per day, and this memo does not change it. If the owner's actual goal
is $1,500-$2,000 of profit **per month**, then the answer is **64-126 videos at 30/month - month 2-4 - and sections 3-8 are
irrelevant**: no 75/month cadence, no 37-month throughput gap, no $55,000 labour runway, no $2,000-$3,000/month hire. That is a
question for the owner, not for arithmetic, and it is the only decision in this file that changes every other number.

## 2. Where the target actually sits in the plan - and it is not Month 7-9

`initialBrainstrom/conversations/01-ai-data-documentary-branches.md`, projection rows, with the plan's own monthly column converted:

| Plan row | Library | Views/day | Implied v | Total/day | Profit/day, 2-3 FTE | Plan's own PPM/month | vs $1,500/day |
|---|---|---|---|---|---|---|---|
| Month 7-9 | 450 | 10,000 | 22.22 | **$95** | **-$10.14 to +$24.44** | $2,850 | **6.3%** |
| Month 10-12 | 650 | 25,000 | 38.5 | $280 | $174.86-$209.44 | $8,400 | 18.7% |
| Month 13-16 | 900 | 55,000 | 61.1 | $665 | $559.86-$594.44 | $19,950 | 44.3% |
| Month 17-20 | 1,200 | 95,000 | 79.2 | $1,183 | $1,077.86-$1,112.44 | $35,490 | 78.9% |
| Month 21-24 | 1,500 | 140,000 | 93.3 | **$1,800** | $1,694.86-$1,729.44 | $54,000 | **120%** |
| Month 25-28 | 1,800 | 170,000 | 94.4 | $2,295 | $2,189.86-$2,224.44 | $68,850 | 153% |
| Year 3 | 2,500 | 220,000 | 88.0 | $3,080 | $2,974.86-$3,009.44 | $92,400 | 205% |

Every `Profit/day` cell is `Total/day - $70.56...$105.14` (1.4); `x 30` makes it /month. **The Month 7-9 row does not pay for the
hires**: -$10.14 to +$24.44/day is **-$304.20 to +$733.20/month**, and the first row that clears $1,500/day of *profit* on the hired
stack is Month 21-24 at $1,694.86-$1,729.44.

**$1,500/day is the Month 20-22 band; $2,000/day is Month 25-26.** The plan says so itself: line 217, *"$2,000/day hit at Month
25-26"*. Its own calibration line 534 is the honest one: **"expected value at Month 28: ~$1,400/day"**.

So the goal is **the plan's median outcome at ~2.3 years**. The Month 7-9 row is $95/day - **6.3% of the floor**, a milestone, not
the goal. The earlier monthly reading of this memo mistook that milestone for the target and concluded the target was near.

## 3. The binding constraint is throughput, and the sprint is 2.5x under it

The plan reaches 1,800 videos at Month 25 from 450 at Month 9 - that is **50/month ramping to 84/month**. `SPRINT_30_DAYS.md`
commits to **30 videos in 30 days, 1/day**. Section 1.3 prices that difference:

```
1,827 videos at 30/month = 61 months
1,827 videos at 75/month = 24 months
```

Not one tracker item sets a cadence above 30/month. `REN-02`/`ORC-01`/`ORC-02` make 75-90/month *possible* and then stop; the
hiring that would use it does not appear anywhere in the repo. **At a monthly target, throughput was worth $0. At a daily target it
is worth 37 months.**

Labour, which the plan half-prices at `branches.md` line 463 ("3 hires, $3,000/month") but then credits with lifting revenue from
$84,000 to $120,000-150,000/month - a claim with no mechanism, since hiring buys throughput and throughput only becomes revenue as
the library compounds:

```
75 videos/month x 4-6 h of human time = 300-450 h/month = 2-3 FTE
in India at $600-1,000/month each      = $2,000-3,000/month from roughly Month 3
cumulative labour before the first $1,500 day (Month 24) = ~$55,000
```

At $45,000/month of revenue that labour is **4.4-6.7%** - affordable, but it is **$55,000 of runway before the first $1,500 day**, and
nothing in this repository acknowledges it.

## 4. The four contradictions that decide which cell you land in

**(a) The repo contains two different publishing rates.** `SPRINT_30_DAYS.md` says 30 videos in 30 days. The plan's library column
says 450 by month 9 - 50-64/month - and `REN-02`'s own claim in `PPM_REVIEW.md` is "3 vs 2 episodes/day", i.e. 60-90/month. The
sprint is the conservative one, and at 30/month the $1,500/day target cannot arrive before month 61.

**(b) The plan's per-video rate is not a constant - it rises 4.25x as the library grows.**

| Plan row | Library | Views/day | Implied views/video/day |
|---|---|---|---|
| Month 7-9 | 450 | 10,000 | 22.22 |
| Month 13-16 | 900 | 55,000 | 61.1 |
| Month 17-20 | 1,200 | 95,000 | 79.2 |
| Month 21-24 | 1,500 | 140,000 | 93.3 |
| Month 25-28 | 1,800 | 170,000 | 94.4 |

A growing library normally sees *decaying* per-video performance, because new uploads cannibalise old ones. Here it is assumed to
rise 22.2 -> 94.4 (4.25x) while the library rises 4x. **Hold the rate at 22.22 and the Month 25-28 row is $420/day, not $2,295/day
(a 5.5x overstatement); the Year-3 row is $611/day, not $3,080/day.** At a daily target this is good news as well as bad: the goal
does not *require* the compounding, only the inventory (1.1.2).

**(c) Localization trades views up against blended RPM down.** `PUB-02` and `ANA-04` dub into ES/PT/HI/AR. `PPM_REVIEW.md` prices
non-English views at **$3.00 / $2.33** against $7 English. The same 5,400 extra views/day that `ANA-04` claims are worth **$12.58 at
$2.33** and would have been worth **$37.80 at $7** - so localization pays only on audience that would *never* watch the English
version, which is exactly what nobody has measured. At a monthly target this was a rounding error; at a daily target, where RPM is a
third of the equation, a -40% blend against +15% views can be net negative. **Do not build `ANA-04` before measuring `PUB-02`'s
actual RPM effect.** It is the weakest of the twelve priced items and the cheapest to leave unbuilt.

**(d) Ancillary is 22% of the plan's revenue and 0% of the tracker.** $510/day at Month 25, roughly **$330-470/day at the target**,
produced by nothing that is scheduled, estimated, or owned. Either it becomes an item (needs the owner to add one) or the ad-side
library requirements in 1.2 rise by 1.28x.

## 5. What that changes in the decisions

| Was (monthly framing) | Is now (daily framing) | Why |
|---|---|---|
| `REN-02` throughput is worth **$0** at this scale | **The primary lever.** It is the only thing that moves a row leftwards in 1.3 without improving quality | 1,827 videos is 61 months at 30/month and 24 at 75/month: **37 months** |
| `THM-01` is worth $418/month | **$572/day** at 1,827 videos and $10.50 RPM - and it cuts the required library 1,827 -> 1,224 (-33%) | It is the only tracker lever that is worth more at the daily target than the monthly one, because it moves both terms at once |
| `CMP-04` is worth $125/month | **$90/day**: 30% vs 15% withholding on 40% US-origin revenue = 6% of revenue | Bigger than every other item at the base, and it is the only one with an external deadline (before the first AdSense payment) |
| Packaging levers (G1/G2/G3) dominate | They matter **after** the per-video rate is measured, not before | A +20% on an unmeasured 61 is worth less than knowing whether it is 45 or 91 - see the gate in `SPRINT_30_DAYS.md` |
| Ancillary is undisputed revenue | **22% of the goal that no item produces** | 4(d) |

### 5.1 What the twelve priced items are worth at the target

They are percentages, so their dollars scale with revenue - which is why they look trivial at the base and large at the goal.

| Operating point | Ad revenue/day | Twelve items at +49.1% = $/day | = $/month (x30) |
|---|---|---|---|
| 900 videos, 61 v/v/day, $7 (the `PPM_REVIEW.md` likely base) | $384.30 | **+$188.69** | +$5,660.70 |
| 1,827 videos, 61 v/v/day, $10.50 ($1,500/day) | $1,170.00 | **+$574.47** | +$17,234.10 |
| 2,436 videos, 61 v/v/day, $10.50 ($2,000/day) | $1,560.00 | **+$765.96** | +$22,978.80 |

At the base the twelve priced items are worth **$188.69/day ($5,660.70/month)** against a $1,500/day goal - **12.6% of one day's
target**. At the goal the same percentage is worth $574.47-$765.96/day ($17,234.10-$22,978.80/month), i.e. it buys back roughly a
third of a year of library building. **Multiplicative, never additive: build
it, but it cannot be the answer to how the goal is reached.**

## 6. The measurement plan - three checkpoints, no new documents

| Checkpoint | What it settles | What it changes |
|---|---|---|
| **Video 10** | CTR and AVD on a real thumbnail/title | Whether `THM-01`'s +20% is real |
| **Video 30** | **views/video/day on a 30-video library** - the first real reading of the number the whole of 1.2 and 1.3 turns on | Which cell you are in, and therefore whether the answer is month 12 or month 67 |
| **Video 60** | whether the rate is holding as the library doubles | 30/month or 75/month for the rest of the year |

`ANA-01` (3h) is what makes those readings exist. It is worth $0/month in PPM terms and is the most valuable item in the tracker.

**The video-30 gate is an open decision, not a recommendation.** `SPRINT_30_DAYS.md` carries it as
`OPEN DECISION - Video-30 views/video/day gate`, with three thresholds (>=90 / 45-90 / <45) and their consequences. **No threshold
is chosen in this repository, and this memo does not choose one.** The choice belongs to the owner, on the evidence, at video 30.

## 7. Sequencing: the five value-bearing items on the 125-hour spine

| Item | Hours | Must come after | Blocks | Slot | Deferral limit |
|---|---|---|---|---|---|
| `THM-01` | 3.0 | `REN-01` <- `INF-03` <- `INF-02` <- `INF-01` | `QAG-02` -> `PUB-01` -> every upload | Days 1-5 | **None** |
| `TOP-03` | 2.0 | `TOP-02` <- `TOP-01` <- `DAT-01` | only `ANA-02` | Days 6-7 | Past EP01-EP05, not past EP06 |
| `PUB-02` | 3.0 | `PUB-01` + `AUD-03` | nothing | Days 8-20 | **Unbounded** - retrofittable; designated slip item ($15/h) |
| `PUB-03` | 3.5 | `REN-09` + `AUD-03` | nothing | Days 21-30 | Any published video can be re-cut |
| `CMP-04` | 2.0 | `CMP-03` <- `CMP-01` + `CMP-02` | nothing | Day 30+ | **Before the first AdSense payment** |

**Deferral order:** `PUB-02` -> `PUB-03` -> `CMP-04` -> `TOP-03` -> `THM-01` (never). `ANA-04` is outside this set by 4(c): it is
the one priced item whose sign is unknown, so it is not deferred, it is unpriced.

**The spine is 125.0h / 46 items** (Phase 0: 33 items / 93.0h; Phase 1: 13 items / 32.0h), not 128.0h - that figure counted
`PUB-02` twice, since it is both `P0`-priority and Phase 1. `SPRINT_30_DAYS.md` assigns all 93.0h of Phase 0 to Days 1-5, which is
**93.0h / 5 days = 18.6 h/day** against 60.0h available at 12h/day - a **33.0h** shortfall, so `TOP-01`/`TOP-02`/`TOP-03` are the
correct overflow into the Day 6-7 buffer.

## 8. The rule

**49.0h of work across 17 items** stands between the current state and the first published video (`PUB-01`). Nothing in this file
reduces that by an hour. No new analysis document until 30 episodes are published; then re-derive 1.2 and 1.3 from `ANA-01`
instead of from the plan's rows.

At the daily target the three things that actually move the number are, in order: **cadence** (37 months), **library or RPM**
(a factor of 1.8-2.0 on the videos required), and **the twelve items** (+49.1%, worth $574-766/day once you are there). Only the
third one is in the tracker.

**Profit is not a fourth lever, and it is not a fifth unit either.** 1.4 fixes profit at revenue minus $2.14-$105.14/day depending on
regime - 93-95% of the goal once hired - under one conversion, `profit/month = profit/day x 30`. The withholding line there is a
2-hour filing rather than a build, and 1.5's reading of the same goal as a *monthly* figure is a 30x smaller business (64-126 videos,
month 2-4) that would make sections 2-8 unnecessary. Between gross and net the daily answer moves by 86-128 videos and 1-4 months;
between the daily and monthly readings it moves by a factor of 30.
