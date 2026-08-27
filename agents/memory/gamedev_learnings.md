---
name: GameDev Agent Learnings
description: Cross-project knowledge accumulated by the GameDev agent from engine integrations and dev workflow support
type: agent_memory
agent: gamedev
---

# GameDev Agent Learnings

## Engine MCPs

_No learnings yet. Will accumulate as we test engine MCPs against client projects._

## 2026-04-17 — Steamworks Partner MCP [, ToA]  [Build Pipelines]

Built first-ever Steamworks Partner MCP server. Key learnings:

**Architecture:**
- MCP SDK stdio transport works perfectly for game platform APIs
- Separate API client layer (axios wrapper) from MCP tool definitions keeps code clean
- TypeScript types for API responses essential for maintainability
- Environment variables for API keys (never commit credentials)

**API Structure:**
- Partner API uses `partner.steam-api.com` (NOT `api.steampowered.com`)
- Two key types: Publisher Key (general access) + Financial API Key (revenue data)
- Financial API Key requires separate approval, 1-2 business day turnaround
- Some useful endpoints are in public Store API (reviews, app details) — mix both in one server

**Tools Implemented (Phase 1):**
1. `get_partner_apps` — List publisher's apps
2. `get_sales_data` — Revenue/units sold (requires Financial key)
3. `get_wishlist_data` — Wishlist analytics with country/language breakdown
4. `get_news` — Read news/announcements
5. `get_app_details` — Store page data (public API)
6. `get_reviews` — Review monitoring (public API)
7. `get_app_builds` — Build history
8. `get_app_betas` — Beta branch listing

**What CAN'T be automated:**
- Store page text updates
- Capsule art / screenshot uploads
- Creating news posts (read-only via API)
- Pricing / discount management
- Event creation

**Phase 2 Complete [2026-05-02, ToA]:**

Built build management layer on top of Phase 1 analytics:

**Tools Added:**
1. `set_app_build_live` — API call to switch which build is live on a branch (WRITE op)
2. `generate_build_script` — Creates VDF files for SteamCMD uploads
3. `check_steamcmd` — Verifies SteamCMD installation

**SteamCMD Module:**
- Separate `steamcmd.ts` module for build automation
- VDF template generation with proper escaping
- Handles multi-depot builds, branch selection, local content paths
- Steam Guard authentication considerations documented
- Child process execution with proper error handling (10MB buffer for output)
- Path validation before upload (content root must exist)

**CI/CD Integration:**
- GitHub Actions workflow: tag-triggered deploy, multi-step (build → upload → verify)
- GitLab CI pipeline: staged approach (build → deploy → verify)
- Security patterns: masked secrets, Steam Guard pre-authorization for self-hosted runners
- Rollback strategy: use `set_app_build_live` to revert to last known good build on failure

**Key Learnings:**
- WRITE operations need very clear warnings in tool descriptions — added "use with caution" language
- VDF format is simple but strict: quoted keys/values, nested braces, specific field names
- SteamCMD first-time login is interactive (Steam Guard), so CI/CD needs pre-auth or manual step
- Separate "generate script" from "execute upload" for safety — user can review VDF before running
- Build verification via API after upload is essential for CI/CD confidence

**Next phases:**
- Phase 3: Review sentiment analysis, wishlist trend tracking, sales spike detection, Death Board integration

**File structure:**
```
mcp-servers/steamworks-partner/
├── src/
│   ├── index.ts         # MCP server + tool definitions
│   ├── api-client.ts    # Axios wrapper for Steam APIs
│   └── types.ts         # TypeScript response types
├── dist/                # Compiled output
├── README.md
├── TESTING.md
└── .env.example
```

**Build quirk:** npm install wasn't installing devDependencies by default in this environment — needed `npm install --include=dev` to get typescript + @types/node. Use `npx --yes --package=typescript tsc` in build script to ensure it always works.

## 2026-05-04 — PS5 Regression Pattern [, ToA]  [Console Platform Porting]

When investigating PS5-specific bugs on a game that's already shipping on Steam:

**What to check first:**
1. Cross-reference existing bug tracker with platform filters — look for "fixed on Steam" but missing from PS5 section
2. Cluster the reported bugs — if they concentrate in specific progression areas/systems, suggests platform-specific constraint (memory, performance, timing)
3. Identify likely root causes by system:
   - **Animation/Camera freeze**: PS5 render timing difference or animation state corruption under load
   - **Input unresponsiveness**: Controller input latency or button polling timing on PS5
   - **Invisible walkables/collision**: Collision layer visibility or rendering order issue on PS5's graphics pipeline
   - **Widespread freezing**: Memory pressure or GPU vram constraints specific to PS5 hardware

**Red flags for platform-specific bugs:**
- Bug tracker heavily skewed to one platform (Steam 40+ bugs, PS5 only 5)
- Bugs in same progression sequence but not documented
- Multi-system freezing (boss freeze + camera freeze + climb unresponsive) suggests shared timing or state issue

