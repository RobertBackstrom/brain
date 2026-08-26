# Prep note — RankOne sync with Peter Warman (Wed Jun 17, 10:00)

## Addendum (2026-06-17, pre-call) — the pending sentiment numbers, now confirmed
Earlier this prep flagged App Store / Play / Discord as "pending, once the browser frees up." Pulled them. They all reinforce the read - the public/mobile footprint is near zero against 100k web users:
- **iOS App Store** (id6757848256, "Rankone: Game Library Tracker"): **0 ratings, 0 reviews.** Apple's page literally says "hasn't received enough ratings or reviews to display an overview." Confirmed.
- **Google Play** (`co.median.android.pwwwlxl`): **1,000+ installs, no rating shown** (too few ratings to display). 100k web users, ~1k Android installs.
- **Mobile app = a webview wrapper, not native.** The Android package is `co.median.android.*` - that is Median.co (ex-GoNative), an off-the-shelf "wrap your website as an app" service. So the 2026 "iOS + Android launch" is the existing web product in a wrapper, not a built-for-mobile app. Worth knowing before anyone treats the mobile launch as a growth lever - it is a distribution checkbox, not a new product surface.
- **Discord public invite (discord.gg/rpQhHJeRgp): dead.** Confirmed via the Discord API (404 / Unknown Invite), not just a static-fetch miss. Their community door in the shareholder-email signature is broken.
- **First-party sentiment stays positive for the core** (413k reviews, 2.6M curated relations, top-10 Twitch tool) - the engaged 20% love it; the external footprint is ~zero.

**Takeaway for the call:** for an 8-year-old consumer product, near-zero public ratings + a wrapped-webview mobile "launch" + a dead community link is the "nice-to-have R&D" read made concrete. They have never pushed for the public traction a growth story needs.

A clean standalone "KPI dashboard ask for Johan" is drafted at `drafts/rankone_kpi_dashboard_ask_johan.md` - bring it into the 10:00, refine with Peter, hand to Johan after.

## My take in one line
Your "nice-to-have R&D" read is correct, and the numbers confirm it. RankOne is 8 years old, has a genuinely loved core product and a real data asset, but it is optimising for craft instead of for a trajectory. The fork you describe (aggressive growth vs profitability) is real, and the decision window is now: runway to ~mid-2027 means they need to commit in the next 6-9 months while there's still enough runway to execute the choice.

## The fork, sharpened
- **Path A - venture-scale growth / position for acquisition.** Needs one compounding metric and a buyer thesis. For a data company that's retention + B2B Insights traction, not cumulative signups. Acquirer set = games-data players (Newzoo, Sensor Tower, Video Game Insights), platforms (Discord, IGDB/Amazon, Twitch-adjacent), or a publisher that wants first-party discovery data. Peter is literally the canonical comp here.
- **Path B - profitability.** Low Umeå cost base (~5 heads) makes breakeven reachable IF the B2B Insights line converts. But profitability throttles growth spend and kills the Path A optionality. You can't sit between them.
- **The trap (current state).** Organic growth is ~1.9%/month (~25%/yr) - too slow to excite a growth VC. Revenue 89 Tkr - too thin to approach profit. Neither narrative is fundable at scale today. That's the "nice-to-have R&D" feeling, quantified.

