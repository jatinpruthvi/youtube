# 30 Videos in 30 Days — Production & Launch Tracker

> **Rule:** build a concentrated editorial slate, not a fixed production quota. The first and later episodes use the complete 1440p60 factory. Publishing cadence is derived from measured build, QA, approval, and platform throughput. 1080p30 is a fallback and 4K60 is a post-YPP upgrade ([DECISIONS.md](DECISIONS.md) D-12). Facebook output remains eligibility-gated ([DECISIONS.md](DECISIONS.md) D-06).

---

> **Sequencing is decided, not open.** [`DECISIONS.md`](DECISIONS.md) fixes capacity-led publishing (D-01), the real first launch episode (D-02), the concentrated editorial slate (D-11), captions-before-metadata (D-05), and the Facebook eligibility gate (D-06). The tracker is the source of truth for implementation dependencies.

## ✅ Video-30 views/video/day gate — thresholds derived

**Status: the threshold follows from the path you pick, at the sprint's own cadence and the plan's own RPM.** Both numbers below are
the memo's own equation read backwards, so nothing here is a new assumption:

```
ad revenue/day needed     = $1,500 x 78%                       = $1,170/day     (1.1)
videos in the library     = 30/month x months                   (the sprint's 1 video/day)
views/video/day required  = ad revenue x 1000 / (videos x RPM)  (1.1)
```

| Path | Months at 30/month | Videos in library | v required at $10.50 RPM | v required at $14 RPM |
| :--- | :---: | :---: | :---: | :---: |
| **24-month path** | 24 | 720 | **155** | 116 |
| **36-month path** | 36 | 1,080 | **103** | 77 |

At the $2,000/day end of the goal the same two paths need 206 and 138 views/video/day at $10.50 RPM.

**Read the gate at the right scale — 155 is a library-scale rate, not a 30-video one.** 155 views/video/day is what 720 videos
need: it is **111,600 views/day** of channel traffic. Applied to 30 videos it would demand 4,650 views/day from a channel with zero
subscribers, which is not a launch target, it is a lottery ticket. A realistic first cohort — 500 to 15,000 views across 28 days —
reads **0.6 to 17.9 views/video/day**. So the threshold below is the *destination*, and the only usable early signal is the trend,
not the level.

**The measurement.** When 30 episodes are published, `ANA-01`'s YouTube Analytics ETL gives total views for the trailing 28 days:

```
views/video/day = views(last 28 days) / published videos / 28
```

| Reading at 30 videos | Formula | What it decides |
| :--- | :--- | :--- |
| **Level** (v) | `views(28d) / 30 / 28` | Sets the extrapolation only. Under 3 says the slate has no search demand; it does **not** say the plan is dead, because v is an authority metric that keeps rising with the library |
| **Cohort trend** | latest 5 uploads' day-28 views vs the previous 5 | **The only pass/fail.** Flat or rising means the format compounds; falling means the topic shape is wrong and more episodes will not fix it |
| **Dilution line** | adding 30 videos to a 900-video library cuts v by 3.3% | Below **+3.3% views per month** the library grows faster than demand, so v falls even when total views rise. Publishing is not a v lever; it is a v tax |

| | Decision state |
| :--- | :--- |
| Threshold, at library scale | **≥ 155** keeps the 24-month path at 720 videos; **103–155** means the 36-month path at 1 video/day; **below 103** means neither path closes at this cadence and RPM — raise RPM or cadence instead of adding episodes. Read it at 720 videos, never at 30 |
| Reading captured | ⬜ blocked until 30 episodes are published and `ANA-01` has 28 days of trailing data |
| Recorded where | `ANA-01`'s SQLite analytics table; quote the reading here when it exists |

**The same reading decides monetization.** YPP needs 1,000 subscribers + 4,000 watch hours, and the subscriber gate is the harder
one: at a 1% subscribe rate it needs 3,333 views per video across 30 videos, i.e. **v ≈ 111** — the same number as the 36-month
path. Watch hours need only 1,429 views per video. So the Day-17 and Day-45 readings answer *both* questions at once: whether the
format compounds, and whether the channel becomes monetizable at this cadence. Subscribers per view is the term to watch, because
it is the one the end-screen and series structure of `PUB-04` can move (`BASELINE.md` §8, rules R13–R18).

**What actually moves v, since publishing does not.** Six mechanisms raise views per video per day, and only three of them are
items on the tracker in Phase 0-1 (`VIEW_OPTIMIZATION.md` §15 ranks all six with their evidence class). The order matters: query
selection is decided before production and dominates; CTR only converts impressions that exist; satisfaction decides *future*
impressions, which is the compounding term; surfaces add inventory without dilution; and a refresh wave adds views to episodes
that already exist, which is the one lever that raises v without adding library.

