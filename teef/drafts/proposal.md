# Aurora Punks - Co-Development Proposal: Teef

*Response to The Experimentation Group / Makosch VGDC co-dev brief (15 May 2026). Prepared for Tom Storr. Confidential.*

> Draft for Robert's review before sending. **Dual quote**, each total = build + QA (Northify €8k) + 10% contingency:
> **Option A reads-as-London €110k** (build €92k), recommended. **Option B street-accurate €121k** (build €102k, environment artist 50%->100%). Builds trimmed ~€4k each vs first numbers: with no A/B creative test, Hassan goes straight to in-game representation, so less environment art in the pre-prod fortnight (shows the client we are responsive - figure to confirm). Client pays Unity engine license fees. Naming/redactions resolved (see bottom).

---

## Studio fit

Aurora Punks is a collective of independent game developers, 40+ members across several studios, built around co-development and self-publishing. We work full-cycle, from concept and prototype through live ops, porting and post-launch updates, and we have shipped across PC, console, mobile, Roblox and VR. Our model is to plug an experienced, senior team into a partner's project and hit a fixed date on a defined slice. That is exactly the shape of this brief.

Why we are a strong fit for Teef specifically:

- **Mobile and fast prototyping.** We built Hooja the Game, a 16-bit mobile auto-runner for one of Sweden's biggest pop acts, taken from a music-video concept to a shipped, stylised mobile title at speed. The kind of fast, art-led mobile turnaround Teef's first slice needs.
- **RPG and Unity networking.** We developed and self-published Tears of Adria, a Unity RPG with online multiplayer, 180 launch upgrades and a 94% Very Positive Steam rating. The systems, networking and performance work was led by the engineer we would put on Teef.
- **Real-world maps in 3D.** On the BADASS XR platform our team reconstructs real locations as game-ready 3D environments from geo data, which is precisely the geo-to-3D approach Teef's London needs.
- **Casual mobile, our own IP.** BlockEm is live on Steam and shipped to browser via Wavedash in 2026, a casual title in our own hands end to end.
- **Co-development to AA.** Active, shipped, cross-platform co-dev with Raw Fury (PC and console), plus others across PC, console and VR, plugging senior teams into partner projects under their direction.
- **AI-assisted production.** We use AI in our tech-art pipeline to produce environment and asset volume at speed, matched to your art style. It is what lets a small, senior team deliver a full London and a large cast inside a six-week build.
- **Unity and map APIs.** Unity is our primary engine across co-dev and our own titles, and we have hands-on experience with the runtime map-API route too (we have shipped on Cesium). For Teef we recommend baking from open geo data instead, for offline play and cost, with map SDKs kept as reference/fallback.
- **Backend and live services.** We build on industry-standard backends (PlayFab, AccelByte, Firebase) and smaller or proprietary ones (LootLocker), and roll our own when a project needs it. Directly relevant to Teef's remote config, event tracking and crash reporting.
- **Time zone.** Central European, one hour ahead of the UK, full working-day overlap and same-day turnaround on the Friday demos.

---

## Track record

A spread of what the collective has shipped and is shipping, from live AA co-op and arena shooters to full self-published titles and real-world-data tech. The same people are on Teef. (Steam capsule per title in the pitch page.)

- **Helldivers 2 (Arrowhead).** Backend and UI art on the live co-op shooter, at AA scale and under live-service load.
- **Warhammer 40,000: Darktide (Fatshark).** Senior gameplay and engine/render programming on the four-player co-op shooter. Robert ran the first-party and engine team at Fatshark as Senior Producer.
- **The Finals (Embark).** Cross-platform release management, commerce guidelines and QA analysts on the free-to-play arena shooter.
- **Ready or Not (Void Interactive).** Multi-year co-development: UI programming, the UE4 to UE5 tech migration, console porting and optimisation, and QA.
- **Ghost Signal: A Stellaris Game (Fast Travel Games / Paradox / Meta).** Full development partner on the Paradox VR title for Meta Quest. Cross-platform VR, shipped.
- **Tears of Adria.** Our own Unity RPG, developed and self-published. Online multiplayer, 180 launch upgrades, 94% Very Positive on Steam.
- **Hooja the Game.** Full development. A 16-bit mobile auto-runner taken from a music-video concept to a shipped, stylised title for one of Sweden's biggest pop acts.
- **BADASS XR platform.** Real-world data integration - reconstructing real locations as game-ready 3D environments from geo data, the same geo-to-3D approach Teef's London needs.
- **Raw Fury.** Co-developing an unannounced upcoming DLC for a major franchise. Active, cross-platform, under the partner's direction. (No franchise or repo named, per confidentiality rules.)

