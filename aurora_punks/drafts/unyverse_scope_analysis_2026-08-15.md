# Unyverse - scope and cost sanity check

**Date:** 2026-08-15 | **Ticket:** apb-029 | **Internal advisory memo for Robert. Nothing here goes to Erik or any third party.**
**Prepared by:** BizDev agent
**Builds on:** `erik_afrime_bizdev_analysis.md` Part B (studio maturity, team, funding, the 670M TAM claim) and `erik_valuation_analysis_2026-08-15.md` (the 30 % bid). Neither is repeated here.
**Question this answers (Robert, 2026-08-15):** can the prototype Afrime has today be developed as far as it needs to go on the money Erik is putting in?
**Deadline:** Aurora Punks AB + Strategic Entertainment meeting Monday 2026-08-17, 16:00 CEST.

---

## 0. Assumptions, stated up front

These drive every number below. If one is wrong, tell me which and I will rerun it.

1. **FX 9.7 SEK/USD**, the rate used in the 2026-08-15 valuation analysis.
2. **AP sell rate: ~104 000 SEK per seat-month, about $10 700.** Two independent sources agree. The rate card retainer anchor is 100 000 SEK/month for a mixed-discipline seat. The K2C contract is 5 600 000 SEK gross across nine months for a team of six, which is 622 000 SEK/month, or 103 704 SEK per seat-month. I use $10 700 throughout and flag where a cheaper blend changes the answer.
3. **AP net margin on a network-model co-dev: 17 %.** That is the K2C actual (965 000 SEK net on 5.6M SEK gross, per `k2c_reconciliation_2026-07-13.md`). AP keeps 17 %, the rest passes to subcontractors.
4. **Current build state** is Erik's own description on WhatsApp 2026-08-15: a playable combat test area and a character creator, described by him as "while it feels like there's not a lot there, there is a budding unique fighting game meets rpg combat mechanic." **I have not seen either build.** He said he would send links that day and they had not arrived when this was written. Everything below treats the build as two isolated systems with no connected game around them, which is what his description and Afrime's public statements both indicate.
5. **The money.** The memo allocates $1.0M to $2.0M to "Unyverse development" out of a $1.5M to $5.0M SBA facility. On WhatsApp Erik was more specific: "$1m in cash to develop one of my games (most likely Unyverse)" plus $100K reserve plus $100K for OIP squads. So **$1M is the working number and $2M is the ceiling.** I model both.
6. **Critically: the memo never says the $1-2M is Aurora Punks' contract value.** It says Unyverse development. Afrime has its own distributed team of roughly 15 people across the US, Ghana and Nigeria who are also paid out of it. Section 4 models what happens when they take their share.
7. Where a comparable's budget is public I cite it. Where it is not, I say so rather than estimating one.

---

## 1. What an action-RPG of this ambition costs to finish

### 1.1 The method

Team size times duration times blended seat cost. I express everything in **seat-months** so the scope question and the money question use the same unit, and so a change in rate assumption does not change the scope conclusion.

At AP rates, **$1M buys 93 seat-months and $2M buys 187 seat-months.** Hold those two numbers.

### 1.2 What Unyverse still needs, honestly

The two things that exist are a combat sandbox and a character creator. Neither is a game. What is missing is the entire connective structure, and it is the expensive part:

1. World and level content. A semi-open-world continent means terrain, biomes, streaming, navmesh, points of interest, traversal, and art passes on all of it.
2. Enemy and boss roster. For fighting-game-grade combat this means unique movesets, AI behaviour trees, tells and counters, and an animation set per enemy several times larger than a normal ARPG enemy needs.
3. Progression and RPG systems. Loot, stats, skill trees, crafting, economy, save/load, balance.
4. Narrative delivery. Quests, dialogue, VO, cinematics, the story hub they showed in May 2026.
5. UI and UX across all of the above, which on an RPG is a full-time discipline for the whole project.
6. Audio, music, mix.
7. Production infrastructure. UE5 needs Perforce, a build farm, automated testing and a release pipeline. Across three or four sites this is a real line item, not an afterthought.
8. QA, certification, age ratings, localisation, launch.

