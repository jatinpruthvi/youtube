# Decision log

Every material decision in the main thread, with the reasoning given and the turn it came from.
`[NN]` = turn in `conversations/01-ai-data-documentary-part-*.md`.

## Chosen

| # | Decision | Rationale as argued | Turn |
|---|----------|--------------------|------|
| D1 | Build an **AI data documentary network**, not a clipping channel | Clipping has no moat and dead RPM; data documentaries have evergreen library value + high-CPM audience | [14] |
| D2 | **No clients, no courses, no affiliate, no sponsorships** at the start | Requested constraint; keeps it 100% platform ad revenue and fully passive | [9],[10],[24] |
| D3 | **Strategy before code** — no code until the plan is final | Explicit instruction; the thread spends ~50 turns planning | [23] |
| D4 | **One channel first** (`EconomicsByNumbers`), not 15 per-language channels | 15 channels split authority, multiply maintenance 15x, slow algorithmic growth | [60] |
| D5 | **Frontier LLM API** for scripts (~$0.05/script), not a local 8B model | Local 8B writes generic scripts → ~60% drop-off in first 30s | [22],[60] |
| D6 | **Data grounding via FastMCP** against World Bank / OECD / DBnomics / FRED / UN | Eliminates hallucinated numbers — the "0% hallucination" rule | [60] |
| D7 | **4K60 Manim + FFmpeg** rendering | 4K forces YouTube's premium vp09/av01 codecs → sharper text, 30-50% higher TV CPM | [60] |
| D8 | **Dynamic frame motion** (ticking counters, bar races, Ken Burns) | Static slides cause visual habituation → retention cliff + "mass-produced content" risk | [60] |
| D9 | **AVT congruence** — on-screen text matches narration and title | Raises YouTube's internal candidate-confidence score | [60] |
| D10 | **Metadata hijacking / anchor model** | Steal traffic from 2M+ sub competitors via 60-70% transcript entity overlap, stale-content reclamation, comment-gap mining | [52] |
| D11 | **ATS engine**, 24h feedback loop, auto thumbnail swap if CTR < 4% | Called the highest-leverage lever in the whole plan | [46],[50],[60] |
| D12 | **Native YouTube "Test & Compare"** with 3 thumbnails | Optimises CTR without metadata penalties | [60] |
| D13 | **Dual publish to Facebook In-Stream** | Extra $3-7 RPM from older demographics at zero extra production cost | [60] |
| D14 | **Manual mid-rolls at 3:15 / 6:45 / 9:30** | Raises impressions per view 1.2 → 2.8+ without hurting watch time | [60] |
| D15 | **Contextual B2B keyword seeding** in scripts | Attracts $15-35 CPM advertiser bids | [60] |
| D16 | **Indian LLP/Pvt Ltd + W-8BEN** | US withholding 30% → 15%; effective tax 39% → 22%; keeps ~$800-1,100/day more net at scale | [60] |
| D17 | **RSS trend radar** (15+ feeds) | Catches topics before search volume peaks | [40],[42],[60] |
| D18 | Upload **unlisted 24h early** and run pre-checks | Catch Content-ID / monetisation warnings before release | [60] |

## Rejected

| # | Rejected | Why | Turn |
|---|----------|-----|------|
| X1 | Multi-account + comment-interaction manipulation | Engagement fraud; assistant refused to design it | [5],[6] |
| X2 | Shorts-only / clipping network | RPM $0.01-0.04/1k → needs 50M views/day for $2,000 | [60] |
| X3 | 24/7 ambient music streams | Low RPM ($1.50-3.00), hard ceiling ($100-250/day), saturation. **Chosen at [11], reversed at [60]** | [11],[12],[60] |
| X4 | Mobile game ad harvesting | UA costs exceed ad revenue, store bans, low ARPDAU | [18],[60] |
| X5 | Cricket marketing website | Cricbuzz/ESPN competition, no tech moat, seasonality, low Indian CPM | [20],[60] |
| X6 | TikTok distribution | Banned in India since 2020; no payouts to Indian banks | [60] |
| X7 | 15 separate language channels | Splits authority, 15x maintenance | [60] |
| X8 | Meta MusicGen for music | Weights are CC-BY-NC 4.0 → DMCA risk | [60] |
| X9 | Coqui XTTS v2 | Unmaintained, weak Hindi/Arabic, CPML licence risk | [60] |
| X10 | Broker/finance affiliate links | SEBI penalises unregistered promotions for compensation | [60] |
| X11 | Numbeo / yfinance scraping | ToS prohibit commercial use; unofficial wrapper | [60] |
| X12 | **Fake camera/EXIF metadata** (claiming iPhone, etc.) | 0% algorithmic boost; cross-modal discrepancy flags (synthetic video + real sensor tag) | [56],[60] |
| X13 | Bot comment seeding / WhatsApp spam | Marginal lift, instant termination risk | [60] |
| X14 | Pure local 8B LLM for scripts | Generic output, retention loss | [22],[60] |
| X15 | Temporal + Kubernetes microservices | Over-engineering; ~2 months of dev-ops for zero revenue | [60] |
| X16 | Static slides / PowerPoint charts | Habituation + "mass-produced content" policy risk | [60] |