**How to brief dev team:**
- Request platform-specific profiling (frame rate, memory, CPU load during freeze sequences)
- Ask for input lag analysis (PS5 controllers vs Steam)
- Check animation timing under platform constraints (not just animation correctness)
- Isolate individual systems (camera → boss → climb) before integrating fixes

**Why this matters:** Porting teams often use the original platform's bug tracker. New platforms need separate profiling or a merged tracker with platform awareness, or you miss the porting-specific regressions that made it through QA.

## 2026-06-08 — Xbox Partner Center: reparenting freeze vs. user-grant [, SWA]  [Console Platform Account / Backend Access]

When a game's Xbox publishing rights transfer between companies (e.g. publisher change after a bankruptcy), there are TWO separate things and they're easy to conflate:

1. **Reparenting** = moving the *product* into the new publisher's own Partner Center account. Microsoft engineering has **frozen reparenting for MSA V2 products** (any game created in Partner Center after **March 2022**) due to a technical limitation that can break players. **No ETA.** Pre-Mar-2022 games are MSA V1 and can still be reparented. This is the hard blocker.
2. **Granting users** = inviting the new team's emails as users into the *old* publisher's Partner Center directory. This is **NOT** blocked by the V2 freeze. If the old publisher can still log in, this is the fastest interim unblock - the new team gets management access (promos, sales data, updates) immediately, no engineering dependency.

**The trap:** Microsoft's reps (ID@Xbox / Hanson Consulting) tend to push the heavy path first - "MSA Transfer" / owner-account change to an Outlook account - when often the old publisher simply never added the new team as users after the contractual transfer. Always check whether a plain user-invite solves it before agreeing to an owner change.

**Royalty vs. access decouple:** The contractual/TLA transfer (royalties flowing to the new party) completes independently and long before Partner Center access is sorted. A team can be getting paid for months while still locked out of managing the game.

**Process catch (voice/mail):** Before reporting "you already replied" on any thread, verify against `in:sent` - gmail_thread returns DRAFTS inline as if they were messages. Here a reply that looked sent was an unsent draft. Reinforces [[feedback_verify_draft_sent]].

## 2026-06-10 — Xbox MSA Transfer = whole-account, not per-title [, SWA]  [Console Platform Account / Backend Access]

Microsoft's "MSA Transfer" workaround (swap the Owner MSA of a Partner Center account to a new Outlook/MSA account) transfers the **entire account and every title in it** - not a single product. ID@Xbox proposes it as the fix for the V2 reparenting freeze, but it's a **trap when the seller's account holds more than one game**: you'd hand over titles you mean to keep. Always ask "how many titles are in this Partner Center account?" before agreeing.

**Process Microsoft requires for an MSA Transfer:** (1) a **Letter of Consent** from the current owner consenting to replace the Owner MSA from `old@` to `new@`, and (2) the **PUID** of the new MSA (sign into the new MSA → account.live.com/EditProf.aspx → "Unique ID"). Engineering completes it in ~couple days after receiving both.

**If only one title should move but the account has several:** per-product reparenting is the clean answer but it's frozen for V2. The viable inverse is to reparent the *other* (non-transferring) titles out to a fresh owner MSA first - leaving the target title alone in the account - then MSA-transfer the remainder. Only works if those other titles are V1 (pre-Mar-2022); if they're also V2, engineering has to weigh in. We scoped a Letter of Consent to the single title explicitly and put the mechanism question to the MS rep rather than signing a whole-account consent.

**Account authority gotcha:** the Owner MSA can be a *personal Gmail/Outlook* belonging to a founder, not a company account - and if the publishing entity went bankrupt, there's a real signing-authority question (who can consent to transferring the estate's asset). Flag to Lawyer before a consent letter goes out.

**Doc tooling:** legal letters → `node md-to-docx.js in.md out.docx --title "..."` (bakes house legal style: EB Garamond body, Calibri headings, A4) then `node gdrive-upload.js out.docx <folderId> --convert` to land a native Google Doc. Robert exports to PDF from there. SWA Drive layout: `sir_whoopass/{steam,xbox,playstation,nintendo}` - platform-specific docs go in the matching subfolder.

## 2026-06-10 — Self-signed PDF via OpenSign (one-party Letter of Consent) [, SWA]  [Console Platform Account / Backend Access]

Chain to produce a signed PDF Robert can download:
1. `md` → `node md-to-docx.js in.md out.docx` (house legal style) → `node gdrive-upload.js out.docx <folderId> --convert` (native GDoc). Iterate in place with `node gdrive-update-doc.js <md> <fileId>` so the link stays stable.
2. Export the GDoc to PDF: Drive `files.export?mimeType=application/pdf`, token via `require('./gdoc-replace').getAccessToken`.
3. `const os = require('./opensign'); os.createSignatureRequest({ pdfPath, signers:[{name,email,order:0}], placement:'manual', signerWidgets:[[widget]], sendEmail:false })`.