Two systems is roughly ten per cent of the work by cost. The remaining ninety per cent is what the budget question is actually about.

### 1.3 Two production shapes, costed

**Shape A: Unyverse as publicly described.** Semi-open world, fighting-game combat depth, bespoke character creator, PC in 2027 with stated ambition toward "every platform, including mobile."

1. Team at full production: 28 to 35 seats.
2. Duration remaining from today's state: 36 to 48 months. That is not pessimism, it is what pre-production to gold takes on a first title with a bespoke combat pillar.
3. **1 000 to 1 700 seat-months.**
4. At AP rates: **$10.7M to $18.2M.** On a blend that runs a meaningful share of seats through Ghana and Nigeria contractors, plausibly $6 000 to $8 000 per seat-month, it lands at **$7M to $12M.** I have not verified West African contractor rates from any source in the repo, so treat the blended figure as the softer of the two.

**Shape B: the cheapest version that is still a complete ARPG.** No open world, hub-and-spoke level structure, 12 to 18 hours of content, trimmed character creator, PC only.

1. Team: 18 to 22 seats.
2. Duration: 28 to 34 months.
3. **500 to 750 seat-months.**
4. At AP rates: **$5.4M to $8.0M.** On the cheaper blend: **$3.5M to $5.3M.**

So the defensible answer to "what does it cost to finish" is **$3.5M at the absolute floor for a much smaller game than the one being described, and $7M to $15M for the game as described.** Anything below $3.5M is not a finished ARPG under any set of assumptions I can construct.

### 1.4 Comparables

