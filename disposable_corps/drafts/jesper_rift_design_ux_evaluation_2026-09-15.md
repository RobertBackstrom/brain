# Disposable Corps - Design & UX Evaluation

## 1. Player Fantasy & USP

What is the player fantasy this game is aiming for?

You are an officer, leading your unit on the battlefield. You are a skilled soldier, making the difference through individual combat brilliance. You are a logistics expert, turning the tide of the battle through well positioned buildings and infrastructure. 
All of these are powerful player fantasies and they offer a ton of strategic gameplay moments to toy around with. They do compete with each other though so balancing them against one another as the game grows will be a continuous challenge.

I wasn’t entirely sure what angle the game was going for. It seems to lean a little towards a slower and more immersive mil sim. Historically accurate weapons and vehicles. Poor visibility from tanks, dying to a single bullet, etc. 
On the other hand, the low fidelity, simple AI movements, snappy one shot kills, latrine as a spawn point, etc. seems like it leans towards a goofy multiplayer sandbox game to play with friends.

Both can be true at the same time but defining what the core identity of the game is and leaning into that fantasy will make it feel more concise and will help refine all future decisions into a fully realised game.

PS: My preference would be to go for the goofy angle. Add silly ragdoll effects to the characters, leave mechanics a little wonky, aim for fun and functional and save yourself the trouble of over-polishing. 
I think both can work though so I’ll leave this angle out of my analysis below and stick to the point.

## 2. Onboarding & Tutorial

### Onboarding Principles & Recommendations

A strong onboarding experience teaches the player everything they need while keeping them immersed. A few things to aim for

- Make sure your tutorial conveys all the information a player needs to enjoy the game.

- Make sure it showcases the game's unique selling points well.

- Make sure it prepares the player for the game as a whole rather than just its individual systems. Especially since this is a multiplayer game and they will face existing players who will already have an advantage.

The first few moments are crucial - confused, frustrated, or bored players leave. A key goal with creating a strong FTUE is to keep players around long enough to experience one full loop of the intended game. Make sure to place as much focus as possible on the unique and exciting aspects of the game.

Get to the point - Get players into a complete gameplay loop as soon as possible.

Reduce confusion - Make every onboarding step easy to understand.

Reduce frustration - Keep tutorial steps short and snappy, and remove the ability to fail wherever possible.

Excite and reward - Reward players at every step. No need to pander, but showcase the exciting parts of the game, acknowledge correct actions, and make sure movement, gunplay, and construction all feel good.

Keep it simple

- Pace and structure the tutorial steps deliberately; remove unnecessary information from the UI.

- Don't run the tutorial and the normal game sequence in parallel. This is currently confusing, especially since both have their own tutorial sequences and voiceover text.

- Build a bespoke, smaller map containing only what's needed to complete the tutorial. If you also want players to try a map representing the final gameplay experience, have them enter that version at the end of the tutorial.

- Rethink the order in which steps are introduced. The current order conveys the necessary information adequately, but could better mirror the pace of a natural game. This is especially important when you reach the game phase sequence of the tutorial.

- Move the tutorial at the player's pace: give them time and space to actually try each mechanic before moving on (in the construction tutorial, designate a space, assign the item to build, switch to the hammer, construct it, repeat as needed for a second item like a trench, then a machine gun).

#### Reduce friction and increase clarity

- Moving to the "red smoke" objective has two issues: the smoke isn't visible enough (exaggerate the effect), and the trigger volume is too small (enlarge it, players should never fail such a simple task).

- Add HUD elements for objectives, and teach the HUD as part of the tutorial. The current onboarding puts too much information in a single text box; a separate UI element that only shows the current step's objective would clarify exactly what to do.

- Help players through the UI as part of the tutorial itself. Use simple highlights, arrows, and guiding prompts the first time a menu opens will help players find the correct buttons and slots.

#### Remove failure points

- Don't let the player move freely across a large map. Gate the level so movement only follows the tutorial sequence. If you want to keep a more open level, add a reset sequence that kills and respawns the player if they wander too far from the objective.

