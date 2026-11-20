# initialBrainstrom

Verbatim capture of the **one** Arena.ai conversation that seeded this project
(**Automated Data Documentary Network**), taken from the logged-in Arena account.

Source: https://arena.ai/c/01a1d911-36fc-7344-9f71-ec5b8fa4f328 · Captured 2026-11-20

## Contents

| File | What it is |
|---|---|
| `conversations/01-ai-data-documentary-part-01..06-of-06.md` | **The full conversation, verbatim** — 70 messages, 732,742 characters |
| `conversations/01-ai-data-documentary-branches.md` | The 4 hidden sibling replies (metadata) + alternate bodies recovered from the payload, and the proof that Arena has no branch switcher |
| `SUMMARY.md` | The arc, start to end, with turn refs `[NN]` |
| `DECISIONS.md` | What was decided, what was killed, and why |
| `REQUIREMENTS.md` | Consolidated spec + drift vs `docs/ARCHITECTURE.md` / `tracker/items.json` |
| `IDEAS.md` | Idea graveyard and survivors |
| `OPEN_QUESTIONS.md` | Unresolved points |
| `EXTRACTION_LOG.md` | Capture method, completeness proof, known gaps |
| `raw/items.json` | Machine-readable capture (one entry per message) |
| `raw/branch-candidates.json` | Raw alternate bodies pulled from the Flight stream |
| `raw/outline-main.txt` | One line per turn: role, model, length, opening text |

## Reading order

1. `SUMMARY.md` — the whole story in ~5 minutes.
2. `DECISIONS.md` — the decision record.
3. `conversations/01-…` — the primary source, in six parts.
4. `REQUIREMENTS.md` and `OPEN_QUESTIONS.md` — what to reconcile before building.

## Fidelity notes

* Text is the rendered page text verbatim, including attribution lines
  (`Max` → `Response provided by` → vendor → `Thought for Ns`) and ASCII diagrams.
* Turn numbers are chronological (1 = first message); they are **not** the page's internal ids.
* Where the user pasted another model's output into the chat, the page renders it as a user turn,
  so it is captured as `USER` with the model name visible in the text.
