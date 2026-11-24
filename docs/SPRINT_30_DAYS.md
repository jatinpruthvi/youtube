# 30 Videos in 30 Days — Production & Launch Tracker

> **Rule:** 30 videos in 30 days. One flagship English channel. 10–18 min 4K 60FPS fact-grounded documentaries. Automated de/fr/ja localized metadata & SRTs (the revenue set) + es-419/pt-BR/hi captions (reach) + Facebook In-Stream companion cuts.

---

> **Improvement sequencing:** precedence and deferral limits for `THM-01`, `TOP-03`, `PUB-02`, `PUB-03` and `CMP-04` - the value-bearing items that sit in the windows below - are specified in [`IMPROVEMENT_VALUE_AT_2K.md`](IMPROVEMENT_VALUE_AT_2K.md) §7, together with the Phase-0 overload (93.0h assigned to Days 1–5).

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

**The measurement.** When 30 episodes are published, `ANA-01`'s YouTube Analytics ETL gives total views for the trailing 28 days:

```
views/video/day = views(last 28 days) / published videos / 28
```

| | Decision state |
| :--- | :--- |
| Threshold | **≥ 155** keeps the 24-month path; **103–155** means the 36-month path at 1 video/day; **below 103** means neither path closes at this cadence and RPM — raise RPM or cadence instead of adding episodes |
| Reading captured | ⬜ blocked until 30 episodes are published and `ANA-01` has 28 days of trailing data |
| Recorded where | `ANA-01`'s SQLite analytics table; quote the reading here when it exists |

**Why the gate is the rate and not the view count.** Holding the $1,500–$2,000/day of profit, the library required is exactly inverse
to this number: 22.22 views/video/day needs 5,015 videos, 61 needs 1,827, 155 needs 720, 103 needs 1,080. A gate turns that
relationship into a decision; a dashboard metric turns it into an observation taken after 40 hours of work that cannot be un-spent.

---

## Execution Rhythm (How a Solo Dev Hits 30-in-30 Without Burnout)

| Window | Primary Focus | Output Target |
| :--- | :--- | :--- |
| **Days 1–5 (Factory Build)** | Complete `P0` MVP items (`INF-01` → `REN-09`, `THM-01`, `PUB-01`). Build first 4 templates (`BarChartRace`, `WorldChoroplethMap`, `SpotlightCountryCard`, `DualSplitComparison`). | End-to-end automated pipeline verified |
| **Days 6–7 (Batch Buffer)** | Run Episodes `EP01`–`EP05` overnight; tune voice pacing, audio LUFS, and thumbnail CTR legibility. Publish `EP01`–`EP02` to prime YouTube's topic graph. | 5 videos rendered, 2 published |
| **Days 8–20 (Daily Automated Cadence)** | Autonomous overnight cron renders 1–2 episodes/night; morning 08:00 IST Telegram 3-min review & `/approve`. Add Templates 6–8 (`HistoricalLineRace`, `AnimatedBubbleScatter`, `DistributionHistogram`) & de/fr/ja localization (`PUB-02`). | 18 videos live (cumulative) |
| **Days 21–30 (Optimization & FB Rollout)** | Activate Facebook In-Stream cut publisher (`PUB-03`) & YouTube Analytics ETL (`ANA-01`). Double down on top-CTR/AVD angles for final 12 episodes. | **30 videos published in 30 days** |

### Daily Solo-Developer Operating Schedule (India Standard Time — IST)
* **02:00 – 06:30 IST (Automated):** GPU VPS executes ETL → Claude Script + Fact Audit → GPU TTS + WhisperX → Parallel 4K60 NVENC Render → QC + 3 Thumbnails.
* **08:00 – 08:15 IST (15 min human):** Review Telegram approval bundle on phone (30s hook clip + mobile-size thumbnail test + fact ledger) → reply `/approve`.
* **08:15 – 08:30 IST (Automated):** Resumable upload to YouTube (scheduled for **19:30 IST / 14:00 UTC** Tier-1 US East morning / EU afternoon peak) + localized de/fr/ja metadata/SRTs (plus es-419/pt-BR/hi captions) + Facebook cut.
* **Rest of Day:** Engineering improvements, new visual templates, and retention analysis.

---

## 30-Video High-CPM Launch Slate Tracker

All 30 episodes are selected for **high Tier-1 advertiser CPM (Finance / Economics / Salaries / Housing / Global Wealth)**, **multi-year evergreen search demand**, and **100% free public API verifiability**.