- Remove interactions that could confuse or distract: don't allow selling items the player needs (e.g., the hammer, losing it can mean missing the building system entirely), don't allow buying items irrelevant to the current step, don't allow building anything outside the current lesson. Remove irrelevant options from the UI wherever possible.

- Don't let players interact with the AI squad or its deployment before it's relevant. Consider removing the option to spawn or control a squad from every earlier interaction with the map, since this is the player's first exposure to it and there's no reason to expose options without necessary context yet.

- Dying to unseen enemies during scripted tutorial events is confusing, even if intentional. Add feedback to contextualize the event, or place visible dummy enemies so the player understands what happened.

#### Divide basic and advanced tutorials

- Consider splitting the onboarding: cover the basics first, then offer more advanced tutorials either at the end of the sequence or as optional next steps (this also gets players into the game faster).

  - Candidates for separate tutorials:

    - Advanced economy

    - Construction/building strategy

    - Advanced squad controls and strategy

    - Detailed walkthrough of the game phases

- A lot of the game phase tutorial sequence is spent describing what will happen when the player dies. Focus on conveying how the game works and present details about death penalties as advice, either in the current tutorial, a separate advanced tutorial, or as contextual advice during normal gameplay.

### Onboarding Sequencing

Players won't absorb the game's full complexity in their first few minutes. Get the fundamentals across first, then layer in mechanics and objectives in a structured order. Build lessons on top of one another, repeat important steps, and get the timing right.

The game blends several genres, which is a lot for a new player to take in. Two questions help set priority:

- Which part is most important to understand first?

- Which part showcases the game best? Assume a player will give it less than 10 minutes before deciding if they will keep playing or return the game.

Key gameplay elements players need to understand:

- Basic mechanics / micro loops - Movement, shooting, etc.

- Strategy and economy loops - Buildings, equipment, vehicles, etc.

- Objective and game tactics - Game phases, squad mechanics, etc.

- General strategy and application - How to apply previous learnings to achieve their objectives

Questions to help order these:

- What fundamentals does every player need, regardless of playstyle?

- What are the most important concepts and rules for succeeding in the game?

- Which of these concepts are prerequisites for understanding the rest?

- What part of the game should the player's attention be focused on?

Initial categorization to sort into an order: Fundamentals → Concepts and rules → Advanced mechanics.

### UI Text & Objective Clarity

- Many UI prompts currently contain too much information at once.

- Separate flavor text from tutorial/instruction text, use distinct UI elements or sequence them rather than combining them.

- Create a simplified UI element that shows only the current objective (e.g., "Move to the red smoke," "Interact with the flag"). This doesn't need to replace the fuller prompts, it complements them, and is especially useful for guiding players through sequences with many small steps.

### Step-by-Step Walkthrough of the Current Tutorial

I’ll go through the individual steps of the tutorial and give my thoughts on their current state. Most should be relevant regardless of how you rework the onboarding.

- Basic movement

  - This works well enough for the most part. The “red smoke" trigger volume is a little problematic though. I would make the trigger volume bigger so players don’t miss it and the smoke effect more visible.

- Shooting

  - The "red ball" target is too abstract; give players something more relevant to shoot (e.g., a dummy soldier). Since repetition is valuable and shooting is fun, add more targets for practice.

- Equipment

  - The spawned flag is easy to miss with another flag also in view, this is unnecessarily confusing. Move this sequence closer to the "real" flag instead. The step also combines too much information and too many objectives. I’d suggest splitting it into two steps:

    - Move to the flag and open the store as a single step.

    - Then a separate step inside the store UI with info and objectives about how to purchase the equipment.

  - Add UI graphics (highlights, arrows) to help players navigate the HUD/menus here. Example of an overly dense instruction: "Choose the vacant equipment slot right under 'hammer,' and buy a shovel for that slot."

  - Potential resequencing: move this step ahead of the shooting tutorial so players purchase their weapon first, then trigger the shooting tutorial, then return to the store for the next step - buying the shovel then return again for the hammer before moving into the construction tutorial.