---

## Approach

### Art direction

Your style guide proposes three directions. We have rendered two of them here to show our build quality, and can take any of the three to production - your call. The visual direction is also independent of map fidelity (Option A or B, below): any direction works at either fidelity.

- **Brutalist.** Desaturated London stone, a dramatic crimson zone-glow, green objective accents. Premium, gritty, high-contrast. Leans mid-core, and makes a striking store creative.
- **Casual.** Vibrant, saturated, playful neon over warm London streets. Broad-appeal, soft and inviting. Leans casual, and widens the top of the install funnel.

We would lock the art direction with you early, from your style guide. Whichever of the three you pick, the same stylized character cast - the Teef crew and their marks, in the designer-toy style from your guide - carries through, so it is one base re-skinned, not separate builds. (Two of the three directions shown in the pitch page.)

### Mapping and London building rendering

We want the same thing you do: London that reads as London at a glance, including for an Argentine player landing cold on Mission 1. Whichever fidelity we land on below, the method is the same - we reconstruct Soho and East Mayfair from real geo data and stylise it, baked into the build, rather than rendering a generic map layer at runtime.

- **Geo data, reconstructed once.** We take real building footprints and heights for Soho, East Mayfair and the bordering areas from open geo data (OpenStreetMap / Ordnance Survey OpenData), plus street-level reference imagery, and reconstruct the block layout as 3D geometry. The map is built once and baked into the Unity project as static scene data - so play is fully offline and there is no per-load runtime map cost.
- **Stylise on top.** Tech art, AI-assisted, treats that massing in the agreed art style - real-feel proportions and recognisable London landmarks (Big Ben, black cabs and similar cues), not abstract blocks. This is what gives the map character rather than a generic extruded look.
- **Camera-relative transparency.** Tall buildings that would obstruct the player fade to transparent based on camera angle and player position.
- **Bordering-area fade.** Fitzrovia, Covent Garden and parts of West Mayfair appear and fade with distance from the unlocked space; far areas (Knightsbridge) sit outside the visible range for this build.
- **Licensing, stated up front.** Open geo data carries clean, well-understood terms (OSM under ODbL; OS OpenData), with no runtime mapping dependency. Mapbox remains a reference/fallback if we ever need its 3D-buildings layer; if used, we confirm its terms permit baking derived geometry into a shipped product before relying on it. We state the final licensing position in writing before kickoff.
- **Brand safety:** we follow your "Danny's Dogs" pattern and invent fictional brand names for any in-game signage to avoid trademark exposure.

Where we land on fidelity is what sizes the art, so we are quoting both, as you asked:

- **Option A - Reads-as-London (our recommendation for the test).** Regent Street and Oxford Street as recognisable navigational spines, Georgian terraces, a handful of black cabs and red phone boxes so it reads as London at a glance, and stylised building facades in the Soho/Mayfair palette. Individual buildings are not street-accurate, but the neighbourhood feel is there. This is the efficient route for a soft-launch test that is really measuring CPI and early retention - it puts the art budget into the first-day surface that moves your numbers, which matches your own read that efficiency is the right call.
- **Option B - Street-accurate Soho and Mayfair.** Real footprint accuracy for Soho and Mayfair on top of the same baked-geo base - materially more environment art, as you would expect. The map matches the real street layout block for block. We carry this by putting the environment artist on the build full-time rather than half-time (see Commercials for the cost difference).

Our honest read: Option A gets you clean CPI/D3 numbers faster and cheaper, and it is what we would pick for this test. Option B is there if the "looks like London" bar in the brief means literal street accuracy.

### Tuning workflow (Google Sheet to remote config)

You keep the Google Sheet as the single source of truth. We build a thin, safe push:

