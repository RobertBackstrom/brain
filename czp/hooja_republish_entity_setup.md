# Hooja republish - entity + developer-account setup plan

**Owner:** CorpBot (admin) · **Prefix:** hoj / czp · **Date:** 2026-07-13
**Scope from Robert:** stand up the ENTITY + STORE DEVELOPER ACCOUNTS now. Legal IP-chain review is ON HOLD until Robert speaks with the konkursförvaltare. This document is research + a scoped plan only. Nothing is filed and no account is created here (autonomous-queue: draft/plan OK, never execute external actions).

---

## 0. Situation in one paragraph

Hooja (F2P mobile auto-runner on the Hooja music-artist IP, bundle `com.AuroraPunks.Hooja` / App Store `id1659828753`) is delisted from both Google Play and App Store - both URLs 404. The attributed cause is the bankruptcy of the developer entity **APDS = Aurora Punks Development Services AB** (559320-7466, konkurs since 2025-12-12, konkursförvaltare Ellen Berglund, Advokatfirman Carler), which terminated the store developer accounts. Robert wants to republish under a **CZP-controlled publishing entity** and reuse that same vehicle for future titles (K2C, BlockEm, a MENA horse-race reskin). This mirrors the entity swap already in flight on Steam (apb-026) and PlayStation (apb-015), where **Creation Zero Point Holding AB** is the successor platform entity.

---

## 1. Entity choice - which company publishes

### Candidates
1. **Creation Zero Point Holding AB (CZP Holding)** - 559182-7471, VAT SE559182747101, dba "Aurora Punks", Bondegatan 31, 116 33 Stockholm. Robert 100%. Already the chosen successor entity on Steam + PlayStation.
2. **A new dedicated wholly-owned publishing subsidiary** under CZP (e.g. "Aurora Punks Publishing AB").

### Pros / cons

**CZP Holding AB directly**
- Pro: fastest path. It already has a live VAT number, an established payee history on Microsoft/Xbox (ID@Xbox 2022) and now Steam + PlayStation, so one entity = one payee + one tax profile + one D-U-N-S across every storefront.
- Pro: consistency with apb-026 / apb-015 - Robert is already migrating the other platforms to CZP Holding, so mobile lands in the same place.
- Pro: verksamhetsföremål already broad - the 2019 bolagsordning states the main business as "computer, video and mobile game development and investments into game development studios and IPs," so publishing/operating activity is within scope (still worth a fresh read at setup, per the Lawyer note on holdingbolag as an operating/contract party).
- Con (structural): CZP Holding is Robert's personal holding company - it holds his stakes in AP (30.14%), Runatyr (50%, contested), Dark Riviera, Malformation, and others. Loading consumer-facing publishing risk (product liability, IAP/consumer-protection, third-party IP-infringement exposure from the music-artist license and the "external client" IP question) onto the entity that also holds all his equity is poor isolation. An IP or consumer claim against the publishing operation could reach the shareholdings.
- Con: mixes operating cashflow (IAP + ad revenue) into the holding co's books, muddying per-title P&L and any future sale/partner-in.

**New dedicated publishing subsidiary**
- Pro: clean liability ring-fence - operating risk sits in a thin subsidiary, not the holding.
- Pro: purpose-built as the reusable vehicle for many titles, easy per-title P&L, easy to bring in a co-publishing partner or sell later.
- Pro: isolates MENA revenue + withholding-tax exposure from the horse-race title away from the holding.
- Con: slowest path - fresh VAT registration, a fresh D-U-N-S, fresh bank account, and store accounts built from zero. Weeks of lead time before a single upload.
- Con: diverges from the Steam/PS entity swap, so storefronts end up split across two entities (CZP Holding on desktop/console, subsidiary on mobile) unless everything is later consolidated.

