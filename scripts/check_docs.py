#!/usr/bin/env python3
"""Re-verify the one-target invariant after a doc edit.

    python3 scripts/check_docs.py

Runs the three documentation checks in order and fails if any of them fails:

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
  selftest_goal.py
                   plants monthly-target violations in a temp copy of the docs
                   and requires check_goal.py to fail on each one, so its
                   labels cannot loosen without this test noticing

All five scripts are stdlib-only and resolve the repo root from their own path,
so this works from any working directory. Shared helpers live in doccheck.py.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKS = ("check_memo.py", "check_render.py", "check_goal.py", "selftest_goal.py")

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