| Ep | Status | Working Title (≤60 chars) | Pillar | Primary Data APIs | Hero Visuals | Dur | Stage Check (`D/S/A/V/T/YT/FB`) |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **EP01** | ⬜ | Every Country Ranked by Real Average Salary | Salaries | OECD + World Bank (PPP) | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP02** | ⬜ | Where a $100,000 Salary Actually Makes You Rich | Cost of Living | World Bank ICP + OECD | Choropleth + DualSplit | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP03** | ⬜ | Every Country Ranked by GDP Per Capita (1960–2026) | Macro Wealth | World Bank WDI + IMF | BarRace + LineRace | 16m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP04** | ⬜ | Every Country Ranked by Effective Income Tax Rate | Taxes | OECD Tax Wedge + IMF | Choropleth + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP05** | ⬜ | Why Your Salary Buys Less Every Year: 50 Years of CPI | Inflation | FRED + World Bank | LineRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP06** | ⬜ | Every Country Ranked by Housing Affordability | Housing | OECD Housing + FRED | BubbleScatter + BarRace | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP07** | ⬜ | The Global Wealth Pyramid: Where Do You Rank? | Personal Wealth | World Bank + OWID | Distribution + Spotlight | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP08** | ⬜ | Every Country Ranked by National Debt to GDP | Macro Debt | IMF DataMapper + FRED | Choropleth + BarRace | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP09** | ⬜ | Every Country Ranked by Minimum Wage vs Cost of Living | Salaries | OECD + World Bank | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP10** | ⬜ | Top 15 Economies Ranked From 1950 to 2050 | Macro Wealth | World Bank + IMF + OWID | BarRace + LineRace | 16m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP11** | ⬜ | Every Country Ranked by Hours Worked vs Income | Productivity | OECD + OWID | BubbleScatter + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP12** | ⬜ | Every Country Ranked by Household Debt Burden | Personal Debt | OECD + IMF + FRED | Choropleth + BarRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP13** | ⬜ | Which Countries Actually Have the Largest Middle Class? | Income Dist. | World Bank PIP + OWID | Distribution + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP14** | ⬜ | Every Country Ranked by Income Inequality (Gini Index) | Inequality | World Bank WDI + OECD | Choropleth + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP15** | ⬜ | Every Country Ranked by Life Expectancy vs Healthcare Cost | Quality of Life | World Bank + OECD Health | BubbleScatter + DualSplit | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP16** | ⬜ | How $1,000 in Purchasing Power Looks in 50 Countries | Cost of Living | World Bank ICP PPP | Spotlight + Choropleth | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP17** | ⬜ | Every Country Ranked by Corporate Tax Rate & Investment | Taxes / Biz | OECD + World Bank FDI | Choropleth + BubbleScatter | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP18** | ⬜ | The Demographic Cliff: Every Country Ranked by Fertility | Demographics | World Bank + UN/OWID | LineRace + Choropleth | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP19** | ⬜ | Every Country Ranked by Retirement Age & Pension Wealth | Retirement | OECD Pensions + WB | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP20** | ⬜ | Every Country Ranked by Gold & Foreign Currency Reserves | Macro Wealth | World Bank + IMF | BarRace + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP21** | ⬜ | US States vs Entire Countries: GDP & Salary Showdown | Tier-1 US Hook | FRED + World Bank | DualSplit + Choropleth | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP22** | ⬜ | Every Country Ranked by Electricity & Energy Costs | Cost of Living | OWID Energy + OECD | Choropleth + LineRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP23** | ⬜ | Every Country Ranked by Exports & Trade Surplus | Global Trade | World Bank + IMF | BarRace + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP24** | ⬜ | Every Country Ranked by Savings Rate (Who Saves Most?) | Personal Wealth | OECD + World Bank | BarRace + BubbleScatter | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP25** | ⬜ | Every Country Ranked by Youth Unemployment & Wages | Labor Market | World Bank + OECD | Choropleth + LineRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP26** | ⬜ | Every Country Ranked by Millionaire & High-Earner Density | Wealth | OWID + World Bank | Distribution + Spotlight | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP27** | ⬜ | How Global Interest Rates Crushed Housing (1980–2026) | Housing / Macro | FRED + OECD | LineRace + DualSplit | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP28** | ⬜ | Every Country Ranked by Education Spending vs Outcomes | Human Capital | World Bank + OECD PISA | BubbleScatter + BarRace | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP29** | ⬜ | Every Country Ranked by Economic Growth Since 2000 | Macro Growth | World Bank + IMF | BarRace + LineRace | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP30** | ⬜ | Where Will the Richest Countries Be in 2050? | Future Macro | IMF + OECD Long-Term | LineRace + Choropleth | 17m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |

*Legend for Stage Check:* `D` = DataBrief frozen, `S` = Script & Fact Audit passed, `A` = Audio & Alignment mastered, `V` = 4K60 Video QC passed, `T` = 3 Thumbnails ready, `YT` = YouTube + de/fr/ja published, `FB` = Facebook In-Stream cut published.

---

## 30-Day Exit KPIs (Definition of Sprint Success)

- [ ] **30/30 episodes** published in native 4K 60FPS with zero fact-audit violations and zero copyright/policy strikes.
- [ ] **Average end-to-end automated pipeline time** ≤ 45 minutes per episode on the CPX41 control plane + on-demand RTX 4090 worker.
- [ ] **Monthly operating spend** verified ≤ $100–$115/month (compute + Claude API + storage).
- [ ] **Baseline telemetry captured** across all 30 videos: Top 5 CTR hooks, Top 5 Average View Duration (AVD) pacing styles, and Tier-1 (US/UK/CA/AU) audience percentage ≥ 55%.
- [ ] **Channel momentum:** Clear path to YouTube Partner Program (1,000 subscribers + 4,000 valid public watch hours) triggered by the top 3–5 breakout evergreen videos.
