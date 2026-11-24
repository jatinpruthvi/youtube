#!/usr/bin/env python3
"""Self-test for track.py validate: does the graph check still have teeth?

Works on a throw-away copy of scripts/track.py and tracker/items.json, so the
repository is never modified. Each case plants one broken graph and requires
`track.py validate` to exit nonzero with a named problem; a control case runs the
unmodified copy and requires it to pass.

This exists because validate is the only thing standing between a typo'd
dependency and a 51-item plan. A cycle, a dangling ID, a duplicate ID and an
unknown status all parse as JSON and every other command tolerates them, so if
the checks are weakened or the exit status stops being propagated, the planted
cases stop failing and this test fails with them. A validator that rejected
everything would also fail here, on the control.
"""
import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker

# (case name, mutation of the parsed items.json, text the validator must print)
CASES = [
    ("dependency cycle",
     lambda d: d["items"][0].__setitem__("dependencies", [d["items"][1]["id"]]),
     "dependency cycle:"),
    ("dangling dependency",
     lambda d: d["items"][0].__setitem__("dependencies", ["NOPE-99"]),
     "dangling dependency"),
    ("duplicate id",
     lambda d: d["items"].append(copy.deepcopy(d["items"][0])),
     "duplicate id"),
    ("bad status",
     lambda d: d["items"][0].__setitem__("status", "doing"),
     "invalid status"),
    ("bad priority",
     lambda d: d["items"][0].__setitem__("priority", "P9"),
     "invalid priority"),
    ("unknown track",
     lambda d: d["items"][0].__setitem__("track", "T99"),
     "unknown track"),
]


def validated(root):
    r = subprocess.run(
        [sys.executable, os.path.join(root, "scripts", "track.py"), "validate"],
        capture_output=True, text=True,
    )
    return r.returncode, r.stdout + r.stderr


ck = Checker()
tmp = tempfile.mkdtemp(prefix="track-validate-selftest-")
try:
    # a faithful copy of everything validate reads, at the same relative paths
    os.makedirs(os.path.join(tmp, "scripts"))
    os.makedirs(os.path.join(tmp, "tracker"))
    shutil.copy(os.path.join(ROOT, "scripts", "track.py"), os.path.join(tmp, "scripts"))
    target = os.path.join(tmp, "tracker", "items.json")
    shutil.copy(os.path.join(ROOT, "tracker", "items.json"), target)
    base = json.loads(open(target, encoding="utf-8").read())

    def write(data):
        with open(target, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)

    code, out = validated(tmp)
    ck.ck("unmodified copy validates", code == 0 and "OK:" in out, out[-300:])

    for name, mutate, message in CASES:
        data = copy.deepcopy(base)
        mutate(data)
        write(data)
        code, out = validated(tmp)
        ck.ck(f"caught: {name}", code != 0 and message in out,
              f"exit {code}, no {message!r} in output")

    write(base)
    code, out = validated(tmp)
    ck.ck("restored copy validates", code == 0 and "OK:" in out, out[-300:])
finally:
    shutil.rmtree(tmp, ignore_errors=True)

sys.exit(ck.report())
