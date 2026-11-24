# Decision Audit — every number in `DECISIONS.md`, re-derived

> **Purpose.** `DECISIONS.md` is the document that authorises spending. A decision record whose arithmetic is taken on trust is
> worse than no record, so every numeric claim in it was recomputed from first principles and from `tracker/items.json`.
> **Result: 12 decisions audited, 5 defects found and fixed, 155 assertions now run on every push.**

Reproduce the whole audit with:

```bash
python3 scripts/check_decisions.py      # the decisions, re-derived
python3 scripts/check_baseline.py       # the inputs, banded and re-derived
```

Round 2 (below, §6) audits the *inputs* the decisions rest on, and is what produced [`BASELINE.md`](BASELINE.md).

That script is not a description of this file — it is the check this file reports on, wired into `scripts/check_docs.py` and CI.

---

## 1. What was recomputed, and against what

| Source of truth | Used for |
| :--- | :--- |
| `IMPROVEMENT_VALUE_AT_2K.md` 1.1–1.4 constants (78% ad share, $10.50 RPM, $2.64/day of infra cost, $1,500/day of profit) | every revenue and arrival figure |
| `tracker/items.json` (60 items, 166.5h) | every effort, count and enforcement claim |
| `docs/SPRINT_30_DAYS.md` gate rows | the two rates (155 and 103) the whole cadence decision rests on |
| `git show 2f24056:docs/SPRINT_30_DAYS.md` (the pre-decision slate) | D-03's *measured* claims — the only measured numbers in the record |
| `PPM_REVIEW.md` G5 column | the localization figures D-05 quotes |

---

## 2. Decision-by-decision audit

| ID | Claim as written | Recomputed | Verdict |
| :--- | :--- | :--- | :--- |
| **D-01** | 24-month path needs v = **155** | 1,170 × 1000 ÷ (24 × 30 × 10.5) = **154.76** | ✅ valid |
| **D-01** | 36-month path needs v = **103** | 1,170 × 1000 ÷ (36 × 30 × 10.5) = **103.17** | ✅ valid |
| **D-01** | 1,827 videos = **61 months** at 30/mo, **24 months** at 75/mo | 60.9 and 24.4 | ✅ valid |
| **D-01** | $1,500/day of profit lands "month **26–32**" | simulating the ramp: month **28** at v=61, 23 at v=80, 34 at v=50, **41** at v=40 | ⚠️ **defect — band understated the downside; now "month 23–41, centre 28"** |
| **D-02** | `VAL-01` is **6h**, against T06's **31.5h** | VAL-01 = 6.0h; T06 was 31.5h and is 36.0h now (SHR-01, REN-10 added) | ⚠️ **defect — stale figure; now dated "31.5h when decided, 36.0h now"** |
| **D-03** | **21 of 30** titles carried the format label | 21 contain it, **20 begin with it** (`EP18` uses it mid-title) | ⚠️ **defect — imprecise; wording corrected in both docs** |
| **D-03** | **24 distinct pillars**, largest 3, top-3 = 8, longest title 58 chars | 24, 3, 8, 58 — all exact | ✅ valid |
| **D-04** | 51 → 56 items, 142.0h → 157.5h | five items sum to **15.5h**, 142.0 + 15.5 = 157.5 | ✅ valid |
| **D-05** | +$202 / $307 / $474 of PPM arithmetic for `PUB-02` | matches the G5 low column in `PPM_REVIEW.md` | ✅ valid |
| **D-06** | Facebook is ~15% of the plan's revenue | G4 in `PPM_REVIEW.md` is +15% of ad revenue = $176–$234/day | ✅ valid |
| **D-07** | 30 episodes at $0.30 of cost each stays inside the plan's LLM line | 30 × 0.30 = **$9.00** against the plan's $10 line | ✅ valid |
| **D-09** | hired voice at "roughly **$15–$40** of cost per episode" | 1,550–2,790 words × $0.02–$0.05/word = **$31–$140** | ⚠️ **defect — invented band, 2–4x too low; now derived from word count × rate** |
| **D-10** | dilution is **1,830 views/day = +3.3%/month** | 30 × 61 = 1,830; 30 ÷ 900 = 3.33% | ✅ valid |
| **D-10** | **111,600 views/day** at 720 videos; **4,650** at 30 videos | 720 × 155 = 111,600; 155 × 30 = 4,650 | ✅ valid |
| **D-10** | a 30-video launch reads **0.6–17.9** | 500 ÷ 30 ÷ 28 = 0.60; 15,000 ÷ 30 ÷ 28 = 17.86 | ✅ valid |
| **D-10** | the goal implies **1.9–2.8M impressions/day** | 111,600 ÷ 6% = 1.86M; ÷ 4% = 2.79M | ✅ valid |
| **D-11** | a 5-video pillar reads **32–118**, a **3.7x** span | 61 × exp(±1.64 × 0.9/√5) = 31.5–118.0; 3.74x | ✅ valid (σ is labelled an assumption) |
| **D-12** | 4K60 is **2.25x** the pixels | 8.29M ÷ 3.69M = **2.25** | ✅ valid (prose said 2.2x in one place — corrected) |
| **D-12** | "roughly **30h** of the original T06 spend moves behind evidence" | only **2h** (`REN-10`) is deferred; 34 of T06's 36h are needed at 1440p too | ⚠️ **defect — inflated 15x; replaced with the real 2h + the running saving** |
| **D-12** | "episodes ship **three weeks earlier**" | not derivable from any schedule in the repo | ⚠️ **defect — unsupported; removed** |
| **D-12** | **5.6–9.7** fewer GPU-hours a month | (20 − 20/2.25) × 30/60 = 5.6; (35 − 35/2.25) × 30/60 = 9.7 | ✅ valid |
| **D-02/05/06/08** | each decision is enforced in an acceptance criterion or a dependency | all eight gates present in `tracker/items.json` | ✅ valid |

