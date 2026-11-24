# 30 Videos in 30 Days — Production & Launch Tracker

> **Rule:** **30 episodes in 33 days, all inside one cluster** — 1/day from Day 4, after the Day 1–3 demand research and falsification slice (`VAL-01`). One flagship English channel, 10–18 min fact-grounded documentaries, **1080p30 on the slice and 1440p60 from `EP01`** (4K60 is a post-YPP upgrade, [DECISIONS.md](DECISIONS.md) D-12). Automated de/fr/ja captions & localized metadata (the revenue set), es-419/pt-BR/hi captions (reach), and Facebook cuts **only once the Page is confirmed eligible** (D-06).

---

> **Sequencing is decided, not open.** [`DECISIONS.md`](DECISIONS.md) fixes the cadence ramp (D-01), the falsification gate (D-02), the slate shape (D-03), the captions-before-metadata rule (D-05) and the Facebook eligibility gate (D-06). Value precedence for `THM-01`, `TOP-03`, `PUB-02`, `PUB-03` and `CMP-04` remains in [`IMPROVEMENT_VALUE_AT_2K.md`](IMPROVEMENT_VALUE_AT_2K.md) §7; Phase 0 is 93.0h of work, which is why it is no longer compressed into five days.

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

**What actually moves v, since publishing does not.** Six mechanisms raise views per video per day, and only three of them are
items on the tracker in Phase 0-1 (`VIEW_OPTIMIZATION.md` §15 ranks all six with their evidence class). The order matters: query
selection is decided before production and dominates; CTR only converts impressions that exist; satisfaction decides *future*
impressions, which is the compounding term; surfaces add inventory without dilution; and a refresh wave adds views to episodes
that already exist, which is the one lever that raises v without adding library.

**Why the gate is the rate and not the view count.** Holding the $1,500–$2,000/day of profit, the library required is exactly inverse
to this number: 22.22 views/video/day needs 5,015 videos, 61 needs 1,827, 155 needs 720, 103 needs 1,080. A gate turns that
relationship into a decision; a dashboard metric turns it into an observation taken after 40 hours of work that cannot be un-spent.

---

## Where the Phase-0 overflow goes

Phase 0 is 101.0h of work across 35 items, and no calendar makes that fit Days 1–10 alone. The deferral order is fixed rather than
improvised: `REN-03`–`REN-08` (templates) slide into the Days 18–25 window because the static path in `VAL-01` already produces
publishable episodes; `DAT-04`, `DAT-05`, `REN-07`, `REN-08` and `TOP-03` are P1 and are the last to be picked up; and nothing in
T01/T02/T04/T05 (`INF-*`, `DAT-01`/`02`/`06`/`07`/`09`, `SCR-*`, `AUD-*`) is deferrable, because a later start there moves every
episode rather than one.

## Execution Rhythm (How a Solo Dev Hits 30-in-30 Without Burnout)