1. A small export step reads the Sheet and produces a validated config payload.
2. Schema validation catches bad or out-of-range values before anything ships.
3. A dry-run diff shows exactly what will change, then a publish step pushes to **Firebase Remote Config** (acceptable per the brief).
4. The running game fetches remote config on launch - so you re-balance economy, progression and skill values with no code release and no new build.

This keeps you in control of the numbers while protecting the live build from a bad paste.

---

## Delivery

### Team

A small, senior team drawn from people we have shipped with before. Four full-time-equivalent on the build for Option A; Option B adds the environment artist to full-time.

- **Tech Lead, Oskar Hansen (full-time).** Unity systems, online multiplayer, performance optimisation and platform porting. He built the systems and networking behind Tears of Adria. On Teef he owns the core systems, mobile performance and the geo-to-3D London map. He also carries enough design capacity to drive day-to-day calls against the GDD, with Tom as design authority on your side.
- **Gameplay programmer, Fredrik Laurent (full-time).** Missions 1 to 6, economy, save/autosave, the Magnetic SDK and the Sheet-to-remote-config pipeline. Unity architecture with an enterprise engineering background at Accenture.
- **Concept and art direction, tech / character artist, Hasan Chenari (AI-assisted, full-time).** Concept and art direction for the build, plus the cast of around 35, the full animation set and supporting art.
- **Environment artist, Prateek Karajgikar (AI-assisted).** The geo-to-3D London map, the locations, UI and app icon. Half-time on the build for Option A; full-time for Option B, where the street-accurate Soho and Mayfair footprints are the extra workload.
- **Production, audio and design (shared half-seat).** Robert Bäckström on production - oversight, client cadence, weekly demos and milestone sign-off (20 years shipping games, from Fatshark and Raw Fury to founding Aurora Punks); Tim Browne (Creative Director and Lead Designer) advisory on design direction; and Carolina on SFX and audio. Light-touch functions sharing one seat, so the build headcount stays lean.

QA and Play submission are covered inside the team - the Tech Lead and build run the device matrix and the pre-submission compliance pass (see QA and device matrix below), rather than a separate QA seat, which keeps the build at four FTE.

### Roadmap (6-week build to soft-launch candidate)

A focused six-week build, delivered ahead of the end-Q4 launch window to leave you runway for balancing and soft-launch operations. It is sequenced so the CPI/D3-critical surface - Mission 1, the FTUE and the opening 30 seconds - is proven and polished first, with Missions 2-6 filling in behind it. One playable build and live demo every Friday, per the brief.

- **Week 1 - Pre-prod:** tech spikes on the geo-to-3D bake and the Sheet-to-remote-config pipeline; repo, CI and Play internal track set up; art direction agreed; Mission 1 planned.
- **Week 2 - Foundation:** art style and direction locked from your one-pagers; Mission 1 vertical slice underway and de-risked - FTUE, Phase 1 (approach), Phase 2 (resolution), Wanted/chase - on a real-feel Soho map, running on device.
- **Week 3 - Soho:** Missions 2-4 playable end to end, economy wired to remote config, Magnetic SDK producing clean install and in-game events.
- **Week 4 - Mayfair:** Missions 5-6, full character and animation set, audio in, app icon delivered.
- **Week 5 - Hardening:** balance pass with TXG across Missions 1-6, 30 fps stable on min spec, QA device-matrix pass.
- **Week 6 - Soft-launch candidate:** Play Console internal track, then the Argentina release build.

This pace assumes the GDD and art one-pagers are build-ready at kickoff and that the prototype's logic is available to build on.

### Working channel and meeting rhythm

- Weekly Friday playable build + live demo as the heartbeat of the project.
- Async day to day on your channel of choice (Slack/Discord/email).
- Google Sheet as the design source of truth; agency-hosted repo with read access for the client, transferred on delivery.

### Handling scope changes

The Friday demo is the change surface. Small tweaks that fall inside the §3 scope we absorb in flow. Anything beyond it gets a short written change order - effort, cost and schedule impact stated - against the rate card, so the fixed date stays protected and there are no surprises.

### Handling slipping milestones

