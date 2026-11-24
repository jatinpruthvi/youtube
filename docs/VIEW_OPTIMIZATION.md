# View Optimization — Every Lever, Specified

> **Mission:** **$1,500–$2,000/day of profit** (`AGENTS.md` §1). This document is the engineering specification for the
> **views** side of that equation. The money side is priced in [`PROFIT_MULTIPLIERS.md`](PROFIT_MULTIPLIERS.md) and
> [`IMPROVEMENT_VALUE_AT_2K.md`](IMPROVEMENT_VALUE_AT_2K.md); every $/day figure quoted here is the same figure, derived the
> same way (`V x v x RPM / 1000`, V = 1,827, v = 61, RPM = $10.50). The section 14 table mirrors the rows of
> [`PROFIT_MULTIPLIERS.md`](PROFIT_MULTIPLIERS.md), which `scripts/check_memo.py` pins to that baseline.

**Status: adopted as decisions, nothing built.** `DECISIONS.md` D-03 and D-05 turn this document's two structural
recommendations into tracker acceptance criteria (the 6-pillars-x-5 query-shaped slate, and captions before localized metadata);
the rest remains specification. No item below has been implemented, and every input marked *(assumption)* still has no measurement
anywhere in this repository.

---

## 0. The law, and the four kinds of lever

```
views      = impressions shown  x  click-through rate
impressions = f(predicted satisfaction: watch time, likes, surveys, history)
revenue/day = V x v x RPM / 1000 + ancillary          (IMPROVEMENT_VALUE_AT_2K 1)
```

Impressions are not bought with metadata; they are earned by the system predicting that a viewer will be satisfied. So every
lever in this document is exactly one of four things:

1. **More surfaces** — the same asset reachable from more places (languages, Shorts, Facebook, external).
2. **A better click** — title and thumbnail.
3. **A longer stay** — hook, pacing, structure, session bridging.
4. **A stronger topic** — demand, freshness, angle.

Each lever below is tagged with which of the four it moves, because most "more views" advice is a surface lever sold as a
retention fix.

---

## 1. What the repository's own slate shows (measured, not assumed)

| Reading | Value | Where it comes from |
| :--- | :---: | :--- |
| Titles beginning "Every Country Ranked by …" | **21 of 30** | `SPRINT_30_DAYS.md` title column |
| Distinct pillar labels across 30 episodes | **24** | pillar column |
| Videos in the largest single pillar | **3** (10%) | pillar column |
| Videos in the top three pillars | **8 of 30** (27%) | pillar column |
| Longest working title | **58 chars** (limit 60) | title column |
| Near-duplicate theses | **4 pairs** | EP02/EP16, EP03/EP10/EP29, EP01/EP09/EP24, EP08/EP12 |

Two failures at once: **too narrow in phrasing** (one template label repeated 21 times is a format, not a query) and **too
broad in subject** (24 topics means ~1.25 videos of evidence per topic, which the recommender cannot learn from and which
makes every 28-day reading unreadable as a measurement).

---

## 2. Topic selection — the dominant variable

### 2.1 The scorer is weighting production convenience as demand

`ARCHITECTURE.md` §3 Module 1 used to score topics as `0.30(search demand) + 0.25(CPM) + 0.25(API data richness) + 0.20(curiosity gap)`.
"API data richness" answers *can I make this easily?* — a filter, not a demand signal. **Adopted** (`DECISIONS.md` D-03), and
`ARCHITECTURE.md` now carries the reweighted formula:

| Component | Weight | Input | Source |
| :--- | :---: | :--- | :--- |
| Proven demand | 50% | top-3 competitor views/day for the query | `TOP-02` outlier miner |
| Auction value | 25% | niche CPM band | `TOP-03` |
| Angle novelty | 25% | can this episode say something the top 3 did not | editorial |
| Data verifiability | **filter** | can every number trace to a frozen snapshot row | `DAT-01`…`DAT-07` |

### 2.2 The stale-result test (refresh gap)

Search is the only surface where a zero-subscriber channel can rank. Where the top results are old, a new video wins on
freshness, cited sources and 4K clarity. Per candidate query, record the top 3 results and score:

```
refresh_score = median(top-3 views/day since publish) / years_since_publish
```

High score + top results older than ~2 years = build it. Low score + recent top results = skip. Budget: 10 minutes per topic, no
API. This replaces the "curiosity gap" guess with an observation.