### Recommendation - two-phase
1. **Phase 1 (now, republish-first):** publish Hooja under **CZP Holding AB**, reusing the exact entity, VAT, bank and D-U-N-S already being stood up for Steam + PlayStation. This is the fastest route to relisting and keeps all storefronts under one payee/tax profile. It matches Robert's "republish-first, template-later" decision (2026-07-13).
2. **Phase 2 (before the vehicle scales to multiple third-party-IP titles + MENA revenue):** spin out a **wholly-owned publishing subsidiary** under CZP and migrate the developer accounts into it, so operating risk is ring-fenced away from the holding. Trigger points: adding a second/third live title, taking a co-pub partner, or launching the MENA horse-race title with IAP-led revenue.

Flag for Robert: the Phase-1 tradeoff (operating risk inside the holding) is deliberate and temporary. If he would rather not put mobile IAP risk on the holding at all, we go straight to the subsidiary and accept the extra weeks of setup. **One decision needed - Phase-1 CZP-Holding-now, or subsidiary-from-the-start.**

---

## 2. Google Play Developer account (organization type)

Requirements to create a new organization Play Console account:
1. **D-U-N-S number** for CZP Holding AB - mandatory for org accounts. Free from Dun & Bradstreet (in Sweden via D&B/Bisnode). Check first whether CZP already has one (free lookup at dnb.com UPIK); if not, request it. Precedent: Robert obtained a D-U-N-S for the WLBS entity in 2022 (350685539) specifically to set up an Apple Dev account, and Sifferrådet (Henrik Franzén) assisted - so the accountant can help pull/request the CZP number.
2. **Organization verification** - business name, address and contact must match the D-U-N-S record and Bolagsverket registration. Google verifies org identity in **up to 5 business days** once the D-U-N-S + supporting docs are submitted (2026 requirement). Publishing is blocked until verification clears, so submit the D-U-N-S on day one.
3. **One-time registration fee** - USD 25 (one-time, per account).
4. **Payments / merchant profile** - a Google Play payments profile (Google merchant) with CZP's bank details + Swedish tax info, required before Hooja can take IAP or receive payouts. This is set up in Play Console after the account is verified.
5. **Developer identity + contact verification** - Google's 2026 identity-verification regime requires the account owner to complete identity verification; expect document requests.

**Scrutiny risk flag:** the account owner (Robert) is a director tied to two recently bankrupt games entities (APDS and WLBS), and WLBS itself previously had a Google Play org that drew "complete account verification" notices (Sept 2024 thread). A brand-new CZP org account is the clean path, but be ready for extra verification friction - have registreringsbevis, D-U-N-S confirmation, and proof of Robert's authority to represent CZP ready up front. Do NOT try to reinstate or inherit the bankrupt entities' accounts.

---

## 3. Apple Developer Program (organization, not individual)

Requirements to enrol CZP Holding AB as an organization:
1. **D-U-N-S number** - same CZP D-U-N-S as above; Apple uses it to verify legal-entity status, name and address. Timeline: up to 5 business days to receive a new D-U-N-S from D&B, then up to 2 business days for Apple to receive the data from D&B.
2. **Legal-entity verification + legal-authority review** - Apple confirms CZP is a legal entity and that the enroller has authority to bind it. Standard internal verification is up to ~6 working days, but **organization enrollments with D-U-N-S + legal-authority checks run 2-4 weeks** (2026). This is a genuine lead-time item, plan for the upper end given the bankrupt-affiliate context.
3. **Membership fee** - USD 99 per year.
4. **Paid Applications Agreement + banking/tax in App Store Connect** - this is the **longest-lead, highest-friction** item. After enrollment, the Account Holder must accept the Paid Applications Agreement and complete the banking (CZP IBAN/BIC) + tax forms (incl. US tax forms / W-8BEN-E equivalent, VAT). Until this is fully green, the app cannot take IAP or receive payouts even if the build is approved. Start it the moment enrollment clears.
5. **Account Holder assignment** - the Apple "Account Holder" role must be a natural person tied to CZP with authority (Robert). Assign deliberately - the Account Holder legally binds the org and is the only role that can accept agreements and manage membership.

---

## 4. New app listings - republish = new app

