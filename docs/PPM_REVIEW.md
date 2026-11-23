# Per-item PPM review - all 51 tracker items

Mission question: *would improving, accelerating or resequencing this item increase PPM, and by how much per month?*
Answer for every item in `tracker/items.json`, in tracker order, with the arithmetic shown.

> **This document reviews only. No item has been started, resequenced, or edited, and `tracker/items.json` is untouched.**

## 0. Which inputs are measured, and which are assumed

**This repository contains no measured performance data.** `src/` does not exist, so no pipeline has run; all 51 tracker items
are `todo`, so no episode has been produced, nothing has been uploaded, and no revenue or analytics row exists anywhere in the
repo. There is no YouTube Studio export, no CTR log, no RPM history and no invoice in this repository.

So the honest position is: **the revenue side is entirely assumed; the only hard facts are zero episodes and zero earnings.**

| Input | Value used | Status | Where it comes from | Plausible range |
|---|---|---|---|---|
| Published episodes | 0 | **MEASURED** | tracker: 51/51 items `todo` | 0 |
| Revenue earned to date | $0 | **MEASURED** | no channel exists (`CMP-01` todo) | $0 |
| Library size | 900 videos | ASSUMED | `01-ai-data-documentary-branches.md`, Month 13-16 projection row | 360 - 1,500 |
| Views per video per day | **40 / 61 / 94** (low / likely / high) | ASSUMED | branches projection rows: 61 at Month 13-16 (55,000 / 900), 94 at Month 25-28 (170,000 / 1,800); 40 is this review's floor | 40 - 94 |
| RPM | $7 | ASSUMED | ARCHITECTURE sec.6: $8-16 RPM, $10 baseline | $5 - $16 |
| Monthly cost | $85 | ASSUMED (list prices, not an invoice) | ARCHITECTURE sec.5 Topology A table | $64 - $100 |
| US share of revenue | 40% | ASSUMED | not stated anywhere in the repo | 25% - 55% |
| FB In-Stream lift | +15% | ASSUMED | ARCHITECTURE sec.6: "+15% to +30%" | +15% - +30% |
| Non-EN RPM | $3.00 / $2.33 | ASSUMED | not stated anywhere in the repo | $2 - $4 |

**The base now carries the range the plan itself states** instead of a single figure below it. 61 views per video per day is the
plan's own Month 13-16 projection rate; 94 is its Month 25-28 rate; 40 is kept as the floor. Nothing above multiplies two guesses
together, and each input carries its own range.

### Cost line, derived from the plan's own table

```
fixed      = CPX41 $27 + R2 ~$2                       = $29/month
variable   = (GPU $20-35 + LLM $10 + voice $5) / 30    = $1.17-1.67 per episode
itemised   = $29 + 30 x $1.17 ... 30 x $1.67           = $64 - $79/month
plan total =                                              ~$85 - $100/month
used here  = $85 (the plan's own low end, above the itemised total, so it cannot flatter the result)
```

Cost sensitivity is trivial: +/-$20/month of infra moves PPM by +/-$20, which is under 0.3% at every base.

## Three bases, because the per-video rate is the one input nobody has measured

| | Base L | Base M (likely) | Base H |
|---|---|---|---|
| Views per video per day | 40 | **61** | 94 |
| Source | this review's floor | plan Month 13-16 row | plan Month 25-28 row |
| Views/month | 1,080,000 | 1,647,000 | 2,538,000 |
| Revenue/month at $7 RPM | $7,560 | $11,529 | $17,766 |
| Cost/month | -$85 | -$85 | -$85 |
| **Base PPM** | **$7,475** | **$11,444** | **$17,681** |
| Base PPM per day | $249 | $381 | $589 |

Base A - the measured state - is still **$0/month**: 0 videos, 0 views, 0 revenue, and -$29/month if the control plane is already
running. Every figure below is a percentage of revenue, so the percentages transfer to whatever base materialises; at Base A they
are all $0. That is why the ranking by $/hour is the durable finding and the totals are conditional.

### Derived units (one per base)

```
1% of views     = 10,800 / 16,470 / 25,380 views/mo = $75.60 / $115.29 / $177.66 per month
one video-month = 8.4 / 12.81 / 19.74 dollars per video per month
```

**Three kinds of improvement, kept separate:** **(a)** raises views or RPM, so it is counted. **(b)** lowers cost per episode,
counted but small. **(c)** only lowers loss risk or saves labour, so it is **$0/month until a failure actually happens** and is
never added to the total. **(g)** is a gate: it unlocks revenue the base already assumes.

## 1. Item-by-item review

Every dollar figure in this section is written **at 40 / 61 / 94 views per video per day**. `Group` points at section 2: items in
the same group move the same variable and **cannot be added to each other**.

