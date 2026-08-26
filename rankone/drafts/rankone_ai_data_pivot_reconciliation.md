# AI Data Monetization Pivot - reconciliation

What the Jun 17 sync decision ("pivot toward providing user-preference data for AI entities, reduces pressure on immediate revenue") changes versus the prep-doc thinking. Internal note for Robert.

## What the pivot actually is
The prep doc framed the money question as **B2B Insights sold to game developers** (paying dev customers, ACV/ARR). The pivot reframes the same underlying asset - 2.6M human-curated game relations, 413k written reviews, multi-platform, longitudinal, consented - as a **data feed/licence for AI**, not a dashboard product for studios.

Read it as the Reddit / Stack Overflow / Photobucket data-licensing playbook applied to gaming taste: in a market where scraped and synthetic data are increasingly suspect, *authentic, human-curated, rights-cleared preference data with provenance* is the scarce thing. RankOne's strongest dimension (the corpus, +51% relations / +60% reviews YoY) becomes the headline; its weakest (consumer MAU/retention) drops out of the lead.

## Why this is directionally right
1. It plays the strength, not the weakness. The prep-doc trap was "consumer growth curve too flat to excite a growth VC, revenue too thin for profitability." A data-licensing thesis is underwritten by **corpus uniqueness and rights**, not by the ~1.8%/mo signup curve. The single fact that has held the raise back for 5 years (linear, decelerating user growth) matters far less to a data buyer than to a consumer-growth VC.
2. Peter is the canonical mind for it. He ran Newzoo - he can price exactly what curated games-preference data is worth and to whom. This is the highest-leverage thing to get from him.
3. "Reduces near-term revenue pressure" is consistent with a licensing/asset bet (deals take time, but each is large and recurring) rather than a per-seat SaaS grind.

## But it reframes the fork - it does not resolve it
The prep doc's fork was Path A (venture growth / position for acquisition) vs Path B (profitability). The pivot is **not a third escape route** - it is essentially a Path-B-leaning **asset/licensing play with Path-A optionality** (an AI-data or games-data acquirer at the end). It still forces the same discipline: pick the data thesis and commit, don't keep the consumer-growth narrative running in parallel as a hedge. Runway to mid-2027 means the commit window is the next 6-9 months, same as before.

**The thing to watch:** "reduces pressure on immediate revenue" is the same shape as the deck's projected-ARR problem - a reason to defer proving monetization. Pin it down: the pivot earns its keep only if it produces **one paid data pilot or signed LOI within ~6 months**. Otherwise it is the "nice-to-have R&D" pattern wearing a new label.

## What it changes about the KPI ask (Johan dashboard)
The drafted dashboard (`rankone_kpi_dashboard_ask_johan.md`) is consumer-app-centric. Keep it, but re-weight: the data-asset group moves from #7-afterthought to the **headline**, and add a rights line. Revised emphasis:
1. **Corpus metrics (now the lead)** - total curated relations + reviews, unique users represented, breadth (# games / genres covered), recency, and growth rate of the corpus. This is what a data buyer diligences first.
2. **Data uniqueness / defensibility** - what RankOne has that scraped Steam reviews, IGDB, or synthetic data do not (human-curated, longitudinal, cross-platform, consented). Peter defines what "defensible" looks like.
3. **Rights / consent posture (NEW, critical)** - can RankOne lawfully licence EU users' preference data to AI entities? Lawful basis + ToS/privacy-policy coverage + consent mechanics. This is a hard gate, not a metric - see risks below.
4. **AI-data pipeline** - conversations / LOIs / pilots with data buyers, replacing "paying dev customers" as the money line.
5. Retention / activation / growth-rate (the old lead) demote to **inputs**: they still matter because the corpus only compounds if users keep curating - but they are no longer the headline scoreboard.

## What it changes about the acquirer / buyer set
Prep-doc set was games-data (Newzoo, Sensor Tower, Video Game Insights), platforms (Discord, IGDB/Amazon, Twitch-adjacent), publishers wanting first-party discovery data. The pivot **adds a licensee layer above the acquirer layer**:
- AI / recommendation-infra companies and games-adjacent AI products as **licensees** (recurring revenue), more than direct acquirers near-term.
- Data marketplaces / licensing aggregators.
- The end-state acquirer is more likely a **data company or a games-data player buying the corpus**, less likely a consumer-platform buying the app. That sharpens the prep-doc point: an acquirer underwrites the dataset, not the app - the pivot just makes that explicit and moves it to the center.

## Risks to pressure-test (mostly with Peter, one with Lawyer)
1. **Is games-preference data actually valuable to "AI entities," or does everyone underpay for it?** Narrow taste graphs are valuable to a *games* recommendation AI, far less to a general LLM lab. This is the core Peter/Newzoo question - scarce asset or nice dataset nobody pays real money for.
2. **Rights / consent (GDPR) - hard gate.** Licensing EU users' preference data for AI use needs a lawful basis and ToS/privacy coverage that almost certainly was not written for this. This gates the whole pivot. Route to Lawyer before any buyer conversation gets concrete.
3. **User-trust collision.** "We sell your taste data to AI" can spook the engaged 20% who are the entire corpus engine. Framing + consent matter; the KM Troedsson-era "didn't deliver on the identity promise" trust gap is the relevant precedent.
4. **Defer-the-revenue-question risk** (see fork section) - the pivot must carry a concrete near-term proof point or it becomes another deferral.

## Net recommendation
Endorse the direction - it is the smartest available reframe and it points the company at its real asset. But land three things with Johan/Peter:
- Re-cut the KPI ask so the **corpus + rights** layer leads (above).
- Get Peter's blunt valuation of the data thesis (scarce vs underpaid) and his read on likely first buyers - this is his unique value.
- Open the **data-rights question with Lawyer now** (GDPR lawful basis + ToS), because it gates everything downstream and is invisible until someone checks.
- Hold the pivot to **one paid pilot / LOI in ~6 months** so "reduces near-term revenue pressure" does not quietly become "defers revenue indefinitely."

---
*Sources: Gemini notes "RankOne - Robert + Peter sync" Jun 17 2026 (Gmail thread 19ed4cc4fc7e2428, raw log rko-002); rankone_peter_sync_prep.md; rankone_kpi_dashboard_ask_johan.md; wiki/company/rankone.md.*
