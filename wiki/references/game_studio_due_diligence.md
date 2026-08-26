---
title: "Game Studio Due Diligence"
source: substack
author: Sebastian Cardoso
publication: Game Studio Unlocked
date: 2026-07-07
retrieved: 2026-07-13
tags: [due-diligence, investment, publishing, studio-assessment, fundraising, m-and-a, biz-dev]
url: https://gamestudiounlocked.substack.com/p/game-studio-due-diligence
---

# Game Studio Due Diligence

By Sebastian Cardoso (Game Studio Unlocked). Seven lenses investors, publishers and acquirers use to price the risk of a studio - and which founders should proactively turn on themselves before those conversations happen.

## Framing

Sooner or later someone with money looks at your studio and asks "do we want to open our checkbook for this?" - a publisher checking a build, an angel reading a deck, or a larger company weighing an acquisition offer. However friendly the chat, they are putting a price tag on the risk of the investment. They already have interest (that is why DD is happening), so now they hunt for reasons to offer terms more beneficial to them, offer less, or pass.

Roughly the same lenses are used in every evaluation. Founders should run these lenses on themselves for two reasons: (1) you are the only one who can fix what they uncover - investors who find problems usually walk away with flowery euphemisms and leave no actionable feedback; (2) you are the person with the least perspective and the most emotional compromise, which is exactly why the self-assessment matters - the more you see what they see, the more empowered you are.

Seven lenses: the game, the team, leadership, culture, technology/tools, work systems, and the money.

## 1. The Game Itself

The actual game is checked first and weighed highest. Fundamental question: will this game make money? Sub-questions (dev-stage and shipped):

1. Clear, compelling vision and pillars?
2. Clear, credible differentiation?
3. Large enough addressable market? (great game + small player base = low revenue ceiling)
4. Can it keep monetizing after release? DLC fit? Other revenue streams?
5. Good franchise / transmedia potential?
6. Fits the competitive landscape, or fighting a red ocean / 800-lb gorillas?
7. Existing traction to validate interest (Discord, wishlists, trailer reception)?
8. Is it marketable? Some games are great but hard to communicate or build community around.
9. Fits the publisher's portfolio and roadmap? (won't cannibalize their other games or collide with GTA VII)
10. Macro trends supporting or disrupting it? (e.g. regulatory hurdles if geared at a market with deteriorating relations)

Extra check: talk to random team members about the strength of the team-game connection - is the team "locked in"? Aligned on vision, excited, driven by the genre, still believing it is doable and setting a high quality bar? Team and game form an overlooked symbiosis.

## 2. The Team

Five axes:

- **Capacity** - enough hands for the work in the time available, or a *credible* ramp-up plan. (A studio planning to hire ~100 in months is technically doable but a recipe for disaster.)
- **Competencies** - right functional expertise covered. A combat game with no combat designer is almost inevitably a deal-breaker; a promise to hire later counts for little. Angels and early-stage VCs lean hardest here - early on they bet on the team more than the build.
- **Seniority balance** - right mix of direction, seniority and execution. All-junior animators with no lead, or 7 directors with no one to execute, are both bad.
- **Genre and platform expertise** - a great 2D-platformer-on-PC team is not automatically great at a high-fidelity 3D FPS live-service on PS5. Some expertise transfers; growing pains are inevitable.
- **Team cohesion** - a collection of great developers is not a great team. Shipped together, disagree constructively, collective identity - invaluable intangibles that separate seminal studios. Not top of investor lists, but high on the author's.

## 3. Leadership

Publishers underweight this; VCs somewhat more but still shallow. Most indie studios have a leadership vacuum - execs come up as great programmers/artists/designers or founders, and leadership gets tacked on without training or mentorship. Result: a team that is underled and overmanaged - perfunctory standups, Jira boards with 900 equal-priority tickets, status reports for no one, no sense of where the game is going. It is hard to spot from inside because the studio looks busy and managed (it is), but leadership is lacking.

Check whether the leadership job is being done by anyone, title or not:
- Who ensures a clear, ambitious, agreed-upon vision?
- Who empowers and sets teammates up for success?
- Who decides what gets cut, what pivots, what new ideas to pursue?
- Who celebrates success and holds the team to account?
- Who models integrity, honesty, humility, consistency, hard work?
- Who brings people together in conflict?
- And does it work - does the team believe in the project, the plan, themselves?

