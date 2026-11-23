#!/usr/bin/env python3
"""Memo validator for docs/IMPROVEMENT_VALUE_AT_2K.md: does every figure follow
from the arithmetic the memo itself states?

Table shape is check_render.py's job and the per-month labelling rule is
check_goal.py's, so neither is repeated here. What is checked: the table count,
1.1 ad share -> views per RPM, 1.2 library size, 1.3 calendar, 1.4 cost per
month / 30 and profit = revenue - cost, the margins and the +86-128% inventory
premium, the 2 plan rows, the 5.1 x30 columns, and that 1.5 stays a short
rejection record.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker, cells, read, strip_fences, tables

os.chdir(ROOT)

PATH = "docs/IMPROVEMENT_VALUE_AT_2K.md"
lines = read(PATH).split("\n")
text = "\n".join(lines)

# 1.4 daily cost rows: infrastructure $2.14-$2.64, labour $70.56-$105.14
INFRA_LO, INFRA_HI = 2.14, 2.64
LABOUR_LO, LABOUR_HI = 70.56, 105.14

ck = Checker()


def num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s.replace(",", ""))
    return float(m.group(0)) if m else 0.0


def row_by_first(table, key):
    return next((c for c in map(cells, table) if key in c[0]), None)


# fenced arithmetic scratchpads are not tables
tabs = tables(strip_fences(text).split("\n"))
ck.ck("table count", len(tabs) == 14, f"found {len(tabs)}")

# ---- 1.1 views/day -------------------------------------------------------
for profit in ("1,500", "2,000"):
    r = row_by_first(tabs[0], f"${profit}/day")
    ck.ck(f"1.1 row ${profit}", r is not None)
    if r is None:
        continue
    ad, adsense = num(r[1]), num(r[5])
    ck.ck(f"1.1 ${profit} ad=78%", abs(ad - num(profit) * 0.78) < 0.5, f"{ad} vs {num(profit) * 0.78}")
    for label, col, rpm in (("7", 2, 7), ("10.50", 3, 10.5), ("14", 4, 14)):
        ck.ck(f"1.1 ${profit} views@{label}", abs(num(r[col]) - ad * 1000 / rpm) < 1.5,
              f"{r[col]} vs {ad * 1000 / rpm}")
    ck.ck(f"1.1 ${profit} adsense-only", abs(adsense - num(profit) * 1000 / 10.5) < 1.5,
          f"{adsense} vs {num(profit) * 1000 / 10.5}")

# ---- 1.2 library size ----------------------------------------------------
for t, rev in ((tabs[1], 1500), (tabs[2], 2000)):
    for r in t[2:]:
        c = cells(r)
        rpm = num(c[0])
        for j, videos in enumerate((22.22, 61, 91, 94)):
            want = rev * 0.78 * 1000 / (rpm * videos)
            got = num(c[1 + j])
            ck.ck(f"1.2 {rev}@{rpm} v={videos}", abs(got - want) / want < 0.02, f"{got} vs {want:.0f}")

# ---- 1.3 calendar --------------------------------------------------------
for r in tabs[3][2:]:
    c = cells(r)
    videos = num(c[0].split()[0])
    for j, per_month in enumerate((30, 60, 75, 90)):
        want = videos / per_month
        ck.ck(f"1.3 {videos:g} @{per_month}/mo", abs(num(c[1 + j]) - want) / want < 0.05,
              f"{c[1 + j]} vs {want:.1f}")

# ---- 1.4 cost stack: per month / 30 -------------------------------------
t14 = next(t for t in tabs if "Cost line" in t[0])
for r in t14[2:]:
    c = cells(r)
    if "Flat line" in c[0]:
        continue
    month = re.findall(r"\$([\d,]+\.\d\d)", c[1])
    day = re.findall(r"\$([\d,]+\.\d\d)", c[2])
    if len(month) == 2 and len(day) == 2:
        for i in (0, 1):
            ck.ck(f"1.4 {c[0][:28]} /30 [{i}]", abs(num(day[i]) - num(month[i]) / 30) <= 0.011,
                  f"{day[i]} vs {num(month[i]) / 30:.2f}")
        ck.ck(f"1.4 {c[0][:28]} band", num(day[0]) <= num(day[1]))

# ---- 1.4 profit = revenue - cost, and its margin -------------------------
for r in next(t for t in tabs if "Operating point" in t[0])[2:]:
    c = cells(r)
    rev = num(c[1])
    ck.ck(f"1.4 rev x30 {c[0][:20]}", abs(num(c[2]) - rev * 30) < 0.6, f"{c[2]} vs {rev * 30:.2f}")
    solo = [num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", c[3])]
    hire = [num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", c[5])]
    ck.ck(f"1.4 profit/day solo {c[0][:20]}", abs(solo[0] - (rev - INFRA_HI)) < 0.01
          and abs(solo[1] - (rev - INFRA_LO)) < 0.01, f"{solo} vs {rev - INFRA_HI:.2f}/{rev - INFRA_LO:.2f}")
    ck.ck(f"1.4 profit/day hire {c[0][:20]}", abs(hire[0] - (rev - LABOUR_HI)) < 0.01
          and abs(hire[1] - (rev - LABOUR_LO)) < 0.01, f"{hire} vs {rev - LABOUR_HI:.2f}/{rev - LABOUR_LO:.2f}")
    mlo, mhi = (float(x) for x in re.findall(r"(\d+\.\d)-(\d+\.\d)%", c[7])[0])
    ck.ck(f"1.4 margin lo {c[0][:20]}", abs(mlo - 100 * hire[0] / rev) < 0.2, f"{mlo} vs {100 * hire[0] / rev:.1f}")
    ck.ck(f"1.4 margin hi {c[0][:20]}", abs(mhi - 100 * hire[1] / rev) < 0.2, f"{mhi} vs {100 * hire[1] / rev:.1f}")

# ---- 1.4 +86-128% inventory premium -------------------------------------
for r in next(t for t in tabs if t[0].startswith("| Profit goal | Revenue/day needed"))[2:]:
    c = cells(r)
    goal = num(re.search(r"\$([\d,]+)/day", c[0]).group(1))
    lo, hi = (num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", c[1]))
    ck.ck(f"1.4 premium rev lo {goal}", abs(lo - (goal + LABOUR_LO)) < 0.01, f"{lo}")
    ck.ck(f"1.4 premium rev hi {goal}", abs(hi - (goal + LABOUR_HI)) < 0.01, f"{hi}")

# ---- 2 plan rows ---------------------------------------------------------
for r in next(t for t in tabs if "Plan's own PPM/month" in t[0])[2:]:
    c = cells(r)
    library, views, total = num(c[1]), num(c[2]), num(c[4])
    ck.ck(f"2 implied v {c[0]}", abs(num(c[3]) - views / library) < 0.1, c[3])
    signs = re.findall(r"(?:^|[^\d.$])([-+])?\$([\d,]+\.\d\d)", c[5])
    p = [(-1 if sign == "-" else 1) * num(x) for sign, x in signs]
    ck.ck(f"2 profit lo {c[0]}", abs(p[0] - (total - LABOUR_HI)) < 0.01, f"{p[0]}")
    ck.ck(f"2 profit hi {c[0]}", abs(p[1] - (total - LABOUR_LO)) < 0.01, f"{p[1]}")

# ---- 5.1 twelve items at +49.1% -----------------------------------------
for r in next(t for t in tabs if "Twelve items at +49.1%" in t[0])[2:]:
    c = cells(r)
    ad = num(c[1])
    ck.ck(f"5.1 {c[0][:18]} +49.1%", abs(num(c[2]) - ad * 0.491) < 0.02,
          f"{c[2]} vs {ad * 0.491:.2f}")
    ck.ck(f"5.1 {c[0][:18]} x30", abs(num(c[3]) - num(c[2]) * 30) < 0.6,
          f"{c[3]} vs {num(c[2]) * 30:.2f}")

# ---- the plan's monthly column is never read as a repo projection --------
for i, ln in enumerate(lines):
    if "2,850" in ln:
        window = "\n".join(lines[max(0, i - 3):i + 1])
        ck.ck("$2,850 only as the plan's own PPM column", "Plan's own PPM/month" in window, ln[:90])

# ---- 1.5 must stay a short rejection record -----------------------------
sec15 = text[text.index("### 1.5"):text.index("## 2. Where the target")]
ck.ck("1.5 short", len(sec15.split()) < 340, f"{len(sec15.split())} words")
ck.ck("1.5 rejects", "rejected" in sec15.lower())
ck.ck("1.5 points at revision", "git show 0285821" in sec15)

sys.exit(ck.report())
