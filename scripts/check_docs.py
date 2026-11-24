#!/usr/bin/env python3
"""Re-verify the one-target invariant after a doc edit.

    python3 scripts/check_docs.py

Runs the documentation and tracker checks in order and fails if any of them fails:

  check_memo.py    docs/IMPROVEMENT_VALUE_AT_2K.md - table shape and the
                   arithmetic behind every figure (views, library size,
                   calendar, cost/day, profit/day, margins, x30 columns)
  check_render.py  every Markdown table in the project docs - header,
                   separator and row widths agree, no nested tables, no
                   unescaped pipes
  check_goal.py    repo-wide: the only stated target is $1,500-$2,000 of
                   profit per day, and every per-month figure shows what it is
                   (a x30 of a day figure, a cost, a plan source, a stated
                   worth, or the rejected monthly record)
  check_decisions.py
                   docs/DECISIONS.md - every numeric claim re-derived from first
                   principles and from tracker/items.json: the gate rates, the
                   arrival month under the decided ramp, the effort chain, the
                   dilution arithmetic, the five-video interval, the pixel
                   ratio. Also fails if a corrected inflated claim returns
  check_baseline.py
                   docs/BASELINE.md - the input register: the ad-side RPM band,
                   the metered GPU hours, the exact Mann-Whitney bound that
                   replaced sigma, the v x RPM library grid, and that every
                   unmeasured input still names its retirement instrument and
                   its pre-registered rule
  check_consistency.py
                   cross-document tracker totals and launch-resolution claims
                   match tracker/items.json
  selftest_goal.py
                   plants monthly-target violations in a temp copy of the docs
                   and requires check_goal.py to fail on each one, so its
                   labels cannot loosen without this test noticing
  selftest_track.py
                   plants a dependency cycle, a dangling dependency, a duplicate
                   ID and invalid enum values in a temp copy of the tracker and
                   requires track.py validate to fail on each, so the graph
                   check cannot go quiet without this test noticing

All eight scripts are stdlib-only and resolve the repo root from their own path,
so this works from any working directory. Shared helpers live in doccheck.py.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKS = ("check_memo.py", "check_render.py", "check_goal.py", "check_decisions.py",
          "check_baseline.py", "check_consistency.py", "selftest_goal.py", "selftest_track.py")

failed = []
for name in CHECKS:
    path = os.path.join(ROOT, "scripts", name)
    print(f"\n=== {name} " + "=" * (66 - len(name)), flush=True)
    result = subprocess.run([sys.executable, path], cwd=ROOT)
    if result.returncode != 0:
        failed.append(name)

print("\n" + "=" * 70, flush=True)
if failed:
    print(f"FAILED: {', '.join(failed)}")
    sys.exit(1)
print(f"ALL PASS: {' + '.join(CHECKS)}")