The weekly demo gives early warning, not an end-of-project shock. Because the end-Q4 date is fixed, we protect it by triaging scope, not quality: the M1/first-30-seconds polish is non-negotiable; art depth on Missions 2-6 is the planned flex. If a milestone is at risk we raise it at that Friday's demo with options, not after the fact.

### QA and device matrix

We carry development QA inside the team - the Tech Lead and build run continuous testing across the device matrix throughout the build. For independent functional and compliance QA we bring in a specialist QA studio rather than self-certify; our preferred partner is Northify. That gives the soft-launch build a dedicated functional and Google Play compliance pass from a team whose only job is to try to break it, which matters more than usual when the test is spending real UA money against the result.

- Test plan covering the full mission flow, save/autosave integrity across sessions, 30 fps stability, and correctness of Magnetic SDK event reporting.
- Android device matrix spanning the min spec (Android 9+, 4 GB RAM) up to current devices, agreed with you at kickoff.
- Crash reporting via Firebase Crashlytics, on the same Firebase backend as remote config, so there is no extra dependency in the build. Live crash and ANR visibility from the first internal build through the Argentina release.
- Functional and compliance QA via our specialist partner (Northify): a structured functional pass plus the Google Play pre-submission compliance pass before the Argentina release build.

---

## Commercials

- **Model:** milestone-based fixed price over a six-week build. It fits the fixed launch date and the mandatory weekly cadence, gives Makosch budget certainty, and ties payment to accepted milestones.
- **Two quotes, per your ask on London fidelity. Each total includes the build, functional + compliance QA (Northify, €8k), and a 10% contingency:**
  - **Option A - Reads-as-London: €110k** (build €92k + QA €8k + 10% contingency). Four-FTE team, six-week build at €80/h. Our recommendation for the soft-launch test.
  - **Option B - Street-accurate Soho and Mayfair: €121k** (build €102k + QA €8k + 10% contingency). Same six-week build, environment artist full-time rather than half-time, to carry the street-accurate footprint work.
  - **Leaner pre-prod.** With no separate creative test to produce, our art director (Hassan) goes straight to getting the concepts into the game rather than building variants, so we trim environment art in the opening fortnight and take roughly €4k off each build versus our first pass.
  - **Option A is the budget call.** Running the environment artist at half time carries only half the map-art cost, so the recommended route is also the cheaper one - the right discipline for a soft-launch test where you keep spend lean until the numbers justify scaling. Step up to Option B only if you want street-accurate footprints.
  - Pass-through costs are billed at cost on top of either, and production oversight is included in both. Assumptions stated: Android only; scope per §3; polish concentrated on the CPI/D3-critical surface; GDD and art one-pagers build-ready at kickoff.
- **Functional and compliance QA (specialist partner, Northify):** €8k, included in each total above. An external specialist functional + Google Play compliance pass; in-team development QA runs throughout the build on top of it.
- **Contingency:** a 10% contingency is held in each total against the fixed end-Q4 date.
- **Engine licensing:** Unity engine license fees are paid by the client.
- **Payment schedule (either option):** 30% deposit on signature; 40% on the mid-build milestone (Missions 1-4 accepted); 20% on content-complete; 10% on store-live acceptance, with a small retention released after the support window.
- **Pass-through costs (at cost):** open geo data (open-licensed, near-zero), AI tooling, music licensing, QA device hardware, Play Console fee.
- **Post-launch support:** 30 days for critical bug fixes and store re-submissions, capped hours, then time-and-materials.
- **IP:** the client owns all code, art and audio on delivery, with unrestricted rights to take the codebase forward. Source repository transferred at end of project.

---

## Risks and open questions

**Top three risks**

1. **Geo-to-3D reconstruction landing on-style and on-time.** Turning raw footprints into a stylised London that reads at a glance is the first dependency for everything visual. Mitigation: a Week-1 spike that proves the geo-to-3D-to-art-style pipeline on one Soho block before production scales; open-data licensing (OSM/OS) keeps the source clean.
2. **Art volume against a six-week build, and keeping it human.** ~35 characters, ~9 locations, UI and a full animation set in a custom style is the critical path. Mitigation: an AI-assisted pipeline carries the volume, but under human art direction (Hasan) with a human-feel check on every asset so it reads as crafted, not generated; polish concentrated on the CPI/D3-critical surface (Mission 1 + first 30 seconds); aggressive NPC-variant reuse.
3. **Second-to-second gameplay not yet proven in the prototype.** The prototype proves the concept, but not the moment-to-moment feel yet, and that is the thing we will watch hardest. Mitigation: treat the prototype as a logic reference, prove the Mission 1 loop feel first in weeks 1-2, and put a playable on device every Friday so feel is tuned with you early, not discovered late. Missions 2-6 are fully specified but not yet played end to end, so the same weekly loop plus remote config (tuning with no code release) covers them.

