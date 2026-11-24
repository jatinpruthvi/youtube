#!/usr/bin/env python3
"""Repo-wide goal sweep: the only target anywhere is $1,500-$2,000 of PROFIT
per day.

A per-month figure is allowed, but only when its own line (and, inside a table,
its column header) shows which of these it is: a x30 of a day figure, PPM
arithmetic, a cost or budget, a quoted plan source, a stated worth, a measured
state, or the one rejected monthly record. Bare words that appear all over these
docs - "revenue", "current", "today", "source", "delta", "worth" - are
deliberately not labels, because any of them alone would bless a restated
monthly target ("current pace is $1,900/month" must fail). A monthly figure under
a target noun must also carry its own day figure, and a daily band that is not the goal must say what it is (revenue, cost, views, milestone, ...), with the
pre-goal band staying marked as one.

Pass a repo root to sweep a copy instead of this checkout (selftest_goal.py does
that to prove the labels still catch a planted violation).
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker, cells, labelled, money, read, strip_fences, table_after, width

os.chdir(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else ROOT)

SKIP = {".git", "initialBrainstrom", "node_modules", ".agents", ".roo", "ralph"}
docs = [f for f in sorted(glob.glob("**/*.md", recursive=True)) if not (set(f.split(os.sep)) & SKIP)]

GOAL_EN, GOAL_ASC = "$1,500–$2,000", "$1,500-$2,000"
ck = Checker()

# ---------- A. mission strings -------------------------------------------
MISSION = {
    "AGENTS.md": GOAL_EN,
    "README.md": GOAL_EN,
    "docs/ARCHITECTURE.md": GOAL_EN,
    "docs/SPRINT_30_DAYS.md": GOAL_EN,
    "docs/TRACKER.md": GOAL_ASC,
    "docs/IMPROVEMENT_VALUE_AT_2K.md": GOAL_ASC,
    "tracker/items.json": GOAL_ASC,
}
for path, goal in MISSION.items():
    text = read(path)
    ck.ck(f"mission carries {goal} in {path}", goal in text, "goal not found")
    stated = next((ln for ln in text.split("\n")
                   if goal in ln and "profit" in ln.lower() and re.search(r"(?:/|per)\s*day\b", ln)), "")
    ck.ck(f"mission is {goal} of profit per day in {path}", bool(stated),
          "no line states it per day")

items = json.load(open("tracker/items.json", encoding="utf-8"))
ck.ck("items.json mission is the daily profit goal",
      "profit" in items["mission"] and re.search(r"/\s*day\b", items["mission"]) is not None,
      items["mission"][:90])
ck.ck("docs/TRACKER.md mission matches items.json",
      items["mission"].split(" of profit")[0] in read("docs/TRACKER.md"), items["mission"][:70])

# ---------- B. per-month figures, per-day bands, the pre-goal band --------
MONTH = r"\$([\d][\d,]*(?:\.\d+)?)\s*(?:/|per|a)\s*(?:month|mo)\b"
GOAL_PER_MONTH = r"\$\s*1,?500\s*[–-]\s*\$?\s*2,?000\s*(?:/|per|a)\s*(?:month|mo)\b"
GOAL_AS_MONTH_TARGET = (r"(?:target|trajectory|forecast|projection|goal)\D{0,20}\$?\s*"
                        r"(?:1,?500|2,?000|45,?000|60,?000)\D{0,10}(?:/|per)\s*(?:month|mo)\b")
DAILY_BAND = r"\$([\d][\d,]*)\s*[–-]\s*\$?([\d][\d,]*)\s*(?:/|per)\s*day"
PRE_GOAL_BAND = r"1,000[–-]1,600|\$1,600\s*/\s*day"
# a monthly figure under one of these nouns must carry its own /day figure
TARGET_NOUN = re.compile(r"\b(?:target|trajectory|forecast|projection|on pace|on track|plans? to|"
                         r"expects? to|aims? (?:for|at))")

MONTH_LABELS = {
    "a x30 of a day figure": ("/day", "/ day", "per day", "x 30", "x30", "× 30", "/ 30", "/30",
                             "derived"),
    "PPM arithmetic": ("ppm", "monthly p&l", "per month (source)", "month delta (arithmetic)"),
    "a cost or budget": ("cost", "budget", "spend", "labour", "labor", "infra", "infrastructure",
                         "salary", "hire", "runway", "withholding", "subscription", "recoup",
                         "fixed at", "rent", "control plane", "cpx41", "vps", "unit economics",
                         "constraint"),
    "a quoted plan source": ("plan's own", "branches.md", "plan's year", "plan row"),
    "a stated worth": ("worth $", "is worth"),
    "a measured state": ("measured", "actual"),
    "the rejected monthly record": ("reject", "earlier revision", "not the target"),
}
DAILY_LABELS = ("profit", "revenue", "cost", "views", "rpm", "derived", "plan", "row", "milestone",
                "pre-goal", "withholding", "cash", "worth", "spend", "priced", "ad revenue",
                "ad-side", "labour", "infra", "top edge", "floor", "ceiling")
PRE_GOAL_LABELS = ("pre-goal", "top edge", "below the $1,500", "milestone")

for path in docs:
    lines = strip_fences(read(path)).split("\n")

    for m, win, span in money(lines, MONTH):
        kind = next((k for k, marks in MONTH_LABELS.items() if labelled(win, marks)), None)
        ck.ck(f"monthly figure labelled in {path}", kind is not None,
              f"${m.group(1)}/month, no label :: {win[:90]!r}")
        if TARGET_NOUN.search(span):
            ck.ck(f"monthly target figure shows its day figure in {path}",
                  kind in ("a x30 of a day figure", "the rejected monthly record"), span[:100])
    for _, win, _ in money(lines, GOAL_PER_MONTH):
        ck.ck(f"goal range per month only as the rejected record in {path}",
              labelled(win, MONTH_LABELS["the rejected monthly record"]), win[:90])
    for _, win, _ in money(lines, GOAL_AS_MONTH_TARGET):
        ck.ck(f"no monthly target using the goal's own numbers in {path}",
              labelled(win, MONTH_LABELS["the rejected monthly record"]), win[:90])
    for m, win, _ in money(lines, DAILY_BAND):
        if (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", ""))) == (1500, 2000):
            continue  # the goal itself
        ck.ck(f"daily band qualified in {path}", labelled(win, DAILY_LABELS), win[:80])
    for _, win, _ in money(lines, PRE_GOAL_BAND):
        ck.ck(f"pre-goal band labelled in {path}", labelled(win, PRE_GOAL_LABELS), win[:80])

# ---------- C. the phase table is its own arithmetic ---------------------
rows = table_after(read("docs/ARCHITECTURE.md").split("\n"), "| Phase | Timeline |")
ck.ck("phase table found with 7 columns", bool(rows) and width(rows[0]) == 7,
      rows[0][:90] if rows else "header not found")
for r in rows[2:]:
    c = cells(r)
    name = c[0][:18]
    ck.ck(f"phase row {name} width", len(c) == 7, str(len(c)))
    if len(c) < 7:
        continue
    views, rev = re.search(r"([\d,]+)–([\d,]+)", c[4]), re.search(r"\$([\d,]+)–\$([\d,]+)", c[5])
    if views and rev:
        v = [float(x.replace(",", "")) for x in views.groups()]
        rng = [float(x.replace(",", "")) for x in rev.groups()]
        ck.ck(f"phase row {name} revenue = views x $10 RPM",
              abs(rng[0] - v[0] * 0.01) < 1 and abs(rng[1] - v[1] * 0.01) < 1,
              f"{rng} vs {[round(x * 0.01) for x in v]}")
    else:
        ck.ck(f"phase row {name} revenue cell arithmetic", "Pre-YPP" in c[5], c[5][:40])
    ck.ck(f"phase row {name} goal status", bool(re.sub(r"[*\s]", "", c[6])), c[6][:40])
    ck.ck(f"phase row {name} revenue is a band, not open-ended +", "+" not in c[5], c[5][:40])

phase3 = next((r for r in rows if "Phase 3" in r), "")
ck.ck("Phase 3 labelled pre-goal", "pre-goal" in phase3.lower() and "not the target" in phase3.lower())
phase4 = next((r for r in rows if "Phase 4" in r), "")
ck.ck("Phase 4 contains the goal", "contains the goal" in phase4.lower())

# ---------- D. capacity-led launch plan is per-day/economics disciplined ----
sprint = read("docs/SPRINT_30_DAYS.md")
ck.ck("launch plan is capacity-led",
      "capacity-led" in sprint.lower() and "fixed quota" not in sprint.lower(), "launch plan is still fixed")
ck.ck("launch plan names measured production capacity",
      "build/review" in sprint.lower() or "measured minimum" in sprint.lower(), "capacity metrics missing")
ck.ck("launch plan is not a false 30-in-30 promise",
      "30/30 episodes" not in sprint and "30-in-30" not in sprint.lower(), "stale fixed sprint remains")

sys.exit(ck.report())
