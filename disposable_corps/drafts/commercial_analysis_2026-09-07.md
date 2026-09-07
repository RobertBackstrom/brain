---
title: Disposable Corps, commercial and sales-potential analysis
project: dsc
status: draft
created: 2026-09-07
author: Assistant (analytics + bizdev), for Robert Bäckström
audience: internal. Basis for the Rift Gaming conversation and for Robert's own decision on the deferral and revenue share. Nothing in here goes to LUG, Armoured Dudes or Rift as-is.
---

# Disposable Corps: what is this game expected to sell

## 0. Summary

1. **Expected units, first 12 months after the Early Access release:** low 3 000, base 10 800, high 31 500. First month: 1 400 / 4 300 / 10 800. Estimates, built from a follower-derived wishlist band and published conversion benchmarks, cross-checked against nine comparables. Arithmetic in section 3.
2. **Net revenue to the project, year one** (after Steam's cut, regional pricing, discounts, VAT and refunds): low 129 000 SEK, base 562 000 SEK, high 1 827 000 SEK.
3. **The plan's "roughly 7 500 units to clear the 750 000 recoup" is wrong.** It assumes 100 SEK net per unit, which is 14,99 USD times 0,70 and nothing else. Realised net per unit is 43 to 58 SEK. The recoup crosses at **about 14 400 units** if AP takes 100 percent of net until it is whole, and at **about 50 000 units** if AP recoups pro rata with the investors' 1,86 MSEK. The plan does not say which. That single clause is worth more than every other assumption in this document combined.
4. **No wishlist figure.** LUG has it, we do not. The 2 741 Steam followers imply 19 000 to 55 000 wishlists on the published multiplier, and a playtest-heavy page like this one tends to sit at the bottom of that range. Getting the real number from LUG collapses the band by roughly half. It is a one-line ask and should be made before anything is said to Rift.
5. **Verdict:** the sales case does not carry a 2,16 MSEK budget. Base-case year-one net is about a quarter of the cost. The engagement holds up as **cash-funded services with a bounded deferral**, and only with AP in first position on recoup. It does not hold up as a revenue-share investment, and it should not be sold to Rift as one. Conditions that would change that are in section 6.

## 1. What the game actually is

### Today

Sources: the Steam store page and its news feed (25 posts, 2025-05-12 to 2026-01-10), the demo's 77 reviews (Steam API, all languages), Robert's play sessions (`build_feedback.md`), the developer's own control list of 2025-09-25, LUG's problem list of 2026-06-12.

1. A low-poly first/third-person shooter in a WW1 setting with steampunk mechs. Rounds cycle Prepare / Defense / Attack with the two teams on opposite phases. Money is earned from kills and objectives and spent on gear, fortifications, a tank factory, and AI soldiers. Each player recruits and commands an AI squad. Digging and terrain destruction are in.
2. It is four games in one (shooter, squad RTS, base builder, vehicle sim) on a map the publisher itself calls too big. The demo reviews say the same thing independently, in two languages: "interesting concept but that is where it ends", "the AI is awful on both sides", "I still have not figured out how to aim the field gun", "too much money, all the structures have to be built by yourself", "hitboxes are broken".
3. Demo reception: **77 reviews, 65 percent positive, "Mixed"**, accumulated over 16 months of a free demo plus two playtests and six trade-show appearances (ChinaJoy, BitSummit, Steam China Showcase, TPS Fest, WEPLAY, BGM). 53 of the 77 are in Chinese, 19 in English. SteamSpy puts demo owners in the 0 to 20 000 band. Live demo players when checked: 0. Store discussions: 30 threads total, the last one in October 2025.
4. Store followers: **2 741** (Steam community XML, 2026-09-07). For scale: Striden had 6 343, Last Flag 9 279, Trench Tales 21 894, Beyond The Wire 41 838, Easy Red 2 59 466.
5. Steam tags as set by users: Turn-Based Tactics, FPS, Third-Person Shooter, Wargame, Tower Defense, Military, World War I, Base Building. That tag set is the confusion in the product made visible: Steam does not know what shelf to put it on either.

### The plan's re-cut

The plan (`dev_plan_high_level.md` section 3) cuts it to one thing: a 20 to 25 minute match in three sectors, 90 seconds to dig in, five to seven minutes to attack one trench line, collapse, next sector. Each player commands a four to six man AI squad so 5v5 plays as sixty men. Economy, tank factory, nation roster, deep armour sim, PvE co-op as a marketed mode, LAN, separate tutorial: all parked.

### The differentiator, and whether it is enough

**You dig the trench, you fight in the trench you dug, and it is blown apart under you.** That is real. Nothing in the comparable set does it in this format. Battlefield 1 sells the fantasy at AAA scale without letting the player shape the ground; Foxhole lets the player shape the ground but at MMO scale over weeks; Ravenfield and Easy Red 2 give the low-poly war sandbox with no persistent player-built terrain at all. The name is also the design, and the "sixty men on a front from ten players" line is a genuinely good pitch sentence.

Three things cut against it:

1. **The people who buy the differentiator are not the people the art sells to.** RankOne's WW1 audience profile (Verdun, Tannenberg, Isonzo, Beyond The Wire; 209 profiles, 99 percent PC) over-indexes on RTS 2,7x and realism, and under-indexes on sandbox mechanics (0,77x). The low-poly sandbox audience (Ravenfield, BattleBit, Easy Red 2) is the reverse. R1's own line: "these two groups are driven by different mechanical preferences, realism and lethality for the WW1 group versus chaos and sandbox freedom for the low-poly group". The game sits between two audiences and the store page currently speaks to neither clearly.
2. **The differentiator is a multiplayer differentiator.** A dug trench is only interesting if someone else has to storm it. Every comparable at this budget that survived (Easy Red 2, Ravenfield, Operation: Harsh Doorstop, and per Chris Zukowski's 2025 list, Wild Assault) is playable against bots when nobody else is online. The plan parks PvE co-op as a marketed mode. Section 5 argues that is the one cut to reverse.
3. **The demo has already told 77 people what it is, and 27 of them said no.** A re-cut that ships under the same name and store page inherits that "Mixed" score on the demo and the tag confusion. Section 5.

Is it enough? As a design, yes: it is a clean, defensible hook with a name that does its own marketing. As a commercial engine, only if the game does not die the moment the launch population thins, which is where the money question actually lives.

## 2. Comparable set

Selection rule: honest matches on **format and budget**, not aspiration. Small team, PC-only, multiplayer-first military shooter, indie price, ideally period setting or low-poly art. Data pulled 2026-09-07 via `assistant/market-intel.js` (Steam Store API, SteamSpy, Steam reviews with `language=all`, ISteamUserStats live players) and steamcharts.com where it answered; Steam community XML for followers; web sources for launch peaks where noted. Owner bands are SteamSpy's and are wide; the "est. units" column is the Boxleiter method from [[analytics_learnings]] (reviews times 30 to 50, house median 40), which is the number to use.

| # | Game | Why in the set | Released | Price USD | Reviews / score | Est. units (reviews x30 to x50) | All-time peak CCU | Live CCU 2026-09-07 | Followers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Striden** (5 Fortress, SE) | Small Swedish team, multiplayer-first, EA, AP has inside numbers | EA 2025-07-11, closed within a year | n/a (25 percent off) | 271 / 69 percent Mixed | 8 000 to 13 500 | 285 (launch day) | 0 | 6 343 |
| 2 | **Last Flag** (Night Street Games) | 5v5, 2026, celebrity PR, still died in three weeks | 2026-04-14 | 4,99 | 704 / 76 percent | 21 000 to 35 000 | 558 (day 2) | 0 | 9 279 |
| 3 | **Trench Tales** (solo dev, Crytivo) | WW1-inspired, EA, same year, publisher-backed | EA 2025-05-06 | 24,99 | 699 / 70 percent | 21 000 to 35 000 | 107 | 1 | 21 894 |
| 4 | **Beyond The Wire** (Redstone, Offworld) | The WW1 multiplayer cautionary tale; Squad's publisher, Squad's engine, still dead | EA 2020-10-21, 1.0 2022-08-31 | 9,99 (from 29,99) | 7 542 / 63 percent Mixed | 225 000 to 375 000 | 2 310 | 1 | 41 838 |
| 5 | **Due Process** (Giant Enemy Crab, Annapurna) | 5v5 tactical, EA, small team, strong publisher | EA 2020-11-03 | 9,99 | 8 557 / 81 percent | 255 000 to 430 000 | 2 093 | 1 | 31 117 |
| 6 | **Zero Hour** (Attrito, Bangladesh) | 5v5 tactical, small team, EA to 1.0, the "it worked" case at this budget | EA 2020-08, 1.0 2024-09-09 | 9,99 | 33 399 / 77 percent | 1,0M to 1,7M | 7 302 | 70 | 82 072 |
| 7 | **Easy Red 2** (solo dev, IT) | Low-budget war shooter with bots, WW2, the survival model | 2022-01-06 | 8,99 | 14 941 / 90 percent | 450 000 to 750 000 (a third-party estimate says 647 000) | 12 000 | 1 106 | 59 466 |
| 8 | **Holdfast: Nations At War** (Anvil, MT) | Period line-battle multiplayer, small team, EA to 1.0, the good mid-case | EA 2017, 1.0 2020-03-05 | 19,99 | 29 513 / 90 percent | 885 000 to 1,5M | 3 419 | 274 | n/a |
| 9 | **Isonzo** (BlackMill, NL) | The WW1 ceiling at indie scale; series has sold 2M+ across three titles | 2022-09-13 | 29,99 | 17 230 / 83 percent | 515 000 to 860 000 | 5 408 | 131 | 49 723 |
| 10 | **Mark of the Deep** (LUG-published) | What a LUG launch looks like, Western-style indie | 2025-01-24 | 19,99 | 354 / 75 percent | 10 000 to 18 000 | n/a | 2 | 5 379 |
| 11 | **Blackthorn Arena: Reforged** (LUG-published, CN dev) | LUG's best recent result, China-native audience | 2024-11-02 | 24,99 | 1 000 / 67 percent Mixed | 30 000 to 50 000 | 1 762 | 23 | n/a |
| 12 | **Folklands** (LUG-published) | LUG's low case | EA 2025-03-24 | 14,99 | 59 / 76 percent | 1 800 to 3 000 | n/a | 1 | 2 729 |

Deliberately out:

1. **BattleBit Remastered** (146 000 reviews, 5 to 10M owners). Low-poly, yes, but a 254-player Battlefield built over seven years by three people with a viral moment. It is the lottery ticket, not the comparable.
2. **Hell Let Loose, Squad, Insurgency: Sandstorm.** Budgets an order of magnitude up, and R1's audience for them (899 profiles, NA and Western Europe, 25 to 45, realism-first) is not the audience the low-poly art is speaking to.
3. **Ravenfield** (80 000 reviews, 97 percent) and **Operation: Harsh Doorstop** (20 700 reviews, free). Both are bot-sandbox games first; they are in the argument (section 5) as the survival model, not in the numbers.
4. **Verdun / Tannenberg.** Same series as Isonzo, older, and Isonzo is the cleaner data point.
5. **Foxhole.** Persistent-world MMO logistics; different product.

What the table says:

1. **Everything at this budget that stayed alive plays offline.** Easy Red 2 (1 106 live), Holdfast (274) and Isonzo (131) hold a population; Easy Red 2 is the only one of the three with full bot play, and it is the one with the most players three years on. Zero Hour and Due Process, both good 5v5 games with real publishers and 8 000 to 33 000 reviews, are at 70 and 1 live players.
2. **The 2025 to 2026 5v5 launches died in weeks.** Striden (285 peak, servers closed, staff let go), Last Flag (558 peak, "player count is not where we need it" three weeks after launch), Trench Tales (107 peak). None of them had a broken tutorial or a "Mixed" demo going in.
3. **LUG's published range is 2 000 to 50 000 units.** Three titles, three data points, all inside that band. Disposable Corps has a bigger audience in China than those (Blackthorn Arena excepted) and a worse demo score.

## 3. Expected sales

### The wishlist gap

We do not have the wishlist count. LUG has it. Everything below derives it from the 2 741 followers, and that is the single largest source of width in the band.

1. GameDiscoverCo's published multiplier (2023 survey): wishlists are 7x to 20x followers, median 12x, and lower for deep PC titles (7,5x to 9,5x for 4X, turn-based, survival). Applied to 2 741 that gives **19 000 to 55 000**, midpoint 33 000.
2. Reasons to sit low in that range: the page has had a free demo and two playtests, which convert lookers to followers without a wishlist; the store has been silent for seven months and wishlist banks decay; 69 percent of the demo's reviewers write in Chinese, and Chinese wishlists convert at Chinese prices (section 3.3). Striden's own number, from Emil Darsbo's mail of 2024-06-10, was 12 000 wishlists against what became 6 343 followers, roughly 2x, for exactly this kind of playtest-driven page.
3. Assumed wishlists at the EA launch in month 10, after AP's re-marketing and a Next Fest: **15 000 low / 30 000 base / 50 000 high.**

If LUG's real figure comes back at 10 000, the base case becomes the low case. If it comes back at 60 000, the high case becomes plausible as base. Ask.

### Conversion

1. First week: GameDiscoverCo's 2024 to 2025 median is 0,15x of launch wishlists for titles with over 25 000 wishlists, dropping to **0,10x for titles priced above 10 USD**. AP's house tiers (the Rust Racers model, [[analytics_learnings]]) say 10 to 30 percent week one. A "Mixed" demo and a multiplayer-only product sit at the bottom. Assumed: **8 / 12 / 18 percent.**
2. Month one: house tier is week one times 1,1 to 1,3. Assumed **1,2x.**
3. Year one: GameDiscoverCo's median year-one multiple on first week is 3,77x for titles with 10 000 to 50 000 first-week sales; smaller titles run lower, multiplayer titles run lower still when the population dies. Assumed **2,5 / 3,0 / 3,5x.**
4. The EA to 1.0 spike is not modelled. Only 21 percent of EA graduates earn more at 1.0 than in their first 30 days of EA ([[analytics_learnings]], GDCo 2026 dataset). Year one here means the twelve months from the EA launch.

### Units

| | Low | Base | High |
|---|---|---|---|
| Wishlists at launch (assumption) | 15 000 | 30 000 | 50 000 |
| Week-one conversion (assumption) | 8 percent | 12 percent | 18 percent |
| **Week one units** | 1 200 | 3 600 | 9 000 |
| **EA launch month (x1,2)** | 1 440 | 4 320 | 10 800 |
| Year-one multiple on week one | 2,5x | 3,0x | 3,5x |
| **First 12 months post-EA** | **3 000** | **10 800** | **31 500** |

Cross-check against section 2 with the review method: low equals Folklands; base sits between Striden (8 000 to 13 500) and Mark of the Deep (10 000 to 18 000); high equals Trench Tales or Last Flag (21 000 to 35 000). Nothing in the band requires the game to outperform anything LUG has published. The high case requires it to match a Crytivo-published title with 22 000 followers, which is a stretch from 2 741.

### Price and net per unit

Price is not set in the plan. Assumed **14,99 USD** for the EA launch. Comparables cluster at 9,99 (Zero Hour, Due Process, Easy Red 2, Beyond The Wire after its cut) and 19,99 to 24,99 (Holdfast, Trench Tales). 14,99 is the middle; going to 9,99 raises units modestly and cuts net per unit by a third, going to 19,99 does the reverse and a "Mixed" demo does not support it.

FX used: **USD/SEK 9,56** (Frankfurter 9,5513 for 2026-09-04, open.er-api 9,5717 for 2026-09-07, 0,2 percent apart, midpoint taken). EUR/SEK 11,11 (11,1005 / 11,1164). Not read from `.fx_cache.json`, which still holds a seeded 11,05 from June.

Each factor on its own line so any one of them can be attacked:

| Factor | Low | Base | High | Basis |
|---|---|---|---|---|
| Headline price USD | 14,99 | 14,99 | 14,99 | assumption |
| Share of units sold at China-tier pricing | 65 percent | 55 percent | 45 percent | 69 percent of demo reviews are Chinese; LUG's stated model is "China kicks it off, then global" (Odd/LUG/AP notes 2025-06-09) |
| China-tier price as share of USD | 50 percent | 50 percent | 50 percent | Valve's recommended CNY tier is 40 to 60 percent below USD (GDCo regional-pricing study) |
| Blended regional factor | 0,675 | 0,725 | 0,775 | arithmetic |
| Blended discount over year one | 0,80 | 0,88 | 0,90 | 10 percent launch discount plus seasonal sales; heavier in a slow-seller case ([[analytics_learnings]], Ironcrest) |
| VAT and sales tax deducted before split | 0,90 | 0,90 | 0,90 | EU 20 to 25 percent, CN 13 percent, US partial; blended estimate |
| Refunds | 0,88 | 0,90 | 0,92 | house range 3 to 17 percent, average 10 |
| Steam share | 0,70 | 0,70 | 0,70 | standard tier |
| **Net per unit, USD** | **4,49** | **5,42** | **6,06** | product |
| **Net per unit, SEK** | **43** | **52** | **58** | at 9,56 |

Gross consumer spend per unit for reference: about 10 to 12 USD blended. The plan's 100 SEK is 14,99 times 0,70 times 9,56, so it skipped every row above except the last.

### Net revenue to the project

| | Low | Base | High |
|---|---|---|---|
| EA launch month, units x net | 1 440 x 43 = **62 000 SEK** | 4 320 x 52 = **225 000 SEK** | 10 800 x 58 = **626 000 SEK** |
| First 12 months, units x net | 3 000 x 43 = **129 000 SEK** | 10 800 x 52 = **562 000 SEK** | 31 500 x 58 = **1 827 000 SEK** |
| In EUR at 11,11 | 11 600 | 50 600 | 164 400 |

No console, no other storefronts, no DLC: the plan does not include them inside the twelve months and Steam baseline DLC attach is low single digits outside engaged strategy bases ([[analytics_learnings]]). A supporter pack at 4 USD could add 5 to 10 percent; not modelled.

### How much the missing wishlist figure widens the band

Holding conversion and price fixed, the wishlist assumption alone moves year-one net from 129 000 to 1 827 000 SEK, a factor of 14. With a real wishlist count the remaining uncertainty is conversion and price, roughly a factor of 3 to 4. Half the width of this analysis is one number LUG can read off Steamworks in ten seconds.

## 4. Revenue to AP under the current model

The model: AP defers 300 000 SEK over twelve months, recoups it at 2,5x, **750 000 SEK, at release**, then takes **15 percent revenue share**. Cash from investors is 1 860 000 SEK over the term.

### The clause that is not written

The plan says "recoupas 2,5x vid spelsläpp, därefter 15 procent". It does not say **from what share of net**. Two readings:

1. **Case A, AP first position.** AP receives 100 percent of project net until 750 000 SEK is paid, then 15 percent. This is what the plan's "7 500 units" implicitly assumes.
2. **Case B, pro rata.** AP's 750 000 recoups alongside the investors' 1 860 000, so AP receives 750 / (750 + 1 860) = 28,7 percent of net until both are whole. An investor who put 1,86 MSEK cash in will ask for this at minimum, and more likely for priority (Case C: investors first, AP second, which for AP is the same or worse than B).

### Crossing points

| | Low price (43) | Base price (52) | High price (58) |
|---|---|---|---|
| Case A: units to recoup 750 000 at 100 percent of net | 17 400 | **14 400** | 12 900 |
| Case B: units to recoup at 28,7 percent of net (project net 2 613 000) | 60 800 | **50 300** | 45 100 |

The plan's 7 500 is corrected to **about 14 400 units in the best legal reading and about 50 000 in the reading an investor will want**. In the base case (10 800 units) AP does not cross the recoup in year one under either reading.

### AP's year-one take

| | Low | Base | High |
|---|---|---|---|
| Project net, year one | 129 000 | 562 000 | 1 827 000 |
| Case A: AP recoup received | 129 000 | 562 000 | 750 000 |
| Case A: 15 percent on the excess above 750 000 | 0 | 0 | 161 600 |
| **Case A: AP total** | **129 000** | **562 000** | **911 600** |
| Case A vs the 300 000 deferred in cash | minus 171 000 | plus 262 000 | plus 611 600 |
| Case B: 28,7 percent of net | 37 000 | 161 000 | 524 000 |
| **Case B: AP total** | **37 000** | **161 000** | **524 000** |
| Case B vs the 300 000 deferred | minus 263 000 | minus 139 000 | plus 224 000 |

Reading it:

1. Under Case A the base case pays AP 562 000 on 300 000 deferred, 1,9x nominal, and the low case loses 171 000. The 2,5x is reached only in the high case.
2. Under Case B the base case **loses AP 139 000** of its deferred fee, and even the high case never reaches the 750 000.
3. The 15 percent revenue share is worth 0 in low and base under either reading. It only has value above 14 400 units (A) or 50 000 units (B). Do not price it as if it had expected value; it is a call option that pays in the high case.
4. The real economics of this engagement for AP are the **1 500 000 SEK cash fee** and the margin on it at rate card. The deferral is a bounded bet, and it is only a reasonable bet with Case A written into the term sheet.

### For the Rift conversation

If Rift shares the deferral proportionally, it shares these outcomes. The honest framing is paid co-delivery on the cash portion, with the deferral as a small, first-position kicker. A Rift pitch built on the revenue share as the return would need the high case as its base, and nothing in sections 2 or 3 supports that.

## 5. The honest risks to the number

### Cold start: what a 5v5 game needs to not feel dead

1. **What it needs.** A 5v5 match needs ten players in the same region and time window. To fill a match inside two minutes around the clock in two regions (China and the West, which is what LUG's model implies), the game needs on the order of **150 to 200 average CCU, 400 plus at daily peak**. Estimate, from: ten per match, two regions, a 3x to 4x peak-to-average daily curve, and at least two matches per region at off-peak so a player is never the only one in the browser. R1's modelled floor is stricter, **500 global CCU** (section 5, R1 notes). Below either line, the server browser is empty outside prime time and the reviews say so within a week.
2. **What launches produce.** Launch-weekend peak CCU runs at roughly 8 to 10 percent of first-week units in the comparables where both are visible (Striden: 285 peak; Last Flag: 558 peak on an estimated 5 000 to 8 000 first week; Beyond The Wire: 1 228 peak in its EA launch month). Applied to section 3: **low 100 to 120, base 300 to 400, high 800 to 900 peak CCU on launch weekend.** Multiplayer indie launches then lose 70 to 80 percent of peak inside four weeks (Last Flag "decreased steadily" from 558 to under 100; Trench Tales 107 to 1; Striden 285 to 3). So by week five: **low 25 to 35, base 80 to 100, high 200 to 250 peak**, average a third of that, split across two time zones.
3. **What that does to the sales case.** The base case falls below the viable line inside a month. The tail multiple of 3,0x on week one assumes the game is still buyable in month six; for a multiplayer-only product with an empty browser it is not, and the tail collapses toward 1,5x, which pulls base-case year-one units to about 5 400 and net to about 280 000 SEK. Only the high case holds a population in one region without help.
4. **The mitigation is already in the game.** The AI squads and bots exist. The comparables that survive at this budget (Easy Red 2, Ravenfield, Operation: Harsh Doorstop, Wild Assault in Chris Zukowski's 2025 list, which "survives partially through bot-filling") are playable with zero other humans online. The plan parks "PvE co-op as a marketed mode" and treats bots as the enemy to be tuned down. **Reverse that one cut.** Every mode should start with bots filling the empty seats and the store page should say the game is playable solo and co-op. It costs the plan little because the systems are there; it is the difference between a game that dies in week five and one that sells at 1 live player like Easy Red 2 did at 8,99.
5. Striden is the in-house version of this lesson: 8 200 playtesters and 12 000 wishlists in June 2024, self-capped at 247 CCU, and the studio's own post-mortem line was that publishers "were put off by low player numbers", a Catch-22. AP watched it from the cap table.

### Seven months of silence

1. Last public post 2026-01-10, "we will go dark to work on the next update". Nothing since. The store discussions stopped in October 2025. Followers are 2 741 after 16 months and six trade shows.
2. Wishlists decay when a page goes silent; the exact rate is not public, but every re-marketing dollar in month 6 to 9 of the plan is spent first on recovering what has been lost, not on growth. The plan's month-10 EA launch will effectively be a relaunch of a page with a "Mixed" demo attached. Delisting the old demo and shipping a new one under the re-cut is the cheap fix and should be in phase 2.

### A China-weighted publisher

1. Two thirds of the demo's reviewers write in Chinese. LUG's own description of its model (Odd/LUG/AP call 2025-06-09) is China first, then global. That is the right channel for this game's existing audience and the wrong one for the WW1 tactical audience R1 describes (NA and Western Europe, 25 to 45).
2. It sets the price. Chinese-tier pricing at half the USD price is the single biggest haircut in the net-per-unit table. If the launch skews further Chinese than the base assumption, net per unit moves toward 43 SEK and the recoup moves toward 17 400 units.
3. LUG's demonstrated Western range on Steam is 2 000 to 50 000 units per title. There is no Western marketing budget in the 2,16 MSEK, and Anthony's June signal was "probably only revenue, maybe a bit from marketing".

### No release date, no repo, no engine

Every number in section 3 assumes the plan's month-10 EA date holds. Phase 0 has not run; engine, netcode state and the founders' delivery cadence are unverified. A six-month slip does not change the band, it changes the date on which the low case starts.

### The demo score travels with the app

The 65 percent "Mixed" on the demo is attached to app 3617330, and Steam shows demo reviews on the parent page. A new demo app ID under the re-cut resets it. Small, cheap, and easy to forget.

### What R1 added and did not

1. R1 (RankOne's agent, four queries, 2026-09-07, transcript at `drafts/r1_transcript_2026-09-07.md`) profiles the tactical squad shooter audience at 1,2 to 2,0M MAU, 97 percent PC, 25 to 45, NA and Western Europe, over-indexing RTS 2,7x, "military jargon" 3,4x and "objective-based team gameplay" 2,3x. The squad-command layer is the right feature for that group, and the low-poly art is the wrong signal to it.
2. Its WW1 audience sample is 209 profiles (100 in the comparables query). That is thin enough that the affinity numbers (Rising Storm 2 at 28x to 85x depending on the query, Zero Hour at 11,6x to 40,6x) should be read as direction, not magnitude. It has no view of the Chinese demo audience at all. Treat R1 as a Western-audience instrument here.
3. Its comparables table is stale and should not be quoted. It gives Easy Red 2 "4 500+" reviews (actual 14 941), Beyond The Wire at 34,99 USD and 70 percent (actual 9,99 and 63 percent), Holdfast a 6 243 peak (steamcharts: 3 419). Section 2 uses the live API numbers instead. Same pattern as noted in [[reference_rankone_agent]]: the headline metrics read as modelled web estimates, the affinity and over-index data is the part that is RankOne's own.
4. Where it agrees with this document, unprompted: it names Easy Red 2 as "the blueprint", credits its survival to AI squads and single-player/co-op viability, and calls that the mitigation for "the empty server death spiral that claimed Due Process and Beyond The Wire". It also says a 15 to 20 USD EA price "will require a robust AI/single-player offering at launch to justify the cost while the multiplayer community builds". Same conclusion as section 5, from a different route.
5. Its KPI answer puts the matchmaking floor for a 5v5 game at **500 global CCU** ("the emergency floor" for sub-two-minute queues across regions and skill levels), and the share of indie shooters under 50 CCU at six months at **70 to 85 percent**. It also models a 15 to 20 percent refund rate for multiplayer-only titles, against the 10 percent average, on the logic that a player who cannot find a match refunds. These are modelled, not measured, and unsourced beyond "2024 GDCo and VG Insights". They are stricter than the 150 to 200 average CCU estimate above; if R1's floor is the right one, even the high case in this document is under it by week five. Either way the conclusion is the same: the population does not carry the game, the bots have to.

## 6. Go / no-go

### The read

1. **The commercial case does not support 2,16 MSEK on sales.** Base-case year-one net of 562 000 SEK is 26 percent of cost. Even the high case, 1,83 MSEK, does not return the cash inside the year, and the EA-to-1.0 spike cannot be counted on to close the gap. For LUG's investors this is a loss in the base case and roughly break-even over a long tail in the high case.
2. **The case does support the engagement as cash-funded services.** AP's 1,5 MSEK is earned at rate card whether the game sells 3 000 or 30 000. The 300 000 deferral is a bounded bet that returns 1,9x nominal in the base case **if and only if** AP is first in the waterfall, and loses money in every other configuration except the high case.
3. **The 15 percent revenue share has no expected value in low or base.** Keep it, it costs nothing, but do not let anyone (including Rift) price it as income.
4. **Go**, on these terms: cash fee as planned, deferral capped at 300 000, first-position recoup written down, and the four product conditions below inside the plan. **No-go** on raising the deferral, on selling the revenue share as the return story, and on any version where AP's recoup sits behind or beside the investors'.

### What would have to be true for the sales case to carry the budget

1. **A verified wishlist count of 50 000 or more at launch.** Ask LUG for the current number now. At 50 000 with 18 percent conversion and a held population, year-one net reaches 1,8 MSEK and the investors' cash is in sight over 24 months. Below 25 000 the base case is the ceiling.
2. **Bots-first.** Every mode playable solo and co-op against AI from the EA launch, with bots filling empty seats in public matches. This is the one cut in the plan to reverse. It converts the tail multiple from a hope into something the comparables actually show.
3. **Price and region set on purpose.** 14,99 USD, Valve's recommended CNY tier and not lower, no launch discount deeper than 10 percent. Each 10 percent off the blended realised price moves the recoup crossing by about 1 500 units.
4. **A Western channel.** A Next Fest slot in the launch window and a named Western marketing partner or creator plan. LUG's Steam track record says its reach stops at 50 000 units and this game's differentiator sells to a Western audience.
5. **A retention gate at the end of phase 1.** The closed playtest in month five should produce day-7 retention and returning-player share, and the EA launch should be conditional on them. That is the moment to re-run this analysis with real numbers instead of a follower multiplier.

### Three assumptions most likely to be wrong

1. **The wishlist band (15 000 / 30 000 / 50 000).** Derived from followers with a multiplier that varies 7x to 20x. One question to LUG removes it.
2. **The year-one tail multiple (2,5 / 3,0 / 3,5x).** For a multiplayer-only game with no bot play it is closer to 1,5x. Bots-first is what makes 3,0x defensible.
3. **First-position recoup (Case A).** The plan reads as if it were agreed. It is not written, and the investor who funds 1,86 MSEK will have a view.

## Sources

1. Local: `disposable_corps/CLAUDE.md`, `drafts/dev_plan_high_level.md`, `build_feedback.md`, `output_log.md`, `pitches/disposable-corps/index.html`, `wiki/deals/projects/disposable_corps.md`, memory `project_disposable_corps`, `agents/memory/analytics_learnings.md` (conversion tiers, refund range, sales-per-review ratio, EA 1.0 spike, net-per-unit method), `agents/memory/bizdev_learnings.md`.
2. Steam: store and demo pages, `ISteamNews` (25 posts), `appreviews` with `language=all` and per-language counts, community XML follower counts, `ISteamUserStats` live players, all 2026-09-07.
3. `assistant/market-intel.js overview` on 30 app IDs (Steam Store API, SteamSpy, reviews, live CCU).
4. steamcharts.com all-time peaks for Easy Red 2, Zero Hour, Isonzo, Intruder, Holdfast, War of Rights, Blackthorn Arena: Reforged; web-reported peaks for Beyond The Wire (2 310), Due Process (2 093), Striden (285), Last Flag (558), Trench Tales (107). SteamDB and raijin.gg return 403 from the VPS.
5. GameDiscoverCo: "The state of Steam wishlist conversions 2024-2025" (0,15x median, 0,10x above 10 USD, year-one 2,7x to 3,8x); "Deep dive: how Steam followers and wishlists relate" (7x to 20x, median 12x); "Does Steam have its regional pricing recommendations right" (CNY tier).
6. How To Market A Game: "2025 Q2 games that are selling" (seven multiplayer shooters over 1 000 reviews, six dead; Wild Assault survives on bots); "What the hell happened in 2025" (3 percent of releases reach 1 000 reviews).
7. PC Gamer on Striden's closure and on Last Flag; GameSpot on Last Flag ending content; Emil Darsbo's 5 Fortress update of 2024-06-10 (Gmail); Gemini notes from Odd/LUG/AP 2025-06-09 and Ark Island/LUG 2026-06-02 (GDrive).
8. RankOne R1 agent, four queries 2026-09-07, cleaned transcript at `disposable_corps/drafts/r1_transcript_2026-09-07.md`. Reddit and YouTube comments not sampled (blocked from the VPS, [[reference_vps_web_collection_limits]]).
9. FX: api.frankfurter.dev and open.er-api.com, 2026-09-07.