| Window | Primary Focus | Output Target |
| :--- | :--- | :--- |
| **Days 1–3 (Falsification slice)** | `VAL-01`: one episode assembled by hand — hand-authored `DataBrief` (1 indicator, ~40 countries), single static-slide template, 1080p30, TTS + -14 LUFS master, `QAG-01` QC, `THM-01` thumbnails. Publish it and start the 14-day clock. | 1 published slice; the format's first retention evidence exists |
| **Days 4–10 (Factory build + daily publish)** | `INF-01`→`INF-03`, `DAT-01`/`DAT-02`/`DAT-09`, `SCR-01`→`SCR-03`, `AUD-01`/`AUD-03`/`AUD-05`, `REN-01`/`REN-09`, `PUB-01`. Publish 1/day on the 1080p30 static path meanwhile. | `EP01`–`EP07` live; the pipeline runs end to end unattended |
| **Days 11–17 (4K60 engine + the go/no-go)** | `REN-02` core engine, templates 1–4, `ORC-01` resumable DAG, `QAG-02` approval bot. **Day 17: read `VAL-01` at 14 days** — ≥20 views/video/day keeps the 4K60 investment, <10 stops the sprint and re-cuts the slate. | `EP08`–`EP14` live; 4K60 code either justified or stopped by evidence |
| **Days 18–25 (Surfaces + measurement)** | Templates 5–8, `PUB-04` session bridging, `SHR-01` Shorts extractor, `PUB-02` captions-first localization (never metadata without captions, D-05), `ANA-01` analytics ETL, `ORC-02` cron. 1440p60 throughout — 4K60 is deferred (D-12). | `EP15`–`EP22` live; first real CTR/AVD table |
| **Days 26–33 (Optimize on measurement)** | Repackage the top-CTR angles, `THM-02` mobile legibility, `ANC-01` dataset pages, `TOP-04` verdicts on the next 30 queries. Facebook stays untouched pending `PUB-03` eligibility (D-06). | **`EP23`–`EP30` live — 30/30 published** |
| **Days 34–45 (The hard gate)** | Nothing new is built. `ANA-01` gives the cohort trend from `EP01`–`EP30`; `ANA-05` refreshes the top 10. **Day 45 decides: scale or stop** — details below. | A written go/no-go, and the deferred work either released or cancelled |

### Daily Solo-Developer Operating Schedule (India Standard Time — IST)
* **02:00 – 06:30 IST (Automated):** GPU VPS executes ETL → script + fact audit → GPU TTS + WhisperX → scene render (1080p30 static path for `EP01`–`EP14`, 4K60 NVENC from `EP15`) → QC + 3 thumbnails.
* **08:00 – 08:15 IST (15 min human):** Review Telegram approval bundle on phone (30s hook clip + mobile-size thumbnail test + fact ledger) → reply `/approve`.
* **08:15 – 08:30 IST (Automated):** Resumable upload to YouTube (scheduled for **19:30 IST / 14:00 UTC** Tier-1 US East morning / EU afternoon peak) + de/fr/ja captions with metadata in the same commit (plus es-419/pt-BR/hi captions). Facebook cut only if `PUB-03` eligibility was confirmed.
* **Rest of Day:** Engineering improvements, new visual templates, and retention analysis.

---

## 30-Video High-CPM Launch Slate Tracker

**One cluster, 30 deep** (`DECISIONS.md` D-11, which supersedes the 6-pillar spread of D-03 while keeping its title rules). 20
episodes in salary and take-home pay, 10 in the adjacent cost-of-living band. Every title is the query a person types, ≤60
characters, promise in the first ~40, and no "Every Country Ranked by …" format label anywhere.

**Why not six pillars of five.** A five-video pillar cannot be read: at a log-normal view spread (σ ≈ 0.9) the 90% interval around
61 views/video/day is **32–118**, a 3.7x span — wider than the entire 61 → 94 gap this plan argues about. Six pillars of five would
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

- [ ] **30/30 episodes** published by Day 33 (1080p30 static path for `EP01`–`EP14`, native 4K60 from `EP15`), zero fact-audit violations, zero copyright/policy strikes.
- [ ] **`VAL-01` read recorded on Day 17** as views/video/day, and the `REN-02` decision written down either way — the sprint's first job is evidence, not output.
- [ ] **Average end-to-end automated pipeline time** ≤ 45 minutes per episode on the CPX41 control plane + on-demand RTX 4090 worker.
- [ ] **Operating spend** verified as a cost of ≤ $100–$115/month (compute + LLM API + storage).
- [ ] **Baseline telemetry captured** across all 30 videos: Top 5 CTR hooks, Top 5 Average View Duration (AVD) pacing styles, and Tier-1 (US/UK/CA/AU) audience percentage ≥ 55%.
- [ ] **Channel momentum:** Clear path to YouTube Partner Program (1,000 subscribers + 4,000 valid public watch hours) triggered by the top 3–5 breakout evergreen videos.
