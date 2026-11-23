#!/usr/bin/env python3
"""Markdown render check: every table in the project docs must have a header, a
separator and at least one row of the same width, with no bare pipe inside an
inline code span, and balanced code fences (an unclosed fence turns the rest of
a file into code and silently drops its tables).

Row width and separator syntax are what break rendering; a "nested table" cannot
survive those two checks, so it is not asserted separately.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doccheck import ROOT, Checker, cells, fences_balanced, read, strip_fences, tables, width

os.chdir(ROOT)

# README/AGENTS/CLAUDE sit at the root; every other doc is under docs/. glob()
# does not descend into dot-directories, so vendored .agents/.roo markdown is
# never read.
files = ["README.md", "AGENTS.md", "CLAUDE.md"]
files += sorted(glob.glob("docs/**/*.md", recursive=True))
files = [f for f in dict.fromkeys(files) if os.path.exists(f)]

ck = Checker()
counts = {}
for path in files:
    text = read(path)
    ck.ck(f"{path} fences balanced", fences_balanced(text), f"{text.count('```')} fence markers")

    found = tables(strip_fences(text).split("\n"))
    counts[path] = len(found)
    for i, t in enumerate(found, 1):
        tag = f"{path} t{i}"
        ck.ck(f"{tag} has a data row", len(t) >= 3, f"{len(t)} lines")
        w = width(t[0])
        ck.ck(f"{tag} header/separator width", w == width(t[1]), f"{w} vs {width(t[1])}")
        sep = cells(t[1])
        ck.ck(f"{tag} separator cells",
              len(sep) == w and all(re.fullmatch(r":?-{2,}:?", c) for c in sep), t[1][:80])
        for r in t[2:]:
            ck.ck(f"{tag} row width", width(r) == w, f"{width(r)} vs {w}: {r[:80]}")
        for r in t:
            for span in re.findall(r"`[^`]*`", r):
                ck.ck(f"{tag} escaped pipe in code", not re.search(r"(?<!\\)\|", span), span[:60])

print("tables:", ", ".join(f"{os.path.basename(k)}={v}" for k, v in counts.items()))
sys.exit(ck.report("CLEAN"))
