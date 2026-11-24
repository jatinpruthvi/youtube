#!/usr/bin/env python3
"""Re-derive every numeric claim in docs/DECISIONS.md from first principles.

The decision record is the document that authorises spending, so its numbers
have to be reproducible the same way docs/IMPROVEMENT_VALUE_AT_2K.md's are
(scripts/check_memo.py). This check recomputes:

  D-01  the two gate rates (155 / 103 views/video/day) from ad revenue, and the
        arrival month of the goal under the decided cadence ramp, by simulation
  D-02  VAL-01's effort against T06's own total
  D-03  the 51 -> 60 item chain and the 142.0h -> 166.5h effort chain, item by
        item from tracker/items.json
  D-04  that each decision's added hours sum to the total it claims
  D-07  that the script budget still fits the plan's own LLM line
  D-09  the hired-voice cost band from word count x market rate
  D-10  the dilution arithmetic (1,830 views/day, +3.3%/month), the library-scale
        view requirement, and what a 30-video launch cohort actually reads
  D-11  the five-video confidence interval and its span
  D-12  the pixel ratio, the deferred engineering, and the GPU-hours saved

It also fails on the specific inflated claims that were corrected, so they
cannot creep back in: "~30h" of T06 behind D-12, "three weeks earlier", and the
asserted "month 26-32" band.

Nothing here is a new assumption: every constant is read from the repo
(ad share 78%, $10.50 RPM, $2.64/day of infra cost, $1,500/day of profit) or
from tracker/items.json.
"""
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker, read

os.chdir(ROOT)

DECISIONS = read("docs/DECISIONS.md")
SPRINT = read("docs/SPRINT_30_DAYS.md")
PPM = read("docs/PPM_REVIEW.md")
VIEW = read("docs/VIEW_OPTIMIZATION.md")
ITEMS = json.load(open("tracker/items.json", encoding="utf-8"))["items"]

HOURS = {i["id"]: i["effort_hours"] for i in ITEMS}
BY_ID = {i["id"]: i for i in ITEMS}
TOTAL_ITEMS = len(ITEMS)
TOTAL_HOURS = sum(HOURS.values())

# the plan's own constants (IMPROVEMENT_VALUE_AT_2K 1.1-1.4)
AD_SHARE, RPM, V_LIKELY, INFRA_PER_DAY, GOAL = 0.78, 10.5, 61, 2.64, 1500
AD15, AD20 = 1500 * AD_SHARE, 2000 * AD_SHARE
LIBRARY_GOAL = 1827

ck = Checker()


def has(text, s, name):
    ck.ck(name, s in text, f"missing {s!r}")


def absent(text, s, name):
    ck.ck(name, s not in text, f"still present {s!r}")


# ---- D-01: gate rates and the arrival band -------------------------------
v24 = AD15 * 1000 / (24 * 30 * RPM)
v36 = AD15 * 1000 / (36 * 30 * RPM)
ck.ck("D-01 24-month gate = 155", abs(v24 - 155) < 1, f"{v24:.2f}")
ck.ck("D-01 36-month gate = 103", abs(v36 - 103) < 1, f"{v36:.2f}")
has(DECISIONS, f"**{round(v24)}**", "D-01 states 155")
has(DECISIONS, f"**{round(v36)}**", "D-01 states 103")
ck.ck("D-01 1,827 at 30/mo = 61 months", abs(LIBRARY_GOAL / 30 - 60.9) < 0.1)
ck.ck("D-01 1,827 at 75/mo = 24 months", abs(LIBRARY_GOAL / 75 - 24.36) < 0.1)
has(DECISIONS, "61 months at 30/month", "D-01 states 61 months at 30/mo")
has(DECISIONS, "24 months at 75/month", "D-01 states 24 months at 75/mo")


def library(month):
    """Cumulative published videos under the decided ramp (D-01)."""
    if month <= 3:
        return 30 * month
    if month <= 6:
        return 90 + 45 * (month - 3)
    if month <= 9:
        return 225 + 60 * (month - 6)
    return 405 + 75 * (month - 9)


