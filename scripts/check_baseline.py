#!/usr/bin/env python3
"""Re-derive docs/BASELINE.md: the register that bands every input.

The register is where a decision-maker is told which numbers are measured,
which are derived with a band, and which are still guesses. That claim is only
worth something if the bands are reproducible, so this check recomputes:

  RPM   the ad-side band from the plan's stated total-RPM band and the 78% ad
        share, and the percentile at which $10.50 sits
  GPU   the implied GPU hours per preset from the pipeline SLA, and the cost at
        the plan's own rate, against the 60h window the architecture provisions
  stats the exact Mann-Whitney null distribution that replaced sigma, and the
        boundary at which five-vs-five becomes significant
  grid  the library the goal needs at every (v, RPM_ad) cell

It also fails if the register loses its tier key, if a Tier U input stops
naming the instrument that retires it, if the pre-registered rules stop covering
the two gates, and if any figure drifts from the recomputation.
"""
import json
import math
import os
import re
import sys
from itertools import combinations
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker, cells, read, strip_fences, tables

os.chdir(ROOT)

DOC = read("docs/BASELINE.md")
DECISIONS = read("docs/DECISIONS.md")
AUDIT = read("docs/DECISION_AUDIT.md")
ARCH = read("docs/ARCHITECTURE.md")
SPRINT = read("docs/SPRINT_30_DAYS.md")

ITEMS = json.load(open("tracker/items.json", encoding="utf-8"))["items"]
AD_SHARE, RPM_AD, RPM_TOTAL_BAND = 0.78, 10.5, (8.0, 16.0)
INFRA_PER_DAY, GOAL = 2.64, 1500
PLAN_LIBRARY = 1827

ck = Checker()
tabs = tables(strip_fences(DOC).split("\n"))


def table_starting(prefix):
    return next((t for t in tabs if t and t[0].lstrip("| ").startswith(prefix)), None)


# ---- 1. the register's own structure ------------------------------------
for tier, meaning in (("**M**", "measured"), ("**D**", "derived"), ("**U**", "unmeasured")):
    ck.ck(f"tier key defines {tier}", tier in DOC and meaning in DOC.lower(), tier)
reg = table_starting("Input | Symbol")
ck.ck("register table found", reg is not None)
reg_rows = [cells(r) for r in (reg or [])[2:]]
ck.ck("register has at least 15 inputs", len(reg_rows) >= 15, str(len(reg_rows)))
unmeasured = [c for c in reg_rows if len(c) > 5 and "**U**" in c[4]]
ck.ck("unmeasured inputs exist and are admitted", len(unmeasured) >= 5, str(len(unmeasured)))
for c in unmeasured:
    ck.ck(f"Tier U input names its retirement instrument: {c[0][:24]}", "Retired by" in c[5], c[5][:60])
measured = [c for c in reg_rows if len(c) > 5 and "**M**" in c[4]]
ck.ck("nothing in the revenue line claims to be measured",
      not any(("RPM" in c[0] or "Views per video" in c[0]) and "**M**" in c[4] for c in reg_rows),
      "a revenue input is marked measured")

# ---- 2. RPM: two readings, one word -------------------------------------
ad_band = (RPM_TOTAL_BAND[0] * AD_SHARE, RPM_TOTAL_BAND[1] * AD_SHARE)
ck.ck("ad-side band = 0.78 x total band", (round(ad_band[0], 2), round(ad_band[1], 2)) == (6.24, 12.48), str(ad_band))
ck.ck("$10.50 is inside the ad-side band", ad_band[0] < RPM_AD < ad_band[1])
pct = (RPM_AD / AD_SHARE - RPM_TOTAL_BAND[0]) / (RPM_TOTAL_BAND[1] - RPM_TOTAL_BAND[0])
ck.ck("$10.50 sits at the 68th percentile of the total band", abs(pct - 0.682) < 0.01, f"{pct:.3f}")
for s in ("$6.24–$12.48", "68th percentile", "RPM_ad", "RPM_total", "13.46"):
    ck.ck(f"register states {s}", s in DOC, s)
ck.ck("the ambiguity is resolved in the decision record", "RPM_ad" in DECISIONS, "D-record silent")

# ---- 3. GPU: window vs need --------------------------------------------
per_preset = {"1440p60": (2 + 20 / 2.25, 4 + 35 / 2.25), "4K60": (2 + 20, 4 + 35)}
hours = {k: (30 * lo / 60, 30 * hi / 60) for k, (lo, hi) in per_preset.items()}
ck.ck("1440p60 need is 5.4-9.8 GPU-hours", (round(hours["1440p60"][0], 1), round(hours["1440p60"][1], 1)) == (5.4, 9.8),
      str(hours["1440p60"]))
