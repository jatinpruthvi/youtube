#!/usr/bin/env python3
"""Self-test for check_goal.py: does the sweep still have teeth?

Works on a throw-away copy of the docs, so the repository is never modified.
Each case plants one violation of the per-day-only rule and requires the sweep to
fail with a named rule; one control case plants a legitimately labelled monthly
figure and requires the sweep to stay silent.

This exists because the labels are the weak point. If someone widens MONTH_LABELS
back to blanket words like "revenue" or "current", or a substring match lets
"rent" inside "current" count, the planted cases stop failing and this test fails
with them. A sweep that failed everything would also fail here, on the control.
"""
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker

CHECK = os.path.join(ROOT, "scripts", "check_goal.py")

# (case name, text appended to the copy of README.md, rules that must fire)
VIOLATIONS = [
    ("monthly target restated",
     "The target is $1,800/month of revenue by month 12.",
     ("monthly figure labelled", "monthly target figure shows its day figure")),
    ("monthly trajectory",
     "We are on track for $2,000/month by Q4.",
     ("monthly target figure shows its day figure",)),
    ("blanket word: current",
     "Current pace is $1,900/month.",
     ("monthly figure labelled",)),
    ("blanket word: revenue",
     "That is $3,000/month of revenue.",
     ("monthly figure labelled",)),
    ("plan to reach",
     "We plan to reach $45,000/month in revenue.",
     ("monthly figure labelled", "monthly target figure shows its day figure")),
    ("goal restated per month",
     "The goal is $1,500–$2,000 per month of profit.",
     ("goal range per month only as the rejected record",)),
]

# a correctly labelled monthly figure must NOT be flagged
CONTROL = ("derived from its day figure",
           "Revenue needed for the $1,500/day profit floor is $45,085/month.")


def swept(root):
    r = subprocess.run([sys.executable, CHECK, root], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def fails(text):
    return [ln for ln in text.splitlines() if ln.startswith("FAIL")]


ck = Checker()
tmp = tempfile.mkdtemp(prefix="goal-sweep-selftest-")
try:
    # a faithful copy of everything the sweep reads
    shutil.copytree(os.path.join(ROOT, "docs"), os.path.join(tmp, "docs"))
    for name in ("AGENTS.md", "README.md"):
        shutil.copy(os.path.join(ROOT, name), os.path.join(tmp, name))
    os.makedirs(os.path.join(tmp, "tracker"))
    shutil.copy(os.path.join(ROOT, "tracker", "items.json"), os.path.join(tmp, "tracker"))
    readme = os.path.join(tmp, "README.md")
    pristine = open(readme, encoding="utf-8").read()

    code, out = swept(tmp)
    ck.ck("unmodified copy passes", code == 0 and not fails(out), out[-300:])

    for name, planted, rules in VIOLATIONS:
        open(readme, "w", encoding="utf-8").write(pristine + "\n" + planted + "\n")
        code, out = swept(tmp)
        caught = fails(out)
        ck.ck(f"caught: {name}", code != 0 and bool(caught), f"exit {code}, no failure")
        for rule in rules:
            ck.ck(f"caught: {name} -> {rule}", any(rule in ln for ln in caught),
                  "\n".join(caught)[:300])

    name, planted = CONTROL
    open(readme, "w", encoding="utf-8").write(pristine + "\n" + planted + "\n")
    code, out = swept(tmp)
    ck.ck(f"control: {name} is not flagged", code == 0 and not fails(out), out[-300:])
finally:
    shutil.rmtree(tmp, ignore_errors=True)

sys.exit(ck.report())