## 4. Culture

Culture is what the team does when the founder isn't watching - the lingering effect of every behavior rewarded or punished since day one. Careers-page values are aspiration; culture is the actual accumulated behaviors.

Lencioni's five dysfunctions map how it degrades: it starts with trust (being OK being wrong in front of each other); remove trust and disagreement disappears, people nod along, commitment dies, accountability dies, and no one cares about results. Assessing culture honestly is hard because surveys need the very safety that a bad culture lacks. Instruments:

- **Information flow** (Westrum: pathological / bureaucratic / generative; DORA six-question survey). Key item: are messengers punished for bad news? Test: when the last playtest came back bad, what happened in the next 48 hours?
- **Psychological safety - but only as one facet.** Google Project Aristotle found safety the strongest single predictor (Edmondson's 7-item scale), but also found dependability and decision-clarity. A studio can be perfectly safe and perfectly unaccountable - everyone lovely, nothing shipping. Score safety, dependability and decision-clarity together; never take safety alone.
- **Culture adequacy for a creative studio** (Competing Values Framework - clan / adhocracy / market / hierarchy; OCAI Now-vs-Preferred). A creative studio needs real adhocracy plus enough clan; one sliding into dominant hierarchy/market while people beg for adhocracy is strangling what makes the games good.
- **Other metrics:** regrettable senior attrition (seniors leave first, hardest to conceal, most predictive); eNPS (>+20 good, >+40 strong, negative red flag, trend > number); internal mobility (healthy studios fill ~15-20% of roles from inside; #1 quit reason is lack of growth, not pay); crunch (IGDA 2023: ~1/3 still crunch, output per hour falls off a cliff past ~50 hrs/week - crunch buys roughly the same work plus burnout debt paid as post-ship attrition).

Publishers/angels/VCs rarely dig into culture unless it is overtly toxic, but founders should - a healthy culture informs every other lens.

## 5. Technology and Tools

Unless the studio is defined by technology (cutting-edge graphics, massive live-service backend), the grade is not the engine/stack choice but whether the tech is a real asset that lets the team build fast and safely.

- **Build and iteration loop.** Build runs, whole team plays it daily, "build is broken" is an event not a routine. Key number: iteration time (change -> seeing it in the running game). Seconds = explore 100 ideas and find the fun. Minutes+ = team iterates less, does less in-engine, game suffers.
- **Technical uncertainty and debt.** Weak profiler/memory manager, no auto-testing, architecture not ready for emergent systems - all yield inefficiency, surprises, frustration, each feature taking longer, velocity chipped away, missed milestones. Technical visibility and rigorous debt-mitigation standards are a must.
- **Delivery and live-ops health.** DORA metrics for anything online (deploy frequency, lead time, change-failure rate, recovery). Speed and stability rise together - a team claiming it must trade one for the other has a weak pipeline. Backend is under-examined and high-mortality: cost per concurrent user and where it goes at 10x load; can you update without dropping players; plan if day one brings double the modeled players.
- **Technical budgets and certification readiness.** Mature teams enforce GPU/CPU budgets in ms per subsystem and watch memory per platform. Console cert is a hard gate you don't control (Sony TRC, Microsoft XR, Nintendo Lot Check); most titles need two submission rounds, each failure resets the clock. A VFX artist saying "can't use these assets, we'll be GPU-bound here" signals proactive readiness.
- **Key-person / bus-factor risk, per subsystem.** How many must leave before an area stalls - concentrated in engine, game logic, netcode/backend, build/asset pipeline, platform-cert. A bus factor of one on the engine or backend is a hidden liability uncovered in a handful of questions.

## 6. Work Systems

Umbrella for all practices and artifacts that turn effort into a shipped game (processes, standups, charters, burndowns, definitions of done, QA dashboards). Two traps: a busy studio looks healthy (it may not be - we can be diligent at the wrong things), and evaluators over-emphasize production methodology (agile, standups, burndown charts are just tools, means to an end). What to look for:

- **Clarity** - roles, expectations, interrelations, vision/pillars, tactical goals, and how each person's work reaches the game.
- **Communication and collaboration** - sharing ideas, respectful open disagreement, selfless help.
- **Clear processes** - forget labels; can people size work, know what is next, priorities, how to do it, how work blocks/unblocks others, what to do when blocked?
- **Value delivered over tickets moved** - the goal is a great game, not moving cards to Done. Are people empowered to use judgment and expertise, or just rewarded for shuffling Jira tickets?
- **Predictable delivery + legitimate creativity.** Investors obsess over hitting sprint goals/milestones more than whether the output is good; founders shouldn't. Balance scope discipline with judiciously welcoming empirical insight - dev is creative exploration, not just hitting goals set three months back.
- **Proactive risk management** - risk register, challenging questions, humility, ownership of mitigation - not risk-management theater.
- **Sustainable development** - sustained crunch precisely signals the system isn't converting effort into progress. Tells: after-hours activity, longer hours + less output per hour, bug backlog growing faster than it clears, and the smoking gun - the studio buying pizzas for the team.

## 7. The Money

Most measurable, most straightforward lens.

- **Survival first.** Runway in months at current net burn (<6 months = every conversation happens under duress) and cost-to-finish estimated *candidly* - the last 20% (polish, stabilization, cert) eats ~half the real effort, so a plan funding 80% funds zero shippable games. The deal meant to refill runway always closes months later than hoped.
- **Quality of earnings.** How real and repeatable earnings are: recurring revenue vs one-off work-for-hire dressed as a trend; refunds/chargebacks/discounts hiding churn; live-game revenue broad vs propped by a few whales who can all leave at once.
- **Concentration.** One of the most valued numbers to outside assessors. >80% of revenue from a single game, or leaning on one client, is one cancellation from gone - a discount on acquisition price. Little you can do if you make premium games and have shipped one, but be prepared, and note the value of basic diversification.
- **Revenue mix.** Work-for-hire pays bills and builds nothing you own; owning IP burns cash and builds an asset. Neither is wrong, but the split should be deliberate strategy, not an accident.

Timing: runway is bargaining power, so raise well before you need it - a studio with two months of cash negotiates with a gun to its own head, and investors will leverage it.

## On Acquisitions / Formal M&A DD

M&A DD is far more complex, with heavy legal/financial emphasis: corporate governance, compliance docs, full legal/contract and litigation history, financials (P&L, income statement, balance sheet, cashflow), tax reports, credit history, past investments, cap table, past valuations, board/shareholder minutes, copyright/trademarks/patents, turnover, workplace safety, insurances, ethics-violation resolutions. Retain legal counsel and a financial M&A specialist before moving. Also turn the lens on the buyer - the industry's acquisition track record is dismal; be clear on what statistically happens to a studio sold to a large publisher/conglomerate.

## Self-Assessment - How To

- **Separate symptom from cause.** Treat "stated" problems (slow engineers, missed milestones, lost spark) as symptoms. Executives overwhelmingly admit their orgs are bad at diagnosing before solving. Ask why repeatedly - slow engineers may be a leadership problem; missed milestones a clarity problem. If you run the studio, you are statistically the likely driver of a fair share of structural issues - be humble, solve one at a time.
- **Triangulate.** Ask the same hard questions across the studio - director's official story, leads' slightly different one, developers' trenches version. Three different answers to one question flag an issue. Ask blunt questions: who makes the calls, what happens when you disagree, does anyone say when something's broken?
- **Time-box it and check your biases.** Days to form a view and pull hard data (runway, build, milestone history, turnover, conversations); a week or two for a decent picture. Avoid anchoring on the first answer - try to disprove your own conclusion and be transparent about findings.

## Wrapping Up

A studio that makes it tends to have most of the seven lenses in decent shape - not perfect, but in shape - and the best-odds studios are actively looking into these with humility, empathy and a kaizen mindset. The DD investors run to price your risk covers exactly the things you would benefit from examining first. Self-assess on a regular cadence.

---

*Author: Sebastian Cardoso - ~20 years across AAA (Riot, Crytek, EA) and indie; fractional COO / executive producer. gamestudiounlocked.com*