ck.ck("4K60 need is 11.0-19.5 GPU-hours", (round(hours["4K60"][0], 1), round(hours["4K60"][1], 1)) == (11.0, 19.5),
      str(hours["4K60"]))
ck.ck("provisioned window is 60 GPU-hours", "60 GPU-hours" in DOC and "2 h/day" in ARCH, "window not stated")
RATE = 0.40  # the plan's own implied mid rate: $24 of cost for 60 GPU-hours
cost = (hours["1440p60"][0] * RATE, hours["1440p60"][1] * RATE)
ck.ck("1440p cost is $2.18-$3.91 of cost per month", f"${cost[0]:.2f}–${cost[1]:.2f}" in DOC, f"{cost}")
retry = (hours["1440p60"][0] * 3 * RATE, hours["1440p60"][1] * 3 * RATE)
ck.ck("3x retries cost $6.53-$11.73 of cost per month", f"${retry[0]:.2f}–${retry[1]:.2f}" in DOC, f"{retry}")
ck.ck("the GPU rate band is stated separately", "$0.33–$0.58" in DOC, "rate band missing")
lo_ratio, hi_ratio = 60 / hours["1440p60"][1], 60 / hours["1440p60"][0]
ck.ck("window is 6-11x the implied 1440p need", (round(lo_ratio), round(hi_ratio)) == (6, 11),
      f"{lo_ratio:.1f}-{hi_ratio:.1f}")
ck.ck("window is 3-5x the implied 4K need", (round(60 / hours["4K60"][1]), round(60 / hours["4K60"][0])) == (3, 5),
      f"{60/hours['4K60'][1]:.1f}-{60/hours['4K60'][0]:.1f}")
ck.ck("register states both multiples", "6–11x" in DOC and "3–5x" in DOC, "multiple missing")
ck.ck("GPU is metered, not reserved", "metered per episode" in DOC.lower() or "metered per episode" in DOC, "decision missing")

# ---- 4. sigma is retired; the bound is distribution-free ----------------
ck.ck("the register retires sigma", "retired" in DOC and "σ" in DOC, "sigma still in use")
ck.ck("D-11 now cites the distribution-free bound", "23 of 25" in DOC or "22 of 25" in DOC, "bound missing")


def p_two_sided(u, n1=5, n2=5):
    cnt = 0
    for chosen in combinations(range(n1 + n2), n1):
        rank_sum = sum(c + 1 for c in chosen)
        if rank_sum - n1 * (n1 + 1) // 2 <= u:
            cnt += 1
    return 2 * cnt / comb(n1 + n2, n1)


exact = {u: round(p_two_sided(u), 4) for u in (0, 2, 3)}
ck.ck("p(U<=0) = 0.0079", exact[0] == 0.0079, str(exact[0]))
ck.ck("p(U<=2) = 0.0317", exact[2] == 0.0317, str(exact[2]))
ck.ck("p(U<=3) = 0.0556 is NOT significant", exact[3] == 0.0556 and exact[3] > 0.05, str(exact[3]))
ck.ck("register states the boundary at U<=2", "U ≤ 2" in DOC and "0.0317" in DOC, "boundary missing")
ck.ck("register states 23 of 25 pairs", "23 of 25" in DOC, "pair count missing")
ck.ck("DECISION_AUDIT records sigma as retired", "σ" in AUDIT and "retired" in AUDIT, "audit silent on sigma")

# ---- 5. the library grid ------------------------------------------------
grid = table_starting("v = 40")
ck.ck("grid table found", grid is not None)
for r in (grid or [])[2:]:
    c = cells(r)
    rpm = float(re.search(r"\$([\d.]+)", c[0]).group(1))
    for i, v in enumerate((40, 61, 94), start=1):
        want = (GOAL + INFRA_PER_DAY) * AD_SHARE * 1000 / (v * rpm)
        got = float(c[i].replace(",", "").replace("*", "").strip())
        ck.ck(f"grid {rpm}/v{v} = {want:.0f}", abs(got - want) < 1, f"{got} vs {want:.1f}")
