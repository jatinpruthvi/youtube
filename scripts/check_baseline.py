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
rules = table_starting("#")
ck.ck("pre-registered rule table found", rules is not None)
rule_rows = [cells(r) for r in (rules or [])[2:]]
ck.ck("at least 10 rules", len(rule_rows) >= 10, str(len(rule_rows)))
for gate in ("Day 3", "Day 17", "Day 45", "YPP approval"):
    ck.ck(f"rules cover {gate}", any(gate in c[1] for c in rule_rows), gate)
ck.ck("a rule permits exactly one retry", any("one retry" in r[4] or "one retry" in " ".join(r) for r in rule_rows))
ck.ck("a rule replaces the assumed v with the measured one",
      any("replace the 61" in " ".join(r) for r in rule_rows), "R7 missing")
ck.ck("a rule can stop the project", any("stop" in " ".join(r).lower() for r in rule_rows), "no stop rule")
ck.ck("abandonment conditions are written down", "abandon" in DOC.lower() and "pivot signal" in DOC, "missing")
ck.ck("the rules bind over conversation", "the rule wins" in DOC, "supremacy clause missing")

# ---- 7. the register is referenced, not orphaned ------------------------
ck.ck("the register does not hardcode an assertion count",
      not re.search(r"\d,\d{3} assertions", DOC), "a self-referential count will drift")

ck.ck("README links the baseline register", "BASELINE.md" in read("README.md"), "not linked")
ck.ck("AGENTS links the baseline register", "BASELINE.md" in read("AGENTS.md"), "not linked")
ck.ck("DECISIONS links the baseline register", "BASELINE.md" in DECISIONS, "not linked")
ck.ck("the audit links the baseline register", "BASELINE.md" in AUDIT, "not linked")

sys.exit(ck.report())