- Shovel

  - This step works well enough as it is. The shovel could use some visual indication on the ground to help players dig more accurately but it’s not a crucial improvement

- Build sandbag wall -

  - The step should explain the purpose and strategy behind sandbags, not just how to place them; building one in the middle of nowhere teaches the "how" but not the "why."

  - Text instructions here are an improvement over earlier steps, they are shorter and more succinct.

- Build factory -

  - Text instructions here are good: two sentences, clear objective. The "Purchase" button is visible before it can be used, which is confusing. Either indicate it's disabled or hide it until construction is complete.

- Build artillery

  - There's a mismatch between the instruction and the menu: the prompt asks for "light artillery," but the menu only lists "M1897" and "Mle 1915." Instructions should match the actual menu wording exactly.

  - Other than that this step is straight forward enough.

- Towing artillery

  - Finding and aiming at the correct interaction point isn't clear enough; the "aim at the rear end" text helps, but the interaction itself needs improvement. Consider offering two fixed interaction options regardless of aim point (e.g., "E" to operate, "F" to tow).

  - The towing itself is slow and sluggish, understandable as a design choice, but the experience could be made easier to work with.

- Use artillery

  - Too much information in one step; split it up for better readability.

    - Cover stopping the tow and entering the seat,

    - Then aiming and shooting

  - The instruction to aim at "the building" isn't clear enough, add smoke or another marker to indicate the exact target building (always help guide the players attention, even if there is just one visible building)

- Heavy factory

  - Simple and straightforward, with a good amount of text and instructions.

- Enter the tank

  - Simple and straightforward, with a good amount of text and instructions.

- Driving the tank

  - Difficult to drive. Both first- and third-person camera views are poor until the windows are opened; either remove the closed-window option or fix the camera for it.

  - A quick fix would be to enter tanks with windows open, then have players experiment with closing them.

- Tank weapons

  - Camera issues persist here too (less severely) and should be polished.

  - Aiming is harder than it should be, since the crosshair doesn't align with the shell's actual trajectory.

- Repair a tank

  - A simple task, but there's no visual indication of the damaged portion the player is meant to find; this needs to be represented in-game.

