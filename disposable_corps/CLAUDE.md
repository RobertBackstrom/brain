# Disposable Corps (Armoured Dudes) - CLAUDE.md

## Engagement
- **Role:** AP services engagement on *Disposable Corps*, developed by **Armoured Dudes** and published by **Light Up Games (LUG)**. Scope not yet set. The 2025 shape was co-dev / production support (devs + producer on site) plus tech art and tool setup. Re-opened July 2026 via Anthony Wong.
- **DB prefix:** `dsc`
- **Status:** active - live ask. LUG (Magnus) asked 2026-08-17 for a high level plan to take to project investors at Gamescom, framed as **AP taking over production**, dropping the dedicated-server cost and shipping a tight core loop in 6-12 months. Plan delivered 2026-08-26. Still no scope contract, no repo access and no NDA with Armoured Dudes directly (the 2025 NDA was with LUG).
- **Agent owner:** BizDev (deal + outreach), GameDev (any technical assessment), CorpBot/Lawyer (NDA + contract when it gets there)

## Counterparties
Two separate parties. Keep them apart in any material.

**Armoured Dudes** - developer, the actual client. **Two people as of 2026-08-26: the founders.** Paul codes, Hammer carries vision and game design. The earlier four-person team (main programmer, junior programmer, designer/CEO/producer, artist) is gone; Anthony's internal note is that it was junior and its UI/UX was bad. Never put that assessment in writing outside AP. They are now inside the budget at 30 000 SEK a month for both, a number Anthony set.
- **Hammer** - co-founder. Full name unknown. The founder Robert had the Teams call with 2026-07-17.
- **Paul** - co-founder, **technical / lead dev**. Full name unknown. Was the blocker: told Anthony 2026-07-07 that the only way co-dev works is if the technical support "only listens to him". **Resolved in principle 2026-08-26** by Robert's working model, which Anthony accepted in the shared group: AP raises the fixes and sets deadlines, Paul keeps the implementation. Handle it as a working model, never as a person.
- **Hing Chong** - producer, hing@lightup.games. LUG-side producer assigned to help the Disposable Corps team. **Use the lightup.games address, not the personal one** - he explicitly asked for that (2025-09-08).
- 2025 thread addresses, owners unconfirmed: hanmo14010817@gmail.com, cycle6@hotmail.com, zboz85@gmail.com

**Light Up Games (LUG)** - publisher of Disposable Corps, and the intro channel
- **Magnus Lysell** - founder, magnus@lightup.games / lysellmagnus@gmail.com. Ex-Paradox. Made the original intro.
- **Anthony Wong** - anthony@lightup.games / thetonywong@gmail.com. Current live channel (Discord).
- Profile: ex-Paradox team, founded 2023, Shanghai-based, Asia-focused. Publishing-services/advisory model - no project funding, small retainer + small revshare. Strong in China, weaker on Western reach. See [[bizdev_learnings]].

**AP side**
- **Robert Bäckström** - Founder / Exec Producer, robert@aurorapunks.com

