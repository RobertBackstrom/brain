---
name: BlockEm
description: Lite publishing support for Block'Em! (old Aurora Punks IP). Live on Steam since Sept 2022, fresh Wavedash launch March 2026. Death Board prefix: bem
type: project
originSessionId: 3d8a4a7d-5454-40e9-bcd2-2919669a60de
modified: 2026-08-05T22:08:44.878Z
---
Block'Em! — old Aurora Punks IP. Action-filled block-building party platformer for 2-4 players. Lite publishing support — same model as Sir Whoopass and Tears of Adria.

**Title formatting:** Official is `Block'Em!` (apostrophe + exclamation). The DB prefix `bem` and folder name `block_em` keep the path-safe form, but customer-facing copy must use `Block'Em!`.

**Platforms:**
- **Steam** (Win): https://store.steampowered.com/app/1529220/BlockEm/ — app id 1529220, released Sept 8, 2022. Publisher Aurora Punks + IndieArk. Developer Cat Shawl Games. **"Very Positive" - 108 positive of 122 reviews = 89%** (re-verified 2026-08-26). 13 languages. $6.99.
  Pull review stats from `appreviews?json=1&language=all&purchase_type=all&num_per_page=0` and quote `review_score_desc` directly. The store page and the default API call return a locale-filtered subset, which is where the earlier "85% / 40" came from.
- **Wavedash** (browser, instant-play): https://wavedash.com/games/block-em (store) / https://wavedash.com/play/block-em (play). Released March 2026.

The Wavedash launch is the fresh angle — instant-play in the browser drops the friction-to-first-match for a party game. Steam footprint provides credibility (3.5+ years live).

**One-pager:** https://pitch.runatyr.games/blockem (built bem-001, May 2026). Partner-agnostic, reusable for outreach.

## Port workstream, opened 2026-08-05

Target platforms: **PlayStation, Xbox, Switch, Poki, CrazyGames**. Robert's direction: **web first**,
and **bots before anything else**, at Poki/CrazyGames quality.

**Tech, verified from source** (`code-corpus/repos/block-em`):
- **Unity 6000.0.58f1** (upgraded on branch `unity-upgrade`, 2025-08-04). Current, unlike Curveball's
  UE 5.3. Networking is **Mirage** (`com.miragenet`) over **UDP**, plus NetworkPositionSync and EOS.
- **33 branches.** Console work is real (`console`, `ps5-eos`, `ActivitiesFix` with PS5 activities +
  Switch qualified-account, `ER_Switch_Experiments`) but **all 2022-2023, so it predates the Unity 6
  upgrade**. The three AI branches (`Hampus-AI`, `AI-Experiments`, `AI_fixes`) are 2022 and already
  merged to main. `LocalOnlyBuild` (2025-07-08, "Arcade Version of Game") is the likely web base.
- **Bots already exist and are fully wired**: `AiController.cs` (683 lines, personality system),
  `AIWorld.cs`, and integration through `PlayersManager` including human-replaces-bot. The gap is
  that they are **opt-in**, and that `PlayerController` hardcodes `AILevel.Easy` twice so every bot
  plays identically. Spec: `block_em/drafts/bot_autofill_spec.md`.
- **Console wrapper:** see [[reference_source_control_map]]. The GitHub one is Peter Vestman's 2022
  work on Unity 2019.4; Petter Mikaelsson's later one is on AP's self-hosted Git, recoverable
  2026-08-10.

**Wavedash did more than port it.** Kyler, 2026-06-18: they shipped an instant-play build with
**one-player versus AI**, instant load on cached assets, a multiplayer paywall modal, and **working
browser online lobbies** (i.e. they solved browser networking, which Mirage-over-UDP cannot do). The
porting agreement (2026-01-15, signed 2026-03-04) says **AP owns the game, IP and core codebase**,
Wavedash gets a license to host on Wavedash, **90/10 revenue split in AP's favour** minus $0.50 per
transaction, and crucially **game-specific improvements they make are usable by AP on other
platforms**. Robert asked Kyler for the web build code 2026-08-05. **Do not rebuild the web port
before that answer lands.**

**Platform requirements:** Poki wants **under 8 MB initial download** (the hard one for Unity), forced
mobile controls on tablets, static + animated thumbnails, in-game privacy policy. CrazyGames allows a
**Basic Launch with no SDK** (no monetisation) before a Full Launch with SDK, QA in 1-2 days, so it is
the cheaper first real test.

**Why:** Own IP, exploring Wavedash as a platform.
**How to apply:** Death Board prefix `bem`. Project folder at `umbrella/block_em/`. 20 Wavedash redeem keys tracked in `umbrella/block_em/wavedash_keys.md`.

**Mandate:** rights reverted from Curve Games back to AP (Robert, 2026-08-24); the Steam page still shows the old publisher credit. See [[reference_ap_publishing_rights]] before acting on this title outward.
