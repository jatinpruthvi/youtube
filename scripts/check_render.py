#!/usr/bin/env python3
"""Markdown render check: every table in the project docs must have a header,
a separator and rows of exactly the same width, with no unescaped pipe inside
a cell and no table nested inside another."""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)  # every path below is repo-relative

SKIP = (".git", "initialBrainstrom", "node_modules", ".agents", ".roo", ".roomodes")
files = ["README.md", "AGENTS.md", "CLAUDE.md", "docs/PPM_REVIEW.md"]
files = [f for f in files if os.path.exists(f)]
files += [f for f in sorted(glob.glob("docs/**/*.md", recursive=True)) if f not in files]
files = [f for f in dict.fromkeys(files) if not any(s in f.split(os.sep) for s in SKIP)]

fails, n = [], 0
def ck(name, cond, detail=""):
    global n
    n += 1
    if not cond:
        fails.append(f"{name}: {detail}")

def pipes(row):
    return len(re.findall(r"(?<!\\)\|", row)) - 1

counts = {}
for path in files:
    text = open(path, encoding="utf-8").read()
    # strip fenced code blocks: ASCII diagrams are not tables
    body, fence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            fence = not fence
            body.append("")
            continue
        body.append("" if fence else ln)

    tables, cur = [], []
    for ln in body + [""]:
        if ln.strip().startswith("|"):
            cur.append(ln.rstrip())
        else:
            if cur:
                tables.append(cur)
            cur = []
    counts[path] = len(tables)

    for i, t in enumerate(tables, 1):
        tag = f"{path} t{i}"
        ck(f"{tag} >=2 lines", len(t) >= 3, f"{len(t)} lines")
        w = pipes(t[0])
        ck(f"{tag} header/separator", w == pipes(t[1]), f"{w} vs {pipes(t[1])}")
        ck(f"{tag} separator cells",
           all(re.fullmatch(r"\s*:?-{2,}:?\s*", c) for c in t[1].strip().strip("|").split("|")),
           t[1][:80])
        ck(f"{tag} separator width", len(t[1].strip().strip("|").split("|")) == w, t[1][:80])
        for r in t[2:]:
            ck(f"{tag} row width", pipes(r) == w, f"{pipes(r)} vs {w}: {r[:80]}")
        # a bare pipe inside an inline code span breaks the cell count in GFM
        for r in t:
            for cell in re.findall(r"`[^`]*`", r):
                ck(f"{tag} escaped pipe in code", not re.search(r"(?<!\\)\|", cell), cell[:60])
        # nested table markers (a row whose cell starts with '|') are a hard render break
        for r in t[2:]:
            ck(f"{tag} no nested table", not r.strip("|").strip().startswith("|"), r[:60])

# the ASCII architecture tree must not be read as a table
tree = open("docs/ARCHITECTURE.md", encoding="utf-8").read()
ck("ARCH tree is fenced", tree.count("```") % 2 == 0, f"{tree.count('```')} fence markers")

print("tables:", ", ".join(f"{os.path.basename(k)}={v}" for k, v in counts.items()))
print(f"{n} render assertions", "CLEAN" if not fails else f"{len(fails)} FAILURES")
for f in fails:
    print("FAIL", f)
sys.exit(1 if fails else 0)
