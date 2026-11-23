#!/usr/bin/env python3
"""Extended repo-wide goal sweep: the only target anywhere is
$1,500-$2,000 of PROFIT per day. Revenue, cost and monthly figures are allowed
only when labelled as such."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)  # every path below is repo-relative

SKIP = (".git", "initialBrainstrom", "node_modules", ".agents", ".roo", "ralph")
def ok(path):
    return not any(s in path.split(os.sep) for s in SKIP)

docs = [f for f in sorted(glob.glob("**/*.md", recursive=True)) if ok(f)]
docs = [f for f in docs if not f.startswith((".freebuff",))]

fails, n = [], 0
def ck(name, cond, detail=""):
    global n
    n += 1
    if not cond:
        fails.append(f"{name}: {detail}")

GOAL_EN = "$1,500–$2,000"
GOAL_ASC = "$1,500-$2,000"

# ---------- A. mission strings -------------------------------------------
MISSION = {
    "AGENTS.md": GOAL_EN,
    "README.md": GOAL_EN,
    "docs/ARCHITECTURE.md": GOAL_EN,
    "docs/TRACKER.md": GOAL_ASC,
    "tracker/items.json": GOAL_ASC,
    "docs/SPRINT_30_DAYS.md": GOAL_EN,
    "docs/IMPROVEMENT_VALUE_AT_2K.md": GOAL_ASC,
}
for path, goal in MISSION.items():
    text = open(path, encoding="utf-8").read()
    ck(f"mission has the goal range in {path}", goal in text or GOAL_ASC in text or GOAL_EN in text, goal)
    head = "\n".join(text.split("\n")[:6]) if not path.endswith("items.json") else text[:600]
    ck(f"mission names profit in {path}", "profit" in text.lower())
    goal_line = next((ln for ln in text.split("\n") if ("$1,500–$2,000" in ln or "$1,500-$2,000" in ln)), "")
    ck(f"mission is per day in {path}", "/day" in goal_line, goal_line[:90])

items = json.load(open("tracker/items.json", encoding="utf-8"))
ck("items.json mission", "profit" in items["mission"] and "/day" in items["mission"], items["mission"][:90])
ck("tracker md matches items.json mission",
   items["mission"].split(" of profit")[0] in open("docs/TRACKER.md", encoding="utf-8").read(),
   items["mission"][:70])

# ---------- B/C. monthly figures -----------------------------------------
def paragraphs(text):
    out, cur = [], []
    for ln in text.split("\n"):
        if ln.strip():
            cur.append(ln)
        elif cur:
            out.append("\n".join(cur))
            cur = []
    if cur:
        out.append("\n".join(cur))
    return out

DERIVED = ("derived", "x 30", "x30", "ppm", "monthly p&l", "per month (source)", "x 12")
REJECT = ("reject", "earlier revision", "not the target", "was priced", "considered and")
COST = ("cost", "budget", "labour", "infra", "withholding", "spend", "runway", "recoup",
        "fixed at", "holds only", "subscription", "billed", "salary", "hire", "$100/month",
        "unit economics", "vps", "topology", "measured", "base a", "arithmetic", "current", "today",
        "worth", "likely base", "delta")
PLAN = ("plan's own", "the plan", "plan row", "source", "branches.md", "ppm/month")
ALLOW = DERIVED + REJECT + COST + PLAN

for path in docs:
    text = open(path, encoding="utf-8").read()
    for para in paragraphs(text):
        low = para.lower()
        if "```" in para:
            continue  # arithmetic scratchpad, not a stated operating point
        for m in re.finditer(r"\$([\d][\d,]*(?:\.\d+)?)\s*(?:/|per|a)\s*(?:month|mo)\b", para):
            labelled = (any(k in low for k in ALLOW) or "/day" in para or "revenue" in low
                        or "x 30" in low or "x30" in low)
            ck(f"monthly figure labelled in {path}", labelled, f"${m.group(1)}/month :: {para[:70]!r}")
        for m in re.finditer(r"\$\s*1,?500\s*[–-]\s*\$?\s*2,?000\s*(?:/|per|a)\s*(?:month|mo)\b", para):
            ck(f"no per-month goal in {path}", any(k in low for k in REJECT), para[:90])
        # a /month figure may never be the trajectory for the goal
        for m in re.finditer(r"(?:target|trajectory|goal|plan(?:s|ned)?\s+for)\D{0,40}\$([\d,]+)\s*/\s*month", para):
            ck(f"no monthly goal trajectory in {path}",
               any(k in low for k in REJECT + ("revenue", "derived", "cost", "ppm", "floor")), para[:90])

# every daily figure that is not the goal must say what it is
DAILYQ = ("profit", "revenue", "cost", "views", "rpm", "derived", "plan", "row", "milestone", "pre-goal",
          "withholding", "cash", "worth", "spend", "per day", "priced", "ad revenue", "ad-side", "labour",
          "infra", "top edge", "floor", "ceiling")
for path in docs:
    text = open(path, encoding="utf-8").read()
    for para in paragraphs(text):
        low = para.lower()
        for m in re.finditer(r"\$([\d][\d,]*)\s*[–-]\s*\$?([\d][\d,]*)\s*(?:/|per)\s*day", para):
            band = (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", "")))
            if band == (1500, 2000):
                continue  # the goal itself
            ck(f"daily band qualified in {path}", any(k in low for k in DAILYQ), para[:80])

# ---------- D. phase table arithmetic ------------------------------------
arch = open("docs/ARCHITECTURE.md", encoding="utf-8").read().split("\n")
start = next(i for i, ln in enumerate(arch) if ln.startswith("| Phase | Timeline |"))
rows = []
for ln in arch[start:]:
    if not ln.startswith("|"):
        break
    rows.append(ln)
ck("phase table header is 7 columns", len(re.findall(r"(?<!\\)\|", rows[0])) - 1 == 7, rows[0][:90])
for r in rows[2:]:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    ck(f"phase row width {cells[0][:18]}", len(cells) == 7, str(len(cells)))
    views = re.search(r"([\d,]+)–([\d,]+)", cells[4])
    rev = re.search(r"\$([\d,]+)–\$([\d,]+)", cells[5])
    if views and rev:
        lo, hi = float(views.group(1).replace(",", "")), float(views.group(2).replace(",", ""))
        rlo, rhi = float(rev.group(1).replace(",", "")), float(rev.group(2).replace(",", ""))
        ck(f"{cells[0][:18]} revenue low = views x RPM", abs(rlo - lo * 10 / 1000) < 1, f"{rlo} vs {lo*10/1000}")
        ck(f"{cells[0][:18]} revenue high = views x RPM", abs(rhi - hi * 10 / 1000) < 1, f"{rhi} vs {hi*10/1000}")
    else:
        ck(f"{cells[0][:18]} revenue cell arithmetic", "Pre-YPP" in cells[5], cells[5][:40])
    ck(f"{cells[0][:18]} goal status present", bool(re.sub(r"[*\s]", "", cells[6])), cells[6][:40])
    ck(f"{cells[0][:18]} revenue cell is a band, not an open-ended +", "+" not in cells[5], cells[5][:40])

phase3 = [r for r in rows if "Phase 3" in r][0]
ck("Phase 3 labelled pre-goal", "pre-goal" in phase3.lower() and "not the target" in phase3.lower())
phase4 = [r for r in rows if "Phase 4" in r][0]
ck("Phase 4 contains the goal", "contains the goal" in phase4.lower())

# ---------- E. sprint gate table is per-day only -------------------------
sprint = open("docs/SPRINT_30_DAYS.md", encoding="utf-8").read()
ck("sprint has no $2,850", "2,850" not in sprint)
gate = sprint[sprint.index("| Threshold | What it means |"):]
gate = gate[:gate.index("\n\n", gate.index("| **< 45 views"))]
ck("sprint gate table: no money per month", not re.search(r"\$[\d,]+\s*/\s*(?:mo|month)", gate),
   str(re.findall(r"\$[\d,]+\s*/\s*month", gate)))
ck("sprint gate names the daily interim milestone", "$95/day" in gate)
ck("sprint gate stakes the daily goal", "$1,500/day" in gate)
ck("sprint gate has no money-to-month conversion",
   not re.search(r"\$[\d,]+[^|]{0,10}(?:/|per)\s*(?:mo|month)", gate), gate[:200])

# ---------- F. the pre-goal band is never read as a target ---------------
for path in docs:
    text = open(path, encoding="utf-8").read()
    for para in paragraphs(text):
        if "1,000–1,600" in para or "1,000-1,600" in para:
            ck(f"pre-goal band labelled in {path}",
               any(k in para.lower() for k in ("pre-goal", "top edge", "below the $1,500", "milestone")),
               para[:80])
        if "$1,600/day" in para:
            ck(f"$1,600/day labelled in {path}",
               any(k in para.lower() for k in ("pre-goal", "top edge", "milestone", "below")), para[:80])

# ---------- G. one goal, one unit ---------------------------------------
for path in docs:
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"\$45k?\s*[–-]\s*\$?60k?\s*/\s*month", text):
        para = text[max(0, text.rfind("\n\n", 0, m.start())): text.find("\n\n", m.start())]
        ck(f"$45k-$60k/month is the derived month of the daily goal in {path}",
           any(k in para.lower() for k in ("day", "derived", "mission")), para[:90])

print(f"{n} assertions", "ALL PASS" if not fails else f"{len(fails)} FAILURES")
for f in fails:
    print("FAIL", f)
sys.exit(1 if fails else 0)