## Their growth KPIs - what they report vs what matters
What they currently put forward (State of RankOne, May 2026):
- Users **101,155** (cumulative - a vanity number)
- Reach **77.8M** (sum of users' Twitch following - not their audience, also vanity)
- MAU **20%** (the one honest engagement number - implies ~20k real actives, 80% churned)
- Runway to **2027-06-24**

What a VC / acquirer actually diligences, and which they do NOT foreground - this is the ask for Johan:
1. **New-user growth RATE** (not absolute) - currently ~1.9%/mo
2. **Retention cohorts** - D1/D7/D30 or month-N curves. MAU 20% suggests these are weak; this is the single most important number for a data/social product.
3. **Activation** - % of signups who build a real profile / add N games
4. **Engagement depth** - games logged + reviews per active user (the engaged core looks strong here)
5. **CAC + channel mix** - historically ~10 SEK/user via streamers; is that still true and does it scale?
6. **B2B Insights revenue** - number of paying dev customers, pipeline, ACV / ARR. This is the money metric and it's basically absent from the deck.
7. **Data-asset metrics** - coverage / uniqueness vs competitors. This is what an acquirer is really buying.

The core conversation: the gap between what they celebrate (101k, 77M reach) and what a buyer underwrites (retention + ARR).

## User sentiment - what we know, and how to get hard numbers
What we can see:
- The engaged core is real and passionate: **2.6M** manually-curated game relations (+51% in a year), **413k** written reviews (+60%), and the Twitch extension is cited as a top-10 Twitch tool. The 20% who stay clearly love it.
- The 80% who churned are the open question. 20% MAU is low for an identity/social product that needs network effects.
- Historical skeptic signal worth re-testing: KM Troedsson (2020) felt it under-delivered on the "connect all my accounts, one gaming identity" promise and that the valuation was high. Has the 2026 product (Profile Similarity, iOS, feeds) closed that gap?

There is **no publicly aggregated sentiment score**. To get real signal I can pull: App Store + Google Play ratings and review text (fresh - iOS just launched), the Discord tone (discord.gg/rpQhHJeRgp), and Twitch extension reviews. Say the word and I'll have hard numbers before the call.

## What to get specifically from Peter (his unique value)
- He ran Newzoo. He knows precisely what games-market data is worth, who pays for it, and what an acquirer diligences. Use him to pressure-test the B2B Insights thesis: is curated-profile data a defensible, sellable asset, or a nice dataset that everyone underpays for? His own likely skepticism about data depth is exactly the risk to surface.
- Ask his blunt read on the fork: does RankOne have a genuine venture-scale story, or is the honest answer "profitable niche tool / acqui-hire"? He can save you months.
- Map the acquirer/partner set with him before anyone gets approached.

## KPI trajectory (from the full State of RankOne series, 2023-2026)
Johan has sent a monthly "State of RankOne" since 2021. User-count anchor points:
- 2023-05: **39,254** profiles (mostly influencers)
- 2023-06: **40,932** (+1,678/mo)
- 2025-10: **~90,000** ("about to surpass 90k"), reach >70M Twitch
- 2026-05: **101,155**, reach 77.8M, MAU 20%, runway 2027-06-24

Read: ~+49k users over the 28 months Jun'23->Oct'25 (~1,750/mo), then ~+11k over the 7 months Oct'25->May'26 (~1,570/mo). Net adds are roughly **flat ~1.5-1.8k/month for years = linear growth, decelerating in percentage terms.** That is the single most important fact: this is not a compounding curve, and no amount of feature polish changes that without a step-change in acquisition or a different (B2B) engine. The 7.3 MSEK round (4.8 equity + 2.5 convertible) closed Mar 2026 buys runway, not a new trajectory.
Historical note: a Series A pitch deck (2021) and pre-IPO/listing talks (Eminova) date back ~5 years with a stated "become world-leading" ambition - the "stuck in the middle" pattern is long-standing, not new.
(I have the anchor points from the email bodies; exact monthly figures live in the attached PDFs - I can extract the full month-by-month chart if you want it.)

## Public sentiment - what's actually out there (pulled 2026-06-15)
The honest headline: **there is almost no external third-party sentiment to read yet**, which is itself a finding.
- **iOS (official):** "Rankone: Game Library Tracker" by RankOne Global AB (App Store id6757848256) - **0 ratings, 0 reviews.** Brand new (launched ~May 2026). They have 100k web users but have not converted them into App Store ratings.
- **Watch out:** a different "Rank One" app (AllPlayers Network, a school-athletics app) has 3.72 stars / 556 ratings. Not them - don't let anyone cite it.
- **Google Play:** rating not exposed via static fetch (JS-rendered); needs a rendered browser, which was occupied. Pending.
- **Discord:** the public invite in their shareholder-email signature (discord.gg/rpQhHJeRgp) returns 404 - dead link. Minor, but their public community door is broken.
- **On-platform (first-party) sentiment is the real signal and it's positive for the core:** 413k written reviews, 2.6M curated relations, self-claimed top-10 Twitch tool 3 years running. The engaged 20% clearly love it; the external/public footprint is near zero.

Conclusion for the call: for a consumer product 8 years in, a near-zero public review footprint reinforces the "nice-to-have R&D" read - they haven't pushed for the public traction a growth story needs. (I can get the Play rating + read actual App Store/Play review text once the browser frees up.)

## Deck read - "The Future of Creation v2.1" (Nov 2025)
**Positioning:** "Rankone is for play what LinkedIn is for work" - self-curated gaming identity → "the most authentically sourced taste graph in gaming." TAM framed as LinkedIn-scale (1B+ self-curated identities).
**Business model (3 subs):** Rankone+ $5/mo (gamers), Create $39/mo (creators), Pro $295/mo (devs, incl. API). Plan assumptions: conversion 1% / 1.25% / 1.5%; churn 10% / 12.5% / 15%. Revenue plan ~$17k (2025) → $464k (26) → $1.1M (27) → $4M (28) → $10.6M (29).
**The ask:** $3M for 20%, max 5 investors (same $3M/20% that closed Feb 2026 at just 7.3 MSEK / 80 MSEK pre - the market already discounted this deck heavily).

**Where it's genuinely strong:**
1. **Retention, and it's improving:** 7-day 36.3% (up from 32.8% YoY), 1-day 42.8%, 30-day 26.7%. For a niche product that's a real, defensible engagement core - the best number in the deck.
2. **Capital efficiency:** 68M reach / 100k users / top-10 Twitch tool on **<$10k marketing**, 105% CAGR. That's a real organic engine, not paid growth.
3. **The taste-graph / authentic-data asset** is differentiated and exactly what Peter (Newzoo) can value.

**Where Peter (or any VC) will poke holes:**
1. **Monetization is entirely projected.** Current ARR ≈ $0; paid tiers barely launched (Create beta Q3'25). The whole $10.6M-by-2029 rests on 1-1.5% conversion + the stated churn, none of it yet proven. That's the crux of "growth vs profitability" - the revenue line is a model, not a track record.
2. **The growth curve has to bend 90x.** 6 years to reach 100k users; the plan assumes 100k→10M in 4 years. Nothing in the linear history supports the inflection.
3. **Tiny absolute active base:** ~18.8k MAU. "101k users / 68M reach" are top-of-funnel; the engaged core is small.
4. **It's a growth-raise pitch, not a profitability story** - which is precisely the path the market just declined.

**Two corrections to flag:**
- **Peter Warman is listed as an ADVISOR in their own deck** (with Ulrika Viklund), not a board director - and holds ~1.8% via Warman Vision BV. Worth confirming how you two are actually positioned (advisor-level vs board-level mandate) before the call.
- **CZP (Creation Zero Point Holding AB) shows as 4.7%** on the deck cap table - i.e. Robert's stake post-round is ~4.7%, diluted from the old ~5%.

## Anton Wallén / GeoGuessr - the most useful comp on the board
Robert's instinct is right: Anton (GeoGuessr co-founder, came in via the Feb-2026 round) is the single most relevant mind for the path RankOne probably *should* take.
- GeoGuessr is the canonical case of a **niche, streamer/Twitch-driven, community product that grew massively organically and became highly profitable WITHOUT chasing growth-VC** - then took outside money from a position of strength. That is almost exactly RankOne's shape (Twitch-native, creator-driven, capital-efficient), but GeoGuessr actually cracked monetization and virality.
- What Anton can teach/de-risk: (1) converting passionate-niche + streamer reach into paying users without burning capital, (2) the viral loop that took GeoGuessr from cult tool to mass, (3) what "default-alive then raise from strength" looks like in practice.
- So Anton's playbook is evidence *for* the profitability-first lean - and a credibility asset if a future raise is repositioned around a proven, profitable community engine rather than a pre-revenue growth bet. Get his honest take on whether RankOne's funnel can do what GeoGuessr's did.

## Suggested 60-min agenda
1. Align on the diagnosis (5 min) - agreed it's "nice-to-have R&D" and the fork is now?
2. The KPI dashboard we need from Johan (10 min) - agree the exact ask above.
3. B2B Insights thesis - Peter's Newzoo read (20 min) - is there a real revenue/asset story?
4. The fork: pick a default (growth vs profitability) to take to Johan (15 min).
5. Division of labour + next step with Johan (10 min).