**Why the gate is the rate and not the view count.** Holding the $1,500–$2,000/day of profit, the library required is exactly inverse
to this number: 22.22 views/video/day needs 5,015 videos, 61 needs 1,827, 155 needs 720, 103 needs 1,080. A gate turns that
relationship into a decision; a dashboard metric turns it into an observation taken after 40 hours of work that cannot be un-spent.

---

## Capacity-led production

Publishing capacity is the measured minimum of:

1. topic/data readiness,
2. end-to-end build time,
3. render queue capacity,
4. QA and fact-audit time,
5. operator review time,
6. platform quota and approval throughput.

The schedule is recorded as episodes/week, production hours/week, review hours/week, and median cost/episode. A fixed output
count is never used to justify more work. The next item is expanded only if measured quality and policy health remain stable.

## Execution sequence

| Phase | Primary work | Exit condition |
| :--- | :--- | :--- |
| **Factory foundation** | infrastructure, contracts, migrations, warehouse, providers, fixtures | clean checkout creates and replays a frozen fixture episode |
| **Episode system** | editorial queue, script/scene, fact-audits, TTS/alignment, 1440p60 render | one complete approved episode can be rebuilt from immutable hashes |
| **Publishing system** | thumbnails, QC, approval, upload, chapters, captions, analytics | an approved episode publishes and returns measured telemetry |
| **Measured optimization** | topic performance, retention, CTR, RPM, refreshes, localization, eligible Facebook | each new surface has a recorded unit value and kill/retain decision |
| **Scale** | batching, workers, remaining templates, second-channel isolation | batch size grows only when review and policy capacity remain acceptable |

Automated steps may build the next queued episode; they never publish or spend outside a configured approval and budget gate.

---

## 30-Video High-CPM Launch Slate Tracker

**One cluster, 30 deep** (`DECISIONS.md` D-11, which supersedes the 6-pillar spread of D-03 while keeping its title rules). 20
episodes in salary and take-home pay, 10 in the adjacent cost-of-living band. Every title is the query a person types, ≤60
characters, promise in the first ~40, and no "Every Country Ranked by …" format label anywhere.

**Why not six pillars of five.** A five-video pillar cannot be read: at a log-normal view spread (σ ≈ 0.9, a modelling assumption
rather than a measured one) the 90% interval around 61 views/video/day is **32–118**, a 3.7x span — wider than the entire 61 → 94 gap this plan argues about. Six pillars of five would
produce six unreadable numbers *and* divide the one asset that compounds: cluster authority for browse and suggested traffic.

| Pillar | Episodes | Advertiser band | Why this cluster |
| :--- | :---: | :--- | :--- |
| Salary & Take-Home | `EP01`–`EP20` | Tier-1 finance CPM | The highest-volume evergreen query family in the economics niche, with a personal-stake hook on every episode and enough distinct angles to go 20 deep without repeating a thesis |
| Cost of Living (adjacent) | `EP21`–`EP30` | Tier-1 finance CPM | Adjacent enough to reinforce the same cluster, broad enough to reach "what rent/costs" queries; it is the beachhead for a second pillar only after the Day-45 read |

