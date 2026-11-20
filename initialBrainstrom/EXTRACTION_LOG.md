# Extraction log — conversation 01

**Session:** `01a1d911-36fc-7344-9f71-ec5b8fa4f328`
**Result:** 70 messages · 732,742 characters · 6 transcript files

## Method
1. Opened the thread in the logged-in cloud browser. Signed out, the URL returned
   *"Session not found"* — Arena session URLs resolve only for the account owner.
2. Tried the Next.js RSC payload (`?_rsc=…`, `RSC: 1`) as a shortcut. It contains the session
   object and `messages[]` (74 records), **but message bodies are deferred React Flight references**
   (`content: "$a4"`) whose chunks are not present in the payload or the HTML flight stream —
   only 31 records carry inline text. Unusable as a source, so DOM capture was used.
3. Found the message list: `ol.flex-col-reverse` inside a virtualised scroller
   (~199-401k px tall, 286-1202 px viewport). The list is **reversed** in DOM order.
4. Captured **per item**: for each `ol` child, `scrollIntoView({block:'center'})`, wait 210-300 ms,
   re-query the list (the virtualiser re-creates nodes) and read `innerText`. Deterministic
   regardless of virtualiser window sizes; items render completely even when taller than the viewport.
5. **Completeness proof:** the virtualiser is slightly flaky per pass (an independent pass captured
   68 items instead of 70), so the capture was repeated **4 times** and unioned. Every pass agreed on
   71 list slots, of which exactly **one (index 0) is always empty** (spacer/sentinel) → 70 real
   messages. All four passes produced the same turn heads, roles, first message and last message.
   Differences between passes were trailing whitespace only (~208 chars total).
6. Verified no "Load earlier / show older messages" control exists — the first rendered turn is the
   true first message (`createdAt` 2026-11-14 07:59:15) and the last is the newest (2026-11-20 08:23:58).

## Known gaps

* The server reports **74 message records**; the page renders **70**. The 4 extra records are the
  second reply of four `direct-battle` turns (`participantPosition` `a`/`b`). **There is no branch
  switcher, response pager or A/B toggle anywhere in the UI** — checked on every turn's toolbar and
  page-wide — so the alternates are never rendered. Their ids, parents, models and timestamps are
  recorded in `01-ai-data-documentary-branches.md`, together with four alternate bodies recovered
  verbatim from the RSC Flight stream (`raw/branch-candidates.json`).
* Flight chunk ids are re-numbered per serialisation, so a hidden body cannot be tied to its turn
  with certainty; the appendix labels the recovered bodies as candidates rather than H1–H4.
* Turns marked `USER` that visibly contain another model's prose (`kimi-k3`, `muse-wonder-max`,
  `claude-haiku-5.5-xhigh`) are third-party output the user pasted in; the page renders them as user
  turns and they are preserved that way with the model name visible.
* Nothing inside `conversations/` is paraphrased. `SUMMARY`, `DECISIONS`, `REQUIREMENTS`, `IDEAS`
  and `OPEN_QUESTIONS` are derived from it and labelled as such.