Consequences to set expectations:
1. **Republishing is a NEW app, not a restore.** New store listing on each platform, built from scratch (metadata, screenshots, ratings questionnaire, privacy/data-safety forms).
2. **Almost certainly a new bundle/package ID.** The old IDs (`com.AuroraPunks.Hooja`, App Store `id1659828753`) are tied to the terminated/bankrupt-entity accounts and cannot be assumed transferable into a fresh CZP account, especially with the estate question open. Plan for a new ID under the CZP namespace, e.g. `games.creationzeropoint.hooja` or a retained `com.aurorapunks.hooja2` style - decide the naming convention now because it is baked into the build and is effectively permanent. (If a clean app-transfer of the existing ID from the estate later proves possible, that is upside, not the plan.)
3. **Loss of legacy footprint.** New listing = zero ratings, zero reviews, reset install base and store ranking/history. The old reviews and installs do not carry over. Factor this into the relaunch/marketing plan.
4. **Bundle-ID + package-name change is a code/build task** - hand the actual ID change and re-signing to the GameDev agent (new Android keystore hygiene already flagged; new signing identity needed under the CZP account anyway).

---

## 5. Merchant of record / tax

1. **Merchant of record.** On both stores, Apple and Google act as merchant/agent for consumer IAP in most territories and remit net of their commission + local consumer VAT they collect. The **CZP Holding payee/tax profile** on each account is what receives IAP payouts and ad revenue (LevelPlay/ironSource pays the account holder). So CZP becomes the revenue-receiving entity for both IAP and ads.
2. **VAT / MOSS.** For EU B2C digital sales the platforms handle the consumer VAT under the OSS/one-stop-shop mechanism, so CZP generally receives VAT-exclusive payouts; CZP still books the revenue and reports per Swedish VAT rules. Ad revenue (LevelPlay) is typically a B2B service - reverse-charge / VAT handling depends on the ad-network entity's location; confirm with Sifferrådet at setup.
3. **MENA flag (future horse-race title).** Robert wants IAP-led MENA monetization. Several MENA markets have withholding tax, local VAT (e.g. KSA/UAE 15%/5%), and app-store payout rules that differ from EU - and carrier billing / Huawei AppGallery may route revenue outside Apple/Google's merchant-of-record umbrella, which changes who is liable for local tax. This is a tax-structuring question for the dedicated-subsidiary decision (section 1, Phase 2) and for Lawyer + Sifferrådet before the MENA title ships. Not resolved here - flagged.

---

## 6. PlayFab title ownership

1. Hooja uses **PlayFab** for login, leaderboards and telemetry (no catalog). The PlayFab **title** sits inside a PlayFab **Studio**, owned by whichever Microsoft/Azure/PlayFab account was used to create it - historically an Aurora Punks / APDS-era account, not CZP.
2. **Action (research/flag, do not execute):** identify the owning PlayFab Studio + account, then either (a) transfer the title to a CZP-owned PlayFab Studio, or (b) re-point the game to a fresh CZP PlayFab title. Note that PlayFab title ownership is a Microsoft account/Studio-membership question, adjacent to the Xbox/ID@Xbox history CZP already holds - it may be simplest to house the PlayFab Studio under the same Microsoft account CZP uses for Xbox.
3. **Dependency:** if the PlayFab title is tangled with the APDS account, it touches the estate question (section 7b) - flag, do not resolve. GameDev owns the technical re-point; CorpBot owns the account/ownership side.

---

## 7. Dependency flags - DO NOT RESOLVE (on hold per Robert)