def arrival(v):
    for m in range(1, 200):
        if library(m) * v * RPM / 1000 / AD_SHARE - INFRA_PER_DAY >= GOAL:
            return m
    return None


for v, month in ((80, 23), (61, 28), (70, 25), (50, 34), (40, 41)):
    ck.ck(f"D-01 arrival at v={v} is month {month}", arrival(v) == month, str(arrival(v)))
has(DECISIONS, "**month 28", "D-01 states the centre month")
has(DECISIONS, "month 23–41", "D-01 states the derived band")
absent(DECISIONS, "month 26–32", "D-01 asserted band is gone")

# ---- D-02 / D-12: what T06 actually costs --------------------------------
t06 = [i for i in ITEMS if i["track"] == "T06"]
t06_hours = sum(i["effort_hours"] for i in t06)
val_dependencies = {
    "INF-03", "DAT-07", "DAT-08", "TOP-03", "SCR-03", "AUD-05", "AUD-06",
    "REN-09", "THM-02", "QAG-02", "PUB-03", "ORC-02",
}
ck.ck("D-02 VAL-01 is a terminal integration item",
      set(BY_ID["VAL-01"]["dependencies"]) == val_dependencies,
      str(BY_ID["VAL-01"]["dependencies"]))
ck.ck("D-02 T06 is 36.0h", abs(t06_hours - 36.0) < 0.01, f"{t06_hours}")
ck.ck("D-02 T06 remains fully in the launch architecture", "4K60" in BY_ID["REN-10"]["title"] or "4K60" in BY_ID["REN-10"]["acceptance_criteria"])

# ---- D-04 / D-10 / D-12: the effort chain --------------------------------
added = {
    "D-04": ["VAL-01", "DAT-09", "SHR-01", "ANC-01", "CMP-05"],
    "D-10": ["TOP-04", "PUB-04", "ANA-05"],
    "D-12": ["REN-10"],
    "D-14": ["AUD-06"],
    "D-15": ["ANA-06"],
}
running = 142.0
for label, ids in added.items():
    running += sum(HOURS[i] for i in ids)
    ck.ck(f"{label} items exist in the tracker", all(i in HOURS for i in ids), str(ids))
ck.ck("effort chain lands on the tracker total", abs(running - TOTAL_HOURS) < 0.01, f"{running} vs {TOTAL_HOURS}")
ck.ck(f"item chain 51 + {sum(len(v) for v in added.values())} = {TOTAL_ITEMS}",
      len([i for v in added.values() for i in v]) + 51 == TOTAL_ITEMS, str(TOTAL_ITEMS))
has(DECISIONS, f"142.0h to **{TOTAL_HOURS:.1f}h**", "DECISIONS states the effort chain")
has(DECISIONS, f"(0/{TOTAL_ITEMS} items)", "DECISIONS states the item chain")
has(DECISIONS, "51 → 56", "D-04 states its own count")

# every acceptance criterion and title referenced must exist
for ref in re.findall(r"`((?:VAL|DAT|TOP|SCR|AUD|REN|THM|QAG|PUB|ORC|CMP|ANA|SHR|ANC)-\d\d)`", DECISIONS):
    ck.ck(f"DECISIONS references a real item: {ref}", ref in BY_ID, ref)

# ---- D-07: the script budget fits the plan's LLM line --------------------
ck.ck("D-07 30 x $0.30 fits the $10 line", 30 * 0.30 <= 10, str(30 * 0.30))
has(DECISIONS, "$0.15–$0.30", "D-07 states the script cost band")

