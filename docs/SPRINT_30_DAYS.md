# 30 Videos in 30 Days — Production & Launch Tracker

> **Rule:** **30 episodes in 33 days** — 1/day from Day 4, after the Day 1–3 falsification slice (`VAL-01`). One flagship English channel. 10–18 min fact-grounded documentaries, 1080p30 for the first 14 episodes and 4K60 from `EP15` onward (see [DECISIONS.md](DECISIONS.md) D-01 and D-02). Automated de/fr/ja captions & localized metadata (the revenue set), es-419/pt-BR/hi captions (reach), and Facebook cuts **only once the Page is confirmed eligible** (D-06).

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
| **Days 18–25 (Visual entropy + reach)** | Templates 5–8, `SHR-01` Shorts extractor, `PUB-02` captions-first localization (never metadata without captions, D-05), `ANA-01` analytics ETL, `ORC-02` cron. 4K60 output from `EP15`. | `EP15`–`EP22` live; first real CTR/AVD table |
| **Days 26–33 (Optimize on measurement)** | Repackage the top-CTR angles, `THM-02` mobile legibility, `PUB-03` eligibility test before any Facebook build, `ANC-01` dataset pages. | **`EP23`–`EP30` live — 30/30 published** |

### Daily Solo-Developer Operating Schedule (India Standard Time — IST)
* **02:00 – 06:30 IST (Automated):** GPU VPS executes ETL → script + fact audit → GPU TTS + WhisperX → scene render (1080p30 static path for `EP01`–`EP14`, 4K60 NVENC from `EP15`) → QC + 3 thumbnails.
* **08:00 – 08:15 IST (15 min human):** Review Telegram approval bundle on phone (30s hook clip + mobile-size thumbnail test + fact ledger) → reply `/approve`.
* **08:15 – 08:30 IST (Automated):** Resumable upload to YouTube (scheduled for **19:30 IST / 14:00 UTC** Tier-1 US East morning / EU afternoon peak) + de/fr/ja captions with metadata in the same commit (plus es-419/pt-BR/hi captions). Facebook cut only if `PUB-03` eligibility was confirmed.
* **Rest of Day:** Engineering improvements, new visual templates, and retention analysis.

---

## 30-Video High-CPM Launch Slate Tracker

The slate is **6 pillars x 5 episodes** (`DECISIONS.md` D-03). Every title is the query a person types, ≤60 characters, with the promise in the first ~40 so mobile does not truncate it, and no "Every Country Ranked by …" format label anywhere. One dataset, many questions — never one template, many countries (`VIEW_OPTIMIZATION.md` §2.3). No two episodes share a thesis.

| Pillar | Episodes | Advertiser band | Why this pillar |
| :--- | :---: | :--- | :--- |
| Salaries & Take-Home | `EP01`–`EP05` | Tier-1 finance CPM | The highest-volume evergreen query family in the niche, and every episode has a personal-stake hook |
| Cost of Living & Housing | `EP06`–`EP10` | Tier-1 finance CPM | Housing is the single most-searched affordability topic; rate history is a durable causal story |
| Macro Wealth & Debt | `EP11`–`EP15` | Tier-1 finance CPM | Ranking and race formats carry the best session time, and the data is the most complete |
| Taxes & Retirement | `EP16`–`EP20` | Tier-1 / Tier-2 mix | High commercial intent (tax, pension, savings products bid well) |
| Demographics & Labour | `EP21`–`EP25` | Tier-1 / Tier-2 mix | Slower-burning but compounding: fertility and labour series are re-read every year |
| US-vs-World (Tier-1 hook) | `EP26`–`EP30` | Tier-1 US | The US is the largest single RPM market; a domestic comparison frame lifts CTR for the audience that pays most |