| Ep | Status | Working Title (≤60 chars) | Pillar | Primary Data APIs | Hero Visuals | Dur | Stage Check (`D/S/A/V/T/YT/FB`) |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **EP01** | ⬜ | Average Salary by Country (2026): Take-Home Pay | Salary & Take-Home | OECD + World Bank (PPP) | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP02** | ⬜ | Median Salary by Country: Who Really Earns Most | Salary & Take-Home | OECD + World Bank | BarRace + Choropleth | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP03** | ⬜ | What a $60,000 Salary Buys in 30 Countries | Salary & Take-Home | World Bank ICP + OECD | Choropleth + DualSplit | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP04** | ⬜ | Salary vs Cost of Living: The Real Ranking | Salary & Take-Home | OECD + World Bank ICP | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP05** | ⬜ | Take-Home Pay After Tax: 30 Countries Compared | Salary & Take-Home | OECD Tax Wedge + World Bank | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP06** | ⬜ | Why Your Salary Buys Less Every Year (1976–2026) | Salary & Take-Home | FRED + World Bank | LineRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP07** | ⬜ | Minimum Wage by Country: Who Actually Gets More | Salary & Take-Home | OECD + World Bank | BarRace + Choropleth | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP08** | ⬜ | Nurse Salaries by Country: 20 Places Compared | Salary & Take-Home | OECD Health + World Bank | Spotlight + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP09** | ⬜ | Teacher Salaries by Country: 20 Places Compared | Salary & Take-Home | OECD Education + World Bank | Spotlight + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP10** | ⬜ | Engineer Salaries by Country: 20 Places Compared | Salary & Take-Home | OECD + World Bank | Spotlight + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP11** | ⬜ | Overtime, Hours Worked and Pay: 30 Countries | Salary & Take-Home | OECD + OWID | BubbleScatter + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP12** | ⬜ | Gender Pay Gap by Country: The 2026 Numbers | Salary & Take-Home | OECD + World Bank | DualSplit + Choropleth | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP13** | ⬜ | Public vs Private Sector Pay: 25 Countries | Salary & Take-Home | OECD + World Bank | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP14** | ⬜ | Disposable Income by Country: What's Really Left | Salary & Take-Home | OECD + World Bank | BarRace + DualSplit | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP15** | ⬜ | Savings Rate by Country: Who Saves Most in 2026 | Salary & Take-Home | OECD + World Bank | BarRace + BubbleScatter | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP16** | ⬜ | Gig and Freelance Pay by Country: 20 Markets | Salary & Take-Home | OECD + World Bank | Spotlight + Choropleth | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP17** | ⬜ | Remote Work Salary Arbitrage: 15 Countries | Salary & Take-Home | World Bank PPP + OECD | DualSplit + Choropleth | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP18** | ⬜ | Wage Growth vs Inflation: 20 Years of Data | Salary & Take-Home | FRED + OECD | LineRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP19** | ⬜ | Wage Share of GDP: Where Workers Get the Least | Salary & Take-Home | OECD + World Bank | Choropleth + LineRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP20** | ⬜ | CEO Pay vs the Average Worker: 20 Countries | Salary & Take-Home | OECD + World Bank | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP21** | ⬜ | What $1,000 Buys in 50 Countries | Cost of Living (adjacent) | World Bank ICP PPP | Spotlight + Choropleth | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP22** | ⬜ | Rent vs Income: Where Housing Eats Your Paycheck | Cost of Living (adjacent) | OECD Housing + FRED | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP23** | ⬜ | Grocery Basket Costs: 30 Countries Compared | Cost of Living (adjacent) | World Bank ICP + OECD | Choropleth + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP24** | ⬜ | Utilities and Energy Bills: Who Pays Most to Live | Cost of Living (adjacent) | OWID Energy + OECD | Choropleth + LineRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP25** | ⬜ | Housing Affordability by Country, 20 Years of Data | Cost of Living (adjacent) | OECD Housing + FRED | BubbleScatter + BarRace | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP26** | ⬜ | Childcare Costs vs Salary: 20 Countries | Cost of Living (adjacent) | OECD + World Bank | DualSplit + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP27** | ⬜ | Healthcare Costs Out of Pocket: 30 Countries | Cost of Living (adjacent) | World Bank + OECD Health | Choropleth + BubbleScatter | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP28** | ⬜ | Commute Cost and Time: 20 Cities Compared | Cost of Living (adjacent) | OECD + World Bank | Spotlight + LineRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP29** | ⬜ | Retirement Replacement Rate: What Pensions Pay | Cost of Living (adjacent) | OECD Pensions + World Bank | BarRace + LineRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP30** | ⬜ | Where the Middle Class Is Actually Shrinking | Cost of Living (adjacent) | World Bank PIP + OWID | Distribution + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |

*Legend for Stage Check:* `D` = DataBrief frozen, `S` = Script & Fact Audit passed, `A` = Audio & Alignment mastered, `V` = 4K60 Video QC passed, `T` = 3 Thumbnails ready, `YT` = YouTube + de/fr/ja published, `FB` = Facebook In-Stream cut published.

---

## 30-Day Exit KPIs (Definition of Sprint Success)

- [ ] Publishing capacity is measured and recorded as episodes/week, build/review hours, and cost/episode, zero fact-audit violations, zero copyright/policy strikes.
- [ ] `VAL-01` is published through the complete 1440p60 factory and contributes measured operating telemetry.
- [ ] **Average end-to-end automated pipeline time** ≤ 45 minutes per episode on the CPX41 control plane + on-demand RTX 4090 worker.
- [ ] **Operating spend** verified as a cost of ≤ $100–$115/month (compute + LLM API + storage).
- [ ] **Baseline telemetry captured** across all 30 videos: Top 5 CTR hooks, Top 5 Average View Duration (AVD) pacing styles, and Tier-1 (US/UK/CA/AU) audience percentage ≥ 55%.
- [ ] **Channel momentum:** Clear path to YouTube Partner Program (1,000 subscribers + 4,000 valid public watch hours) triggered by the top 3–5 breakout evergreen videos.