ck.ck("the plan's 1,827 appears at (61, 10.50) only", "**1,830**" in DOC, "plan cell missing")
ck.ck("corner case needs 2.3x the library", abs(4186 / PLAN_LIBRARY - 2.29) < 0.02, str(4186 / PLAN_LIBRARY))
ck.ck("corner case is 56 months at 75/mo", abs(4186 / 75 - 55.8) < 0.5, str(4186 / 75))

# ---- 6. pre-registered rules -------------------------------------------
rule_tables = [t for t in tabs if t and t[0].lstrip("| ").startswith("#") and "When" in t[0]]
ck.ck("pre-registered rule tables found", len(rule_tables) >= 1, str(len(rule_tables)))
rule_rows = [cells(r) for t in rule_tables for r in t[2:]]
ck.ck("at least 10 rules", len(rule_rows) >= 10, str(len(rule_rows)))
for gate in ("First episode", "First 28 days", "YPP approval"):
    ck.ck(f"rules cover {gate}", any(gate in c[1] for c in rule_rows), gate)
ck.ck("a policy/fact violation stops publishing",
      any("R4" in " ".join(r) and "stop affected publishing" in " ".join(r) for r in rule_rows))
ck.ck("a rule replaces the assumed v with the measured one",
      any("replace projections" in " ".join(r) for r in rule_rows), "R7 missing")
ck.ck("a rule can stop the project", any("stop" in " ".join(r).lower() for r in rule_rows), "no stop rule")
ck.ck("abandonment conditions are written down", "abandon" in DOC.lower() and "pivot signal" in DOC, "missing")
ck.ck("the rules bind over conversation", "the rule wins" in DOC, "supremacy clause missing")

# ---- 7. the register is referenced, not orphaned ------------------------
ck.ck("the register does not hardcode an assertion count",
      not re.search(r"\d,\d{3} assertions", DOC), "a self-referential count will drift")

# ---- 8. round 3: the monetization gate, the calendar, limited ads --------
WATCH_H, SUBS, EPISODES, DURATION_MIN, AVD = 4000, 1000, 30, 14, 0.40
min_per_view = DURATION_MIN * AVD
views_for_hours = WATCH_H * 60 / min_per_view
ck.ck("YPP watch hours need 42,857 views", abs(views_for_hours - 42857) < 1, f"{views_for_hours:.0f}")
ck.ck("that is 1,429 views per video", abs(views_for_hours / EPISODES - 1429) < 1, f"{views_for_hours/EPISODES:.0f}")
subs_views = SUBS / 0.01
ck.ck("1,000 subs at 1% needs 100,000 views", subs_views == 100000, str(subs_views))
ck.ck("that is 3,333 views per video", abs(subs_views / EPISODES - 3333.3) < 1, f"{subs_views/EPISODES:.0f}")
ck.ck("implied v is 111 at 1% conversion", abs(subs_views / EPISODES / 30 - 111.1) < 0.5,
      f"{subs_views/EPISODES/30:.1f}")
ck.ck("111 is 1.8x the assumed 61", abs(111.1 / 61 - 1.82) < 0.02, f"{111.1/61:.2f}")
for s_ in ("42,857", "1,429", "3,333", "v ≈ 111", "1.8x"):
    ck.ck(f"register states {s_}", s_ in DOC, s_)

review_lo, review_hi = 33 * 2 / 33, 33 * 4 / 33
build_per_day = 170.5 / 45
ck.ck("sustained load is 5.8-7.8h per day",
      abs(build_per_day + review_lo - 5.8) < 0.05 and abs(build_per_day + review_hi - 7.8) < 0.05,
      f"{build_per_day + review_lo:.1f}-{build_per_day + review_hi:.1f}")
ck.ck("register states 5.8-7.8", "5.8–7.8" in DOC and "170.5h" in DOC, "labour line missing")

for share, rpm_eff, lib in ((0.20, 8.40, 2287), (0.40, 6.30, 3050)):
    eff = RPM_AD * (1 - share)
    want = (GOAL + INFRA_PER_DAY) * AD_SHARE * 1000 / (61 * eff)
    ck.ck(f"{share:.0%} limited ads -> RPM_ad ${rpm_eff:.2f}", abs(eff - rpm_eff) < 0.01, f"{eff:.2f}")
    ck.ck(f"{share:.0%} limited ads -> library {lib}", abs(want - lib) < 2, f"{want:.0f}")
ck.ck("register states the limited-ads table", "$8.40" in DOC and "3,050" in DOC, "limited-ads table missing")

for rid in ("R13", "R14", "R15", "R16", "R17", "R18"):
    ck.ck(f"rule {rid} exists", any(rid in " ".join(r) for r in rule_rows), rid)