**Open questions**

- Target kickoff date? End-Q4 is fixed, so this sets when the six-week clock starts.
- Option A or Option B on London fidelity - quoted both above; your pick sets the environment-artist allocation.
- Magnetic SDK integration specifics and credentials timing.
- Art-direction one-pager availability (the highest-leverage input for M1).
- Expected soft-launch install volume.
- Confirmation of the min-spec device list for the QA matrix.

---

## Voice / mood pieces (Copy Style Guide demo)

Three thirty-second moments, first person, in the Lock Stock register the Copy Style Guide calls for. Shows we have the tone before a line of in-game copy is written. Placed in the pitch as interludes between the numbered sections (paired with Hassan's character art), to carry the reader through the data with a feel for what the IP delivers.

**The guv'nor - top of the manor**

That's him. The guv'nor. Owns this manor end to end, every corner, every fence, every little firm pays up to him. Struts about like the pavement's his, and right now, fair enough, it is.

Me, I'm nobody yet. Few quid in me pocket, a crew you could count on one hand, a name nobody's lost a wink of sleep over. I know it. It's a long old road from here to where he's standing.

But I'm watching. How he moves, who he leans on, where he's gone soft. Every wallet I lift, every kid I bring in, that's another brick out of his wall. He don't know me name yet. He will. One day the whole manor's mine, and he just don't know it.

**New blood - keep it on the low**

Quick word on the blower to me newest earner. Kid's flying. Three clean lifts this week, brought a couple of his mates in, got a proper eye for a fat pocket. Reminds me of meself, not so long back.

But I tell him straight. Easy, son. Nothing burns a face quicker than flash. New garms, gold round the neck, flashing your takings about, that's how you get known, and known is how you get nicked.

Keep it quiet. Spend small, look skint, let the money sit. The ones who last ain't the loud ones, they're the ones nobody clocks. Stay low, keep earning, and one day you won't have to hide it. Not yet, though. Not yet.

**The haggle - Harry the fence**

Built like a brick outhouse, face like a smacked arse, a stare that'd curdle milk. First time you meet Harry you'd swear he's about to fold you in half. He plays it mean and all, grunts, glares, makes you sweat. It's an act. Mostly.

Cos here's the thing. Whatever you've lifted, whatever's gone warm in your pocket, Harry'll move it. Gold, watches, the odd dodgy phone, he's got a buyer for the lot. No questions, no grassing, fair coin in the end. Best fence in the manor, bar none.

So you let him do his big-man routine. "Hundred quid," he goes, not even looking up. Hundred? Harry, you having a laugh, this is eighteen carat. Back and forth we go, he sucks his teeth, I act wounded, we meet in the middle and both pretend we got done. Always do business in the end. Pleasure as always, you robbing old goat.

---

## Naming / redactions - RESOLVED (Robert, 2026-06-18)

Robert greenlit naming all of the following **in this document specifically** (the no-other-client rule is overridden here by explicit, doc-scoped permission; it does not transfer to other docs):

- **Named credentials kept:** Hooja (the Game), Tears of Adria, BlockEm, BADASS (cited for the maps / geo-to-3D experience), Raw Fury, plus Fatshark in Robert's bio.
- **Named resources kept:** Oskar Hansen (Tech Lead), Fredrik Laurent (engineering bench), Tim Browne (design direction - has history with Tom, a relationship asset), Robert Bäckström (production).
- **Resolved (Robert, 2026-06-18):** Oskar Hansen front-of-house Tech Lead, Fredrik Laurent on the engineering bench. Tim Browne is light-touch advisory design direction (not a costed seat), which keeps the 4-5 dev / €96k envelope intact. "Hansen" spelling confirmed.