**(a) Hooja IP chain-of-title is UNCONFIRMED.**
- AP records classify Hooja as "external client vs Own IP 50%" - ownership is ambiguous, and there is a separate **music-artist licensing deal** (the Hooja artist IP) underneath the game.
- Both must clear **Lawyer + the konkursförvaltare** before Hooja can lawfully be republished under CZP. Publishing a title whose IP chain is unconfirmed exposes CZP to an infringement/estate clawback claim.
- Related open item: the signed **APDS-estate Asset Transfer Agreement** (CZP's purchase of APDS assets from the estate) is flagged missing from Drive/mail (apb-006). apb-026 asserts "CZP bought the APDS assets from the bankruptcy estate," but the document evidencing it has not been located. That agreement is what would (or would not) carry Hooja's rights to CZP. **Locate it via Carler correspondence before relying on it.**
- **On hold** until Robert speaks with the konkursförvaltare himself. This plan proceeds only on the entity + account scaffolding, which does not require the IP question resolved - but nothing publishes until it clears.

**(b) APDS store assets/accounts may be part of the bankruptcy estate.**
- The developer accounts, the app listings, the bundle IDs, and possibly the PlayFab title could be property of the konkursbo. Whether any of it can be transferred (vs must be rebuilt fresh under CZP) is a question for the konkursförvaltare. The Steam matter (apb-026) already hit this - Valve directed an app-by-app transfer to a NEW CZP account rather than mirroring the bankrupt account. Expect the same shape on mobile: build fresh under CZP, do not try to inherit the estate's accounts.

**(c) Verification/fact flag to resolve before filing (not an IP question):** which legal entity actually held the Google Play + Apple developer accounts for Hooja needs confirming. A Sept 2024 mail from Hektor states Hooja was published under **Aurora Punks AB's** Google Play account ("Den vi använder och där Hooja är publicerat heter Aurora Punks AB"), while the 2026 delisting is attributed to **APDS's** bankruptcy. AP AB is NOT bankrupt, so if Hooja's account were truly AP AB's it would not have been terminated for APDS's konkurs. Possible the account moved to APDS later, or the delist cause differs. Confirm the actual account holder + the real delist reason before the republish plan is executed - it changes whether a transfer is even on the table.

---

## 8. Ordered timeline - longest-lead first

Rough durations; run the parallelizable items together. Wall-clock to "both stores accepting a build" is roughly **3-6 weeks** from a standing start, dominated by Apple org verification + the Paid Applications Agreement banking/tax.

1. **Entity decision** (Robert, ~same day) - confirm Phase-1 CZP Holding vs subsidiary-from-start (section 1). Blocks everything.
2. **D-U-N-S for CZP Holding** (~up to 5 business days) - check for an existing number first (dnb.com UPIK); request if none. Sifferrådet can assist. Feeds BOTH stores, so do this first and in parallel with nothing depending on it.
3. **Apple Developer Program org enrollment** (~2-4 weeks) - longest single item. Submit as soon as the D-U-N-S is live. USD 99/yr. Assign Robert as Account Holder.
4. **Apple Paid Applications Agreement + App Store Connect banking/tax** (days-to-weeks, starts only after enrollment clears) - the true critical path for taking revenue. Accept agreement, enter CZP IBAN/BIC + tax forms. Nothing sells until green.
5. **Google Play org account + verification** (~5 business days after D-U-N-S) - USD 25 one-time, then org verification, then payments/merchant profile with CZP bank + tax. Faster than Apple; can run fully in parallel.
6. **Google Play payments/merchant profile + Apple banking** - complete both so IAP + payouts route to CZP.
7. **PlayFab title ownership** (parallel, GameDev + CorpBot) - identify owner, transfer or re-point to CZP Studio.
8. **Bundle/package ID decision + rebuild/re-sign** (parallel, GameDev) - lock the new CZP-namespace ID, new signing identity/keystore, and the SDK-modernization build (Unity 6 / LevelPlay 8 / Unity IAP) so a submittable build exists when the accounts are ready.
9. **New store listings** (after accounts live) - metadata, screenshots, ratings/data-safety questionnaires from scratch under CZP.
10. **GATE before any submission:** IP chain-of-title (7a) + estate-asset question (7b) cleared with Lawyer + konkursförvaltare, and the account-holder fact (7c) confirmed. No upload before this gate, regardless of account readiness.

---

## Cross-references
- apb-026 (Steam APDS to CZP entity swap) · apb-015 (PlayStation, same swap) · apb-006 (missing APDS Asset Transfer Agreement)
- project_hooja (memory) · project_rlr_ip_dispute (parallel APDS/estate matter) · reference_company_structure · reference_entity_accountants
- GameDev owns: bundle-ID change, re-sign, SDK modernization, PlayFab re-point. Lawyer owns: IP chain + music license review. Konkursförvaltare (Ellen Berglund, Advokatfirman Carler): estate-asset + IP clearance.