- Defense phase and defense zone

  - This step carries a lot of necessary rules information, which is hard to avoid, but it should be broken into multiple steps: first frame the structure of the game mode, then cover the phases (their order, what's expected in each), then play the phases out in order. As currently built, the player doesn't get to try any part of the defense phase, the step only covers dying and its related cost.

  - Flag capture information should be moved to its own separate tutorial step (performing an actual capture), with this step circling back afterward to remind players the new flag needs defending.

  - Immediately dying at the start of this step is an unusual way to open it. It's a little funny and doesn't necessarily need removing, but it needs context and feedback (show enemies somewhere, and set it closer to the front line so the player understands they're in a risky position, add audio cues, etc).

  - Suggested rework

    - Place the player in a much smaller defense zone.

    - Have them practice constructing defensive buildings (sandbags, a trench, a machine gun).

    - Play the defense phase - assign the player to the machine gun and spawn a small wave of enemies.

- Respawn/Deploy

  - The tutorial text asks the player to "respawn at [B]," but the UI buttons say "Deploy", align the wording here.

  - The squad hasn't been introduced yet, so squad-deployment buttons should be removed for now.

  - The economy hasn't been introduced either, so death fines have no context yet, move this to a separate economy tutorial step.

- Excessive death penalty

  - Introduce the economy before explaining death penalties. That said, this is a better implementation of the player death sequence than in the defense tutorial step, deliberately moving outside the defense zone lets the player anticipate what will happen.

- Attack phase

  - The distance to the objective is too far. Shift this step's focus to what a successful attack looks like

  - KIA reward information can move to the end of this step or into a separate economy tutorial.

  - This is the third time in a short span the player is killed to teach a game-loop lesson  while the underlying lesson is useful, the repetition becomes excessive and distracts from learning about the phases.

- Spawn NPC squad

  - Jumping straight into commanding an attack and then ending the tutorial is a missed opportunity.

  - Teach more about squad control here, basic move/form-up commands, plus some sense of how this is used strategically, would go a long way.

  - Potential resequencing: Move this step to the start or middle of the attack phase tutorial

## 3. Core Design Elements

There's a lot going on in this game. Once you get the hang of it, it's fun and has real potential. Making the core loops compelling, impactful, and intuitive will be a continuous, evolving challenge. I’ll present some feedback in key areas below.

Map size

- The current map size and distribution of gameplay elements turns a significant portion of playtime into walking.

- Consider a smaller map and/or more concentrated control points to increase action and reduce travel distance.

- Consider transport vehicles to move players and squads between control points, factories, and other points of interest.

- The map is mostly empty. A blank canvas may work for advanced players, but could be improved with some simple additions:

  - Landscape features that encourage different play styles: high ground for defensive visibility, water to impede movement, rock formations for cover, dense forests to sneak through, civilian buildings for corridor gameplay and vantage points.

  - Pre-placed military structures the player's own options can build onto: towers to add machine guns, sturdy walls to reinforce with sandbags, bunkers to dig trenches toward, static artillery positions to defend.

  - General battlefield props to give the map some flavor and visual distinction between areas to help players identify different areas

Game phases

- The attack and defense phases feel arbitrary and static.

- Transitioning from the attack phase back to prepare is clunky. Too much time is spent walking back and forth, which takes away from the fun parts of the experience.

  - A teleport/redeploy option may or may not be the right long-term answer, but it's a cheap fallback that could be implemented quickly.

  - Shorter distances between points (see Map Size) would also help here.

Player health / power

- Being killed instantly, without understanding how, is confusing and frustrating. The feedback is insufficient, which makes it hard to learn how to improve and the immediate effect is quite jarring.

- Consider giving the player more health (just to avoid one-shot kills) so there's time to react. This would add tension to engagements and help avoid frustrating players in crucial moments.

- The power fantasy itself is solid: players feel they can meaningfully affect the tide of battle.

Control points

- It's barely explained how control points are captured or what the benefits are.

- Give more weight to holding a point, especially one just captured. Currently, capturing a point mostly means immediately defending a point you just took, with no clear additional benefit.

AI behavior

- Squad control feels janky, particularly around complex terrain and buildings.

- Enemy and allied NPCs both engage from ranges that make it hard to apply strategy.

- NPC movement and combat behavior is static and predictable, making rounds feel repetitive.

- NPCs make poor use of buildings, vehicles, and artillery.

- There are no squad commands for operating vehicles. Giving the squad the ability to make use of vehicles would give those vehicles more impact and add more weight to the squad command gameplay.

Progression, economy, and power dynamics

- Progression exists through the economy but arrives slowly, and the general loop feels static.

- It takes a long time to earn enough money to meaningfully affect the game.

- Many rounds play out similarly. Soldiers advancing in a straight line, then funneled into a pre-built barbed-wire maze.

- NPC count doesn't change over the course of a round, I think this is a missed opportunity.

- The most effective way to earn money is dying repeatedly near the enemy point. Rewarding proximity makes sense conceptually, but the payout is disproportionate to successful play.

- Alternative rewards that avoid an easily-griefed economy: kills inside the enemy point, time spent inside it, destroying enemy equipment, getting friendly NPCs inside it, building structures near it. Rebalance the KIA reward around time spent/enemies killed rather than raw distance to the flag.

#### New progression gameplay suggestion

I want to suggest an angle from which to redesign of the current game round progression. The idea is to build a clearer and more satisfying progression throughout each game, relying on existing mechanics, focused on making the initial rounds intimate then scaling in power as you get further into a match.

- Start smaller and grow faster:  fewer soldiers, less money, shorter distances between initial capture points, then unlock more as the round progresses. Even a slight shift toward a more minimal start could help; this can be taken as far as desired. I would experiment from as small of a start as possible and then scale up until you find your sweet spot.

- Scale the size of the conflict: start with smaller control points placed closer together for a more intense opening, then grow outward as points are captured and teams expand. A smaller starting scale makes early decisions (placement, attack/defense strategy, movement) more impactful and manageable, and teaches players to handle the same decisions at larger scale later.

- Grow your army: start with fewer NPC soldiers and a smaller player squad, recruiting more as the game progresses (either automatically or through buildings/UI menus). The cheapest version scales NPC count automatically over time or as control points are captured; a more advanced version lets players construct recruitment buildings, which builds soldiers into the economy (satisfying, but requires more balancing, assets, and UI work). This lets the game start on a smaller section of the map and grow the army to naturally overpower the early control points, giving players a power progression that matches the map's growing scale.

  - Optionally, add upgrades or new abilities for soldiers (cutting barbed wire, driving vehicles, new weapons, grenades, etc.)

- Mechanics with built in counters: the current building suite makes sense narratively but feels static in strategic impact. For every building, vehicle, and other strategic mechanic, consider introducing a mechanic that counters it in some way. It does not have to be perfectly 1:1 but there should always be some way to deal with the threat posed by the opponent.

  - For example, tools to cut through barbed wire or static weaponry to defend against vehicles

## 4. UX Improvements - Specific Interactions

Building mode

Snapping

- Issue: free-form object placement adds unnecessary friction.

- Suggestion: snap buildable objects to valid positions in the world; snap the pivot to the world geometry for ground-based objects, snap trenches to appropriate depths, etc..

Context UI interactions

- Issue: the "Construct" and "Operate" context prompts compete for the same UI space, and "Operate" doesn't work until construction is complete with no visual indication of that.

- Suggestion: add a visual indicator for each interaction's assigned button (e.g., a mouse-button symbol for Construct, an "E" symbol for Operate/Purchase/etc.), matching whatever control scheme or key the player has actually assigned.

Camera

- Issue: building on the ground requires pointing the camera downward, a poor angle mid-battle.

- Suggestion: find a better camera angle for build mode. Or as a quick fix, move the pivot point on buildable objects so that the player doesn’t need to aim downwards when building.

Digging

- Issue: no visual indication of where digging will occur.

- Suggestion: add a HUD element (e.g., a ground circle) showing the dig area in advance.

Streamlining

- Issue: the construction flow resets after every purchase, making it clunky to build multiples (the most common case for sandbags, wire, and trenches).

- Suggestion: keep the player in build mode until they manually exit, either for all buildings or for preselected ones.

Building menu

Affordability

- Issue: no indication of what the player can currently afford.

- Suggestion: color-code the cost text (green if affordable, red if not) and fade icons for items that the player can’t afford.

Sorting and categorization

- Issue: options in the building menu are listed in a somewhat arbitrary order.

- Suggestion: group into categories and sort the options by cost.

Lacking information

- Issue: no in-menu explanation of what the various buildings do.

- Suggestion: add brief description text in the available UI space.

Inconsistent interactions

- Issue: Buildings use a click-once-then-place flow, while weapons/utility use select-slot → select-item → confirm-buy.

- Suggestion: Unify the two flows. since items sell back at full price, the extra "buy" confirmation step may not be necessary at all.

Store menu

Poor readability in equipment store

- Issue: nothing distinguishes weapon slots from utility slots. Without experimenting, a player might not realize that you have different slots for different types of equipment.

- Suggestion: adjust the UI to make the different slot types clear, both in the shop and in the player equipment section (just making the UI elements stand out from one another would be enough as a start).

Vehicle interactions

- Interaction points for towing vs. operating aren't distinct enough.

- Artillery controls feel sluggish and "floaty." Deliberately slow controls can be a valid design choice, but the controls could be tightened up a bit and movement of the artillery pieces when colliding with other objects could use some polish.

- Player visibility in the tank is too constricted without open windows. Even if the intent is a more immersive, challenging camera view, the current implementation looks broken.

Map icons

- Map icons are initially hard to read.

- Marking the player with a red circle isn't intuitive, and using the same color for enemy spawn points adds to the confusion.

- The circles around squad NPCs, spawn points and vehicles look the same which confuses their intent and gameplay purpose.
