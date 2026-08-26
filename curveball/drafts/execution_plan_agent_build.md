# Curveball: execution plan for an agent-built P2P conversion

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Author** | The Assistant |
| **Revises** | [dev_plan_p2p_steam.md](dev_plan_p2p_steam.md) (Fable, 2026-08-04). The technical plan stands. This changes **who builds it and in what order**. |
| **Build machine** | Bare metal, capable of running the UE 5.3 editor, live **Monday 2026-08-10** |

## 1. What changed and why it matters

Fable's plan assumes one full-time senior developer at roughly 40 h/week, and it sequences work the
way a human would: finish Phase 0, then Phase 1, then Phase 2. Two of its assumptions are now wrong.

1. **The Assistant implements, Robert does QA.** Not Robin. The plan's per-WP ground rule ("Robin
   executing / agent supporting") should read "agent implementing, Robert QA".
2. **Section 11.2 no longer holds.** "100K SEK over ~350 h is ~285 SEK/h, well under market" priced
   a subcontractor invoice. There is no invoice. The hours still describe the *work*, but they stop
   describing a *cost*. The commercial conclusion in 11.3 survives intact and is the one that
   matters: **the mobile port does not fit and should be priced separately.**

Two consequences follow, and they are the whole reason for this document.

**Writing code stops being the bottleneck.** Compiling, running and QA-ing it becomes the bottleneck,
and both need a machine that does not exist until Monday. So the useful question is no longer "what
order do the phases go in" but **"what does each piece of work depend on"**.

**Robert's QA time is now the scarce resource.** Dev hours are elastic; a human reviewing a build is
not. That argues for fewer, fatter QA sessions with a written test script per session, rather than
the continuous back-and-forth a human dev would generate.

## 2. Three lanes, not four phases

| Lane | Depends on | Can start |
|---|---|---|
| **A. VPS-native** | Nothing. No UE, no editor, no compile. | **Now** |
| **B. Build-machine** | UE 5.3 + the project building | **Mon 2026-08-10** |
| **C. Robert QA** | A packaged build that runs | After B produces one |

The re-sequencing insight: **Fable put the grant service in Phase 2 (weeks 5 to 7). It has no
dependency on Unreal at all.** It is a small Node service on the AP VPS, roughly 20 to 26 h of its
30 to 40 h WP2.1 estimate, and it can be written, tested and deployed this week while the build
machine is still in a box. A human dev could not parallelise that against themselves. We can.

### Lane A: what runs before Monday (Tue 2026-08-04 to Sun 2026-08-09)

| Item | From | Why it is machine-independent |
|---|---|---|
| **A1. Grant service** | WP2.1 (service half) | Node/Fastify on the VPS, HMAC signing, replay/nonce/caps, LootLocker server API. Testable end to end against LootLocker with no game client. Port the plausibility rules straight out of `LootLockerServerGranter.cpp`. |
| **A2. `export_blueprints.py`** | WP0.3 (tooling half) | The script is authored blind and runs on Monday hour one. Getting it wrong costs a Monday morning; getting it written now costs nothing. |
| **A3. Backend replacement spec** | WP1.2 + WP1.3 design | **Done**, see [backend_replacement_spec.md](backend_replacement_spec.md). Full API surface mapped, three design findings, including the ULID ↔ SteamID64 mapping that the Fable plan missed. |
| **A4. `Online/` interface headers** | WP1.1 (design half) | Pure interface declarations. Fable flagged the interface design review as "the important one here" because it is the surface EOS lands on later. Reviewing a design before it has an implementation is the correct order anyway. |
| **A5. Repo scaffolding, not the import** | WP0.1 (partial) | `.gitignore`/`.gitattributes` for UE, LFS decision and quota check, and the `SECRETS.md` locations inventory (three cleartext keys already identified). The actual import waits on whether The Gang gives us p4 or another zip. |
| **A6. Machine provisioning list** | new | What Monday needs installed before work starts: UE 5.3 (source or launcher), VS 2022 + the right toolchain, Git + LFS, Python for the editor scripting, Steamworks SDK, disk for a 5.2 GB Content tree plus DDC. Written now so Monday is not spent downloading. |

**What Lane A must not do: write UE C++ implementation against engine APIs.** Interface headers are
safe because they compile against nothing. Implementation written blind against `IOnlineSubsystem`,
`SteamSockets` or GAS would be plausible-looking code that has never seen a compiler, and I would be
handing Robert a pile of guesses wearing a suit. A4 stops at the interface boundary deliberately.

### Lane B: Monday onward, in strict order

1. **B1 = WP0.2 first build.** Nothing else in Lane B can start. Widest band in the plan (16 to 32 h)
   because nobody outside The Gang has ever built this. Expect a scavenger hunt: the dead
   `MajorLeagueCurveball` build target, plugin recompiles, engine-version friction.
2. **B2 = WP0.3 Blueprint export**, using A2's script. **This is the checkpoint the whole estimate
   hangs on.** 5,469 binary assets become readable text, get committed and indexed, and WP1.2/1.3/2.1
   get re-estimated before any Phase 1 work starts.
3. **B3 = WP0.4 LAN listen-server smoke test.** Proves gameplay survives a listen server before a
   single line of Steam code exists. Cheapest possible early answer to the biggest architectural
   assumption.
4. Then Fable's Phase 1 in its stated order, with A1 and A4 already banked.

### Lane C: QA batching

Fable's plan has Robert QA-ing at WP1.2, WP1.3, WP1.4, WP2.2, WP3.4 and the RC review. That is six
touchpoints, several of them small. Proposal: **four QA sessions**, each with a written test script
sent in advance:

