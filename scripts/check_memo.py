#!/usr/bin/env python3
"""Memo validator for docs/IMPROVEMENT_VALUE_AT_2K.md.

Checks: table well-formedness, the arithmetic in 1.1/1.2/1.3/1.4/2/5.1,
and the per-day-only rule (no unlabelled monthly target).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)  # every path below is repo-relative

PATH = "docs/IMPROVEMENT_VALUE_AT_2K.md"
text = open(PATH, encoding="utf-8").read()
lines = text.split("\n")
fails = []
n = 0

def ck(name, cond, detail=""):
    global n
    n += 1
    if not cond:
        fails.append(f"{name}: {detail}")

def pipes(row):
    return len(re.findall(r"(?<!\\)\|", row)) - 1

# ---- collect tables -------------------------------------------------------
def tables(ls):
    out, cur = [], []
    for ln in ls + [""]:
        s = ln.strip()
        if s.startswith("|"):
            cur.append(s)
        else:
            if len(cur) >= 2:
                out.append(cur)
            cur = []
    return out

tabs = tables(lines)
ck("table count", len(tabs) == 14, f"found {len(tabs)}")

for i, t in enumerate(tabs, 1):
    hdr, sep = pipes(t[0]), pipes(t[1])
    ck(f"t{i} header==separator", hdr == sep, f"{t[0][:60]} -> {hdr} vs {sep}")
    ck(f"t{i} separator syntax", all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in t[1].strip("|").split("|")),
       t[1][:70])
    for r in t[2:]:
        ck(f"t{i} row width", pipes(r) == hdr, f"{pipes(r)} vs {hdr}: {r[:70]}")

# ---- 1.1 views/day -------------------------------------------------------
def num(s):
    m = re.search(r"-?[\d,]+(?:\.\d+)?", s.replace(",", ""))
    return float(m.group(0)) if m else 0.0

def row_by_first(t, key):
    for r in t:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if cells and key in cells[0]:
            return cells
    return None

t11 = tabs[0]
for profit, adrow in (("1,500", None), ("2,000", None)):
    r = row_by_first(t11, f"${profit}/day")
    ck(f"1.1 row ${profit}", r is not None)
    ad, v7, v105, v14, adsense = (num(r[1]), num(r[2]), num(r[3]), num(r[4]), num(r[5]))
    ck(f"1.1 ${profit} ad=78%", abs(ad - num(profit) * 0.78) < 0.5, f"{ad} vs {num(profit)*0.78}")
    for label, v, rpm in (("7", v7, 7), ("10.50", v105, 10.5), ("14", v14, 14)):
        ck(f"1.1 ${profit} views@{label}", abs(v - ad * 1000 / rpm) < 1.5, f"{v} vs {ad*1000/rpm}")
    ck(f"1.1 ${profit} adsense-only", abs(adsense - num(profit) * 1000 / 10.5) < 1.5,
       f"{adsense} vs {num(profit)*1000/10.5}")

# ---- 1.2 library size ---------------------------------------------------
for t, rev in ((tabs[1], 1500), (tabs[2], 2000)):
    for r in t[2:]:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        rpm = num(cells[0])
        for j, v in enumerate((22.22, 61, 91, 94)):
            want = rev * 0.78 * 1000 / (rpm * v)
            got = num(re.sub(r"[^0-9,.]", "", cells[1 + j]))
            ck(f"1.2 {rev}@{rpm} v={v}", abs(got - want) / want < 0.02, f"{got} vs {want:.0f}")

# ---- 1.3 calendar ------------------------------------------------------
t13 = tabs[3]
month_cols = [30, 60, 75, 90]
for r in t13[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    vids = num(cells[0].split()[0])
    for j, m in enumerate(month_cols):
        got = num(re.sub(r"[^0-9.]", "", cells[1 + j]))
        want = vids / m
        ck(f"1.3 {vids:g} @{m}/mo", abs(got - want) / want < 0.05, f"{got} vs {want:.1f}")

# ---- 1.4 cost stack ----------------------------------------------------
t14 = [t for t in tabs if "Cost line" in t[0]][0]
for r in t14[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    if "Flat line" in cells[0]:
        continue
    m = re.findall(r"\$([\d,]+\.\d\d)", cells[1])
    d = re.findall(r"\$([\d,]+\.\d\d)", cells[2])
    if len(m) == 2 and len(d) == 2:
        for a, b in ((0, 0), (1, 1)):
            ck(f"1.4 {cells[0][:28]} /30 [{a}]", abs(num(d[a]) - num(m[a]) / 30) <= 0.011,
               f"{d[a]} vs {num(m[a])/30:.2f}")
        ck(f"1.4 {cells[0][:28]} band", num(d[0]) <= num(d[1]))

# ---- 1.4 profit table --------------------------------------------------
tp = [t for t in tabs if "Operating point" in t[0]][0]
for r in tp[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    rev = num(cells[1])
    ck(f"1.4 rev x30 {cells[0][:20]}", abs(num(cells[2]) - rev * 30) < 0.6, f"{cells[2]} vs {rev*30:.2f}")
    solo = [num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", cells[3])]
    hire = [num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", cells[5])]
    for a, b in ((0, 0), (1, 1)):
        ck(f"1.4 profit/day solo {cells[0][:20]}", abs(solo[a] - (rev - (2.64, 2.14)[a])) < 0.01,
           f"{solo[a]} vs {rev-(2.64,2.14)[a]:.2f}")
        ck(f"1.4 profit/day hire {cells[0][:20]}", abs(hire[a] - (rev - (105.14, 70.56)[a])) < 0.01,
           f"{hire[a]} vs {rev-(105.14,70.56)[a]:.2f}")
    mlo, mhi = [float(x) for x in re.findall(r"(\d+\.\d)-(\d+\.\d)%", cells[7])[0]]
    ck(f"1.4 margin lo {cells[0][:20]}", abs(mlo - 100 * hire[0] / rev) < 0.2, f"{mlo} vs {100*hire[0]/rev:.1f}")
    ck(f"1.4 margin hi {cells[0][:20]}", abs(mhi - 100 * hire[1] / rev) < 0.2, f"{mhi} vs {100*hire[1]/rev:.1f}")

# ---- 1.4 inventory premium --------------------------------------------
tinv = [t for t in tabs if t[0].startswith("| Profit goal | Revenue/day needed")][0]
for r in tinv[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    goal = num(re.search(r"\$([\d,]+)/day", cells[0]).group(1))
    lo, hi = [num(x) for x in re.findall(r"\$([\d,]+\.\d\d)", cells[1])]
    ck(f"1.4 premium rev lo {goal}", abs(lo - (goal + 70.56)) < 0.01, f"{lo}")
    ck(f"1.4 premium rev hi {goal}", abs(hi - (goal + 105.14)) < 0.01, f"{hi}")

# ---- 2 plan rows -------------------------------------------------------
t2 = [t for t in tabs if "Plan's own PPM/month" in t[0]][0]
for r in t2[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    lib, views, total = num(cells[1]), num(cells[2]), num(re.sub(r"[^0-9.]", "", cells[4]))
    ck(f"2 implied v {cells[0]}", abs(num(cells[3]) - views / lib) < 0.1, cells[3])
    p = [(-1 if sgn == "-" else 1) * num(x)
         for sgn, x in re.findall(r"(?:^|[^\d.$])([-+])?\$([\d,]+\.\d\d)", cells[5])]
    ck(f"2 profit lo {cells[0]}", abs(p[0] - (total - 105.14)) < 0.01, f"{p[0]}")
    ck(f"2 profit hi {cells[0]}", abs(p[1] - (total - 70.56)) < 0.01, f"{p[1]}")

# ---- 5.1 twelve items --------------------------------------------------
t51 = [t for t in tabs if "Twelve items at +49.1%" in t[0]][0]
for r in t51[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    ad = num(cells[1])
    v = num(cells[2])
    ck(f"5.1 {cells[0][:18]} +49.1%", abs(v - ad * 0.491) < 0.02, f"{v} vs {ad*0.491:.2f}")
    mo = num(cells[3])
    ck(f"5.1 {cells[0][:18]} x30", abs(mo - v * 30) < 0.6, f"{mo} vs {v*30:.2f}")

# ---- per-day-only rule -------------------------------------------------
for ln in lines:
    if "2,850" in ln:
        i = lines.index(ln)
        window = "\n".join(lines[max(0, i - 3):i + 1])
        ck("$2,850 only as the plan's own PPM column", "Plan's own PPM/month" in window, ln[:90])
for m in re.finditer(r"\$\s*1,?500\s*[–-]\s*\$?\s*2,?000\s*(?:per|/|a)\s*(?:month|mo)\b", text):
    ctx = text[max(0, m.start() - 400):m.start()].lower()
    ck("monthly goal only as the rejected record",
       ("reject" in ctx) or ("earlier revision" in ctx), m.group(0))
para, paras, lineno = [], [], 0
for ln in lines + [""]:
    if ln.strip():
        para.append(ln)
    elif para:
        paras.append((lineno, "\n".join(para)))
        para = []
    lineno += 1
KEY = ("derived", "x 30", "x30", "ppm", "monthly p&l", "reject", "earlier revision", "not the target",
       "budget", "operating spend", "cost", "labour", "infra", "withholding", "per month (source)",
       "recoup", "source", "mission", "plan's own", "runway", "spend", "fixed at", "holds only")
for m in re.finditer(r"\$([\d,]+)\s*/\s*(?:mo|month)\b", text):
    before = text[:m.start()]
    start = before.rfind("\n\n")
    end = text.find("\n\n", m.start())
    ctx = text[start:end if end != -1 else len(text)].lower()
    ck("monthly figure labelled", any(k in ctx for k in KEY), f"${m.group(1)}/month :: {ctx[:80]!r}")
# 1.5 must stay a short rejection record
i15 = text.index("### 1.5")
i2 = text.index("## 2. Where the target")
sec15 = text[i15:i2]
ck("1.5 short", len(sec15.split()) < 340, f"{len(sec15.split())} words")
ck("1.5 rejects", "rejected" in sec15.lower())
ck("1.5 points at revision", "git show 0285821" in sec15)

print(f"{n} assertions", "ALL PASS" if not fails else f"{len(fails)} FAILURES")
for f in fails:
    print("FAIL", f)
sys.exit(1 if fails else 0)