### T01 - Infrastructure, Compute & Cost Guardrails

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `INF-01` | Provision Hetzner CPX41 control plane + on-demand RTX 4090 worker withi... <sub>2h - P0</sub> | b | C | Negligible | GPU window 3h to 2h/day = 30h x $0.40/h (plan: 60h/mo for $20-35) = **+$12** at every base (cost down) | No - $6/h |
| `INF-02` | Install Python 3.11+, CUDA Toolkit, FFmpeg with NVENC (hevc_nvenc/h264_... <sub>2h - P0</sub> | c | - | No impact | $0 - setup labour; enables every later item | No - $0/mo |
| `INF-03` | Initialize Python project skeleton, pyproject.toml, .env secrets templa... <sub>1.5h - P0</sub> | c | - | No impact | $0 - repo skeleton | No - $0/mo |
| `INF-04` | Configure Cloudflare R2 (or Backblaze B2) archive sync & NVMe auto-prun... <sub>1.5h - P1</sub> | b | C | Negligible | R2 archive ~$2/mo replaces NVMe growth = **+$2** at every base | No - $1.33/h |
| `INF-05` | Set up API spend guardrails & monthly cost telemetry (Claude API + GPU... <sub>1h - P1</sub> | c | - | No impact | $0 - caps a $13-100/mo runaway; counted only when it fires | No - $0/mo |

### T02 - Fact-Grounded Economic Data Layer (SQLite + FastMCP)

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `DAT-01` | Design SQLite warehouse schema (data/schema.sql: dim_countries, fact_ob... <sub>2.5h - P0</sub> | c | - | No impact | $0 - schema is a precondition for DAT-02..08 | No - $0/mo |
| `DAT-02` | Build World Bank API v2 connector with pagination, retry backoff, and i... <sub>3h - P0</sub> | c | - | No impact | $0 direct - grounding protects revenue rather than raising it | No - $0/mo |
| `DAT-03` | Build FRED API connector for US/global macro, CPI, wages, housing, and... <sub>2.5h - P0</sub> | c | - | No impact | $0 direct - same mechanism, US coverage only | No - $0/mo |
| `DAT-04` | Build OECD SDMX API connector for Tier-1 average wages, tax wedge, and... <sub>3h - P0</sub> | c | U | Not quantifiable | Unknown - needs: % of the 30-video slate passing a 40-country, 5-year data gate with vs without OECD | Maybe - after the data audit |
| `DAT-05` | Build DBnomics, UN Data, IMF and Our World in Data (OWID) secondary con... <sub>2.5h - P1</sub> | c | U | Not quantifiable | Unknown - needs: same gate metric, per provider (DBnomics, UN, IMF, OWID) | Maybe - after the data audit |
| `DAT-06` | Build Data Normalizer (ISO-3 reconciliation, PPP vs Nominal tagging, mi... <sub>3h - P0</sub> | c | - | No impact | $0 - prevents ISO/unit mismatches (error risk) | No - $0/mo |
| `DAT-07` | Build Deterministic Statistical Analyzer & DataBrief JSON + Fact-ID Led... <sub>3.5h - P0</sub> | c | - | No impact | $0 - the fact ledger is the hallucination defence; a failure costs more than the base | No - $0/mo |
| `DAT-08` | Build FastMCP data-grounding server (get_indicator, rank_countries, get... <sub>3h - P0</sub> | c | - | No impact | $0 - saves ~5h/mo labour and ~$1.50/mo retry tokens (below the noise floor) | No - $0/mo |

### T03 - Topic Intelligence & Editorial Queue

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `TOP-01` | Create Editorial Queue DB & seed initial 30-Video Launch Slate mapped t... <sub>2h - P0</sub> | c | - | No impact | $0 - queue is the container for TOP-02/03 | No - $0/mo |
| `TOP-02` | Build YouTube Autocomplete & Outlier Competitor Video Miner <sub>3h - P1</sub> | a | G2 | Moves PPM | +5% median views = 5% x ($7,560 / $11,529 / $17,766) = **+$378 / $576 / $888** - same view pool as TOP-03, see G2 | Yes - $192/h |
| `TOP-03` | Implement automated Topic Scorer (Tier-1 demand, CPM weight, data compl... <sub>2h - P1</sub> | a | G2 | Moves PPM | +5% median views = 5% x ($7,560 / $11,529 / $17,766) = **+$378 / $576 / $888** - G2 leader | Yes - $288/h |

### T04 - Claude Narrative Script & Fact-Audit Engine

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `SCR-01` | Define Pydantic SceneGraph JSON Schema (acts, scenes, visual templates,... <sub>3h - P0</sub> | c | - | No impact | $0 - schema precondition for SCR-02..04 | No - $0/mo |
| `SCR-02` | Engineer versioned Claude 3.5 Sonnet prompts with prompt caching and a... <sub>4h - P0</sub> | b | C | Negligible | prompt caching cuts a script from $0.15 to $0.08 x 30 = **+$2** at every base (plan: >=70% input-token savings) | No - $0.50/h |
| `SCR-03` | Build Zero-Hallucination Automated Fact-Audit Gate & targeted auto-repa... <sub>3h - P0</sub> | c | - | No impact | $0 - one ungrounded number risks a strike; counted only when it prevents that | No - $0/mo |
| `SCR-04` | Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts... <sub>2h - P1</sub> | a | G3 | Moves PPM | +4% views = 4% x ($7,560 / $11,529 / $17,766) = **+$302 / $461 / $711** - G3 leader | Yes - $230/h |

### T05 - Voiceover, Forced Alignment & Audio Mastering

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `AUD-01` | Deploy local GPU TTS (MeloTTS primary, Kokoro-82M alternate, Azure Neur... <sub>3h - P0</sub> | b | C | Negligible | local TTS removes the whole $5/mo Azure fallback line = **+$5** at every base | No - $1.67/h |
| `AUD-02` | Build Pronunciation Lexicon & SSML/Pause Preprocessor for countries, cu... <sub>1.5h - P0</sub> | a | U | Not quantifiable | Unknown - needs: AVD on 5 episodes with vs without the pronunciation lexicon | Maybe - after 5 episodes |
| `AUD-03` | Integrate WhisperX / stable-ts Forced Word-Level Alignment <sub>2.5h - P0</sub> | c | - | No impact | $0 - alignment enables captions/SRT export only | No - $0/mo |
| `AUD-04` | Curate royalty-free ambient documentary BGM stems & micro-SFX library w... <sub>2h - P0</sub> | c | - | No impact | $0 - licence manifest is strike insurance | No - $0/mo |
| `AUD-05` | Build FFmpeg Audio Mixer (sidechain BGM ducking, timestamped SFX inject... <sub>3h - P0</sub> | a | - | No impact | $0 - YouTube re-normalises loudness itself; -14 LUFS does not change RPM | No - $0/mo |

### T06 - 4K 60FPS GPU Rendering & Visual Template Library

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `REN-01` | Establish 4K 60FPS Documentary Visual Design System (palette, typograph... <sub>3h - P0</sub> | c | - | No impact | $0 - design system is a quality precondition | No - $0/mo |
| `REN-02` | Build Core 4K60 Render Engine (atomic scene worker pool + static textur... <sub>4h - P0</sub> | b | G7 | Moves PPM | 3 vs 2 episodes/day = +30 videos/mo x one video-month ($8.40 / $12.81 / $19.74) = **+$252 / $384 / $592** (only if total views rise - see G7) | Yes - $96/h |
| `REN-03` | Implement Template 1: BarChartRace (interpolated rankings, flags, rolli... <sub>4h - P0</sub> | c | - | No impact | $0 - template is the delivery mechanism for TOP-01 topics | No - $0/mo |
| `REN-04` | Implement Template 2: WorldChoroplethMap (Natural Earth vectors, camera... <sub>4.5h - P0</sub> | c | - | No impact | $0 - same | No - $0/mo |
| `REN-05` | Implement Template 3: SpotlightCountryCard & Template 4: ChapterTitleCard <sub>3h - P0</sub> | c | - | No impact | $0 - same | No - $0/mo |
| `REN-06` | Implement Template 5: DualSplitComparison (e.g., Nominal vs PPP or Coun... <sub>3.5h - P0</sub> | c | - | No impact | $0 - same | No - $0/mo |
| `REN-07` | Implement Template 6: HistoricalLineRace & Template 7: AnimatedBubbleSc... <sub>4h - P1</sub> | a | U | Not quantifiable | Unknown - needs: CTR and AVD of the two new templates vs the bar-chart baseline over 10 videos | Maybe - after 10 videos |
| `REN-08` | Implement Template 8: DistributionHistogram + Pre-Baked 4K60 Ambient Mo... <sub>3h - P1</sub> | c | - | No impact | $0 - backgrounds are polish, not distribution | No - $0/mo |
| `REN-09` | Build Scene Concatenator, Master Audio-Video Muxer & YouTube 4K60 Expor... <sub>2.5h - P0</sub> | c | - | No impact | $0 - muxer/export is the last mile of REN-02 | No - $0/mo |

### T07 - Thumbnail Factory & A/B Packaging

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `THM-01` | Build Playwright HTML/SVG -> 1920x1080 PNG Thumbnail Factory (3 distinc... <sub>3h - P0</sub> | a | G1 | Moves PPM | CTR 3.0% to 3.6% = +20% x ($7,560 / $11,529 / $17,766) = **+$1,512 / $2,306 / $3,553** - G1 leader (quality, not the automation) | Yes - $769/h |
| `THM-02` | Add Mobile-Scale Legibility Preview (168x94px grid) & Contrast Ratio Ch... <sub>1.5h - P1</sub> | a | G1 | Moves PPM | +2% views from legibility = 2% x ($7,560 / $11,529 / $17,766) = **+$151 / $231 / $355** - inside G1, so it is G1's low bound | Yes - $154/h |

### T08 - Automated QA Gate & Mobile Approval Bot

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `QAG-01` | Build Automated QC Suite (ffprobe spec check, blackdetect, freezedetect... <sub>3h - P0</sub> | c | - | No impact | $0 - blocks a bad upload; failure costs one video-month, not a lever | No - $0/mo |
| `QAG-02` | Build Telegram (or Discord) Mobile Approval Bot with 30s hook clip, thu... <sub>2.5h - P0</sub> | c | - | No impact | $0 - saves ~2.5h/mo labour | No - $0/mo |

### T09 - Localization & Multi-Platform Publishing

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `PUB-01` | Configure Google Cloud OAuth & YouTube Data API v3 Resumable Uploader (... <sub>3h - P0</sub> | c | - | No impact | $0 - upload gate; without it revenue is exactly $0 | No - $0/mo |
| `PUB-02` | Build Automated Metadata & SRT Subtitle Localizer (Spanish, Portuguese,... <sub>3h - P0</sub> | a | G5 | Moves PPM | +5% views at non-EN $3 RPM: 1,800 / 2,745 / 4,230 v/day x 30 / 1000 x $3 = **+$162 / $247 / $381** - G5 low bound | Yes - $82/h |
| `PUB-03` | Build Facebook In-Stream Cut Generator (3s visual hook + burned caption... <sub>3.5h - P1</sub> | a | G4 | Moves PPM | plan's FB floor +15% on rendered revenue = 15% x ($7,560 / $11,529 / $17,766) = **+$1,134 / $1,729 / $2,665** | Yes - $494/h |

### T10 - Pipeline Orchestrator & Crash-Resumable DAG

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `ORC-01` | Build Resumable Episode DAG Orchestrator (SQLite state machine with sce... <sub>3.5h - P0</sub> | c | - | No impact | $0 - resumability saves rework, not revenue | No - $0/mo |
| `ORC-02` | Configure Daily Autonomous Cron / Systemd Timer for 30-in-30 Production... <sub>2h - P1</sub> | c | - | No impact | $0 - the cron is the cadence switch for REN-02's throughput | No - $0/mo |

### T11 - Compliance, Monetization & India Payout Setup

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `CMP-01` | Create Flagship YouTube Channel & Facebook Page (branding, banner, abou... <sub>2h - P0</sub> | g | - | No impact | $0 - the gate that makes any revenue possible (base assumes it passed) | No - gate, not a lever |
| `CMP-02` | Implement Anti-Demonetization Policy Checklist & Citation/License Audit... <sub>1.5h - P0</sub> | c | - | No impact | $0 - demonetisation insurance | No - $0/mo |
| `CMP-03` | Apply for YouTube Partner Program (1k subs + 4k watch hrs) & Facebook I... <sub>3h - P1</sub> | g | - | No impact | $0 - unlocks the existing revenue; not a delta | No - gate, not a lever |
| `CMP-04` | Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-... <sub>2h - P1</sub> | a | T | Moves PPM | W-8BEN 30% to 15% on 40% US-origin revenue (assumed, 25-55%) = 6% x ($7,560 / $11,529 / $17,766) = **+$454 / $692 / $1,066** | Yes - $346/h |

### T12 - Analytics Feedback Loop & Multi-Channel Scale

| ID | Item | Kind | Group | Verdict | $/month delta (arithmetic) | Worth the hours? |
|---|---|---|---|---|---|---|
| `ANA-01` | Build YouTube Analytics & Revenue daily ETL into SQLite (CTR, AVD, RPM,... <sub>3h - P1</sub> | c | - | No impact | $0 alone - the meter that makes ANA-02, TOP-02/03 and SCR-04 measurable | No - $0/mo |
| `ANA-02` | Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop <sub>3h - P1</sub> | a | G3 | Moves PPM | +4% views from the retention/RPM loop = **+$302 / $461 / $711** - inside G3, so it repeats SCR-04's claim | Yes - $154/h |
| `ANA-03` | Build Automated Annual Dataset Refresh Trigger ('2027/2028 Edition' re-... <sub>4h - P2</sub> | a | G6 | Moves PPM | refresh 100 of 900 at +60%: 2,400 / 3,660 / 5,640 extra v/day x 30 / 1000 x $7 = **+$504 / $769 / $1,184** | Yes - $192/h |
| `ANA-04` | Add Multi-Channel Config Isolation & Multi-Language Audio Dubbing (YouT... <sub>5h - P2</sub> | a | G5 | Moves PPM | +15% views at one-third RPM: 5,400 / 8,235 / 12,690 v/day x 30 / 1000 x $2.33 = **+$378 / $576 / $888** - G5 leader | Yes - $115/h |

## 2. Why these deltas cannot simply be added

An earlier draft collapsed the overlaps into a multiplier of x0.65. It was removed: nothing in this repository derives 0.65, and a
hand-picked constant applied to a sum of other hand-picked constants is the kind of number this review exists to remove. Each
priced item is assigned to the one variable it moves, and only groups are added to each other.

Rule inside a group: **low** = smallest single member claim; **likely** = largest (all land, but they buy the same variable, so the
largest wins); **high** = the sum (only if the members turn out to be genuinely additive). For a single-member group the high bound is
that lever's own upper case: 30% for FB (G4), 150 refreshed videos at +60% for G6, and no upside beyond the claim for G7.

### Group bounds at 40 views/video/day

| Group | Variable it owns | Members | Low | Likely | High |
|---|---|---|---|---|---|
| **G1** Packaging / CTR | THM-01 +20%, THM-02 +2% | $151 | $1,512 | $1,663 |
| **G2** Topic selection | TOP-02 +5%, TOP-03 +5% | $378 | $378 | $756 |
| **G3** Retention / AVD | SCR-04 +4%, ANA-02 +4% | $302 | $302 | $604 |
| **G4** Separate platform inventory | PUB-03 +15% | $1,134 | $1,134 | $2,268 |
| **G5** Non-English audience | PUB-02 +5% at $3, ANA-04 +15% at one-third RPM | $162 | $378 | $540 |
| **G6** Library refresh | ANA-03, 100 videos at +60% | $147 | $504 | $756 |
| **G7** Production throughput | REN-02 +30 videos/mo | $0 | $252 | $252 |
| **T** Withholding | CMP-04 | $284 | $454 | $624 |
| **C** Cost lines | INF-01 $12, INF-04 $2, SCR-02 $2, AUD-01 $5 | $21 | $21 | $21 |

### Group bounds at 61 views/video/day

| Group | Variable it owns | Members | Low | Likely | High |
|---|---|---|---|---|---|
| **G1** Packaging / CTR | THM-01 +20%, THM-02 +2% | $231 | $2,306 | $2,537 |
| **G2** Topic selection | TOP-02 +5%, TOP-03 +5% | $576 | $576 | $1,152 |
| **G3** Retention / AVD | SCR-04 +4%, ANA-02 +4% | $461 | $461 | $922 |
| **G4** Separate platform inventory | PUB-03 +15% | $1,729 | $1,729 | $3,459 |
| **G5** Non-English audience | PUB-02 +5% at $3, ANA-04 +15% at one-third RPM | $247 | $576 | $823 |
| **G6** Library refresh | ANA-03, 100 videos at +60% | $224 | $769 | $1,153 |
| **G7** Production throughput | REN-02 +30 videos/mo | $0 | $384 | $384 |
| **T** Withholding | CMP-04 | $432 | $692 | $951 |
| **C** Cost lines | INF-01 $12, INF-04 $2, SCR-02 $2, AUD-01 $5 | $21 | $21 | $21 |

### Group bounds at 94 views/video/day

| Group | Variable it owns | Members | Low | Likely | High |
|---|---|---|---|---|---|
| **G1** Packaging / CTR | THM-01 +20%, THM-02 +2% | $355 | $3,553 | $3,908 |
| **G2** Topic selection | TOP-02 +5%, TOP-03 +5% | $888 | $888 | $1,776 |
| **G3** Retention / AVD | SCR-04 +4%, ANA-02 +4% | $711 | $711 | $1,422 |
| **G4** Separate platform inventory | PUB-03 +15% | $2,665 | $2,665 | $5,330 |
| **G5** Non-English audience | PUB-02 +5% at $3, ANA-04 +15% at one-third RPM | $381 | $888 | $1,269 |
| **G6** Library refresh | ANA-03, 100 videos at +60% | $345 | $1,184 | $1,777 |
| **G7** Production throughput | REN-02 +30 videos/mo | $0 | $592 | $592 |
| **T** Withholding | CMP-04 | $666 | $1,066 | $1,466 |
| **C** Cost lines | INF-01 $12, INF-04 $2, SCR-02 $2, AUD-01 $5 | $21 | $21 | $21 |

Two things follow, and both matter more than the totals:

* **Only one of `THM-01`/`THM-02`, one of `TOP-02`/`TOP-03` and one of `SCR-04`/`ANA-02` can be credited at a time.** They are not
  six levers. They are three levers with two names each. Building both is still correct engineering; forecasting both is not.
* **`REN-02` can legitimately be worth $0.** It buys 30 more videos per month, worth one video-month each only while views per video
  per day holds - and that is exactly the number that falls as a library grows. Its low bound is 0.

## 3. Reconciliation to one top line

### At 40 views/video/day (base $7,475/month)

| Line | Low | Likely | High |
|---|---|---|---|
| G1 Packaging | $151 | $1,512 | $1,663 |
| G2 Topic selection | $378 | $378 | $756 |
| G3 Retention | $302 | $302 | $604 |
| G4 Separate platform inventory | $1,134 | $1,134 | $2,268 |
| G5 Non-English audience | $162 | $378 | $540 |
| G6 Library refresh | $147 | $504 | $756 |
| G7 Production throughput | $0 | $252 | $252 |
| T Withholding | $284 | $454 | $624 |
| C Cost lines | $21 | $21 | $21 |
| **Sum of group gains** | **$2,579** | **$4,935** | **$7,484** |
| Base PPM | $7,475 | $7,475 | $7,475 |
| **Resulting PPM** | **$10,054** | **$12,410** | **$14,959** |
| Resulting $/day | $335 | $414 | $499 |

### At 61 views/video/day (base $11,444/month)

| Line | Low | Likely | High |
|---|---|---|---|
| G1 Packaging | $231 | $2,306 | $2,537 |
| G2 Topic selection | $576 | $576 | $1,152 |
| G3 Retention | $461 | $461 | $922 |
| G4 Separate platform inventory | $1,729 | $1,729 | $3,459 |
| G5 Non-English audience | $247 | $576 | $823 |
| G6 Library refresh | $224 | $769 | $1,153 |
| G7 Production throughput | $0 | $384 | $384 |
| T Withholding | $432 | $692 | $951 |
| C Cost lines | $21 | $21 | $21 |
| **Sum of group gains** | **$3,921** | **$7,514** | **$11,402** |
| Base PPM | $11,444 | $11,444 | $11,444 |
| **Resulting PPM** | **$15,365** | **$18,958** | **$22,846** |
| Resulting $/day | $512 | $632 | $762 |

### At 94 views/video/day (base $17,681/month)

| Line | Low | Likely | High |
|---|---|---|---|
| G1 Packaging | $355 | $3,553 | $3,908 |
| G2 Topic selection | $888 | $888 | $1,776 |
| G3 Retention | $711 | $711 | $1,422 |
| G4 Separate platform inventory | $2,665 | $2,665 | $5,330 |
| G5 Non-English audience | $381 | $888 | $1,269 |
| G6 Library refresh | $345 | $1,184 | $1,777 |
| G7 Production throughput | $0 | $592 | $592 |
| T Withholding | $666 | $1,066 | $1,466 |
| C Cost lines | $21 | $21 | $21 |
| **Sum of group gains** | **$6,032** | **$11,568** | **$17,561** |
| Base PPM | $17,681 | $17,681 | $17,681 |
| **Resulting PPM** | **$23,713** | **$29,249** | **$35,242** |
| Resulting $/day | $790 | $975 | $1,175 |

### The nine outcomes, side by side

| Base | Item case | Group gains | Resulting PPM | $/day | % of $1,500/day | % of $2,000/day |
|---|---|---|---|---|---|---|
| 40 views/video/day | low | $2,579 | **$10,054** | $335 | 22% | 17% |
| 40 views/video/day | likely | $4,935 | **$12,410** | $414 | 28% | 21% |
| 40 views/video/day | high | $7,484 | **$14,959** | $499 | 33% | 25% |
| 61 views/video/day | low | $3,921 | **$15,365** | $512 | 34% | 26% |
| 61 views/video/day | likely | $7,514 | **$18,958** | $632 | 42% | 32% |
| 61 views/video/day | high | $11,402 | **$22,846** | $762 | 51% | 38% |
| 94 views/video/day | low | $6,032 | **$23,713** | $790 | 53% | 40% |
| 94 views/video/day | likely | $11,568 | **$29,249** | $975 | 65% | 49% |
| 94 views/video/day | high | $17,561 | **$35,242** | $1,175 | 78% | 59% |

Percentages divide PPM's `$/day` by the **profit** goal itself ($1,500 / $2,000); the revenue needed for that profit is
$1,502.83 / $2,002.83 per day (sec.8), so they overstate progress by 0.2%.

**The single defensible headline is the likely-likely cell: $18,958/month, $632/day.** Everything else in
the grid is a bound. The span between the lowest corner ($10,054/month, $335/day) and the highest
($35,242/month, $1,175/day) is 3.5x, and almost all of it is the per-video rate, not the
items: at a fixed item case, moving the base from 40 to 94 multiplies PPM by 2.36x, while at a fixed base, moving the item case from low to high multiplies it by 1.49x.

**Weakest remaining assumption:** the +20% views claim behind G1 (`THM-01`, CTR 3.0% to 3.6%). It is the largest single lever in
the review, worth $2,306/month at the likely base, so each 10 percentage points of that claim is +/-$1,153/month. The per-video rate is no longer a hidden assumption - it is the axis of the grid above.

## 4. Worth the hours - ranked by $/month per hour of effort

Ranking uses each item's claim **at the likely base (61 views/video/day)** because effort is unaffected by overlap. `Credited` shows
what the item actually contributes to the likely case: within each group only the leader's dollars are counted.

| Rank | ID | Item | Group | Claim $/mo at 61 | Hours | $/mo per hour | Credited in likely case |
|---|---|---|---|---|---|---|---|
| 1 | `THM-01` | Build Playwright HTML/SVG -> 1920x1080 PNG Thumbnail Factory (3 distinc... | G1 | $2,306 | 3h | **$769/h** | $2,306 |
| 2 | `PUB-03` | Build Facebook In-Stream Cut Generator (3s visual hook + burned caption... | G4 | $1,729 | 3.5h | **$494/h** | $1,729 |
| 3 | `CMP-04` | Complete India USD Payout & Tax Optimization (AdSense SWIFT, US Form W-... | T | $692 | 2h | **$346/h** | $692 |
| 4 | `TOP-03` | Implement automated Topic Scorer (Tier-1 demand, CPM weight, data compl... | G2 | $576 | 2h | **$288/h** | $576 |
| 5 | `SCR-04` | Add Retention Pacing Linter (0-35s hook, open loops, pattern interrupts... | G3 | $461 | 2h | **$230/h** | $461 |
| 6 | `ANA-03` | Build Automated Annual Dataset Refresh Trigger ('2027/2028 Edition' re-... | G6 | $769 | 4h | **$192/h** | $769 |
| 7 | `TOP-02` | Build YouTube Autocomplete & Outlier Competitor Video Miner | G2 | $576 | 3h | **$192/h** | capped by group leader |
| 8 | `THM-02` | Add Mobile-Scale Legibility Preview (168x94px grid) & Contrast Ratio Ch... | G1 | $231 | 1.5h | **$154/h** | capped by group leader |
| 9 | `ANA-02` | Build Retention Drop-Off Diagnostic & RPM-per-Topic Feedback Loop | G3 | $461 | 3h | **$154/h** | capped by group leader |
| 10 | `ANA-04` | Add Multi-Channel Config Isolation & Multi-Language Audio Dubbing (YouT... | G5 | $576 | 5h | **$115/h** | $576 |
| 11 | `REN-02` | Build Core 4K60 Render Engine (atomic scene worker pool + static textur... | G7 | $384 | 4h | **$96/h** | $384 |
| 12 | `PUB-02` | Build Automated Metadata & SRT Subtitle Localizer (Spanish, Portuguese,... | G5 | $247 | 3h | **$82/h** | capped by group leader |

Credited total: **$7,493** from these twelve, plus $21 of cost savings from the four negligible items, equals
the $7,514 likely-case sum in section 3. The order of this table is identical at the 40 and 94 bases for every revenue-side
item, because they all scale with revenue together; only the fixed-dollar items (`ANA-03`, `REN-02`, the cost lines) shift, and not
enough to change the order.

A low rank is not a reason to skip an item: `REN-02` and `PUB-02` are prerequisites for items above them, and `PUB-02` is the floor
of G5.

## 5. The 39 items that do not move PPM

Twelve items move PPM. The other 39 do not, and adding them to a forecast is how the plan's earlier numbers got inflated: 4 with
negligible cost savings, 4 unpriceable, and 31 at exactly $0.

* **Gates - not deltas:** `CMP-01`, `CMP-03`, `PUB-01`. The base already assumes they passed, so they cannot be counted twice.
* **Risk spine - large if a failure happens, $0 until it does:** `DAT-02`, `DAT-03`, `DAT-06`, `DAT-07`, `SCR-03`, `CMP-02`,
  `AUD-04`, `QAG-01`. A demonetisation or a strike costs more than the entire base; that is insurance, not a lever.
* **Labour savers:** `DAT-08`, `ORC-01`, `ORC-02`, `QAG-02`, `ANA-01`, `INF-05`. Hours, not dollars.
* **Negligible cost wins (counted, in group C):** `INF-01` +$12, `INF-04` +$2, `SCR-02` +$2, `AUD-01` +$5 - $21/month at every
  base, all under $7/h at the tracker's own effort estimates.
* **Mechanism, not margin:** `REN-01`, `REN-03` to `REN-09`, `SCR-01`, `TOP-01`, `DAT-01`, `AUD-03`, `AUD-05`.
  `AUD-05` in particular: YouTube re-normalises loudness itself, so -14 LUFS does not change RPM.

## 6. Not quantifiable from current data (four items)

These have a real mechanism but no defensible size. Each gets the single measurement that would price it, and **all four are
counted at $0 in section 3** - not at an invented number.

| Item | Why it cannot be priced | The one measurement that fixes it |
|---|---|---|
| `DAT-04` OECD | extra coverage may make more slate topics viable, or none | % of the 30-video slate passing a 40-country, 5-year gate, with vs without OECD |
| `DAT-05` DBnomics/UN/IMF/OWID | same, four providers deep | the same gate metric, per provider |
| `AUD-02` pronunciation lexicon | pronunciation plausibly affects retention, by an unknown amount | AVD on 5 episodes with vs without the lexicon |
| `REN-07` template variety | novelty effect unknown | CTR and AVD of the two new templates vs the bar-chart baseline over 10 videos |

## 7. What this does not claim - and the plan's own fudge factors

* It does **not** claim any of these dollars exist today. Base A is $0 and that is the measured state.
* It does **not** claim the resulting PPM is reachable in month 1; that is the Month-13-onward steady state.
* It does **not** include sponsorships, which the plan excludes by decision D2, nor annual-refresh compounding beyond one cycle.

Three numbers in the plan itself are the pattern this review refuses to repeat:

1. `01-ai-data-documentary-part-06-of-06.md` computes an effective RPM of **$22.46** as $6 x 1.6 (geo) x 1.8 (mid-rolls) x 1.3
   (keyword seeding), then multiplies by a **0.55 fill-rate adjustment**. Four unmeasured multipliers compounded, then discounted
   by a fifth hand-picked number. None of the five is measured anywhere.
2. The branch document claims the intelligence layer adds **$400-600/day** with no derivation at all.
3. The same document claims "+80-100% CTR = 2x views", while part-05 states 2% vs 6% CTR is "500 lifetime views vs 50,000" - a 100x
   claim that cannot be linear. This review uses +20% views for a 3.0% to 3.6% CTR move instead.

The plan's Year-3 figure ($92,400/month, 2,500 videos at 220,000 views/day) is not reproduced here: it rests on 88 views per video
per day - inside the 40-94 range used here - and on $11 RPM, which is above the $7 used here.

## 8. The $1,500-$2,000/day of profit goal, measured against these numbers

PPM is revenue and the goal is profit, so there are two conversions, both fixed by this review rather than chosen here.
**$/day = PPM/month / 30**, and **revenue needed = profit goal + $85/month** of infrastructure (sec.0). The full 2-3 FTE stack is
priced in `IMPROVEMENT_VALUE_AT_2K.md` sec.1.4; the tables below use this review's own $85/month line, so they read as the solo case -
the only regime where this review's 900-video base is reachable without hiring.

**Why the floor moved.** The goal is **$1,500-$2,000 of profit per day** (`AGENTS.md` sec.1, `README.md` line 3, `docs/TRACKER.md`
line 4, `docs/ARCHITECTURE.md` line 3). Earlier printings of this section measured a lower bound on revenue rather than profit; that
bound is retired, and every percentage below is against the $1,500 floor or the $2,000 top of the profit range.

**That $85/month is infrastructure only.** `IMPROVEMENT_VALUE_AT_2K.md` sec.1.4 keeps this conversion and adds the 2-3 FTE labour
line: under the full stack profit is **93.0-95.3%** of revenue - **$1,394.86-$1,429.44/day** at $1,500/day and
**$1,894.86-$1,929.44/day** at $2,000/day, against $45,085-$60,085/month of revenue here. A per-month reading of the same wording was
considered and rejected in that memo's sec.1.5; it is not the target anywhere in this repository.

| Profit target | PPM/month needed | Revenue/month needed | Daily views at $7 RPM | at $9 | at $10 |
|---|---|---|---|---|---|
| $1,500/day | $45,000 | $45,085 | 214,690 | 166,981 | 150,283 |
| $2,000/day | $60,000 | $60,085 | 286,119 | 222,537 | 200,283 |

Views/day = revenue x 1000 / (30 x RPM). At the $1,500 floor and $10 RPM: 45,085,000 / 300 = 150,283 views/day.

### 8.1 The nine outcomes against the goal

| Base | Item case | PPM/month | $/day | % of $1,500/day | % of $2,000/day |
|---|---|---|---|---|---|
| measured today | - | $0 | $0 | 0% | 0% |
| 40 views/video/day | low | $10,054 | $335 | 22% | 17% |
| 40 views/video/day | likely | $12,410 | $414 | 28% | 21% |
| 40 views/video/day | high | $14,959 | $499 | 33% | 25% |
| 61 views/video/day | low | $15,365 | $512 | 34% | 26% |
| 61 views/video/day | likely | **$18,958** | **$632** | 42% | 32% |
| 61 views/video/day | high | $22,846 | $762 | 51% | 38% |
| 94 views/video/day | low | $23,713 | $790 | 53% | 40% |
| 94 views/video/day | likely | $29,249 | $975 | 65% | 49% |
| 94 views/video/day | high | $35,242 | $1,175 | 78% | 59% |
| **goal, solo** | $1,500/day of profit | $45,085 | $1,503 | 100% | 75% |
| **goal, solo** | $2,000/day of profit | $60,085 | $2,003 | 134% | 100% |

The percentages divide `$/day` by the profit goal itself; the revenue that profit needs is $1,502.83/$2,002.83 per day, so they
overstate progress by 0.2%.

So the answer to the goal is a band, not a number: **$632/day if the plan's own Month 13-16 rate and the likely
item case both hold, rising to $975/day at the Month 25-28 rate, and falling to $335/day if neither does.**
At 61 views/video/day the items deliver 42% of the $1,500/day floor; at 94 they deliver
65% of it and 49% of the $2,000/day top.

**The goal turns on one number, and it is the one the base now varies over.** At 94 views/video/day the twelve items reach
65% of the floor on their own; at 40 they reach 28% of it. No tracker item can move that number - only publishing can.

### 8.2 What it takes in videos x views-per-video x RPM

Revenue needed for the $1,500/day profit floor is $45,085/month. Growth required from each base, and the share the twelve items
supply in the likely case:

| Base | Revenue/month | Growth needed to $1,500/day | Items supply | Still missing |
|---|---|---|---|---|
| 40 views/video/day | $7,560 | 5.96x | 1.66x | 3.59x |
| 61 views/video/day | $11,529 | 3.91x | 1.66x | 2.36x |
| 94 views/video/day | $17,766 | 2.54x | 1.65x | 1.54x |

Videos needed = revenue x 1000 / (RPM x 30 x views per video per day). Months assume 30 videos/month from a 900-video library.

| Views/video/day | $7 RPM | $9 RPM | $10 RPM |
|---|---|---|---|
| 40 | 5,367 videos (149 months) | 4,175 videos (109 months) | 3,757 videos (95 months) |
| 61 | 3,520 videos (87 months) | 2,738 videos (61 months) | 2,464 videos (52 months) |
| 94 | 2,284 videos (46 months) | 1,776 videos (29 months) | 1,599 videos (23 months) |

For $2,000/day multiply every cell by 1.33. At 900 videos the $1,500/day floor needs **239 views per
video per day at $7 RPM** (214,690 / 900), **186 at $9** (166,981 / 900) and
**167 at $10** (150,283 / 900).

### 8.3 The plan's own tables disagree on that number

| Source | Views per video per day it implies |
|---|---|
| `branches.md` projection, Month 7-9 (10,000 / 450) | 22 |
| `branches.md` projection, Month 13-16 (55,000 / 900) | 61 |
| `branches.md` projection, Month 25-28 (170,000 / 1,800) | 94 |
| ARCHITECTURE Phase 1 mid-point (20,000 / 110) | 182 |
| ARCHITECTURE Phase 2 mid-point (65,000 / 300) | 217 |
| ARCHITECTURE Phase 3 mid-point (130,000 / 725) | 179 |
| ARCHITECTURE Phase 4 mid-point (230,000 / 1,000) | 230 |

Twenty-two to two hundred and thirty is a tenfold spread on the single input that decides whether $1,500/day of profit arrives in month
25 or never, and the two tables sit 2-4x apart from each other. This review ranges over 40-94 - the projection table's own span - which
is the defensible part of the plan's evidence. **No repository file measures it, because nothing has been published.**

### 8.4 Verdict against the goal

The best single item, `THM-01`, is worth $2,306/month ($77/day) at the likely base and
$9,017/month ($301/day) once the channel earns $1,500/day of profit - the same percentage, 3.9 times the money.
All twelve together reach $18,958/month ($632/day).

* At **61 views/video/day** - the plan's own Month 13-16 rate - the floor needs 3.91x the revenue, of which the items
  supply 1.66x. That is $632/day, 42% of the floor.
* At **94** - the plan's Month 25-28 rate - the items nearly close it: $975/day, 65% of the floor.
* At **40** - this review's floor - the same items reach $414/day, 28% of it.

Two things are therefore true at once. The goal is a views-and-RPM problem that the tracker only multiplies - no item, alone, moves
it. And the multiplier is worth having at any base: `THM-01` is $50/day at 40 views/video/day, $77/day at 61, and $118/day at 94,
before a single extra video exists. The cheapest honest next step is still not one of the twelve: it is `ANA-01`, which replaces the
whole 40-94 axis with a measured number after 30 published episodes - at $0/month of PPM.