Place the widget with `os.extractTextAnchors({pdfPath})`: take the last page, find the signer's name line (lowest item matching the name by `yTop`), and set the signature widget ~50pt **above** it (`yPosition = nameYTop - 50`, Width ~175, Height ~44, top-origin pts). `sendEmail:false` returns the `signLink` WITHOUT dispatching email — hand the link to Robert directly; OpenSign emails him the completed PDF once signed (verify via `in:sent` "signed by all parties"). The whole flow stays on our self-hosted `sign.runatyr.games`.

**Gotcha:** the GDoc PDF export came out **US-Letter (612×792)**, not A4, despite md-to-docx's A4 target — page size follows the Google Doc's own default, so anchor by extracted coordinates, never hardcode A4 height.

## 2026-06-10 — Xbox Partner Center: Manager-role login + MFA recovery [, SWA]  [Console Platform Account / Backend Access]

To **add users / assign developer-program roles** you must be signed in as a user holding the **Manager(Windows)** role — NOT merely Azure AD **Global admin**. A Developer-only / Global-admin-only login can assign nothing but directory Global admin; every developer-program role checkbox is greyed out. Check **User management** for which account has Manager(Windows) and sign in as that one (here: `finance@aurorapunks.com`, while `robert@` was Developer-only).

**MFA recovery when the Manager account is locked:** SMS can be blocked by Microsoft's **phone-reputation** system (**error 399287**) on a perfectly valid number — unfixable device-side, and retries deepen the block. **TAP (Temporary Access Pass)** is the recovery bridge but is often disabled by tenant policy. Enable it first: Entra admin → **Skydd → Autentiseringsmetoder → Tillfällig åtkomstkod → Aktivera** (target the user/all). Then issue a TAP for the user (user blade → Autentiseringsmetoder → Lägg till → Tillfällig åtkomstkod), sign in with it, and register **Microsoft Authenticator** at aka.ms/mfasetup. The admin "Add authentication method" panel can only add Email/Phone/TAP/QR — it can't register Authenticator for the user, which is exactly why TAP is the bridge.

## Client Engine Stack

- BADASS Studios: Unreal Engine 5 (BadassXR platform) [BADASS, 2026-03]
- Tears of Adria: Unity (multiplatform, Steam + PlayStation) [ToA, 2026-05]
- Hooja (Aurora Punks): Unity 2021.3.45f2 (Built-in RP, IL2CPP), ironSource LevelPlay ads, PlayFab backend, custom AP UPM packages [Hooja, 2026-07]

## 2026-07-13 — The three (soon four) hard gates that force a Unity upgrade [, Hooja / hoj]  [Mobile Store Compliance Gates]

Any live Unity mobile game that needs a NEW store update in 2026 hits these, dated and non-negotiable:
1. **Google Play target API 35** required for updates since **31 Aug 2025**.
2. **Google Play 16 KB memory-page support** required for target-35 updates since **Nov 2025**. **Unity 2021.3 CANNOT produce a 16 KB-aligned build** - this alone forces off 2021.3. Backported only to late 2022.3 patches (verify exact patch) and Unity 6 (6000.0.23f1+).
3. **App Store: builds must use iOS 18 SDK / Xcode 16** since Apr 2025; 2021.3 not qualified.
4. **Target API 36** expected **~31 Aug 2026** - only Unity 6 is on track.

Consequence for version choice: 2022.3 LTS is a *stepping stone, not a destination* - it's at/past end-of-support and API 36 will force the exercise again within a cycle. Recommend **Unity 6 via a 2022.3 hop** (2022.3 migrates serialized assets/Addressables in a smaller step, then reopen in Unity 6). The mandatory ad-SDK/Gradle/EDM4U work is identical on both targets, so it doesn't bias the choice.