---

## 3. The five defects, and what they had in common

| Defect | Direction of error | Why it mattered |
| :--- | :--- | :--- |
| D-01 arrival band "26–32" | **optimistic** — the v=50 case is month 34, the v=40 case month 41 | would have read a late but normal outcome as a failure |
| D-09 voice cost `$15–$40` | **optimistic by 2–4x** | the human-voice fallback looked cheap enough to be a non-decision |
| D-12 "~30h of T06 deferred" | **optimistic by 15x** | the headline saving for the biggest scope cut was arithmetic that did not exist |
| D-12 "three weeks earlier" | unsupported | a schedule claim with no schedule behind it |
| D-03 / D-02 figures | stale or imprecise | measured claim reduced to "about right", which is how measured claims decay |

Four of the five erred in the same direction: **the case for the decision looked better than the numbers support**. That is the
failure mode a decision record must be audited for, and it is why `check_decisions.py` asserts the *corrected* strings — the
inflated claims cannot return without CI failing.

A sixth, structural inconsistency surfaced during the audit: **D-11 superseded D-03's six-pillar spread but the `TOP-01`
acceptance criterion and `ARCHITECTURE.md` Module 1 still prescribed 6x5.** A decision that is only in the decision document is
not a decision. Both now say one cluster, 30 deep, and the check asserts it.

---

## 4. What this audit cannot validate

Every figure above is *internally* consistent. None of the following is measured anywhere in this repository, and no amount of
re-derivation fixes that:

| Input | Value used | Retired by |
| :--- | :--- | :--- |
| views per video per day (v) | 61 | `ANA-01` with 28 days of trailing data |
| blended RPM | $10.50 | AdSense report after YPP |
| ad share of revenue | 78% | first month of earnings data |
| US-origin share | 40% | Analytics geography |
| log-normal view spread (σ) | 0.9 | the first 30 episodes' own distribution |
| 4K60 render minutes per episode | 20–35 | `REN-02` benchmark |
| GPU rate | $0.33–$0.58 per hour | the first invoice |
| word rate for hired voice | $0.02–$0.05 | one quote |
| approval/QA hire | ~$700 of labour cost per month | one offer letter |

**The honest summary:** the arithmetic is now sound, and the *inputs are still guesses*. That is not a defect in the record — it
is the reason `VAL-01`, `TOP-04` and the Day-45 gate exist. The first three items on that list are replaced by measurement within
45 days; the rest arrive with the first payout.

---

## 5. How the audit stays true

| Guard | Catches |
| :--- | :--- |
| `scripts/check_decisions.py` (155 assertions) | any drift between `DECISIONS.md` and the constants or the tracker; every corrected claim returning |
| `scripts/check_memo.py` (154 assertions) | the `IMPROVEMENT_VALUE_AT_2K.md` baseline that `DECISIONS.md` reads from |
| `scripts/check_goal.py` (184 assertions) | a monthly figure restated as a target; an unqualified daily band |
| `scripts/track.py validate` | a dependency gate that stops being a gate (D-02, D-12) |
| `scripts/selftest_track.py` / `selftest_goal.py` | those checks going quiet — a planted violation must still fail |

---

## 6. Round 2 — auditing the inputs, not just the arithmetic

The first five rounds audited claims about numbers. They could not audit the numbers themselves, because nine of them were guesses.
Round 2 turned each guess into a tier in [`BASELINE.md`](BASELINE.md), and found three defects in the process.

| Defect | What was wrong | Consequence |
| :--- | :--- | :--- |
| **"RPM" carried two meanings** | the memo's `RPM` is **ad-side** (it divides by 0.78 afterwards); `ARCHITECTURE.md`'s "$8–$16 RPM" reads as **total**. 28% apart, same word | `RPM_ad` is now the named quantity, banded **$6.24–$12.48**; $10.50 is registered at the **68th percentile**, i.e. mid-band, not conservative |
| **The GPU line paid for a window the pipeline does not use** | $20–35 of cost per month provisioned 2 h/day = 60 GPU-hours; the SLA implies **5.4–9.8h** at 1440p60 | the worker is metered per episode: **$2.18–$3.91** of cost per month, $6.53–$11.73 at 3x retries. The provisioned line was 6–11x the need |
| **σ = 0.9 was an assumption inside an argument about assumptions** | `D-11`'s "five videos cannot be read" rested on an assumed log-normal spread | **σ is retired.** The exact Mann-Whitney bound is distribution-free: significance needs **23 of 25** cross-pairs ordered correctly (U ≤ 2, p = 0.0317; U ≤ 3 gives 0.0556 and is not significant) |

**What the audit still cannot do.** No procedure inside this repository can validate v, `RPM_ad`, the US share, the render minutes
or the word rate. Round 2's contribution is not that those are now known — it is that each one is **tiered, banded, given a
retirement instrument, and wired to a decision rule (R1–R12) written before the data arrives**. A guess with a pre-registered
decision attached is a manageable business; a guess with a decision made afterwards is a rationalisation.

**Two numbers the register changed.** The reachable library is **1,830** videos at (v = 61, `RPM_ad` = $10.50) but **4,186** at the
band's floor (40, $7) — 2.3x the library, 56 months at 75 videos a month rather than 24. And the ~$100/month cap now has
**$16–$31 of headroom** of cost, which is earmarked in `BASELINE.md` §3 for the approval/QA hire rather than a bigger GPU window.