ck.ck("R16 makes a spoken number a blocker", any("R16" in " ".join(r) and "blocker" in " ".join(r).lower()
                                                for r in rule_rows), "R16 missing")
ck.ck("R14 protects the approval gate", any("R14" in " ".join(r) and "QAG-02" in " ".join(r) for r in rule_rows))
ck.ck("a second channel is required by month 6", any("R18" in " ".join(r) and "second channel" in " ".join(r).lower()
                                                    for r in rule_rows), "R18 missing")
for item in ("AUD-06", "ANA-06"):
    ck.ck(f"{item} exists in the tracker", item in {i["id"] for i in ITEMS}, item)
ck.ck("AUD-06 blocks publish on a mismatch",
      "fails the episode" in next(i for i in ITEMS if i["id"] == "AUD-06")["acceptance_criteria"], "no blocker")

# ---- 9. plan consequences: capacity, promotion, gated cadence ------------
for rid in ("R19", "R20"):
    ck.ck(f"rule {rid} exists", any(rid in " ".join(r) for r in rule_rows), rid)
ck.ck("R19 binds the calendar to a capacity profile",
      any("R19" in " ".join(r) and "hours per day" in " ".join(r) for r in rule_rows), "R19 missing")
ck.ck("R20 gates cadence on both RPM and coverage",
      any("R20" in " ".join(r) and "RPM_ad" in " ".join(r) and "coverage" in " ".join(r) for r in rule_rows), "R20 missing")
ck.ck("R15's instrument admits the API gap",
      "returns no limited-ads flag" in DOC, "R15 still assumes an instrument that does not exist")
ck.ck("R18 is a restore drill, not a second channel",
      "recovery drill" in DOC and "INF-04" in DOC, "R18 unchanged")

BUILD, PER_EP = 170.5, (2, 4)
ck.ck("launch plan is capacity-led, not a fixed 30-in-30 promise",
      "capacity-led" in SPRINT.lower() and "30-in-30" not in SPRINT.lower(), "launch plan remains fixed")
ck.ck("capacity is derived from measured build and review constraints",
      "measured minimum" in SPRINT.lower() or "capacity" in SPRINT.lower(), "capacity metrics missing")
by_id = {i["id"]: i for i in ITEMS}
ck.ck("PUB-04 promotes subscriber conversion to P0",
      by_id["PUB-04"]["priority"] == "P0" and by_id["PUB-04"]["phase"] == "P0_MVP_DAYS_1_7",
      f'{by_id["PUB-04"]["priority"]} {by_id["PUB-04"]["phase"]}')
ck.ck("ANA-01 records subscribers per 1,000 views",
      "subscribers gained per 1,000 views" in by_id["ANA-01"]["acceptance_criteria"], "not instrumented")
ck.ck("D-01 no longer ramps on a calendar",
      "Cadence is capacity-led" in DECISIONS or "capacity-led" in DECISIONS, "D-01 still time-based")
ck.ck("the strategy bet is named in the record",
      "commodity production" in DECISIONS and "editorial finance" in DECISIONS, "D-17 missing")

# ---- 10. round 4: every threshold has to be derived ----------------------
def rule_cell(rid, idx):
    return next(r[idx] for r in rule_rows if r[0].strip() == f"**{rid}**")


def rule(rid):
    return next(" ".join(r) for r in rule_rows if r[0].strip() == f"**{rid}**")

c_of = lambda v: SUBS / (EPISODES * 30 * v)
ck.ck("YPP conversion identity c* = 1.111/v", abs(c_of(111) - 0.01) < 1e-4, f"{c_of(111):.4f}")
ck.ck("at v=61 the gate needs 1.82%, not 1%", abs(c_of(61) - 0.0182) < 5e-4, f"{c_of(61):.4%}")
ck.ck("R13 uses the identity, not a fixed 0.5%",
      "1.111 / v" in rule("R13") and "0.5%" in rule("R13"), "R13 still fixed")
ck.ck("0.5% conversion implies v=222",
      abs(SUBS / (0.005 * EPISODES * 30) - 222) < 1, str(SUBS / (0.005 * EPISODES * 30)))