**Unity upgrade risk hot-spots (static, pre-spike):** custom git-branch UPM packages pinned to `#branch` not `#tag` (pin can move; check each `package.json` `unity` field + editor guards - can't assess without fetching); Addressables 1.x->2.x on Unity 6 = binary catalog migration + full content rebuild; committed 2021-era Gradle templates carry placeholders (`**MINIFY_WITH_R_EIGHT**`) removed in 2022+, so delete+regenerate or template processing fails; TMP merges into uGUI 2.0 on Unity 6 (delete the TMP manifest entry; puts text-animation assets like Febucci 1.x at risk); EDM4U must be >= ~1.2.180 before Unity 6. Own-code deprecation is usually minor (`FindObjectOfType` warnings). An editor spike needs Unity Hub + licenses on a dev machine - can't run headless on the VPS; prep the checklist and hand it off.

## 2026-07-13 — Auditing a stale LevelPlay integration [, Hooja / hoj]  [ironSource / LevelPlay Ad Mediation]

Hooja was on ironSource Unity plugin 7.3.0.1 (2023); LevelPlay is 8.x. Migration is small in surface (1 manager wrapper + facade + few call sites) but mandatory for store compliance (API 35 / 16 KB). Recurring things to check on any LevelPlay audit:
1. **Legacy vs unified API:** old `IronSource.Agent.init` + `IronSourceEvents.*` (often wrapped in `#pragma warning disable CS0618`) vs new `LevelPlay` init + `LevelPlayRewardedAd`. The 8.x API also delivers `IronSourceAdInfo` (eCPM/network) per impression - wire `onImpressionDataReady` -> backend telemetry for LTV/ROAS, usually missing.
2. **OFFERWALL is discontinued** - if it's in the init unit list it breaks on 8.x; remove.
3. **Dead Unity Mediation SDK** (`com.unity3d.mediation:*`) deps often linger post-2024-shutdown; their jfrog/cocoapods sources can 404 at resolve time and break builds - remove.
4. **Android GDPR/CMP is often entirely absent** even when iOS ATT is handled - check for a real consent flow (Google UMP / TCF), not just an age gate. Without TCF, AdMob serves limited ads in EEA = real revenue loss.
5. **iOS SKAdNetwork plist** frequently contains only ironSource's own ID; mediated networks' SKAN IDs missing -> mediated iOS underreports/underbids.
6. **Reward-event plumbing smell:** a single global untyped reward event + manual subscribe/unsubscribe + a re-entrancy lock reset on reward-but-not-on-close = latent double-reward and button-soft-lock bugs. Empty placement strings kill per-placement capping/reporting.
7. **Add bidding-first networks** for a casual runner (impact order): AppLovin (near-mandatory 2nd source), Mintegral, Liftoff/Vungle, then DT Exchange/InMobi. Old adapters without bidding config (e.g. Meta AN 6.12) likely earn ~nothing.
8. Rewarded-only games leave interstitial (between-runs, freq-capped) + banner (idle menu) on the table - the init often already spins up those units unused.

## 2026-07-13 — Greenfield IAP on a PlayFab-backed Unity game [, Hooja / hoj]  [Mobile IAP Design]

- **SDK:** Unity IAP `com.unity.purchasing` 4.13+ for Unity 2021.3+ (bundles Google Play Billing 7, required since Aug 2025; IAP 5.x is Unity-6-only). One `IStoreListener` for both stores; receipts arrive in exactly the shape PlayFab validators want. Pulls Unity Gaming Services core - needs a linked UGS project ID.
- **Validation without a custom server:** Unity IAP `ProcessPurchase` -> set Pending -> PlayFab `ValidateGooglePlayPurchase` (ReceiptJson+Signature) / `ValidateIOSReceipt` (base64) -> grant + telemetry -> `ConfirmPendingPurchase`; leave pending + retry on network failure. PlayFab de-dupes receipts per title (kills replay/sharing). Prereq: Google Play licensing RSA key + iOS bundle in PlayFab Game Manager.
- **Validation protects the purchase, not the balance** - a local (non-server-authoritative) save is trivially editable regardless. Acceptable for small-title v1; mitigate with a PlayFab catalog for auditable grants. Full server-authoritative VC is a separate, bigger refactor.
- **"Remove Ads" is the wrong product when all ads are rewarded opt-ins** - it would sell nothing and *punish* the buyer (lost revives/double-coins/boosts). Reframe as a "VIP" that auto-grants the reward *without* the video (a pre-existing `SKIP_ADS`/editor-skip code path usually proves this is trivial). Also look for cheat-menu-only boolean flags already wired into economy logic (e.g. double-coins/double-score) - those are near-free IAP non-consumables.
- **Longest-lead item is store-side, not code:** App Store Paid Applications Agreement + banking/tax blocks everything - do first. Confirm the merchant *entity* early.

## 2026-07-13 — Committed Android keystore [, Hooja / hoj]  [Secret Hygiene]

Hooja repo commits `user.keystore` at root (the signing keystore) though the password is loaded from an untracked file (so pw not in git). A keystore in git history is still a hygiene issue worth rotating. Standing pattern: when auditing any mobile game repo, grep for committed keystores/`.p12`/`.mobileprovision`/`google-services.json` with embedded secrets and flag per security defaults - even inside a private repo.

## 2026-07-06 — Steamworks partner data: use Playwright, not a bespoke Partner-API MCP [, ToA / toa-012]  [Tooling]

We built Phase 1+2 of a custom Steamworks Partner MCP server (analytics, build management, review fetching wrapping `IPartnerFinancialsService`, wishlist API, `GetAppBuilds`/`SetAppBuildLive`, etc.), but Robert **closed it in favour of Playwright browser automation**. Go-forward pattern for Steamworks partner data (sales/wishlists/reviews) is Playwright-driven, matching the house automation stack (Fortnox `fortnox-login.js`, RankOne R1 at r1-agent.fly.dev). Rationale: avoids publisher-key management + partner-API gaps, and keeps one consistent automation pattern across the VPS. The MCP code is retained as reference only — don't invest further in it. When a future task needs Steamworks partner numbers, reach for a Playwright script, not the MCP.

## 2026-07-13 — Verify a delisting's real cause before attributing it [, Hooja / hoj]  [Tooling]

When a previously-live game is found delisted, do NOT infer the cause from surrounding context (e.g. a related entity's bankruptcy). Confirm the actual mechanism from the store console + mail history BEFORE advising or scoping a fix. Real causes seen on Hooja:
- **Google Play "Removed"** under Device & Network Abuse policy for the **2025 Unity Android runtime CVE (CVE-2025-59489)** ("Unity 2017.1+ for Android") - fix = rebuild on patched Unity + resubmit.
- **App Store removal from an EXPIRED Apple Developer Program membership** (Apple removes all your apps when the annual membership lapses) - fix = renew (999 kr/yr).
- Also common: target-API-below-required unpublish (Google), and EU-DSA trader-status removal (Apple, Feb 2025).

Also: the store **developer account is often a different entity than you assume**. Hooja's Google Play account = solvent **Aurora Punks AB** (owner emelie@, hektor@ has access), NOT the bankrupt APDS; the Apple Developer login = a **qa@aurorapunks.com Google Group** (Account Holder = the founder), with 2FA to a device not the group. Payout banking underneath can still point at old/bankrupt entities (Hooja: Steam + PSN payouts routed to bankrupt APDS; Payoneer under WLBS) - audit the payments profile separately from the listing.

**Why:** I twice asserted "APDS bankruptcy delisted Hooja" and had to retract both times; mail evidence showed a solvent account + a security-CVE removal + a lapsed membership. **How to apply:** for any relisting task, first pull the delist notice (console + search BOTH mailboxes for the store's developer-support sender, e.g. no-reply-googleplay-developer@google.com / developer@insideapple.apple.com), identify the account-holder entity, the exact policy/removal reason, and the payout entity - THEN scope the fix. Cross-refs [[feedback_search_wiki_first]], SWA Xbox reparenting learnings.

## 2026-08-04 — Read a Drive-hosted zip's file list before downloading it [, Curveball / cvb]  [Tooling]

`BBA_dev.zip` sat on Drive at 5.6 GB and everyone assumed it was a build. It was a **full UE project tree**. The cheap way to know: a ZIP keeps its central directory (the complete file index) at the **end** of the archive, so two ranged GETs against the Drive `alt=media` endpoint (`Range: bytes=...`) list every entry, with sizes, without downloading anything. Parse the ZIP64 EOCD at the tail, then fetch the central directory it points at. Individual small files can be pulled the same way via their local-header offsets.

Use this before committing to any multi-GB Drive pull, and before telling Robert "Drive only has builds". Working scripts from this session: `peek-zip.js` (list) and `grab-files.js` (extract single files by regex) — both trivial to rewrite from the ZIP spec.

Gotcha: piping the output through `head` kills node with EPIPE mid-run and silently truncates the extraction. Write to a file instead.

**Unpacking rule for UE projects:** extract Source/Config/Plugins/Saved-Logs, skip Content/Intermediate/Binaries/DerivedDataCache, and write the skipped asset paths to a `_ASSET_MANIFEST.txt`. Curveball went 5.6 GB → 466 MB that way, and the manifest still lets an agent name the Blueprints and maps it cannot read.

## 2026-08-04 — UE MCPs need a live editor, so they are not a VPS play [, Curveball / cvb]  [Tooling]

Every Unreal MCP (Epic's official one included) embeds its server **inside a running UE Editor process**. The Hetzner VPS is headless, 8 GB, no GPU, so it cannot host one for a real project. Epic's first-party MCP plugin also ships with **UE 5.8 and needs a source build**; most shipping projects (Curveball is 5.3) get nothing official, and the third-party servers mostly target 5.7/5.8 too.

Better answer for *reading* a project than fjärrstyrning of someone's editor: **export Blueprint graphs to text once** (T3D or JSON, via commandlet or Python editor scripting) on a machine that can run the editor, check the dumps in, and index them. Permanent, VPS-native, survives the laptop being asleep. An MCP earns its place when you need live editor manipulation (level building, iterating in PIE), not when you need to understand or review logic.

Robert (2026-08-04): "inget självändamål att skohorna en mcp". Also flagged that the stack is moving to a local bare-metal box that *can* run the editor — see [[project_baremetal_migration]] — so this constraint is temporary, but do not build for that machine before it exists.

## 2026-08-04 — Read the code before the estimate reaches a partner [, Curveball / cvb]  [Estimation]

Curveball's pitch to Light Up Games states **under 100K SEK / ~2 months** to finish, including a switch from dedicated servers to P2P. That number was set from the deck, before anyone opened the project. First read of the source surfaced three things that plausibly move it:

1. **Gameplay is in Blueprints.** 94 `.h` + 88 `.cpp` (~1 MB) against 5,469 binary `.uasset` + 304 `.umap`. The C++ is matchmaking, backend glue and GAS helpers. You cannot estimate replication work you cannot read.
2. **Server authority runs deep.** GAS abilities, `ServerHeartbeatSubSystem`, and LootLocker's `ServerGranter` / `ServerLoadoutValidator` all assume a trusted dedicated server. Under P2P the host becomes the entity granting its own items. That is a design problem, not a config change.
3. **Anti-cheat assumes a trusted server too** (TGEAC/EAC + `MLCAC`).

Cheap counterweight found in the same pass: `OnlineSubsystemSteam` is already enabled (transport is still plain `IpNetDriver`), and `EOSIntegrationKit` plus an `EpicClient` target are already scaffolded though disabled. So the *transport* swap is genuinely small; it is the authority model that carries the cost.

**How to apply:** on any "port/convert/finish an existing game" deal, get the project on disk and read it before a number goes outward. When a number is already out, do not quietly re-plan around it — surface the delta to Robert as a producer decision and let the plan say what the work actually is.

## 2026-08-17 — Xbox V2 access: do the plain invite FIRST [, SWA]  [Console Platform Account / Backend Access]

Sequence lesson layered on the 2026-06-08 and 2026-06-10 entries. With V2 reparenting frozen, ID@Xbox offered three routes. Two of them burned 2.5 months and neither shipped:

1. **MSA Transfer** — needs a signed Letter of Consent and moves the **whole account**. Dead the moment the account holds titles that should stay. We drafted, signed and sent a single-title LOI (2026-06-10) that turned out to be unusable, because MS had no single-title mechanism to apply it to.
2. **New `.onmicrosoft.com` tenant** — the MS rep's own alternative, 10 steps. Stalls at step 6-7 on **Microsoft billing/identity verification of the new billing account**, which never cleared (18 Jun to 17 Aug: no approval, no ETA, no escalation path, and the rep did not know the verification step even existed). Treat tenant creation as **blocked-by-default when the billing entity is new or freshly restructured** (here: CZP Holding AB, post-konkurs asset buyer).
3. **Direct directory invite** — sign in to Partner Center as a **Manager on the existing account**, User Management, Invite user, external address, then **custom permissions scoped to a single product group**. No engineering dependency, no legal doc, minutes not months. Product-level scoping is supported and was confirmed by ID@Xbox.

**How to apply:** when a publisher change needs backend access and reparenting is frozen, test route 3 on day one. Escalate to tenant or owner-MSA work only if the Invite user option is genuinely missing for the Manager account. Never sign a Letter of Consent before a lighter route has demonstrably failed. Canonical project state lives in [[project_sir_whoopass]]; ticket swa-002.

**Second-order:** the MS rep proposes the heavy path from habit and only offers the light one when pushed. Ask "is there a way to do this with the access I already have?" before accepting a process that needs new accounts, new entities or signatures.

### 2026-08-25 — Nintendo SDEV: hitta det via OUI, styr det via HTTP, och Target Manager behövs inte för att testa [project: apb / K2C]
Robert kopplade in ett Switch-devkit på subnätet. Hela kedjan från "det finns någonstans på nätet" till "jag läser dess skärm" tog fyra kommandon.
**Hitta kitet:** ARP-cachen räcker inte, den visar bara nyligen kontaktade värdar. Ping-svep hela /24, slå sedan upp MAC-prefixen mot `/usr/share/ieee-data/oui.txt`. **`70:48:F7` = Nintendo Co.,Ltd.** Ett OUI-uppslag pekar ut kitet entydigt bland åtta värdar, ingen portgissning behövs. Detta är den snabbaste identifieringen av vilken konsolhårdvara som helst på ett okänt LAN.
**SDEV:ens webmeny på port 80 är ett fullständigt styrplan** och kräver ingen autentisering på LAN:
- `/cgi-bin/info` — namn, **serienummer**, modell, MAC, HostBridge-firmware
- `/cgi-bin/sion` — target power, batteri, USB, boot mode, DIP-switchar, reset- och knappstyrning
- `/cgi-bin/config` — DHCP, IP, MTU, jumbo frames, **TCP-porten för Data Transfer**
- `/cgi-bin/lcd/landscape.png` — **skärmdump 1280x720 av vad targeten visar just nu**
LCD-capture är det mest underskattade: det ger visuell verifiering av devkitets tillstånd från ett headless Linux-skal, alltså QA-observation utan Windows och utan att stå vid hårdvaran.
**Portbilden:** 23 telnet, 80 webmeny, **8000 Data Transfer** (den Target Manager använder, och den syns i `/cgi-bin/config`, inte i en standardportskanning, så läs configen i stället för att gissa).
**Det som ändrar arbetsflödet:** DevMenu erbjuder **"Install via HTTP"** vid sidan av SD-kort och game card. En nsp kan alltså pushas utan Target Manager, alltså utan Windows i loopen. För att *testa* byggen behövs ingen NDI-maskin. Windows plus NDI behövs först för att **skapa** byggen och köra cert. Anta inte att Target Manager är obligatorisk bara för att installationsdokumentationen utgår från den.
**Hygienfynd värt att kolla varje gång:** kitet hade en annan utgivares opublicerade titel installerad (Amberbite GmbH:s "Shoe it All") från tidigare QA-arbete. Läs alltid DevMenu-listan innan ett lånat eller övertaget kit tas i bruk, både för NDA-hygien och för att veta vad som ska rensas.
**Tags:** Nintendo, SDEV, devkit, OUI, nätverksupptäckt, Target Manager, DevMenu, install-via-HTTP, LCD-capture, NDA-hygien

### 2026-08-26 — Devkit build-drop: bygget når kitet via HTTP från Linux, Target Manager kräver Windows+SDK [project: apb / K2C]
Följdläge på 2026-08-25-fyndet. Oskar la ett K2C Switch-bygge på Drive (en zip med exakt en `.nsp`, 2,26 GB). Kedjan Drive→kit på Nitro, utan Windows:
- **Hämta från Drive headless:** gdrive-MCP:ns OAuth-creds ligger i `/home/assistant/.claude/.gdrive-server-credentials.json` (refresh_token + CLIENT_ID/SECRET från `~/.claude.json` mcpServers.gdrive.env). Refresha access_token mot `oauth2.googleapis.com/token`, ladda sedan `files/<id>?alt=media&supportsAllDrives=true`. `md5Checksum`-fältet i metadata matchade nedladdningen, verifiera alltid.
- **Build-drop-tjänst:** `assistant/build-drop-server.js` + user-unit `build-drop.service`. Zero-dep Node, serverar `/home/assistant/builds` **bara på LAN-interfacet** (resolvar Nitros DHCP-adress på `enp2s0`, inte tailnet/docker), stödjer **Range** (DevMenu drar multi-GB, en server utan Range stallar), path-traversal-skyddad via realpath-inom-root, GET/HEAD only. Kitet drar nsp:n direkt: `http://192.168.32.9:8088/k2c.nsp`.
- **Headless Target Manager går INTE från Nitro.** Port 8000 är Target Managers proprietära binärprotokoll, odokumenterat för oss. Enda headless-motsvarigheten är SDK:ns `ControlTarget`/`RunOnTarget`, som kräver NintendoSDK (Windows-binärer, NDA) — finns inte på Nitro, ingen wine. Telnet:23 är **HostBridge-kortets** PetaLinux (`Built with PetaLinux v2014.4 (Yocto 1.7)`), inte NX-targeten, och ger ingen nsp-push. Slutsats: *installera* headless kräver Windows+SDK; *testa* ett bygge gör man via DevMenu **Install via HTTP** (människa vid kitet med debugkontroll skriver URL), eller Install from SD.
- **FTP:21 är öppet, anonymt och skrivbart** till kitets rot (`220/230 Operation successful` utan pass, STOR/DELE funkar). Odokumenterat i gårdagens inventering. Kitets egen filtjänst, men ett oautentiserat write på LAN värt att känna till. Rotlistning tom, undermappar 550.
**Tags:** Nintendo, SDEV, build-drop, Install-via-HTTP, Target Manager, gdrive-OAuth-headless, Range-requests, systemd-user, FTP-anon

### 2026-08-27 — EDEV skiljer sig radikalt från SDEV: grå dosa, svart skärm, USB inte ethernet [project: apb / K2C]
EDEV (Switch-form-factor debugkit; AP har två, "Ember" + ett namnlöst, köpta från Kinda Brave okt 2024) kopplas och strömförsörjs HELT annorlunda än det stora SDEV:t. Om någon säger "EDEV:t verkar dött / tar inte ström / power-knappen gör inget", kolla dessa tre innan hårdvaran döms ut:
- **Ström går genom en grå dosa**, inte direkt i kitet: Nintendo-adapter → grå dosan → EDEV. Adaptern rakt i EDEV:ns USB-C räcker inte. Grå dosan = "HDMI-till-USB-dockningsstationen" som följde med Ember-kitet.
- **Skärmen är SVART med flit när kitet är kopplat till datorn** (AP-doccen "Installera på Switch": *"skärmen på switchen kommer vara släckt när den är kopplad till datorn, skit störande"*). Ett tjudrat EDEV med svart skärm + till synes död power-knapp kan alltså vara fullt funktionellt. Dra ur USB-datakabeln (behåll ström), testa fristående, innan det döms ut. Djupurladdat 2024-batteri kan dessutom kräva 20-30 min laddning + 15 sek hård reset innan livstecken.
- **EDEV pratar med Target Manager över USB** (kabeln med "lustigt uttag" i nätväskan: grå dosan ↔ PC), till skillnad från SDEV som kör ethernet på subnätet. Konsekvens: NDI + Target Manager 2 måste sitta på maskinen där USB:n är inkopplad, inte på en godtycklig nätvärd.
- **Remote video** (filmkamera-ikonen i TM2, efter Connect) är enda sättet att se EDEV-skärmen när den är tjudrad.
- Setup-referens: Drive-doc "Installera på Switch" (gdrive `1r_nnIpdeyiaavcqBNKEF0yRQJN2WYITNJ7NH1k7OXYM`) + 16-stegsrutinen i "Download Nintendo Dev Interface 2" (`1s9Nye50snLBN5DcGCi1QSXXWdEjb3f65OIXgISMtLtI`).
**Tags:** Nintendo, EDEV, grå-dosa, svart-skärm-tjudrad, USB-inte-ethernet, remote-video, Target-Manager, kit-topologi, deep-discharge

### 2026-08-27 — Xbox Partner Center: släppa in en extern partner på EN titel utan att blotta resten [project: swa / apb]
Sir Whoopass-rättigheterna gick till Atomic Elbow (TLA 2026-02-01) men produkten gick inte att flytta: **per-produkt-reparenting är fryst av Microsoft för alla MSA V2-produkter** (allt skapat efter mars 2022), utan ETA. Två vägar dog på det under juni-augusti: whole-account MSA Transfer (hade dragit med kontots övriga titlar) och ett eget `.onmicrosoft.com`-tenant (fastnade på MS billing-verifiering). **Den som funkar är direktinvite plus custom permissions**, och receptet är värt att återanvända:
- Bjud in partnerns adress i ditt eget Partner Center, välj **Customize permissions**, aldrig en färdig roll. En färdig roll slår ut produktscopingen och de ser hela katalogen.
- Scopa på **produktgrupp** i Product-level permissions. Verifierat att det håller: partnerns egen "Appar och spel"-vy visade bara den ena produktgruppen, medan adminvyn visar alla titlar som urkryssade.
- **För DLC och bundles behövs exakt två extra flaggor**, och Microsofts supportsvar namnger dem: account-level **"New bundles"** och product-level **"New add-ons"**, båda Read/write. Read ensamt räcker inte, de ska kunna skapa.
- **"New bundles" går inte att scopa.** Sektionens egen text: *"Permissions in this section will apply to all products."* Det finns ingen produktnivåvariant. Kostnaden för DLC-arbete är alltså en kontobred bundle-rätt, acceptera den medvetet.
- **Ge ALDRIG "New apps" eller "Manage product groups"** i det här scenariot. De låter partnern skapa nya produkter i ditt konto, vilket är precis den läcka upplägget finns för att undvika. Add-ons behöver dem inte, de hänger under befintlig produkt.
- **Utgråade rutor på add-on-rader är normala, inte ett fel.** Ett add-on ärver Discs, Age ratings, Name reservation och Xbox Live från moderspelet, så Microsoft släcker cellerna. Felsök dem inte.
- **Du kan inte tilldela en behörighet du inte själv har.** En Manager kan inte ge bort Owner-saker. Är just den ruta du behöver utgråad, jämför mot din egen användarrad innan du felsöker något annat.

**Gränssnittsspråket är en riktig felkälla här.** Partner Center serverar UI-språk efter URL-locale och geo-IP, så samma konto kan bli svenskt, tyskt eller engelskt beroende på vilken väg trafiken tog (en session via ett tyskt hosting-ben gav `de-de`). Byggena är dessutom **halvöversatta**: en engelsk lista med enstaka tyska rader mitt i. `Neue Pakete` = New bundles, `Neue Apps` = New apps, `Neue Add-ons` = New add-ons, `Pakete` (produktnivåkolumn) = Packages, alltså spelets binärer och **inte** samma sak som bundles. Två olika "paket" i samma vy är hur man kryssar fel. Fix: sätt `en-us` i URL-segmentet (`partner.microsoft.com/en-us/dashboard`) eller via `partner.microsoft.com/en-us/localeselection`, så matchar vyn Microsofts egna supportskärmdumpar ord för ord. Språket sitter per inloggad användare, så det påverkar inte partnerns vy.

**Sidofynd värt att bära med sig:** kontot bar fortfarande **White Lines Black Spaces AB** som juridisk person, två konkurser bakåt, och Partner Center visade en gul banner om ett ogodkänt uppdaterat utvecklaravtal med passerad deadline. Slutsatsen blev att INTE klicka acceptera: godkännandet signeras av kontots juridiska person, så klicket hade bundit ett konkursat bolag vid ett nytt Microsoft-avtal mitt i en pågående entitetsflytt. Testa i stället empiriskt vid nästa submit. Generellt: **läs kontots juridiska person innan du klickar i något avtalsvillkor i en plattformsportal.**
**Tags:** Xbox, Partner Center, MSA-V2-reparenting-fryst, custom-permissions, produktgruppsscoping, New-bundles, New-add-ons, New-apps-aldrig, Manager-vs-Owner, halvöversatt-UI, URL-locale, entitet-innan-avtalsklick