### 2.3 Entity long tail, editorially

Country-level content is where the long tail lives, but "Every Country Ranked by X — Germany" is the repetition trap
`ARCHITECTURE.md` §3 Module 10 is written to avoid. The rule is **one dataset, many questions; never one template, many
countries**. "Why Germany's wages flatlined while its GDP did not" is editorial and captures the national query.

### 2.4 Barbell portfolio

80% proven-query evergreen (compounding, boring), 20% high-variance bets (occasional 10x). Kill rule: 28 days, compared
against the channel's own median for that pillar — never against day-3 numbers.

---

## 3. Packaging — the click

### 3.1 Title

Rules: the query as a person types it; ≤60 characters; the first ~40 characters carry the promise (mobile truncates);
one specific number; no format label. Worked examples from the existing slate:

| Current | Query-shaped rewrite | Chars |
| :--- | :--- | :---: |
| Every Country Ranked by Real Average Salary | Average Salary by Country (2026): Take-Home Pay | 51 |
| Every Country Ranked by Minimum Wage vs Cost of Living | Minimum Wage vs Cost of Living: 30 Countries | 45 |
| How $1,000 in Purchasing Power Looks in 50 Countries | What $1,000 Buys in 50 Countries | 33 |
| Every Country Ranked by Savings Rate (Who Saves Most?) | Who Saves Most? Savings Rate by Country | 37 |

### 3.2 Thumbnail

Three distinct angles per episode (`THM-01`): map contrast, flag showdown, outlier spike. Verify legibility at 168x94 px
(`THM-02`). **Test & Compare is Studio-only** — there is no API for it — so the approval bot (`QAG-02`) is the correct place to
launch the test. Critically, the test selects on **watch-time share, not CTR**: a variant that wins clicks and loses retention is
a loss. Track the winner, not the CTR.

### 3.3 Coherence

Title and thumbnail must not say the same words. The thumbnail carries the number and the subject; the title carries the
promise and the query. Two restatements of one idea waste one of the two surfaces.

---

## 4. Metadata, field by field

| Field | What it actually does | Verdict |
| :--- | :--- | :--- |
| Title | Earns the click and matches the query | **High** — §3.1 |
| Thumbnail | Largest single lever on any video | **Highest** — §3.2 |
| Description, first ~100 chars | Search snippet, "…more" teaser | Keep, cheap |
| Description, body | Almost nothing except chapters | Low effort only |
| Chapters | Navigation, key-moments in search, retention recovery | **Keep** |
| Tags | Downplayed by YouTube's own documentation | ~Nil |
| Hashtags | Three maximum, marginal | ~Nil |
| Localized title/description | Search presence in a language the video is not *in* | Low alone — see §7 |
| Localized audio track | Unlocks the recommender in that language | **High** — §7 |
| Captions / SRT | Accessibility plus non-English search, effectively free | Keep |
| Publish time | Matters for news, not evergreen data | Low |
| Playlist / series slot | Small per video, compounds across a library | Keep |

---

## 5. Retention — what buys the next impression

1. **0:00–0:10 viewer's own rank.** Name the country the viewer is most likely in and its position, then the change since a
   prior year. Self-relevance in second three is the cheapest retention available, and it is a *template parameter*, not new
   production work — the number comes from the `DataBrief`, the flag from `dim_countries`.
2. **0:10–0:35 contrast and open loop.** Two-country provocation with a visible data reveal, then the promise of the inversion.
3. **1:30–end acts, with a pattern interrupt every 45–60 s** (already specified in `ARCHITECTURE.md` §3 Module 3).
4. **End-screen bridge to one named next video**, not "subscribe" — session time is the channel-level signal that decides how
   many impressions the *next* upload gets.
5. **Satisfaction guardrail.** Post-watch surveys are a named ranking input. Bait packaging that spikes CTR and tanks AVD and
   surveys reduces future impressions; the source overlay (`Source: World Bank / OECD · Year`) and original causal analysis are
   the trust assets, so package the promise the video actually keeps.

---

## 6. Surfaces, one playbook each

