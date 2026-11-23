#!/usr/bin/env python3
"""Shared helpers for the documentation checks (stdlib only).

The three checks in this directory used to carry their own copies of the repo
root, the assertion collector, the fence stripper, the paragraph splitter and the
cell splitter. They live here once.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Checker:
    """Collects assertions by name; a failed one remembers its detail."""

    def __init__(self):
        self.n = 0
        self.fails = []

    def ck(self, name, cond, detail=""):
        self.n += 1
        if not cond:
            self.fails.append(f"{name}: {detail}")

    def report(self, passed="ALL PASS"):
        if self.fails:
            print(f"{self.n} assertions {len(self.fails)} FAILURES")
            for f in self.fails:
                print("FAIL", f)
            return 1
        print(f"{self.n} assertions {passed}")
        return 0


def read(path):
    return open(path, encoding="utf-8").read()


def fences_balanced(text):
    return text.count("```") % 2 == 0


def strip_fences(text):
    """Blank out fenced code blocks: ASCII diagrams and arithmetic scratchpads
    are neither prose nor tables, and a stray fence must not hide a table."""
    out, fenced = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else ln)
    return "\n".join(out)


def paragraphs(lines):
    """Line spans (start, end) of blank-line separated blocks."""
    spans, start = [], None
    for i, ln in enumerate(lines):
        if ln.strip():
            if start is None:
                start = i
        elif start is not None:
            spans.append((start, i))
            start = None
    if start is not None:
        spans.append((start, len(lines)))
    return spans


def money(lines, pattern):
    """(match, window, span) for every match.

    span is the matched lines only; window adds one line either side, clamped to
    the paragraph, so wrapped prose is judged whole. Inside a table the window
    runs back to the column header, because the header is the label a reader
    actually sees."""
    for a, b in paragraphs(lines):
        text = "\n".join(lines[a:b])
        for m in re.finditer(pattern, text):
            first = a + text[:m.start()].count("\n")
            last = a + text[:m.end()].count("\n")
            lo, hi = max(a, first - 1), min(b, last + 2)
            if lines[first].strip().startswith("|"):
                while lo > a and lines[lo - 1].strip().startswith("|"):
                    lo -= 1
                hi = max(hi, min(b, lo + 2))
            span = " ".join(" ".join(lines[first:last + 1]).split()).lower()
            yield m, " ".join(" ".join(lines[lo:hi]).split()).lower(), span


def labelled(window, markers):
    """True when any marker appears in window as a whole word, allowing the
    usual inflections (cost/costs, hire/hires, reject/rejected). Substring
    matching is not good enough: "rent" lives inside "current"."""
    for m in markers:
        head = r"(?<![a-z])" if m[0].isalpha() else ""
        tail = r"(?:s|es|ed|ing)?(?![a-z])" if m[-1].isalpha() else ""
        if re.search(head + re.escape(m) + tail, window):
            return True
    return False


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def width(row):
    """Cell count of a table row; \\| inside inline code is not a boundary."""
    return len(re.findall(r"(?<!\\)\|", row)) - 1


def tables(lines):
    """Runs of lines that start with a pipe."""
    out, cur = [], []
    for ln in lines + [""]:
        if ln.strip().startswith("|"):
            cur.append(ln.rstrip())
        elif cur:
            out.append(cur)
            cur = []
    return out


def table_after(lines, header_prefix):
    """The table whose header starts with header_prefix; [] when absent."""
    start = next((i for i, ln in enumerate(lines) if ln.startswith(header_prefix)), None)
    if start is None:
        return []
    out = []
    for ln in lines[start:]:
        if not ln.startswith("|"):
            break
        out.append(ln)
    return out