| Title | What it tells us | Budget public? |
|---|---|---|
| **Clair Obscur: Expedition 33** (Sandfall, UE5, 2025) | The best comparable available. Creative director Guillaume Broche stated publicly that the budget was **under $10M**. About 20 in-house and 30 to 40 including freelancers, battle animation outsourced to Korea. The studio **deliberately avoided an open world** and used linear authored environments to control cost. No character creator. Turn-based combat, far cheaper in animation volume than real-time fighting-game combat. Publisher-funded. It went on to 8M copies. | **Yes, stated by the studio.** |
| **Sifu** (Sloclap, 2022) | The outcome comparable for a combat-first, tightly scoped premium action game. 1M copies in three weeks, 3M by Feb 2024, 4M+ by May 2025. Sloclap's first title Absolver ran 2015 to 2017. Studio is 50 to 60 people today. | **No. Budget never disclosed. Do not quote one.** |
| **Aurion: Legacy of the Kori-Odan** (Kiro'o Games, Cameroon, 2016) | The nearest African-studio precedent for an African-mythology ARPG. Kickstarter target EUR 40 000, raised about EUR 50 000 from 1 310 backers. Kiro'o raised **$305 000 total in crowdfunding across 2013 to 2018.** 2D hand-drawn, a fraction of Unyverse's technical ambition. | Funding public, sales not disclosed. |
| **Black Myth: Wukong** | Widely reported at roughly $70M and 140 people. Ceiling reference for the lane, not a target. | Reported, not company-confirmed. |

The Clair Obscur line is the one to take to Monday. A 30-person team with a publisher behind it, on UE5, in the same broad genre, spent close to $10M and got there by explicitly refusing an open world, refusing a character creator, and choosing the cheaper combat model. Unyverse as described asks for all three of the things Sandfall cut, on a tenth of the money, with a first-time team.

---

## 2. The gap

**$1M buys 93 AP seat-months. $2M buys 187.**

| Target | Seat-months needed | Short by, at $1M | Short by, at $2M |
|---|--:|--:|--:|
| Shape B, cheaper blend ($3.5M) | ~500 | **3.5x** | **1.8x** |
| Shape B, AP rates ($5.4M to $8.0M) | 500 to 750 | **5.4x to 8.0x** | **2.7x to 4.0x** |
| Shape A, cheaper blend ($7M) | ~1 000 | **7x** | **3.5x** |
| Shape A, AP rates ($10.7M to $18.2M) | 1 000 to 1 700 | **11x to 18x** | **5x to 9x** |

**The answer to Robert's question is no.** The prototype cannot be developed to a shippable, commercially viable Unyverse on $1-2M. The shortfall is between 3.5x and 8x against the cheapest complete version of the game, and roughly 10x against the game as it is publicly described.

Two things this does not mean:

1. It does not mean the money is useless. $1M is close to exactly the right size for a vertical slice and a public demo, which is what Afrime's own public statements say they are doing. Their stated production focus is "moving from pre-production into a playable MVP, followed by a polished demo" to "attract lead investors and unlock further participation." The $1M is demo money. The problem is that the memo calls it finishing Unyverse.
2. It does not mean Afrime is being dishonest. It means nobody has yet written down a cost-to-complete number and compared it to the money. Establishing that is the job on Monday, and it is section 6.

The load-bearing worry is not the size of the gap. It is that the memo commits AP's capacity for 18 months against a number nobody has reconciled to a scope, while leaving AP's own economics on the deal marked TBD. If AP takes an 18-month contract to build toward a target that is 5x underfunded, the predictable ending is that the money runs out around month 14 with no shippable product, AP holds an unpaid final milestone, and AP is by then a shareholder-adjacent counterparty rather than an arm's-length vendor.

---

## 3. What scope does fit $1-2M

Four shapes. Numbers are AP seat-months at $10 700, so they sit at the conservative end.

### 3.1 Shape 1: vertical slice and public demo

1. **Ships:** a 30 to 45 minute playable demo on Steam. Character creator as the opening, one authored space, three to five encounters including one boss, using the combat mechanic that already exists. Plus the thing that matters more than the demo, which is a production plan and a content pipeline built from measured data rather than guesses.
2. **Team and duration:** 8 to 10 seats, 10 to 12 months. **80 to 120 seat-months, $0.9M to $1.3M.**
3. **What it needs to hit:** it sells nothing. Success is one signed lead investor or publisher, plus wishlists. A demo landing on a Steam festival beat should target 40 000 to 60 000 wishlists to be a credible fundraising asset.
4. **Honest read:** this is the correct use of $1M and it is what Afrime already says it is doing. It is not finishing the game. If this is what the deal actually is, it is a clean, well-defined piece of work AP can price and deliver, and I would be comfortable with it. It just has to be named as what it is in the contract.

### 3.2 Shape 2: combat-first premium release (recommended)

1. **Ships:** a complete, small, premium action game built entirely out of the two things that already exist. The character creator is the front door and the retention hook. Behind it sits a stage-based or run-based combat campaign, five to seven authored encounters plus a boss ladder, six to ten hours plus replay, with a light narrative frame set in the Unyverse world. PC first, $19.99 to $24.99.
2. **Team and duration:** 10 to 12 seats, 15 to 18 months. **150 to 215 seat-months, $1.6M to $2.3M.** Fits $2M. Fits $1.5M at 9 to 10 seats and a slightly shorter tail.
3. **What it needs to hit:** at $19.99 with roughly $14 net per unit after platform and VAT, $2M of development returns at about 145 000 units. Add marketing and the success bar is 200 000 to 250 000 units. Sifu shows the ceiling in this lane is high, but the median combat-focused indie does not reach 200 000, so treat that as the bar rather than the expectation.
4. **Why I recommend this one:** it is the only shape where the assets that exist today are the whole product rather than a tenth of it. Everything Afrime has built stays in the shipped game. It gives the IP a real market test on a budget that exists. And if it works, it is the strongest possible pitch for the full ARPG later, because it proves the combat sells rather than asserting it.
5. **Sequencing that protects everyone:** run Shape 1 as the first three to four months inside Shape 2. The slice becomes milestone one of the combat-first game, so if the money stops or the SBA facility does not close, nothing built is thrown away and Afrime still holds the fundraising asset.

### 3.3 Shape 3: Early Access chapter one

1. **Ships:** the character creator, one region, and the opening six to eight hours of the story into Steam Early Access at $19.99 to $24.99, with a published roadmap to 1.0.
2. **Team and duration:** 11 to 13 seats, 16 to 20 months to EA. **175 to 260 seat-months, $1.9M to $2.8M.** Only fits at the very top of the $2M range, and only if 1.0 is funded from EA revenue or the next round.
3. **What it needs to hit:** 60 000 to 100 000 wishlists at EA launch to produce a first week that funds continuation.
4. **Why I rank it below Shape 2:** story-driven RPGs generally underperform in Early Access, because players wait for 1.0 and the roadmap spoils the narrative. More importantly it commits publicly to finishing the whole game later without having funded it. That is the same gap, deferred, and now with an audience watching.

### 3.4 Shape 4: creator-first free product plus UGC

1. **Ships:** the character creator as a free standalone with photo mode, sharing and a light social or fashion layer, monetised on cosmetics, connected to the Fortnite Creator map and mod presences Afrime already runs.
2. **Team and duration:** 6 to 8 seats, 10 to 14 months. **60 to 110 seat-months, $0.6M to $1.2M.**
3. **What it needs to hit:** free-to-play cosmetic economics need continuous content, live-ops staffing and an acquisition budget indefinitely. Standalone it is unlikely to pay for itself, and it converts a one-time development cost into a permanent operating cost.
4. **Better use of the same idea:** run it as free audience building and wishlist generation feeding Shape 2 or Shape 3, funded out of marketing rather than presented as the revenue product. As a marketing asset the creator is genuinely strong. As a business it is the weakest of the four.

### 3.5 Summary

| Shape | Seats | Months | Seat-months | Cost at AP rates | Fits $1M | Fits $2M |
|---|--:|--:|--:|--:|:--:|:--:|
| 1. Slice and demo | 8-10 | 10-12 | 80-120 | $0.9M-1.3M | Yes | Yes |
| 2. Combat-first premium (recommended) | 10-12 | 15-18 | 150-215 | $1.6M-2.3M | No | Yes |
| 3. Early Access chapter one | 11-13 | 16-20 | 175-260 | $1.9M-2.8M | No | At the top only |
| 4. Creator-first free product | 6-8 | 10-14 | 60-110 | $0.6M-1.2M | Yes | Yes |
| B. Cheapest complete ARPG | 18-22 | 28-34 | 500-750 | $5.4M-8.0M | No | No |
| A. Unyverse as described | 28-35 | 36-48 | 1 000-1 700 | $10.7M-18.2M | No | No |

---

## 4. The 18-month framing

The memo sells this as "contracted labor stability for 18 months." Here is what that is worth.

### 4.1 What the money buys per month

| | $1M over 18 months | $2M over 18 months |
|---|--:|--:|
| Per month, USD | $55 600 | $111 100 |
| Per month, SEK | 539 000 | 1 078 000 |
| **AP seats at 104 000 SEK/seat-month** | **5.2** | **10.4** |
| AP net margin at 17 %, SEK/month | 92 000 | 183 000 |
| AP net margin over the full 18 months, SEK | ~1.65M | ~3.3M |

For comparison, K2C runs at 622 000 SEK/month gross for six seats over nine months, and yields about 110 000 SEK/month in AP net margin.

### 4.2 Does it fill the hole after MS7 Gold?

K2C hits MS7 Gold on 2026-12-03 and the contract ends. The data room states AP's recurring floor as roughly 290 000 SEK/month, made of the Netlight placement at 150 000 and the co-dev margin leg at about 140 000.

1. **At $1M, no.** It delivers about 92 000 SEK/month of net margin against the 140 000 that K2C contributes. The floor falls from 290 000 to about 242 000 SEK/month. It is a partial replacement.
2. **The break-even point is about $1.53M.** That is the level at which an 18-month Unyverse engagement restores the co-dev leg at 140 000 SEK/month net.
3. **At $2M, yes and a little more.** The floor goes to about 333 000 SEK/month.

On the calendar it lines up. Eighteen months starting January 2027 runs to June 2028 and covers the hole cleanly. But nothing is contracted, the memo explicitly leaves Unyverse economics TBD, and the money sits downstream of an SBA approval whose eligibility for acquiring a Swedish AB is itself unverified. So this is a plan and not a bridge, and it should not be treated as covering 2027 in any board conversation until there is a signed co-dev agreement.

### 4.3 The dilution nobody has priced

The $1-2M is allocated to Unyverse development, not to Aurora Punks. Afrime has roughly 15 people across three countries who are paid out of the same pot. If Afrime's own team takes half, AP's share over 18 months is **2.6 to 5.2 seats**. That is one senior engineer and a part-time producer. It is not labour stability and it would not replace K2C.

There is a second reduction on top. AP's network model passes 83 % of a co-dev contract straight through to subcontractors. So the 18 months of stability is worth about **1.65M SEK of retained margin at $1M**, roughly 92 000 SEK per month, or about $9 400 a month to AP itself. That is the honest measure of what the 18 months is worth to Aurora Punks as an enterprise, as opposed to what it is worth to the subcontractor bench.

### 4.4 What the 18 months costs that a normal co-dev does not

Eighteen months of AP capacity locked to Unyverse is eighteen months not available for a Raw Fury follow-on, the Starbreeze co-dev Robert is pitching, Equinox, or Teef. A third-party co-dev at the same value carries no equity entanglement. This one comes attached to a counterparty who will simultaneously hold 30 % of AP, who has a salary in the model at Robert's level, and whose acquisition debt the memo proposes servicing out of AP's monthly operating revenue. That is the triple-exposure caution from the July analysis, restated in scope terms: if Unyverse overruns, AP loses the contract, the capacity it reserved, and the counterparty's ability to service the debt sitting against AP's revenue, all at once.

---

## 5. Risk register, ranked by how much it moves the scope answer

**1. Production leadership. No named technical director or production lead.**
Erik is career PR, marketing and BD. Crandon is "creator." Afrime's own public description of the team is "a lean core team and a flexible network of collaborators across art, engineering, design, and audio." Nobody is publicly identified as owning the build, the schedule or the technical architecture. If the honest answer is that Aurora Punks is expected to supply that, then AP is not a co-dev vendor on this project, it is the development studio, and the contract has to be priced, staffed and structured accordingly. Robert's own time is the scarce input in that version and it is in nobody's budget. This is the largest risk because it determines whether any estimate can be trusted at all.

**2. Scope is not fixed to budget, and has been publicly declared unfixable.**
Crandon, in the PocketGamer interview: "the timeline is tied to quality. We're not interested in putting something out that undersells the experience." That is the most expensive sentence in the public record. A team that will not trade scope for time, on a budget already 5x short, overruns by construction. Anchoring scope to money before signing is the whole negotiation.

**3. Content volume for an RPG.**
This is where budgets actually die, and it is invisible from a combat test area. Quests, levels, enemies, bosses, loot tables, VO, cinematics, balance passes. It scales with the hours of gameplay promised and it is the least compressible cost in the project. Every ARPG that overran, overran here.

**4. Combat depth.**
Fighting-game-grade combat is the most animation-heavy and iteration-heavy thing a small team can choose. It needs a combat designer, a combat animator and a gameplay engineer working as a locked triad for the whole project. It is the hardest discipline to outsource, because the quality lives in the iteration loop rather than in the asset. Sandfall avoided this cost entirely by going turn-based and still spent close to $10M.

**5. Character creator scope creep.**
Creators are combinatorial. Every hairstyle has to work on every head, every garment on every body, every skin tone under every light. The bespoke requirement here adds two real technical lines a generic creator does not carry. Textured and coiled hair is expensive to render in real time, whether as strands or cards, and it needs physics. And per published craft writing on the subject, darker skin tones commonly render washed out or muddy, and lighting melanated skin is a genuine technical problem that is immediately visible to exactly the audience this game is for. To be fair to Afrime, the same source argues that offering diverse options is largely a reallocation of art time rather than an added cost. The expense is in building a creator at all, plus a dedicated skin and hair shading pipeline. The trap is that once the creator ships, every future outfit and hairstyle carries the full combinatorial multiplier forever. Note also that this is their strongest differentiator, so cutting it is not free either.

**6. Distributed team across three or four continents.**
US, Ghana, Nigeria, and Sweden if AP joins. Six to eight hours of timezone spread, payment rails, and UE5 infrastructure requirements that are non-trivial at those sites: Perforce, large binary sync, build farm access, power and connectivity reliability. Budget for infrastructure, and for a producer whose actual job is the seams between sites.

**7. First title at this scale.**
No shipped game of comparable ambition. First-time teams systematically underestimate the back half of a project. Any schedule Afrime gives should be read as a floor, and any budget as a floor.

**8. Platform and certification.**
Steam says Windows PC only, 2027. Public statements say "every platform, including mobile." Those are not the same project. A mobile version of a UE5 semi-open-world ARPG is a separate development effort rather than a port. Certification, compliance and age ratings are a real end-of-project cost that first-time teams routinely leave out.

**9. The Steam page is live with a 2027 date and no demo.**
The wishlist clock is running with nothing to convert. Their own plan is a public demo to unlock lead investors, and it has not landed. Minor next to the others, but a soft signal that the schedule has already slipped once.

---

## 6. The one question for Monday

> **What is your total cost-to-complete number for Unyverse, and what does the $1-2M buy inside it?**

This is the highest-information single question available, because every possible answer is useful:

1. **If he has a number and it is $8M to $12M**, the plan is honest, the $1-2M is a slice or demo tranche inside a larger financing plan, and AP's job is a well-defined piece of work Robert can price. That is a good deal, and section 3.1 or 3.2 is the shape of it.
2. **If the number is $1-2M**, the scope is not real, and Robert knows it in one answer without having to argue about it.
3. **If there is no number**, nobody has done production planning on Unyverse, which is the same finding as risk 1. It also tells Robert that whoever writes the plan is going to be him, which is a different engagement at a different price.
4. It exposes the funding chain without an accusatory framing. Erik has to say where the rest comes from, which surfaces the Afrime seed round, CAA, and whether the SBA facility is the whole plan or one leg of it.
5. It creates the natural opening for the follow-up: who built that number, and are they the person running the build?

Ask it plainly and let him answer. Do not lead with the $10M comparison. If he gives a number, then bring in Clair Obscur as the calibration: 30 people, UE5, under $10M, and they got there by cutting the open world, the character creator and the real-time combat.

**Two follow-ups to hold in reserve if the answer is thin:**

1. Who is the technical director or production lead on Unyverse, and what have they shipped?
2. Of the $1-2M, how much lands as an Aurora Punks contract and how much funds Afrime's own team?

---

## 7. Bottom line

1. Finishing Unyverse as described costs **$7M to $15M and three to four more years.** The cheapest version that is still a complete ARPG costs **$3.5M to $8M.**
2. **$1-2M is 3.5x to 8x short** of the cheapest complete version and roughly **10x short** of the game as described. The answer to Robert's question is no.
3. **$2M does fit a real, shippable product** if the scope changes. The recommended shape is a combat-first premium release built entirely out of the character creator and the combat mechanic that already exist: 10 to 12 seats over 15 to 18 months, PC at $19.99 to $24.99, with the vertical slice as milestone one so nothing is wasted if funding stops.
4. **The 18-month labour stability claim is roughly half true at $1M.** It buys 5.2 AP seats and about 92 000 SEK/month of AP net margin, against the 140 000 the K2C leg contributes today. Break-even against the current floor is about $1.53M. That is before Afrime's own team takes its share, which could halve it again.
5. **Fix the Unyverse commercial terms before signing anything.** The memo locks AP's capacity for 18 months and leaves AP's compensation TBD. That ordering is backwards, and it is the thing to change on Monday, alongside the ABL 21:5 problem already flagged in the valuation analysis.

---

*Estimates in this memo are built bottom-up from AP's own contract economics and stated as ranges. Where a comparable's budget is not public, that is noted rather than estimated. I have not seen the Unyverse builds. Nothing here has been shared externally.*