| Surface | What it rewards | Your lever | Metric |
| :--- | :--- | :--- | :--- |
| Search | query match, freshness, chapters | query-shaped title, current-year data, chapter timestamps | impressions → CTR |
| Suggested / browse | similarity to the last video watched | series structure, end-screen bridge, playlist | session duration |
| Home | channel affinity and past satisfaction | topical concentration (§1) | impressions per upload |
| Shorts feed | 1.5-second retention, loopability | climax clip with the Related-video link | swipe-away rate |
| External | a reason to click off-platform | dataset, notebook and SVG charts per episode | traffic-source report |
| Facebook In-Stream | muted-first autoplay | 3-second kinetic hook card, burned captions | 3-second views |

Optimising "YouTube" as one thing usually means optimising one of these six and calling it the platform.

---

## 7. Languages — surfaces multiplied by audience

1. **Multi-language audio, not just localized text.** YouTube's native feature accepts extra audio tracks on **already
   uploaded** videos and supports per-language thumbnails on long-form. Localized title and description alone give a Spanish
   viewer a Spanish thumbnail over English narration — a bounce that feeds the satisfaction signal. Only localize a market where
   you also ship audio, or at minimum captions, in that language.
2. **Automation gap.** The public Data API documents localized titles, captions and thumbnails, but **not** audio-track upload;
   an Audio Tracks API exists in a restricted pilot with no open application. Treat dubbing as a Studio step inside the human
   approval gate until that changes. YouTube's automatic dubbing may cover some channels at no pipeline cost — check eligibility
   in Studio before building anything.
3. **Order by RPM, not population.** `PPM_REVIEW.md` sec.0 prices each market as an index of the English RPM: `de` 0.65, `fr` 0.50,
   `ja` 0.45 against `es-419` 0.30, `pt-BR` 0.20 and `hi` 0.12. A `de` view is worth 1.4x an `es-419` view and 2.4x a `hi` view, so
   a reach market has to out-deliver that multiple before it is worth a dub minute. **The revenue set is de/fr/ja** - metadata and
   SRTs, blended at $3.73 per 1,000 against $7 English; **es-419, pt-BR and hi get captions only** and carry no revenue claim;
   **`ar` is dropped.** `ko` and `nl` sit close to `fr`/`ja` on the same estimates and are the next candidates, added on a measured
   margin test rather than on population. Cost is small: Azure Neural TTS is already the non-English fallback in `ARCHITECTURE.md`
   §3 Module 4 at roughly $0.20 per 12-minute video *(assumption, list price)*.
4. **Tier-1 KPI tension.** `SPRINT_30_DAYS.md` asks for ≥55% Tier-1 audience; adding low-RPM geos works against that number.
   Decide which one is the goal before measuring either.

---

## 8. Shorts — two jobs, not one

1. **Funnel.** A 45–60 s vertical cut with the native **Related-video** link attached, published a couple of hours after the
   long form. Use the **climax**, not the hook: the surprise inversion at ~11:30 is a payoff, and payoff clips convert scrollers
   better than trailers. 2%–5% conversion *(assumption)* on 20,000 Shorts views is 400–1,000 long-form viewers, worth
   $4.20–$10.50 of ad revenue per episode at $10.50 RPM.
2. **Topic probe.** The same 45-second render answers "does anyone want this subject?" for ~5 minutes of compute, *before* a
   14-minute episode is produced. Read 72 hours; green-light or drop. That makes the Shorts pipeline the cheapest market research
   the factory has.

Shorts are identified by aspect ratio and duration, so the `#Shorts` tag is not the mechanism; the Related-video field is the
tap-through and it is Studio-only.

---

## 9. Scheduling against the data, not the calendar

World Bank WDI, OECD tax wedge, IMF WEO and national CPI series all publish on known dates. The video that publishes in the week
a number changes has a defensible "new" hook — the story is the change, not the ranking — without duplicating its own library.
`ANA-03` refreshes annually; aligning that refresh to release dates is where the search spike actually is.

---

## 10. Make the dataset a distribution asset

Every episode already produces a frozen snapshot, a Fact-ID ledger and vector chart exports. Publishing them (SVG/PDF/notebook,
one page per episode, linked from the description) is what earns Wikipedia citations, data-visualisation threads, teacher embeds
and newsletter mentions — warm external traffic on launch day, when early engagement matters most. The artifacts are by-products;
the cost is hosting, not production.

---

## 11. The back catalogue is a lever too

Unlike packaging rules that only touch new uploads, a repackaging pass acts on every video already published. Rank the library by
impressions, rewrite titles and regenerate thumbnails for the top decile, and run Test & Compare on the biggest ones (Studio).
A doubled click rate on 10% of the library is worth +$117/day at the baseline; more importantly it re-tests old videos the system
had stopped showing.

