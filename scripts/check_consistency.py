#!/usr/bin/env python3
"""Check cross-document claims against the machine-readable tracker."""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(relative_path: str) -> str:
    with open(os.path.join(ROOT, relative_path), encoding="utf-8") as handle:
        return handle.read()


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


items = json.loads(read("tracker/items.json"))["items"]
count = len(items)
effort = sum(float(item["effort_hours"]) for item in items)
count_text = str(count)
effort_text = f"{effort:g}h"

baseline = read("docs/BASELINE.md")
audit = read("docs/DECISION_AUDIT.md")
tracker = read("docs/TRACKER.md")

required_claims = (
    (baseline, f"{count_text}/{count_text} items `todo`", "BASELINE item count"),
    (baseline, f"{effort_text} | {effort_text}", "BASELINE effort"),
    (audit, f"`tracker/items.json` ({count} items, {effort_text})", "audit tracker source"),
    (tracker, f"{0}/{count} items", "TRACKER progress count"),
    (tracker, f"{effort_text} remaining", "TRACKER effort"),
)
for document, claim, label in required_claims:
    if claim not in document:
        fail(f"{label} does not match tracker ({claim!r})")

stale_claims = (
    (baseline, "60/60 items `todo`"),
    (baseline, "166.5h | 166.5h"),
    (audit, "tracker/items.json (60 items, 166.5h)"),
    (tracker, "0/60 items"),
)
for document, claim in stale_claims:
    if claim in document:
        fail(f"stale tracker claim remains: {claim}")

sprint = read("docs/SPRINT_30_DAYS.md")
if "1440p60 from `EP01`" in sprint or "native 4K60 from `EP15`" in sprint:
    fail("launch-resolution schedule still promotes an unvalidated preset")

print(f"OK: {count} tracker items and {effort_text} agree across core documents")