# ---- D-09: hired-voice cost from word count ------------------------------
words_lo, words_hi = 10 * 155, 18 * 155
cost_lo, cost_hi = words_lo * 0.02, words_hi * 0.05
ck.ck("D-09 word band", (words_lo, words_hi) == (1550, 2790), f"{words_lo}-{words_hi}")
ck.ck("D-09 cost band", (round(cost_lo), round(cost_hi)) == (31, 140), f"{cost_lo:.0f}-{cost_hi:.0f}")
has(DECISIONS, "**1,550–2,790 words**", "D-09 derives the word count")
has(DECISIONS, "**$31–$140 of cost per episode**", "D-09 derives the cost band")
absent(DECISIONS, "roughly $15–$40 of cost per episode", "D-09's invented band is gone")

# ---- D-10: ratio arithmetic ---------------------------------------------
dilute_per_month = 30 * V_LIKELY
ck.ck("D-10 dilution is 1,830 views/day", dilute_per_month == 1830, str(dilute_per_month))
ck.ck("D-10 dilution is 3.3%/month on 900", abs(30 / 900 * 100 - 3.3) < 0.1, str(30 / 900 * 100))
has(DECISIONS, "1,830/day every month = +3.3%/month", "D-10 states the dilution line")
ck.ck("D-10 library-scale views/day", 720 * 155 == 111600)
has(DECISIONS, "111,600 views/day", "D-10 states the library-scale rate")
ck.ck("D-10 155 at 30 videos = 4,650/day", 155 * 30 == 4650)
has(SPRINT, "4,650 views/day", "the sprint gate states the 30-video equivalent")
launch = [500 / 30 / 28, 15000 / 30 / 28]
ck.ck("D-10 launch cohort reads 0.6-17.9", abs(launch[0] - 0.6) < 0.05 and abs(launch[1] - 17.9) < 0.1, str(launch))
has(DECISIONS, "0.6–17.9", "D-10 states the launch band")
has(SPRINT, "**0.6 to 17.9 views/video/day**", "the sprint gate states the launch band")
for ctr, label in ((0.04, "2.8M"), (0.06, "1.9M")):
    ck.ck(f"D-10 impressions at {ctr:.0%} CTR", 111600 / ctr > 1.8e6, label)
has(VIEW, "1.9–2.8M impressions/day", "D-10 states the impressions implication")

# ---- D-11: the five-video interval --------------------------------------
se = 0.9 / math.sqrt(5)
lo, hi = 61 * math.exp(-1.64 * se), 61 * math.exp(1.64 * se)
ck.ck("D-11 interval is 32-118", (round(lo), round(hi)) == (32, 118), f"{lo:.1f}-{hi:.1f}")
ck.ck("D-11 span is 3.7x", abs(hi / lo - 3.74) < 0.05, f"{hi/lo:.2f}")
has(DECISIONS, "32–118", "D-11 states the interval")
has(SPRINT, "3.7x span", "D-11 states the span in the slate rationale")
has(DECISIONS, "modelling assumption, not measured", "D-11 labels sigma as an assumption")

# ---- D-12: pixels, deferral, GPU saving ---------------------------------
px = (3840 * 2160) / (2560 * 1440)
ck.ck("D-12 pixel ratio 2.25x", abs(px - 2.25) < 0.01, f"{px:.3f}")
has(DECISIONS, "2.25x the pixels", "D-12 states 2.25x")
ck.ck("D-12 deferred engineering is REN-10 only", HOURS["REN-10"] == 2, str(HOURS["REN-10"]))
ck.ck("D-12 REN-10 is gated behind monetization", "CMP-03" in BY_ID["REN-10"]["dependencies"], str(BY_ID["REN-10"]["dependencies"]))
ck.ck("D-12 REN-10 is the only T06 item behind CMP-03",
      [i["id"] for i in t06 if "CMP-03" in i["dependencies"]] == ["REN-10"],
      str([i["id"] for i in t06 if "CMP-03" in i["dependencies"]]))
gpu_lo, gpu_hi = (20 - 20 / px) * 30 / 60, (35 - 35 / px) * 30 / 60
ck.ck("D-12 GPU hours 5.6-9.7", (round(gpu_lo, 1), round(gpu_hi, 1)) == (5.6, 9.7), f"{gpu_lo:.1f}-{gpu_hi:.1f}")
has(DECISIONS, "**5.6–9.7 fewer GPU-hours per month**", "D-12 states the GPU saving")
has(DECISIONS, "the **engineering actually deferred is 2h**", "D-12 states the true deferral")
absent(DECISIONS.replace("An earlier draft of this decision claimed", ""), "~30h of the original T06 spend moves",
       "D-12's inflated saving is gone")
