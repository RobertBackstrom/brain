# Disposable Corps: the August questions and the demo review

Aurora Punks, September 2026. Written for the development team, via Light Up Games.

## 1. The three technical questions

The questions that came through in August were: what the hosting change means, what we would do to the network layer, and what technical direction we propose.

**We cannot answer any of them without the build.**

Answering at the level the questions are asked at, which transport, which replication model, which pathfinding, means reading the code first. An answer from the public demo is a guess.

What we need before they can be answered: the current build rather than the public demo, engine and version, and repository access. The technical direction is then a written deliverable of the first month, in the same terms the questions were asked in.

## 2. Player-hosted sessions

Make sure the game supports player-hosted sessions, peer to peer rather than dedicated servers. It is possible this already works: the store page lists LAN play, and a later update added a server browser with a host region filter. If it does, most of this is a decision to commit to that path rather than work to do.

**This is a commercial decision, not a technical one.** Dedicated servers put a recurring cost into the project that scales with the number of people playing, and it arrives before the revenue does. For a game going into Early Access with a population nobody can predict yet, that cost lands on whoever is funding the project.

Which transport, which library, which architecture is your call, not ours. We are not proposing a rewrite or naming a middleware.

## 3. The design and UX pass on the public demo

The pass went through the tutorial step by step, then the round, the economy, the building and buying flows, the map screen and the vehicles. It produced roughly 120 observations, rated by severity and placed against the twelve month schedule.

Four groups came out of it:

| Group | When | Scope |
|---|---|---|
| First | Months 1 to 2 | Two decisions, a new onboarding, and one fix |
| Before the first public playtest | Month 4 | 18 items |
| Before Early Access | Month 10 | 16 items |
| Longer term ideas, not in the current plan | Decided later | 4 items |

The eight areas the items fall into: game direction, onboarding and tutorial, economy and incentives, round structure and map, squad and AI, build and buy flows, HUD and readability, vehicles and artillery.

One limit on that work, stated plainly: the pass was made against bots, because there are not enough players to fill a match today. The onboarding, economy, menu, vehicle and HUD findings hold with one player. The findings about map scale, travel time, emptiness and round repetition do not, because a map built for ten players reads as empty with one. We are not proposing map work on that basis. The first populated match this game has had will be the month 4 playtest, and that is when those questions get answered.

## 4. Two decisions before anything else

**Decide what the game is: a slower military simulation, or a goofy multiplayer sandbox.** Both are in the build today. Historical weapons, poor visibility from tanks and one shot kills belong to the first; low fidelity models, simple AI movement, snappy kills and a latrine as a spawn point belong to the second. Both can work, and the choice settles player health, time to kill, vehicle visibility and the tone of the onboarding, so a large part of the work below resolves differently depending on the answer.

Our recommendation is the sandbox direction. The game already looks and moves like that, so it is the cheaper direction to finish. Wonkiness becomes a feature instead of a defect to polish out, which matters on this budget. And a simulation is the more expensive direction to finish, because the bar for fidelity, animation and feel is set by games that have had years of polish put into them. This is a recommendation, not a requirement. If you want the simulation direction, say so and the list changes.

**Take the public demo down while the onboarding is rebuilt.** The demo is currently the only thing a new player meets, and it cannot teach them what the game is, for the reasons in section 5. Every player who tries it in that state is a wishlist lost rather than gained. Pulling it stops that, and the demo can be published again the moment the new onboarding is in. The demo is yours, so this is your call, not ours. Our view is that three quiet months cost less than three months of bad first impressions, and that the first public playtest in month 4 is the better reintroduction.

## 5. The onboarding rebuild

The tutorial and the normal game sequence currently run in parallel, each with its own instruction text and its own voice over, so a new player meets several instruction blocks at once and two voices at the same time. Underneath that, the onboarding runs on the full size map with free movement, lets the player sell the hammer and lose the building system entirely, exposes squad and deploy options before the squad exists, and kills the player three times in short order to teach loop lessons.

Most of these are properties of the tutorial as it is built and go away when it is replaced, so we are not proposing fixes to them one at a time.

What a new onboarding needs:

1. A small purpose built tutorial level instead of the full map, with movement bounded by the lesson.
2. One objective on screen at a time, in its own HUD element, taught as part of the tutorial.
3. Fundamentals first, then economy, construction and squad control as separate and optional lessons.
4. Steps that cannot be failed, and no interaction available that the current step does not need.
5. The defense phase played rather than described, in a small zone, with a small wave.
6. At most one scripted death, with enough context that it reads as a lesson.

## 6. The economy fix

**The most profitable thing a player can do is die repeatedly near the enemy point**, because the reward is driven by proximity to the flag rather than by contribution. It rewards the opposite of good play and it is open to griefing. Rebalancing the reward around time spent and enemies killed is a small change and depends on nothing else here.

The smaller findings outside the tutorial are written down and kept: interface wording that does not match the buttons, a Purchase button that looks usable before it is, items the player can sell and then need, placeholder data in the lobby. They are not a work package of their own and get closed when someone is in that system for another reason.

## 7. Milestones

1. **Months 1 to 2.** Direction decided, demo down, new onboarding under way, the economy rebalanced.
2. **Month 4, the first public playtest.** The new onboarding in front of players, measured against your own two playtests so the numbers have a baseline. This is also where the demo comes back.
3. **Month 8, the second public playtest.** The retention comparison between playtest 1 and playtest 2 is the launch decision.
4. **Month 10, Early Access.** Three maps, two factions, light progression. Content beyond that is funded from Early Access revenue and decided at the month 8 playtest.

## 8. Working model

We raise problems, make sure they are understood, and put deadlines on the ones that get agreed. Implementation stays with you. Where we have suggested a solution above, it is a sketch and can be replaced.

The list above is a proposal for your backlog. If an item is wrong, or the cause is something we could not see from outside, say so and it goes.

## 9. What we need to start

1. The current build, not the public demo. The demo is from August 2025 and the December refactor changed a lot.
2. Engine and version, plus whatever repository access can be arranged.
3. The numbers from the two playtests: session length, tutorial completion, where players stopped.
4. The current wishlist count.

The first two decide whether the technical questions in section 1 get an answer. The last two decide what we prioritise, and how much of the list in section 3 to do.
