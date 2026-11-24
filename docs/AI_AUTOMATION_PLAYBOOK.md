# AI and Automation Playbook

> **Purpose:** Define how the factory uses AI to improve views, profit per day, architecture, and operational reliability.
> This is the implementation mapping for the project recommendations. It does not assume revenue or platform outcomes.

---

## 1. AI responsibility boundary

AI may propose:

- topics and query variants
- packaging and title candidates
- script and SceneGraph payloads
- transcript and scene repairs
- thumbnail concepts
- language content
- incident summaries
- configuration and architecture changes

Deterministic automation must:

- freeze source facts
- assign Fact IDs
- validate Pydantic contracts
- hash artifacts
- change pipeline state
- enforce budgets and retry limits
- run QC and fact checks
- gate human approval
- publish and verify platform receipts
- record historical telemetry

No AI model directly changes historical facts, warehouse snapshots, episode state, publication state, or production ceilings.

---

## 2. Top 20 view and profit improvements

1. **Mine demand before production**
   AI searches autocomplete, competitors, stale results, and release calendars. Automation ranks demand, freshness, source
   coverage, policy risk, and auction value. Weak candidates are removed before ETL.

2. **Maintain one concentrated topic cluster**
   AI proposes variants inside salary/take-home and adjacent cost-of-living clusters. Automation rejects duplicates and measures
   cohort performance by cluster.

3. **Engineer the first 30 seconds**
   AI drafts contrast, viewer relevance, visible proof, and an open loop. A pacing linter rejects weak hooks.

4. **Match title and thumbnail promise**
   AI generates query-shaped title and thumbnail candidates. Automation verifies mobile legibility, title length, and promise
   coherence.

5. **Create measured packaging experiments**
   Publish variants through supported YouTube workflows. Record impressions, CTR, average percentage viewed, subscribers,
   and session starts. Optimize satisfaction alongside CTR.

6. **Improve average watch time**
   AI proposes acts, pivots, pattern interrupts, and scene transitions. Scene and audience telemetry identify actual drop-offs.

7. **Build useful chapters**
   AI derives chapters from SceneGraph acts and factual pivots. Automation verifies chapter timestamps and description output.

8. **Automate session bridges**
   AI proposes the next episode and playlist position. Analytics records end-screen clicks and session starts.

9. **Refresh high-impression, low-CTR videos**
   Automation identifies candidates and creates title/thumbnail variants. AI rewrites the candidates and an approval bundle
   launches the measured refresh.

10. **Publish on source freshness**
    AI watches release calendars and identifies meaningful source updates. Deterministic snapshot diffs decide whether an
    episode needs a refresh.

11. **Measure subscriber conversion**
    Automation records subscribers gained per 1,000 views and per episode. AI proposes series and end-screen changes.

12. **Measure effective RPM**
    Analytics separates revenue, monetized playbacks, CPM, playback-based CPM, geography, topic, and limited-ad coverage.
    No AI-generated estimate replaces measured AdSense data.

13. **Optimize Tier-1 traffic quality**
    AI proposes geography- and topic-aware packaging. Analytics measures geography share and effective RPM.

14. **Place natural mid-roll breaks**
    AI proposes narrative break points. Analytics compares watch-time, ad completion, RPM, and satisfaction before enabling it.

15. **Create channel recognition**
    Configuration preserves narrator, source style, opening, methodology, visual rhythm, and licensing conventions.

16. **Use Shorts as topic probes**
    Automation extracts the strongest climax and creates 9:16 clips. Analytics reads completion and long-form subscriber
    conversion before commissioning the full episode.

17. **Reuse proven query families**
    AI creates controlled variants by country, occupation, year, and second data axis. Automation rejects duplicate theses.

18. **Reduce approval and rework**
    Automation creates one compact review package containing facts, 30-second hook, thumbnails, chapters, provenance, and
    policy report. Human review changes only source-approved fields.

19. **Protect and restore the channel asset**
    Automation backs up snapshots, artifacts, configuration, credentials metadata, and licenses. Restoration rebuilds one
    known episode and verifies every Fact ID.

20. **Run only measured revenue experiments**
    Localization, Shorts, dataset pages, Facebook, refreshes, and ancillary channels remain separate, instrumented experiments.
    Automation reports incremental value and stops negative or unmeasured experiments.

---

## 3. AI implementation loop

```text
daily:
  mine demand and source releases
  freeze candidate snapshots
  generate grounded script and SceneGraph
  audit text, overlays, subtitles, and spoken numbers
  render 1440p60 and run QC
  generate thumbnails and review package
  wait for explicit approval
  publish and record the receipt
  ingest audience and revenue telemetry
  rank future topics and refresh candidates
```

The loop is closed by recorded, versioned outcomes—not by model preference.

---

## 4. Model-safe boundaries

### AI may propose

- query variants
- title/thumbnail text
- narrative structure
- SceneGraph candidates
- Fact-ID repair instructions
- pronunciation entries
- end-screen routing
- localization text
- incident explanations
- optimization experiments

### Automation must enforce

- source snapshot validity
- Pydantic schema
- immutable Fact-ID matching
- spoken and visual number agreement
- source and asset licenses
- resolution and QC checks
- approval identity
- spend ceilings
- provider retries
- publish receipt
- historical telemetry

---

## 5. Evidence tables

Every optimization stores enough evidence to calculate incremental value:

- demand: query, competitor result, publish age, views/day, source availability
- packaging: title, thumbnail, impressions, CTR, average percentage viewed, subscribers
- retention: first-30-second retention, scene drop-off, end-screen click
- session: next video, playlist entry, start count
- revenue: revenue, monetized plays, RPM, geography, limited-ad coverage
- refresh: before/after CTR and views/video/day
- production: build time, review time, GPU time, provider cost, retries
- publication: platform response, schedule, artifact hashes, approval record

---

## 6. Implementation order

1. warehouse and provenance
2. Fact-ID script and audio audit
3. 1440p60 renderer, thumbnails, and QC
4. publishing and analytics
5. demand and packaging scoring
6. session bridges
7. back-catalogue refresh
8. effective-RPM and limited-ad measurement
9. Shorts and eligible localization
10. batching, worker scaling, and multi-channel isolation

## 7. Stop conditions

Automation stops or blocks a pipeline if:

- source snapshots are missing or stale
- a script, overlay, caption, or spoken numeral has no valid Fact ID
- ASR or visual verification fails
- an asset license is missing
- QC fails
- provider spend exceeds budget
- approval is absent
- the target platform rejects eligibility or publication
- policy or fact risk cannot be resolved

The AI may explain and propose a repair. It does not override the stop condition.