absent(DECISIONS, "episodes ship three weeks", "D-12's unsupported schedule claim is gone")

# ---- D-05 / D-06: quoted from PPM_REVIEW, not invented -------------------
for fig in ("$202", "$307", "$474"):
    ck.ck(f"D-05 {fig} quoted from PPM_REVIEW G5", fig in PPM, fig)
has(DECISIONS, "+$202 / $307 / $474", "D-05 quotes the G5 low column")
ck.ck("D-06 22% ancillary = $330-$440/day", (1500 * 0.22, 2000 * 0.22) == (330.0, 440.0))
has(DECISIONS, "$330–$440/day", "D-06/D-04 state the ancillary line")

# ---- D-02 / D-05 / D-06 / D-08: is the decision enforced, or just stated? --
ck.ck("D-02 launch episode is not a hand-built separate gate",
      "real warehouse" in BY_ID["VAL-01"]["acceptance_criteria"]
      and "end-to-end pipeline" in BY_ID["VAL-01"]["title"],
      BY_ID["VAL-01"]["acceptance_criteria"][:100])
ck.ck("D-02 REN-02 does not wait for a falsification episode",
      "VAL-01" not in BY_ID["REN-02"]["dependencies"], str(BY_ID["REN-02"]["dependencies"]))
ck.ck("D-02 ORC-02 does not wait for a falsification episode",
      "VAL-01" not in BY_ID["ORC-02"]["dependencies"], str(BY_ID["ORC-02"]["dependencies"]))
ck.ck("D-05 PUB-02 gate is in its acceptance criterion",
      "only receives localized metadata once captions" in BY_ID["PUB-02"]["acceptance_criteria"], "gate missing")
ck.ck("D-06 PUB-03 gate is in its acceptance criterion",
      "Eligibility is confirmed" in BY_ID["PUB-03"]["acceptance_criteria"], "gate missing")
for item, needle, label in (("REN-01", "RenderSpec", "D-08 RenderSpec contract"),
                            ("SCR-01", "schema_version", "D-08 schema version"),
                            ("ORC-01", "data/episodes/<episode_id>/<stage>/<content_hash>", "D-08 artifact layout"),
                            ("DAT-09", "tests/fixtures", "D-08 record/replay cassettes")):
    ck.ck(f"{label} lives in {item}", needle in BY_ID[item]["acceptance_criteria"], needle)
ck.ck("D-11 TOP-01 concentrates topics without fixed fill-the-quota logic",
      "concentrated launch slate" in BY_ID["TOP-01"]["title"].lower()
      and "fixed publish quota" in BY_ID["TOP-01"]["acceptance_criteria"],
      BY_ID["TOP-01"]["acceptance_criteria"][:70])
ck.ck("D-11 no document still prescribes 6x5",
      "6 pillars x 5" not in read("docs/ARCHITECTURE.md") and "6 pillars x 5" not in read("AGENTS.md"),
      "6x5 still prescribed")
ck.ck("D-12 launch preset is 1440p60 in REN-02",
      "1440p60" in BY_ID["REN-02"]["title"], BY_ID["REN-02"]["title"])

# ---- the record must not contradict the tracker -------------------------
ck.ck("no item claims a status other than todo", all(i["status"] == "todo" for i in ITEMS))
ck.ck("counts agree across docs",
      f"0/{TOTAL_ITEMS}" in DECISIONS and f"{TOTAL_ITEMS}/{TOTAL_ITEMS}" in PPM and f"**0/{TOTAL_ITEMS} items" in read("docs/TRACKER.md"),
      f"{TOTAL_ITEMS}")

sys.exit(ck.report())