---

## 12. Cadence

YouTube does not list upload frequency among the ranking signals it describes. The 30-in-30 sprint is a **coverage** device —
it produces measurement quickly — and a mediocre growth device: 30 uploads in 30 days splits one small impression pool 30 ways and
gives each video less time to be re-tested. For compounding, 3–5 uploads a week with packaging iteration on the previous week's
data is the better bet *(inference, not a published rule)*. Consistency matters to humans, not to the ranker.

---

## 13. Measurement that survives noise

Per video, weekly: impressions, CTR, AVD %, watch-time share, traffic-source split, views at day 7 / 28 / 90, RPM and geo mix.
Re-rank topics only on **revenue per 1,000 impressions**.

Two traps:

1. **Arm tests need volume.** With per-video views varying ~60%, a 10-videos-per-arm test detects only a ~54% difference; 40/arm
   detects 27%, 70/arm detects 20%. Early on, use per-video Test & Compare and within-subject before/after instead of arms.
2. **Launch rate is not steady state.** A growing library decays per video (`IMPROVEMENT_VALUE_AT_2K.md` §4(b)). At video 30 every
   video is inside its launch window, so the video-30 gate in `SPRINT_30_DAYS.md` (155 and 103 views/video/day for the 24- and
   36-month paths at $10.50 RPM) reads a **launch rate**. If steady state is half of launch, the gate needs ~2x headroom
   *(assumption: the decay ratio is unmeasured; `ANA-01` supplies it after 28 days of history)*.

---

## 14. Priced levers

All at V = 1,827 videos, v = 61 views/video/day, RPM = $10.50 → $1,170/day of ad revenue at the $1,500 profit goal
($1,560/day at $2,000). The rows are the same arithmetic pinned in `PROFIT_MULTIPLIERS.md` by `scripts/check_memo.py`; they are
**not additive**, because each is measured against the same baseline and RPM and CTR share the same views.

| Lever | Gain | Derivation | Assumption |
| :--- | :--- | :--- | :--- |
| RPM $10.50 → $14–$16 (mid-roll density) | **+$390–$613/day** | 1,827 x 61 x (14 or 16 - 10.50) / 1000 | impressions per view 1.2 → 2.8 |
| Ancillary 22% of revenue | **+$330–$440/day** | 0.22 x 1,500 / 0.22 x 2,000 | plan's ancillary rows materialise |
| CTR +20% everywhere | **+$234–$312/day** | 0.20 x 1,170 / 0.20 x 1,560 | a thumbnail change delivers +20% relative CTR |
| Library +10% (182 videos) | **+$117/day** | 0.10 x 1,170 | new videos behave like the average |
| Back-catalogue top decile doubled | **+$117/day** | 0.10 x 1,170 | a repackaged video doubles its views |
| W-8BEN withholding | **+$70/day** | 1,170 x 0.40 x 0.15 | 40% US-origin share |
| Shorts funnel | **+$4.20–$10.50 per episode** | 400–1,000 views x 10.50 / 1000 | 2%–5% conversion |
| Packaging 2x on new uploads, 30/month | **+$38 → +$461 → +$922/day** | at 1, 12 and 24 months of library growth | 2x on new uploads only |

---

## 15. Assumption register

| Assumption | Where it is used | How to measure | Status |
| :--- | :--- | :--- | :--- |
| v = 61 views/video/day | every $/day figure | `ANA-01` trailing 28 days | plan projection (`IMPROVEMENT_VALUE_AT_2K` 1.2) |
| RPM = $10.50 blended | every $/day figure | AdSense report | plan projection |
| Hits-per-view 1.2 → 2.8 | mid-roll lever | `playbackBasedCpm` before/after | unmeasured |
| +20% relative CTR | packaging lever | Test & Compare (watch-time share) | unmeasured, called weakest by `PPM_REVIEW` |
| 40% US-origin views | withholding lever | Analytics geography | unmeasured |
| 2%–5% Shorts conversion | Shorts funnel | traffic sources on the long form | unmeasured |
| ~$0.20 per 12-minute dub | language cost | Azure invoice | list price |
| Launch : steady-state decay ratio | video-30 gate | `ANA-01` day 7/28/90 | unmeasured |
| Cadence is not a ranking signal | §12 | none available | inference from YouTube's documented signals |

