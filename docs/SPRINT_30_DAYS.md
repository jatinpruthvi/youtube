# 30 Videos in 30 Days — Production & Launch Tracker

> **Rule:** 30 videos in 30 days. One flagship English channel. 10–18 min 4K 60FPS fact-grounded documentaries. Automated ES/PT/HI/AR localized metadata + Facebook In-Stream companion cuts.

---

> **Improvement sequencing:** precedence and deferral limits for `THM-01`, `TOP-03`, `PUB-02`, `PUB-03` and `CMP-04` - the value-bearing items that sit in the windows below - are specified in [`IMPROVEMENT_VALUE_AT_2K.md`](IMPROVEMENT_VALUE_AT_2K.md) §7, together with the Phase-0 overload (93.0h assigned to Days 1–5).

## ⬜ OPEN DECISION — Video-30 views/video/day gate

**Status: OPEN — awaiting the owner's choice. No threshold is selected anywhere in this repository.**
The three options and their consequences are listed so the choice can be made on evidence at video 30 instead of guessed now.

**The measurement.** When 30 episodes are published, `ANA-01`'s YouTube Analytics ETL gives total views for the trailing 28 days:

```
views/video/day = views(last 28 days) / published videos / 28
```

This single number decides which row of `IMPROVEMENT_VALUE_AT_2K.md` §1.2 applies, and therefore whether the
**$1,500–$2,000/day of profit** mission (`AGENTS.md` §1) is a ~12-month build or a ~5.6-year one.

| Threshold | What it means | Videos needed for $1,500/day<br>(at $10.50 RPM, 78% ad share) | Months at<br>30 / 75 videos per month | What choosing this verdict would commit you to |
| :--- | :--- | :---: | :---: | :--- |
| **≥ 90 views/video/day** | Packaging works. The format is at or above the plan's own Month 25-28 assumption (94), before a year of library effects. | **~1,185–1,238** | **40–41 / 16–17** | Scale the cadence, not the format. Hire to 75–90/month, add templates rather than new topics, keep the niche and the thumbnail system unchanged. |
| **45–90 views/video/day** | Ordinary. Between the plan's Month 13-16 rate (61) and its Month 25-28 rate (94). | **~1,238–2,476** | **41–83 / 17–33** | Scale, and accept a 2–3 year build. Treat the plan's Month 7-9 row ($95/day, $2,850/month) as the interim milestone instead of the goal, and re-test the format at video 100. |
| **< 45 views/video/day** | The format or the niche is the problem, not the inventory. | **~2,476–5,015+** | **83–167 / 33–67** | Stop adding episodes. Change topic, hook or template mix before spending the next ~100 hours on the remaining pipeline, because volume cannot recover a rate this low. |

| | Decision state |
| :--- | :--- |
| Threshold | ⬜ **not chosen** — owner to pick one of the three rows above, or substitute a different set |
| Reading captured | ⬜ blocked until 30 episodes are published and `ANA-01` has 28 days of trailing data |
| Recorded where | `ANA-01`'s SQLite analytics table; quote the reading here when it exists |

**Why this is a gate and not a dashboard metric.** Holding the target at $1,500/day, the library required is exactly inverse to this
number: 22.22 views/video/day needs 5,015 videos, 61 needs 1,827, 91 needs 1,224. A gate makes that relationship a decision; a
dashboard metric makes it an observation taken after 40 hours of work that cannot be un-spent.

---

## Execution Rhythm (How a Solo Dev Hits 30-in-30 Without Burnout)

| Window | Primary Focus | Output Target |
| :--- | :--- | :--- |
| **Days 1–5 (Factory Build)** | Complete `P0` MVP items (`INF-01` → `REN-09`, `THM-01`, `PUB-01`). Build first 4 templates (`BarChartRace`, `WorldChoroplethMap`, `SpotlightCountryCard`, `DualSplitComparison`). | End-to-end automated pipeline verified |
| **Days 6–7 (Batch Buffer)** | Run Episodes `EP01`–`EP05` overnight; tune voice pacing, audio LUFS, and thumbnail CTR legibility. Publish `EP01`–`EP02` to prime YouTube's topic graph. | 5 videos rendered, 2 published |
| **Days 8–20 (Daily Automated Cadence)** | Autonomous overnight cron renders 1–2 episodes/night; morning 08:00 IST Telegram 3-min review & `/approve`. Add Templates 6–8 (`HistoricalLineRace`, `AnimatedBubbleScatter`, `DistributionHistogram`) & ES/PT/HI/AR localization (`PUB-02`). | 18 videos live (cumulative) |
| **Days 21–30 (Optimization & FB Rollout)** | Activate Facebook In-Stream cut publisher (`PUB-03`) & YouTube Analytics ETL (`ANA-01`). Double down on top-CTR/AVD angles for final 12 episodes. | **30 videos published in 30 days** |

### Daily Solo-Developer Operating Schedule (India Standard Time — IST)
* **02:00 – 06:30 IST (Automated):** GPU VPS executes ETL → Claude Script + Fact Audit → GPU TTS + WhisperX → Parallel 4K60 NVENC Render → QC + 3 Thumbnails.
* **08:00 – 08:15 IST (15 min human):** Review Telegram approval bundle on phone (30s hook clip + mobile-size thumbnail test + fact ledger) → reply `/approve`.
* **08:15 – 08:30 IST (Automated):** Resumable upload to YouTube (scheduled for **19:30 IST / 14:00 UTC** Tier-1 US East morning / EU afternoon peak) + localized ES/PT/HI/AR metadata/SRTs + Facebook cut.
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

*Legend for Stage Check:* `D` = DataBrief frozen, `S` = Script & Fact Audit passed, `A` = Audio & Alignment mastered, `V` = 4K60 Video QC passed, `T` = 3 Thumbnails ready, `YT` = YouTube + ES/PT/HI/AR published, `FB` = Facebook In-Stream cut published.

---

## 30-Day Exit KPIs (Definition of Sprint Success)

- [ ] **30/30 episodes** published in native 4K 60FPS with zero fact-audit violations and zero copyright/policy strikes.
- [ ] **Average end-to-end automated pipeline time** ≤ 45 minutes per episode on the CPX41 control plane + on-demand RTX 4090 worker.
- [ ] **Monthly operating spend** verified ≤ $100–$115/month (compute + Claude API + storage).
- [ ] **Baseline telemetry captured** across all 30 videos: Top 5 CTR hooks, Top 5 Average View Duration (AVD) pacing styles, and Tier-1 (US/UK/CA/AU) audience percentage ≥ 55%.
- [ ] **Channel momentum:** Clear path to YouTube Partner Program (1,000 subscribers + 4,000 valid public watch hours) triggered by the top 3–5 breakout evergreen videos.
