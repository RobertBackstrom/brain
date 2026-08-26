# Answers to Peter's three asks — RankOne value, moat, personas

Draft for Robert to review, then bring to Peter (and into the advisory-board discussion). Grounded in the actual Pulse "Pragmata Timeline v3" report + the R1 agent. Prefix rko, ties to rko-003.

Peter's three asks (WhatsApp, Insights Feedback group):
1. 3-5 ways Insights have a direct impact on a developer's costs/revenues.
2. A value×moat matrix (Y = business use cases with monetary impact; X = unique data assets).
3. User personas — who can work with an API vs who needs help/visualized features, and how to offer the service without giving away the moat.

---

## 1. Five ways Insights move a developer's P&L

Each tied to the specific budget line it touches, strongest first.

1. **Lower CAC by picking the right creators.** The creator distribution + funnel + reach data shows which creators actually over-index with your audience, and that the mid-tier (101-1k followers) both dominate and convert. Spending a UA/influencer budget on the right 20 creators instead of spray-and-pray is the single biggest lever. Touches: **marketing/UA spend** (efficiency, direct saving).
2. **De-risk the launch call (price, positioning, genre framing) before the money is committed.** Comparables + KPI benchmarks + over-index tell you if your framing and price are right. One avoided mispricing or wrong-genre positioning on a launch is worth more than a year of subscription. (Real example: on a client pitch the tool argued $14.99-19.99 over a sub-$10 brief, with a comparables rationale.) Touches: **launch revenue** (protection).
3. **Find cross-promotion and co-marketing partners you'd otherwise miss.** The FROM/inflow + affinity-overlap data names the exact communities and games your audience already lives in - a ready target list for bundles, cross-promo, and creator collabs at near-zero CAC. Touches: **incremental wishlists/sales** at low cost.
4. **Point the roadmap and the store creative at what the audience actually values.** The library/keyword analysis surfaces the audience's real identity (for Pragmata: "surreal horror" + "custom volume / stereo sound" audio controls). Leading marketing - and dev priority - with the feature they care about is a conversion and retention lever, and it stops wasted dev on things they don't. Touches: **conversion + retention, dev efficiency**.
5. **Recruit playtesters / run surveys / drive wishlists from reachable profiles.** The reachable-profile counts turn insight into action: assemble a targeted playtest or survey cohort without paying a panel provider, and use the same audience as a pre-launch wishlist channel. Touches: **user-research cost** (saving) + **pre-launch wishlist volume**.

Framing line for Peter: 1, 3 and 5 are cost savings; 2 and 4 are revenue protection/upside. All five are things a dev pays real money for today (agencies, panels, consultants) - which is the price anchor.

---

## 2. Value × moat matrix

**Moat = the four data assets RankOne has that Newzoo / GameDiscoverCo / SteamDB do not:**
- **A. Taste graph** - psychographic over-index + cross-game affinity, drawn from a curated audience *broader than your own players*.
- **B. Timeline** - change over time (daily snapshots of the whole games DB since early 2024): rank moves, `NEW` tags, affinity/volume deltas.
- **C. Reachable profiles** - actual identified people you can activate (playtest, survey, creator outreach).
- **D. Inflow / overlap** - community-to-community flow (FROM/PAST/PRESENT/FUTURE).

| Use case (value, monetary impact) | A. Taste graph | B. Timeline | C. Reachable | D. Inflow/overlap | Unique to R1? |
|---|:--:|:--:|:--:|:--:|:--:|
| 1. Creator selection → lower CAC | ● | ● | ● | | **Yes** |
| 2. Launch price/positioning de-risk | ● | ● | | ○ | Partly (comps exist elsewhere; over-index + trend don't) |
| 3. Cross-promo / co-marketing partners | ● | | ○ | ● | **Yes** |
| 4. Roadmap + store-creative priority | ● | ○ | | | **Yes** (taste-graph depth) |
| 5. Playtest / survey / wishlist recruit | ○ | | ● | | **Yes** (activation) |
| 6. Competitor / category watch (trackers) | ○ | ● | | ● | **Yes** (the timeline) |

● = core to the use case, ○ = supporting. Read the "Unique" column as the defensibility line: where an X-axis asset is the engine, a competitor can't copy the output.

The one-sentence version for the board: **the taste graph tells you *who and what*, the timeline tells you *which way it's moving*, and the reachable profiles let you *act on it* - and only RankOne has all three on the same audience.**

---

## 3. Personas + how to offer the service without giving away the moat

### Who the users are, and how each wants to consume it

1. **Publisher / UA / marketing lead (mid-large studio).** Data-fluent, has a BI stack, wants **API** access to pull into their own dashboards. Highest willingness to pay - and the highest moat-leak risk, because they *can* extract. Serve with API, but scoped/rate-limited, and lead them onto the timeline (trends/trackers) so a one-time dump loses value fast.
2. **Indie founder / small-team dev.** Not data-fluent, no BI stack. Needs the **visualized Pulse report + the AI agent** to ask questions in plain language. Lower ticket, higher volume. This is the self-serve funnel and the marketing surface.
3. **Biz-dev / partnerships (Robert's seat).** Wants the FROM/overlap + comparables to find deals and partners. **AI agent + exportable target lists.**
4. **Investor / M&A / consultant.** Wants category-level trends + comparables for diligence. **Periodically published insights** (the brand-building pieces) + the agent.

### The access model that protects the moat

Peter's own instinct is right - two avenues, and I'd structure them as:

1. **Predefined, visualized features around the top 2-3 use cases** (Pulse report, creator finder). Safe, self-serve, the top-of-funnel. This is what indies buy and what markets RankOne. You show the value without exposing the raw graph.
2. **AI agent + API for power users.** The paid, high-value tier.

Four rules keep the moat intact while doing this:
- **Sell the trend, not the snapshot.** A static snapshot gets scraped once and resold; a live timeline (trackers, watchlists on your games/competitors) has to be re-subscribed. This is the recurring-revenue engine and the anti-extraction defence in one - exactly the "don't let people suck out all the data" point.
- **Expose derived analyses, not raw per-profile rows.** Over-index, affinity, funnel, inflow are safe to show; the underlying profile-level data stays inside.
- **Keep activation inside RankOne.** Reaching the reachable profiles (playtest/survey/creator outreach) is a service you pay RankOne to run - un-scrapeable by design, and a second revenue line.
- **Label measured vs modeled + show confidence/n.** (Already being added off the R1 feedback.) Trustworthy data is what justifies the price; it also quietly signals where the proprietary depth is.

### One UX point that ties to personas
Both Peter and Johan flagged that the agent should ask for the **objective first** and help quantify the value ("I'm launching Game X, limited budget, help me be efficient"). That maps cleanly onto onboarding: the agent opens by asking the goal, then routes to the right one of the five use cases above. For persona 2 (indies) this is essential - it's the difference between a blank prompt box and a guided tool.

---

## Suggested next step for Robert
Bring section 1 (the five P&L levers) and the section 2 matrix to the next Peter sync as the shared reference he asked for. If it lands, turn the matrix into the "overview/reminder as we develop and launch" artifact Peter described (Y = use cases, X = data assets), and fold the persona/access model into the rko-003 AI-data-pivot plan.