## Infrastructure / Resources
- **Steam:** [Disposable Corps](https://store.steampowered.com/app/3579070/Disposable_Corps/) app **3579070** (store page also seen as "Disposable Corps: Tactical Trench Warfare"). Demo app **3617330**, first public demo 2025-05-16.
- **The game:** tactical low-poly 5v5 shooter, WW1-era with steampunk mechs. Squad command, base-building, real-time tactical defense. Gameplay trailer + updated demo Aug 2025.
- **Shared with them:** https://pitch.aurorapunks.com/team/ (AP core team + partner studios + shipped titles), delivered on Discord 2026-07-23 for Hammer/Paul to read.
- **The plan (2026-08-26):** internal source at `drafts/dev_plan_high_level.md`, external gated page at **https://pitch.aurorapunks.com/disposable-corps** (`lug` / `kE4hhTF44sXN`). Audience is Magnus plus LUG's project investors.
- **Product state, verified 2026-08-26:** Steam "Coming soon", no release date, no reviews. Demo live since 2025-05-16. Two public playtests (Sep 2025, Dec 2025 "Refactoring Update"). **No public update since 2026-01-10**, seven months of silence. Store page already lists LAN PvP/Co-op and the Dec build added a server list with a host-region filter, so player-hosted play looks partly built already.
- **Publisher-side problem list (Anthony, 2026-06-12), internal only:** UI/UX bad, map poorly designed and too big, players confused about what to do, bots kill the player too fast, bot pathing and commanding bad, overall not fun. His stated cause: lack of skill and no sense of game design. **Never repeat that assessment in writing to anyone outside AP.**
- **Gmail threads:** `19851c3c40f6e46b` ("Disposable Corps", intro) and `1989745d9f5d43d3` ("Aurora Punks Services (Hing Light Up Games)", the proposal + on-hold reply).
- **Discord:** Anthony Wong DM, plus the group **LUG <> AP Disposable Corps** (Anthony, Magnus, Robert), created 2026-08-26 by Anthony and renamed by Robert. This is now the live channel. The proposal has been sent there and LUG will package it for their finance partners.
- **No project GDrive folder yet.** Create one under AP when there are deliverables - [[feedback_deliverables_to_project_folder]].

## How the game works today (reconstructed 2026-08-26)

Sources: the 2025-09-25 playtest post (control list, the clearest single statement), the demo and
playtest patch notes, the store description, and Robert's own tutorial screenshot. **Not verified
against the build by an AP dev.** Correct this section from the phase 0 review, do not treat it as
settled.

**Controls, verbatim from the developer (2025-09-25):**
- `B` buy weapons and items
- `I` build fortifications
- `M` open map and **recruit AI soldiers at spawn icons**
- `T` open the command menu to **issue orders to your AI squad**

**The round.** Phases cycle `[Prepare]`, `[Defense]`, `[Attack]`, with the two teams on opposite
phases. Flags are capture points. Each flag has a white circle on the ground; capturing it makes
that circle your team's **defense zone**, and the tutorial tells the player to stay inside one
during Prepare and Defense. Waypoints are marked with coloured smoke.

**The economy.** Players earn money (kills, presumably objectives; killing a friendly deducts it)
and spend it three ways: gear via `B`, fortifications via `I` (sandbags, gun nests, spawn points,
and since Aug 2025 a **buildable vehicle factory** that produces tanks), and **AI soldiers via `M`**.

**The squad layer already exists.** The player recruits AI soldiers and commands them from a menu.
NPCs also assist with building since the December refactor, and the AI was reworked "to handle more
units and complex tasks". So 5v5 already means far more than ten bodies on the field.

**Combat.** First and third person, WW1 arsenal (Chauchat, Lewis), tanks (A7V) with armour
deformation, track damage and ammo racks, heavy artillery with gunner seats, destructible terrain
and digging.

**Hosting.** A server browser exists, and January 2026 added a **host region filter**. Steam lists
LAN PvP and LAN Co-op.

**What this means for the plan.** Squad recruitment and command are not something AP would add,
they are the existing differentiator and they are on the publisher's fault list precisely because
they do not work well (bad pathing, bad commanding, enemy bots too lethal). Any AP material must
describe this as **retuning and fixing what is there**, never as introducing it. Robert flagged an
earlier draft that got this wrong on 2026-08-26.

## History
1. **2025-07-28** - Magnus Lysell introduces Hing Chong. LUG suggests AP could help the Disposable Corps team with what they need.
2. **2025-08-06** - call, AP tech team + Hing (team sits in China). AP sent a deck ahead of it and asked for source code access under the existing LUG NDA.
3. **2025-08-11** - AP proposal: Oskar + Basil (dev) plus Gustav (producer) on site a few weeks to learn their process and feed back best practices, then tech art and tool setup. Rates normally **40-80 EUR/h**, discounted **flat 35 EUR/h** for the initial August period, with an opening for a hybrid model (lower/no monthly fee + recoup/revshare) once scope was known.
4. **2025-09-02** - Robert follows up, sets up WeChat.
5. **2025-09-08** - Hing: **on hold** after internal discussion. "Once we're ready to move forward and need further support, we'll be sure to reach out."
6. **2026-07-16** - Joel Edström (The Gang) notes LUG has been busy with their own investment round. Robert has a meeting with Anthony "about another project".
7. **2026-07-23** - Anthony asks on Discord for an AP presentation that Hammer/Paul can look at.
8. **2026-07-24** - Robert shares https://pitch.aurorapunks.com/team/.
9. **2026-06-04 to 2026-08-14 (Discord, Anthony Wong)** - Anthony sends the demo as the latest build; Robert plays the tutorial 06-11 and reports rough UX; Anthony gives his problem list 06-12; budget signal 06-18 is "probably only revenue, maybe a bit from marketing"; goal is **Early Access**, 1.0 is far off; Robert proposes co-dev with himself as producer and product owner 06-21; **07-07 the devs are "very anti-codev"**; call with the non-technical founder happens 07-17; **08-12 Hammer and Paul are building their own deck and roadmap to raise capital** and have given no answer on co-dev.
10. **2026-08-14 to 08-18 (WhatsApp, Magnus)** - Magnus asks whether Robert is working on a plan. Robert: ball is with them, one founder not bullish on co-dev. **08-17 Magnus asks for a high level plan**: AP takes over, no server dependency, tight core loop, release in 6-9 or maybe 12 months, investors he meets at Gamescom, modest budget plus incentives. Robert promises the plan before Gamescom.
11. **2026-08-26** - Plan written and published (gated). Awaiting Robert's decision on split and deferral before it is shared.

## Why
LUG keeps sending AP work (Disposable Corps 2025, Curveball 2026) and is the warmest recurring intro channel into Asia-published titles. Disposable Corps is a live, marketed title with a public demo, so the need is real production/co-dev capacity rather than a pitch. Landing it converts a dormant 2025 lead into paid AP dev revenue and deepens the LUG relationship that also carries [[project_curveball]].

## Open items
1. **Robert's three commercial decisions** before the page is shared: the net split opening (50/25/25 is my proposal, not a mandate), the deferral level (30-40 percent of AP's fee from phase 2), and whether phase 0 is paid or goodwill. See `drafts/dev_plan_high_level.md` section 9.
2. **The mandate question.** The plan only delivers if AP can make product decisions. Paul's position is the opposite. Phase 0 is the move that starts without settling it.
3. **Two parallel capital tracks.** Hammer and Paul's own deck versus LUG's investors. Risk that AP's plan becomes a bargaining chip.
4. **Full names and roles for Hammer and Paul.** Only nicknames known.
5. **No repo or build access, engine unknown.** Every number is a range until phase 0.
6. **The 2025 bemanning is stale.** Oskar, Basil and Gustav were the AP constellation then, not now. Any new proposal needs a current team and a current rate.
7. **pitch.aurorapunks.com/team/ is marked Confidential in its og-description but served ungated.** Anyone with the link reads it. Decide whether it should be gated like the Curveball pitch.
8. **No NDA with Armoured Dudes.** The 2025 NDA was with LUG. Scrub IP in anything contractor-facing until that's fixed - [[feedback_scrub_ip_until_mnda]].
9. **Direct vs via-LUG.** Decide whether AP contracts with Armoured Dudes directly or through LUG. Affects pricing, IP and who carries the risk.

## Conventions
- Keep the two counterparties distinct. LUG is publisher and intro channel, Armoured Dudes is the client.
- Never name other AP clients in outward-facing material - [[feedback_no_client_cross_reference]].
- Robert's voice on all drafts - [[writing_voice_robert]]. No hype, no em-dashes.
- If a project pitch is needed, HTML living-doc at pitch.aurorapunks.com/<slug> - [[feedback_html_pitch_living_doc]].
- Deliveries logged to `output_log.md`, local drafts to `drafts/`.
- **Robert's own findings from playing the build go in `build_feedback.md`.** Internal only, nothing goes to Armoured Dudes or LUG without his approval. It feeds the phase 0 fix list.
- Deal pipeline in the wiki: `wiki/deals/projects/disposable_corps.md`, update via `/ingest-deal-email` after every touch.
