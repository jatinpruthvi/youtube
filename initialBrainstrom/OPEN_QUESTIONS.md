# Open questions / unresolved — conversation 01

1. **Chat plan vs repo spec.** DuckDB/Parquet + `DataBrief` Fact IDs, NVENC direct piping,
   WhisperX alignment, and the Telegram approval gate appear in the repo but **not** in this
   conversation. Were they decided elsewhere, or added later by an agent? Needs a human answer.
2. **Budget shape.** Chat: CPU VPS + on-demand RTX 4090 (~$90-130/mo). Repo: a single-GPU VPS
   at ~$100/mo. Which is the operating reality?
3. **Complexity warning unaddressed.** The pasted critiques at [34]/[40] warn that the plan is
   growing more complex and more confident without more evidence. No decision was recorded in reply.
4. **Repeated blocks.** Turns [30]/[31] look like duplicated pastes of the same critique, and a
   9,580-char block appears three times at [34]/[35]/[37]. Confirm that was intentional.
5. **Facebook automation.** FB In-Stream is in the plan, but whether posting is automated via the
   Graph API or done manually was never decided, and the API-approval risk was not examined.
6. **TTS final choice.** MeloTTS vs Kokoro vs Azure fallback — never resolved to one.
7. **Entity / tax action.** LLP vs Pvt Ltd and the W-8BEN filing are planned, not executed.
8. **Channel naming.** `EconomicsByNumbers` / `TechByNumbers` are placeholders from the chat.
9. **Missing message records.** The server holds 74 message records for this session; the page
   renders 70 (see `EXTRACTION_LOG.md`). The 4 extra are almost certainly hidden branch variants,
   but their content was not recoverable from the page.