1. **QA1, after B3**: does the game play at all on a listen server. LAN, two machines.
2. **QA2, after WP1.2**: quick match over Steam, real networks, two accounts.
3. **QA3, after WP1.3 + WP2.2**: party, invites, loadouts, grants. The fat one.
4. **QA4 = WP3.4**: the structured EA readiness cycles.

Everything else is agent-side review gates against acceptance criteria, which do not need Robert.

## 3. Revised shape

The hours in Fable's section 11 are unchanged as a description of the work. What changes is the
calendar, because Lane A runs in parallel with nothing and Lane B starts six days from now.

| Week of | Lane A | Lane B | Robert |
|---|---|---|---|
| Aug 4 (now) | A1 to A6 | blocked | approve A4 interface design |
| Aug 10 | spillover, grant-service hardening | B1 first build, B2 export | **checkpoint sign-off on re-estimate** |
| Aug 17 | grant service integration prep | B3 smoke test, WP1.1 | QA1 |
| Aug 24+ | | WP1.2, WP1.3 | QA2 |

I am deliberately not putting a completion date on this. The honest position is Fable's: medium
confidence on shape, low-to-medium on Phase 1 and 2 hours **until B2**. Anyone who gives Magnus a
date before the Blueprint export has read 5 GB of assets they have not read.

## 4. Risks this model adds

1. **Untested code accumulating.** Every day Lane A runs, unverified work piles up against a compiler
   nobody has run. Mitigation: the A4 boundary above, plus B1 comes before any implementation work.
2. **The Monday machine slipping.** Everything in Lane B, which is everything that matters, sits
   behind one date. Mitigation: A6 exists so Monday is setup-free, and if the machine slips more than
   a few days the fallback is a rented Windows GPU instance for B1 and B2 only. Not elegant, but B2
   is what unlocks honest estimates and it should not wait on hardware logistics.
3. **The Gang not answering on source.** B1 against Olle's workspace zip is possible but means
   building something we know is incomplete. Asked 2026-08-04; Olle is the one with access and his
   availability has been thin all along. Mitigation: start B1 on the zip anyway, treat the missing
   build target as a known defect rather than a blocker.
4. **QA batching hiding a defect longer.** Fewer, later QA sessions mean a bad architectural call
   surfaces later than it would with continuous human review. Mitigation: QA1 is deliberately early
   and deliberately crude, precisely to de-risk the listen-server assumption before anything is built
   on top of it.

## 5. Decisions taken

**D1. Engine stays on UE 5.3 through EA. Parked until the machine is up (2026-08-04).**

Raised by Robert: if console is a long-term target, console SDKs will need a newer engine, so is the
5.3 → 5.x upgrade worth doing now? Answer: no, and the reason is specific to this project rather
than general caution.

1. **The P2P work deletes the three heaviest upgrade blockers.** All eleven plugins are marketplace
   builds pinned to 5.3, which normally argues for upgrading early. But `awsSDK` (the entire AWS C++
   SDK, by far the largest third-party dependency), `GameLiftRegionLatency` and `TGEAC` are removed
   or compiled out by the plan. Upgrading first means porting plugins we are about to throw away.
   Of the six survivors, LootLocker, Tolgee and GameAnalytics have live vendors shipping UE updates,
   `ShaderCompilationScreen` is cosmetic and droppable, `GenericSettings` is The Gang's own with
   source in-tree. **`CPathfinding` is the only real risk** (smaller vendor, load-bearing for bots).
2. **You cannot upgrade before a working 5.3 build exists (B1).** Without a baseline there is no way
   to attribute a failure to the upgrade rather than the project, and nobody outside The Gang has
   ever built this. Upgrading before B2 also means doing it blind against 5,469 unread assets.
3. 5.3 shipped autumn 2023 against a current 5.8. Five versions across three years is its own project
   with its own tail, landing inside a two-month window Magnus has already been told about.

Upgrade window: **after EA ship, before console work**, when the code is built, tested and played,
the plugin set is smaller and the Blueprints are readable.

Kept cheap in the meantime: install the newer engine alongside 5.3 on the build machine (disk is
free, ~1 h compile), run the plugin-compatibility audit in Lane A, avoid 5.3-specific assumptions in
the `Online/` interfaces, and pick the target version now even though the move happens later.

**D2. The Unity console wrapper does not apply here.**

`apds-console-wrapper` was assumed to be the console porting path. It is a **Unity** project (566
`.cs`, `Assets/`, `ProjectSettings/`, `com.unity.gamecore`, `com.unity.inputsystem.gxdk`) with zero
Unreal markers. It cannot be used on a UE5 project.

This costs nothing, because UE does not work that way: console support is first-party via Epic's
platform extensions, available to AP as a licensed developer. There is no wrapper to write. What
carries over from APDS console work is process knowledge (cert, TRC/XR/lotcheck, save and
achievement semantics), not code.

**Open, deliberately unanswered:** the minimum engine version each platform requires for cert this
year sits behind Sony/Microsoft/Nintendo developer portals where AP has licensee access. Not guessed
here. Ask when console becomes concrete; the answer can move the target version.

## 6. What I need from Robert

1. **Sign off on the `Online/` interface design (A4)** when it lands this week. It is the surface EOS
   drops into in step 2, and it is far cheaper to argue about now than after two implementations sit
   on it.
2. **The QA batching call**: four sessions as above, or keep Fable's six touchpoints.
3. Confirmation that the machine lands Monday, and roughly what it is, so A6 targets the right spec.