---

## 16. Build order

1. `TOP-02` stale-result miner (§2.2) and `TOP-03` re-weighting (§2.1) — topic is the dominant term.
2. `THM-01` / `THM-02` packaging, launched through the `QAG-02` approval bot because Test & Compare has no API (§3.2).
3. Hook parameterisation: viewer's own rank in 0:00–0:10, per language track (§5.1, §7).
4. `ANA-01` with traffic-source split and day 7/28/90 views, so the decay ratio exists (§13).
5. Language audio on the ten best-performing videos, high-RPM markets first (§7).
6. Shorts: climax clip with the Related-video link, plus one probe per candidate topic (§8).
7. Dataset and SVG publication page per episode (§10).

---

## 17. What actually moves views per video, ranked

`v = views / videos` is a **ratio**, so it is improved only by adding views, removing videos, or raising views faster than the
library grows. That single fact reframes most of this document:

```
hold v=61 while adding 30 videos to a 900-video library
    -> total views must rise by 30 x 61 = 1,830/day per month = +3.3%/month
    -> adding library is not a v lever, it is a v tax unless demand grows with it
```

At 30 videos the same arithmetic is brutal: adding 30 more doubles the denominator in one month, so **the library has to double its
totals just to stand still**. This is why the video-30 gate (`SPRINT_30_DAYS.md`) reads the trend, not the level — a level reading
at 30 videos is a launch-cohort number (0.6–17.9), not a library-scale one (103–155).

| # | Mechanism | Why it moves v | Evidence class | Cost | Already an item? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Query selection with a freshness gap** | At zero subscribers, search is the only surface a new channel ranks on, so impressions exist only where the query has volume. Decided before production, free to change | measured on the slate (21/30 were format labels, §1); effect size assumed | 10 min per episode | **No** — `TOP-04` added (`DECISIONS.md` D-10) |
| 2 | **Topical concentration** | Browse and suggested are where volume lives above search, and they recommend within a cluster. A 5-video pillar reads 32–118 at 90% confidence, so six of them produce six unreadable numbers | mechanism documented by YouTube; the interval is arithmetic | a decision, not work | **Yes** — `D-11`: one cluster, 30 deep, from Day 1 |
| 3 | **Packaging (title + thumbnail)** | Converts impressions that exist into views. Cannot create impressions, so it is second, not first | +20% relative CTR assumed, never measured here | 3h + 1.5h | Yes — `THM-01`, `THM-02` |
| 4 | **Satisfaction / retention** | Decides *future* impressions, which is the only compounding term in the system. Bait packaging that spikes CTR and loses AVD is a net loss (§5.4) | mechanism documented; effect assumed | pacing linter 2h | Yes — `SCR-04`, plus the source overlay |
| 5 | **Surfaces: languages, Shorts, Facebook** | Adds views from a different pool without adding library, so it raises v directly | Shorts 2%–5% conversion assumed; non-EN RPM is an index assumption | `SHR-01` 2.5h, `PUB-02` 3h | Partly — `SHR-01`, `PUB-02`, `ANA-04` |
| 6 | **Refresh waves on published episodes** | Re-renders an episode whose dataset updated: new search wave, **same library**, so v rises with no dilution. The only lever that is purely a v lever | decay-to-refresh wave assumed; the annual data cycle is measured | `ANA-05` 2.5h | **No** — `ANA-05` added (`D-10`) |
| — | **Session bridging (playlists, series slot, end-screen bridge)** | Session time is the channel-level signal that allocates the *next* upload's impressions | mechanism documented; effect assumed | 2.5h | **No** — `PUB-04` added (`D-10`) |

**Three consequences.**

1. **Most of the tracker cannot move v, by construction.** Rendering, QC, orchestration, audio mastering and the data warehouse
   protect v (they stop a bad upload or a strike) but they do not raise it. `PPM_REVIEW.md` already says this: 45 of 60 items do not
   move PPM at all.
2. **The cheapest v levers are research and decisions, not code** — queries, concentration, refresh. That is why `TOP-04` is a
   gate that costs 10 minutes per episode rather than another pipeline module.
3. **Every effect size in the table above except the measured slate reading is an assumption.** The honest position stays: v is
   unmeasured until `ANA-01` has 28 days of data, and no item in this repository has ever demonstrated a lift.