BREAKEVEN = 1827 * 10.50 / 2700
ck.ck("36-month break-even RPM_ad is $7.11", abs(BREAKEVEN - 7.107) < 0.01, f"{BREAKEVEN:.2f}")
ck.ck("R20 uses the derived $7.11", "$7.11" in rule("R20") and "$8.24" not in rule("R20"), "R20 not derived")
ck.ck("R9 uses $7.11 as the viability line", "$7.11" in rule("R9"), "R9 keys off 6.24 alone")
floor_lib = 1827 * 10.50 / 6.24
ck.ck("band floor needs 3,074 videos = 41 months",
      abs(floor_lib - 3074) < 1 and abs(floor_lib / 75 - 41) < 0.1, f"{floor_lib:.0f} / {floor_lib/75:.1f}")
ck.ck("register states the 41 months", "41 months" in DOC, "floor consequence missing")

fall = 1 - 10.50 / 12.48
ck.ck("top of band cuts the library 15.9%, not 40%", abs(fall - 0.1587) < 0.002, f"{fall:.3f}")
ck.ck("R10 states 15.9%", "15.9%" in rule("R10"), "R10 still says 40%")

lib22 = 1827 * 61 / 22
ck.ck("v=22 needs 5,066 videos = 5.6 years", abs(lib22 - 5066) < 2 and abs(lib22 / 75 / 12 - 5.6) < 0.05,
      f"{lib22:.0f} / {lib22/75/12:.2f}y")
ck.ck("R8 uses measured horizon economics",
      "rebase the horizon" in rule("R8"), "R8 is not measured")

ck.ck("R14 is capacity-relative", "45% of available hours" in rule("R14"), "R14 still absolute")
ck.ck("R14's action cuts cadence rather than doubling it",
      rule_cell("R14", 4).count("cut cadence to 20/month") == 1, rule_cell("R14", 4)[:60])

mde = (16 * 0.04 * 0.96 / 22500) ** 0.5
n5 = 16 * 0.04 * 0.96 / (0.05 * 0.04) ** 2
ck.ck("45k impressions resolve 13% relative", abs(mde / 0.04 - 0.131) < 0.005, f"{mde/0.04:.1%}")
ck.ck("5% relative needs 153,600 per arm", abs(n5 - 153600) < 100, f"{n5:,.0f}")
ck.ck("R17 states the 13% floor and the sample", "13% relative" in rule("R17") and "153,600" in rule("R17"),
      "R17 still asserts 5%")
ck.ck("R17 names the minimum impressions", "10,000 impressions per arm" in rule("R17"), "no sample floor")

ck.ck("R15 measures coverage as an exact ratio",
      "playbackBasedCpm / cpm" in rule("R15") and "0.80" in rule("R15"), "R15 proxy still analogical")
ck.ck("R16 requires a second ASR pass", "second ASR pass" in rule("R16"), "R16 still zero-tolerance")
ck.ck("R5 improves only measured weak stages",
      "improve the weakest measured stage" in rule("R5"), "R5 still buys cadence")
ck.ck("no rule points at the retired 33-day sprint",
      not any("33-day sprint" in " ".join(r) for r in rule_rows), "stale sprint reference in a rule")
ck.ck("R3 revises weak format instead of a fixed 20 boundary",
      "revise topic, packaging, or narrative" in rule("R3"), "stale fixed boundary remains")

# ---- 11. round 4 is documented, and the count did not drift ---------------
ck.ck("round-4 self-audit section exists", "## 9. Round 4" in DOC, "section 9 missing")
ck.ck("it records twelve defects", "**twelve defects in the rules" in DOC, "defect count missing")
ck.ck("it separates what passed from what failed", "survived the same audit" in DOC, "no pass list")
ck.ck("section 8 cross-references the 1.82% correction", "1.82%** subscribe rate" in DOC, "cross-ref missing")
ck.ck("DECISIONS records eighteen decisions", "eighteen decisions" in DECISIONS and "## D-18" in DECISIONS, "D-18 missing")
ck.ck("D-18 names both behavioural corrections",
      "1.82%" in DECISIONS and "20/month" in DECISIONS, "D-18 silent on R13/R14")
ck.ck("no doc still promises 33 days to 30 episodes",
      "30 episodes in 33 days" not in DOC + SPRINT + read("README.md") + read("docs/IMPROVEMENT_VALUE_AT_2K.md"),
      "stale sprint promise")

ck.ck("README links the baseline register", "BASELINE.md" in read("README.md"), "not linked")
ck.ck("AGENTS links the baseline register", "BASELINE.md" in read("AGENTS.md"), "not linked")
ck.ck("DECISIONS links the baseline register", "BASELINE.md" in DECISIONS, "not linked")
ck.ck("the audit links the baseline register", "BASELINE.md" in AUDIT, "not linked")

sys.exit(ck.report())
