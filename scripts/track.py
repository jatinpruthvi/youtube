#!/usr/bin/env python3
"""Master Architecture Tracker CLI.

Manage, filter, inspect unblocked dependencies, and sync docs/TRACKER.md
from tracker/items.json.

Usage:
    python3 scripts/track.py summary
    python3 scripts/track.py list [--track T01] [--phase P0_MVP_DAYS_1_7] [--status todo]
    python3 scripts/track.py next [--limit 10]
    python3 scripts/track.py set INF-01 done
    python3 scripts/track.py validate
    python3 scripts/track.py sync-md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_DIR / "tracker" / "items.json"
TRACKER_MD_PATH = ROOT_DIR / "docs" / "TRACKER.md"

VALID_STATUSES = ("todo", "in_progress", "done", "blocked")
VALID_PRIORITIES = ("P0", "P1", "P2")

PHASE_LABELS = {
    "P0_MVP_DAYS_1_7": "Phase 0: Pipeline MVP (Days 1–7)",
    "P1_SPRINT_DAYS_8_30": "Phase 1: 30-in-30 Launch Sprint (Days 8–30)",
    "P2_OPT_MONTHS_2_6": "Phase 2: Monetization & Retention Optimization (Months 2–6)",
    "P3_SCALE_MONTHS_7_36": "Phase 3: Multi-Channel Network Scale (Months 7–36)",
}

STATUS_BOX = {
    "todo": "[ ]",
    "in_progress": "[-]",
    "done": "[x]",
    "blocked": "[!]",
}


def load_data() -> dict[str, Any]:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data: dict[str, Any]) -> None:
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def progress_bar(done: int, total: int, width: int = 20) -> str:
    if total == 0:
        return "[" + "-" * width + "] 0%"
    ratio = done / total
    filled = int(round(ratio * width))
    pct = int(round(ratio * 100))
    return f"[{'#' * filled}{'-' * (width - filled)}] {pct:3d}% ({done}/{total})"


def cmd_summary(data: dict[str, Any]) -> None:
    items = data["items"]
    tracks = {t["id"]: t for t in data["tracks"]}

    total = len(items)
    done = sum(1 for i in items if i["status"] == "done")
    in_prog = sum(1 for i in items if i["status"] == "in_progress")
    blocked = sum(1 for i in items if i["status"] == "blocked")
    total_hrs = sum(float(i["effort_hours"]) for i in items)
    rem_hrs = sum(float(i["effort_hours"]) for i in items if i["status"] != "done")

    print(f"\n=== {data['project']} — Master Architecture Tracker ===")
    print(f"Mission:  {data['mission']}")
    print(f"Overall:  {progress_bar(done, total)} | in_progress={in_prog}, blocked={blocked}")
    print(f"Effort:   {rem_hrs:.1f}h remaining / {total_hrs:.1f}h total\n")

    print("By Track:")
    for t_id, t_info in tracks.items():
        t_items = [i for i in items if i["track"] == t_id]
        t_done = sum(1 for i in t_items if i["status"] == "done")
        t_hrs = sum(float(i["effort_hours"]) for i in t_items)
        print(f"  {t_id} {t_info['name']:<48} {progress_bar(t_done, len(t_items), 14)} ({t_hrs:4.1f}h)")

    print("\nBy Phase:")
    for p_key, p_label in PHASE_LABELS.items():
        p_items = [i for i in items if i["phase"] == p_key]
        p_done = sum(1 for i in p_items if i["status"] == "done")
        p_hrs = sum(float(i["effort_hours"]) for i in p_items)
        print(f"  {p_label:<58} {progress_bar(p_done, len(p_items), 14)} ({p_hrs:4.1f}h)")
    print()


def cmd_list(data: dict[str, Any], track: str | None, phase: str | None, status: str | None) -> None:
    items = data["items"]
    filtered = [
        i
        for i in items
        if (not track or i["track"].upper() == track.upper())
        and (not phase or i["phase"] == phase)
        and (not status or i["status"] == status)
    ]
    if not filtered:
        print("No matching items found.")
        return

    print(f"\nShowing {len(filtered)} item(s):\n")
    print(f"{'ID':<8} {'St':<4} {'Pri':<4} {'Trk':<4} {'Hrs':>4}  {'Title'}")
    print("-" * 96)
    for i in filtered:
        box = STATUS_BOX[i["status"]]
        print(f"{i['id']:<8} {box:<4} {i['priority']:<4} {i['track']:<4} {i['effort_hours']:>4.1f}  {i['title']}")
    print()


def cmd_next(data: dict[str, Any], limit: int) -> None:
    done_ids = {i["id"] for i in data["items"] if i["status"] == "done"}
    ready = [
        i
        for i in data["items"]
        if i["status"] in ("todo", "in_progress")
        and all(dep in done_ids for dep in i.get("dependencies", []))
    ]
    priority_rank = {"P0": 0, "P1": 1, "P2": 2}
    phase_rank = {k: idx for idx, k in enumerate(PHASE_LABELS.keys())}
    ready.sort(key=lambda x: (phase_rank.get(x["phase"], 99), priority_rank.get(x["priority"], 9), x["id"]))

    if not ready:
        print("No unblocked items remaining (either everything is done or dependencies are blocked).")
        return

    print(f"\nTop {min(limit, len(ready))} Unblocked Actionable Items (Dependencies Satisfied):\n")
    for item in ready[:limit]:
        deps = ", ".join(item["dependencies"]) if item["dependencies"] else "None"
        print(f"  {STATUS_BOX[item['status']]} {item['id']} [{item['priority']} | {item['effort_hours']}h | {item['track']}] {item['title']}")
        print(f"      Deps: {deps}")
        print(f"      Done when: {item['acceptance_criteria']}\n")


def github_anchor(heading: str) -> str:
    slug = heading.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s", "-", slug)
    return slug


def render_markdown(data: dict[str, Any]) -> str:
    items = data["items"]
    tracks = data["tracks"]

    total = len(items)
    done = sum(1 for i in items if i["status"] == "done")
    total_hrs = sum(float(i["effort_hours"]) for i in items)
    rem_hrs = sum(float(i["effort_hours"]) for i in items if i["status"] != "done")
    pct = int(round((done / total) * 100)) if total else 0

    lines: list[str] = [
        "# Master Architecture Track List",
        "",
        f"> **Project:** {data['project']}  ",
        f"> **Mission:** {data['mission']}  ",
        f"> **Progress:** **{done}/{total} items ({pct}%)** · **{rem_hrs:.1f}h remaining** of **{total_hrs:.1f}h total**",
        "",
        "<!-- Generated from tracker/items.json via `python3 scripts/track.py sync-md` -->",
        "",
        "### Quick CLI Commands",
        "```bash",
        "python3 scripts/track.py summary          # Live dashboard by track & phase",
        "python3 scripts/track.py next             # Show unblocked tasks ready to build right now",
        "python3 scripts/track.py set INF-01 done  # Mark item done & auto-sync this Markdown file",
        "```",
        "",
        "---",
        "",
        "## Executive Progress Summary",
        "",
        "### By Phase",
        "| Phase | Items Done | Total Effort |",
        "| :--- | :---: | :---: |",
    ]

    for p_key, p_label in PHASE_LABELS.items():
        p_items = [i for i in items if i["phase"] == p_key]
        p_done = sum(1 for i in p_items if i["status"] == "done")
        p_hrs = sum(float(i["effort_hours"]) for i in p_items)
        lines.append(f"| **{p_label}** | {p_done} / {len(p_items)} | {p_hrs:.1f}h |")

    lines.extend([
        "",
        "### By Architecture Track",
        "| Track | Component | Items Done | Effort |",
        "| :--- | :--- | :---: | :---: |",
    ])

    for t in tracks:
        t_items = [i for i in items if i["track"] == t["id"]]
        t_done = sum(1 for i in t_items if i["status"] == "done")
        t_hrs = sum(float(i["effort_hours"]) for i in t_items)
        anchor = github_anchor(f"{t['id']}: {t['name']}")
        lines.append(f"| **{t['id']}** | [{t['name']}](#{anchor}) | {t_done} / {len(t_items)} | {t_hrs:.1f}h |")

    lines.extend(["", "---", ""])

    for t in tracks:
        t_items = [i for i in items if i["track"] == t["id"]]
        t_done = sum(1 for i in t_items if i["status"] == "done")
        lines.append(f"## {t['id']}: {t['name']}")
        lines.append(f"*{t['description']}* (**{t_done}/{len(t_items)} complete**)")
        lines.append("")
        lines.append("| Status | ID | Priority | Phase | Est. | Dependencies | Item & Acceptance Criteria |")
        lines.append("| :---: | :--- | :---: | :--- | :---: | :--- | :--- |")
        for i in t_items:
            status_badge = {
                "todo": "⬜ Todo",
                "in_progress": "🟡 Active",
                "done": "✅ Done",
                "blocked": "🔴 Blocked",
            }[i["status"]]
            short_phase = i["phase"].split("_")[0]
            deps = ", ".join(f"`{d}`" for d in i["dependencies"]) if i["dependencies"] else "—"
            desc = f"**{i['title']}**<br/><sub>✓ {i['acceptance_criteria']}</sub>"
            lines.append(
                f"| {status_badge} | `{i['id']}` | `{i['priority']}` | `{short_phase}` | {i['effort_hours']}h | {deps} | {desc} |"
            )
        lines.append("")

        # Also provide plain GitHub-clickable checkboxes right beneath each table
        lines.append("<details>")
        lines.append(f"<summary>Checklist View — {t['id']} ({t_done}/{len(t_items)})</summary>")
        lines.append("")
        for i in t_items:
            mark = "x" if i["status"] == "done" else " "
            lines.append(f"- [{mark}] **`{i['id']}`** ({i['priority']}, {i['effort_hours']}h) — {i['title']}")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def cmd_sync_md(data: dict[str, Any]) -> None:
    md = render_markdown(data)
    TRACKER_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_MD_PATH.write_text(md, encoding="utf-8")
    print(f"Synced {TRACKER_MD_PATH.relative_to(ROOT_DIR)} ({len(data['items'])} items).")


def cmd_set(data: dict[str, Any], item_id: str, status: str) -> None:
    if status not in VALID_STATUSES:
        print(f"Invalid status '{status}'. Choose from: {', '.join(VALID_STATUSES)}", file=sys.stderr)
        sys.exit(1)

    target = next((i for i in data["items"] if i["id"].upper() == item_id.upper()), None)
    if not target:
        print(f"Item ID '{item_id}' not found.", file=sys.stderr)
        sys.exit(1)

    old = target["status"]
    target["status"] = status
    save_data(data)
    print(f"Updated {target['id']}: {old} -> {status} ({target['title']})")
    cmd_sync_md(data)


def cmd_validate(data: dict[str, Any]) -> int:
    """Check the tracker graph. Prints one line per problem and returns 1 if any.

    Covers what the CLI silently tolerates elsewhere: duplicate IDs, dependency
    IDs that reference nothing, dependency cycles, and enum values outside the
    sets the CLI and the generated docs assume.
    """
    problems: list[str] = []
    items = data.get("items", [])
    tracks = {t["id"] for t in data.get("tracks", [])}

    first_seen: dict[str, int] = {}
    for pos, item in enumerate(items):
        item_id = item.get("id", f"<no id at items[{pos}]>")
        if item_id in first_seen:
            problems.append(f"duplicate id {item_id}: items[{first_seen[item_id]}] and items[{pos}]")
        else:
            first_seen[item_id] = pos

    for pos, item in enumerate(items):
        item_id = item.get("id", f"items[{pos}]")
        if item.get("status") not in VALID_STATUSES:
            problems.append(f"{item_id}: invalid status {item.get('status')!r} (allowed: {', '.join(VALID_STATUSES)})")
        if item.get("priority") not in VALID_PRIORITIES:
            problems.append(f"{item_id}: invalid priority {item.get('priority')!r} (allowed: {', '.join(VALID_PRIORITIES)})")
        if item.get("phase") not in PHASE_LABELS:
            problems.append(f"{item_id}: invalid phase {item.get('phase')!r} (allowed: {', '.join(PHASE_LABELS)})")
        if item.get("track") not in tracks:
            problems.append(f"{item_id}: unknown track {item.get('track')!r} (known: {', '.join(sorted(tracks))})")
        deps = item.get("dependencies", [])
        if not isinstance(deps, list):
            problems.append(f"{item_id}: dependencies must be a list, got {type(deps).__name__}")
            continue
        for dep in deps:
            if dep not in first_seen:
                problems.append(f"{item_id}: dangling dependency {dep!r} (no item has that id)")

    graph = {
        item.get("id"): [d for d in item.get("dependencies", []) if isinstance(d, str) and d in first_seen]
        for item in items
    }
    WHITE, GREY, BLACK = 0, 1, 2
    colour = dict.fromkeys(graph, WHITE)
    path: list[str] = []

    def walk(node: str) -> None:
        colour[node] = GREY
        path.append(node)
        for nxt in graph[node]:
            if colour.get(nxt) == GREY:
                problems.append("dependency cycle: " + " -> ".join(path[path.index(nxt):] + [nxt]))
            elif colour.get(nxt) == WHITE:
                walk(nxt)
        path.pop()
        colour[node] = BLACK

    for node in graph:
        if colour[node] == WHITE:
            walk(node)

    if problems:
        for problem in problems:
            print(f"INVALID: {problem}", file=sys.stderr)
        print(f"{len(problems)} problem(s) in tracker/items.json", file=sys.stderr)
        return 1

    edges = sum(len(i.get("dependencies", [])) for i in items)
    print(f"tracker/items.json OK: {len(items)} items, {edges} dependency edges, "
          f"{len(tracks)} tracks, no duplicates, no dangling ids, no cycles, enums valid")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Master Architecture Tracker CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary", help="Show overall, track, and phase progress")

    p_list = sub.add_parser("list", help="List tracker items with optional filters")
    p_list.add_argument("--track", help="Filter by track ID (e.g. T01)")
    p_list.add_argument("--phase", choices=list(PHASE_LABELS.keys()), help="Filter by phase")
    p_list.add_argument("--status", choices=list(VALID_STATUSES), help="Filter by status")

    p_next = sub.add_parser("next", help="Show unblocked actionable items ready to start")
    p_next.add_argument("--limit", type=int, default=8, help="Max items to show (default: 8)")

    p_set = sub.add_parser("set", help="Update an item's status and sync docs/TRACKER.md")
    p_set.add_argument("id", help="Item ID (e.g. INF-01)")
    p_set.add_argument("status", choices=list(VALID_STATUSES), help="New status")

    sub.add_parser("validate", help="Check items.json for cycles, dangling dependencies, duplicate IDs and invalid enums")

    sub.add_parser("sync-md", help="Regenerate docs/TRACKER.md from tracker/items.json")

    args = parser.parse_args()
    data = load_data()

    if args.command == "summary":
        cmd_summary(data)
    elif args.command == "list":
        cmd_list(data, args.track, args.phase, args.status)
    elif args.command == "next":
        cmd_next(data, args.limit)
    elif args.command == "set":
        cmd_set(data, args.id, args.status)
    elif args.command == "validate":
        sys.exit(cmd_validate(data))
    elif args.command == "sync-md":
        cmd_sync_md(data)


if __name__ == "__main__":
    main()