| Ep | Status | Working Title (≤60 chars) | Pillar | Primary Data APIs | Hero Visuals | Dur | Stage Check (`D/S/A/V/T/YT/FB`) |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **EP01** | ⬜ | Average Salary by Country (2026): Take-Home Pay | Salaries & Take-Home | OECD + World Bank (PPP) | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP02** | ⬜ | What a $60,000 Salary Buys in 30 Countries | Salaries & Take-Home | World Bank ICP + OECD | Choropleth + DualSplit | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP03** | ⬜ | Minimum Wage vs Cost of Living: 30 Countries | Salaries & Take-Home | OECD + World Bank | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP04** | ⬜ | Why Your Salary Buys Less Every Year (1976–2026) | Salaries & Take-Home | FRED + World Bank | LineRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP05** | ⬜ | US States vs Countries: Where Salaries Stretch Most | Salaries & Take-Home | FRED + World Bank | DualSplit + Choropleth | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP06** | ⬜ | What $1,000 Buys in 50 Countries | Cost of Living & Housing | World Bank ICP PPP | Spotlight + Choropleth | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP07** | ⬜ | Housing Affordability by Country, 20 Years of Data | Cost of Living & Housing | OECD Housing + FRED | BubbleScatter + BarRace | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP08** | ⬜ | How Interest Rates Crushed Housing (1980–2026) | Cost of Living & Housing | FRED + OECD | LineRace + DualSplit | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP09** | ⬜ | Rent vs Income: Where Housing Eats Your Paycheck | Cost of Living & Housing | OECD + FRED | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP10** | ⬜ | Energy Costs by Country: Who Pays Most to Live | Cost of Living & Housing | OWID Energy + OECD | Choropleth + LineRace | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP11** | ⬜ | GDP per Capita by Country (1960–2026) | Macro Wealth & Debt | World Bank WDI + IMF | BarRace + LineRace | 16m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP12** | ⬜ | Top 15 Economies Ranked, 1950 to 2050 | Macro Wealth & Debt | World Bank + IMF + OWID | BarRace + LineRace | 16m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP13** | ⬜ | National Debt to GDP: 40 Countries Compared | Macro Wealth & Debt | IMF DataMapper + FRED | Choropleth + BarRace | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP14** | ⬜ | Who Holds the World's Gold and Currency Reserves | Macro Wealth & Debt | World Bank + IMF | BarRace + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP15** | ⬜ | Exports and Trade Surplus: The 2026 Ranking | Macro Wealth & Debt | World Bank + IMF | BarRace + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP16** | ⬜ | Effective Tax Rate by Country: What You Actually Pay | Taxes & Retirement | OECD Tax Wedge + IMF | Choropleth + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP17** | ⬜ | Tax Wedge: Where Workers Keep the Least | Taxes & Retirement | OECD Tax Wedge + World Bank | BarRace + Spotlight | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP18** | ⬜ | Corporate Tax vs Investment: 30 Countries | Taxes & Retirement | OECD + World Bank FDI | Choropleth + BubbleScatter | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP19** | ⬜ | Retirement Age and Pension Wealth by Country | Taxes & Retirement | OECD Pensions + World Bank | BarRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP20** | ⬜ | Who Saves Most? Savings Rate by Country | Taxes & Retirement | OECD + World Bank | BarRace + BubbleScatter | 12m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP21** | ⬜ | Fertility Rate by Country: The 2026 Demographic Cliff | Demographics & Labour | World Bank + UN/OWID | LineRace + Choropleth | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP22** | ⬜ | Hours Worked vs Income: 30 Countries | Demographics & Labour | OECD + OWID | BubbleScatter + Spotlight | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP23** | ⬜ | Youth Unemployment and Wages by Country | Demographics & Labour | World Bank + OECD | Choropleth + LineRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP24** | ⬜ | Where the Middle Class Is Actually Growing | Demographics & Labour | World Bank PIP + OWID | Distribution + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP25** | ⬜ | Life Expectancy vs Healthcare Spend by Country | Demographics & Labour | World Bank + OECD Health | BubbleScatter + DualSplit | 15m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP26** | ⬜ | US vs Europe: Where a Salary Goes Further | US-vs-World (Tier-1 hook) | OECD + World Bank PPP | DualSplit + Choropleth | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP27** | ⬜ | American Middle Class vs the World: Data Check | US-vs-World (Tier-1 hook) | FRED + World Bank | DualSplit + Distribution | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP28** | ⬜ | US House Prices vs 10 Countries (2000–2026) | US-vs-World (Tier-1 hook) | FRED + OECD | LineRace + DualSplit | 14m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP29** | ⬜ | Is the US Really the Richest Country? Six Charts | US-vs-World (Tier-1 hook) | World Bank + IMF + FRED | DualSplit + BarRace | 13m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |
| **EP30** | ⬜ | Where Will the Richest Countries Be in 2050? | US-vs-World (Tier-1 hook) | IMF + OECD Long-Term | LineRace + Choropleth | 17m | `[ ] [ ] [ ] [ ] [ ] [ ] [ ]` |

*Legend for Stage Check:* `D` = DataBrief frozen, `S` = Script & Fact Audit passed, `A` = Audio & Alignment mastered, `V` = 4K60 Video QC passed, `T` = 3 Thumbnails ready, `YT` = YouTube + de/fr/ja published, `FB` = Facebook In-Stream cut published.

---

## 30-Day Exit KPIs (Definition of Sprint Success)

- [ ] **30/30 episodes** published by Day 33 (1080p30 static path for `EP01`–`EP14`, native 4K60 from `EP15`), zero fact-audit violations, zero copyright/policy strikes.
- [ ] **`VAL-01` read recorded on Day 17** as views/video/day, and the `REN-02` decision written down either way — the sprint's first job is evidence, not output.
- [ ] **Average end-to-end automated pipeline time** ≤ 45 minutes per episode on the CPX41 control plane + on-demand RTX 4090 worker.
- [ ] **Operating spend** verified as a cost of ≤ $100–$115/month (compute + LLM API + storage).
- [ ] **Baseline telemetry captured** across all 30 videos: Top 5 CTR hooks, Top 5 Average View Duration (AVD) pacing styles, and Tier-1 (US/UK/CA/AU) audience percentage ≥ 55%.
- [ ] **Channel momentum:** Clear path to YouTube Partner Program (1,000 subscribers + 4,000 valid public watch hours) triggered by the top 3–5 breakout evergreen videos.
