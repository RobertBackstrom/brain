# Steam / Steamworks support request — entity transfer APDS (konkurs) to CZP

**Status:** DRAFT for Robert review — 2026-06-23
**New entity:** Creation Zero Point Holding AB (org 559182-7471), dba "Aurora Punks"
**Old entity:** Aurora Punks Development Services AB (org 559320-7466), in konkurs since 12 Dec 2025
**Precedent:** mirrors LetterOfConsent_SirWhoopass_AP-to-AE_2026-06-10 (worked for Microsoft Partner Center)

---

## A. Support request (submit via Steamworks Contact Support or to the Valve partner contact)

Subject: Product ownership transfer - bankrupt partner entity to acquiring entity (Aurora Punks Development Services AB to Creation Zero Point Holding AB)

Hello Steam Partner Support,

I am writing to arrange a transfer of product ownership between two Steamworks partner entities following a bankruptcy and asset acquisition.

Background:
- The current partner entity, Aurora Punks Development Services AB (Swedish org. nr 559320-7466), entered bankruptcy (Swedish "konkurs") on 12 December 2025.
- Creation Zero Point Holding AB (Swedish org. nr 559182-7471, VAT SE559182747101, trading as "Aurora Punks") has acquired the relevant game assets, including the Steam titles below, from the bankruptcy estate of Aurora Punks Development Services AB. A signed Asset Transfer Agreement is available on request.
- I, Robert Bäckström, am Director and authorised signatory of Creation Zero Point Holding AB and can sign any documentation Valve requires.

Request:
1. Please advise the correct process to move ownership of the apps listed below from the Aurora Punks Development Services AB Steamworks account to Creation Zero Point Holding AB.
2. Creation Zero Point Holding AB is ready to sign its own Steam Distribution Agreement and complete banking and tax (W-8BEN-E) onboarding for the receiving account.
3. Please confirm what documentation you need from us (e.g. the Asset Transfer Agreement, proof of authority, a letter of consent), and in what order you would like to receive it.

Apps to transfer (to be confirmed by Valve against the account):
- Tears of Adria - app 2561500
- BlockEm! - app 1529220
- Chenso Club - app 1454730
- Ooglians - app 2162070
- [confirm: 1993 Space Machine and any other titles under this account]

Note: Sir Whoopass: Immortal Death (app 1240590) is handled separately and is NOT part of this request.

---

## CONFIRMED TRANSFER LIST — locked 2026-07-13 (supersedes the provisional list above)

Verified live from inside the APDS Steamworks account (PartnerID 301411).
Login `naturenistockholm_2` is admin across MULTIPLE partner orgs (Valiant 53109, Headup 69688,
Red Marmoset 169300, Feral Flame 200248, Duck Tape 210499, Ark Island 229086, Windup 235971,
APDS 301411, Eternal Minds 350400) — so the account-wide /apps/ listing mixes other studios' titles.
**Ownership was resolved authoritatively via APDS's own package-admin (`/pub/packageadmin/301411`)**,
not the store "publisher" display string. Only titles with packages under 301411 are APDS assets.

**Receiving account:** Creation Zero Point Holding AB, dba "Aurora Punks" — **PartnerID 418393**,
login `aurorapunks_user`, sales@aurorapunks.com. Steamworks Partner registered + NDA signed 2026-07-13;
banking (SEB, IBAN SE9650000000052661032177, BIC ESSESESS) + W-8BEN-E onboarding being finalised.
**Note:** CZP registered-office address updated to **Bondegatan 31, 116 33 Stockholm** (was Brännkyrkagatan 10b).

**TRANSFER to 418393 (10 products / 20 appids):**
- Robot Lord Rising — 1420120
- Block'Em! — 1529220 (+ Demo 1776680, Playtest 1722030, Soundtrack 2132150)
- Chenso Club — 1454730 (+ Demo 1666060, Playtest 1781210)
- Ooglians — 2162070
- IRON EVIL — 1795100 (+ Beta 1909980, Demo 2811690)
- 1993 Space Machine — 373480 (+ Soundtrack 1236440)
- Aurora — 2353550
- Innsmouth — 2752910
- JETZNAB — 2352370
- Massive Attax — 1529170

**EXCLUDE — leave on 301411 / not APDS assets:**
- Tears of Adria (2561500) — Robert's explicit call, stays behind (was in the original draft list; removed)
- Five-O (4011710) — no packages under APDS
- Water Me and You (2509360) + Demo — **returned to Shosha Games** per signed Statement of Ownership & Return
  (Shosha owns the IP incl. the not-yet-released Steam version; AP AB is publisher, APDS was tech-ops only)
- KreatureKind (1428090) — Valiant Game Studio (53109)
- BAD BLOOD: 1926 (1920190) — Red Marmoset (169300)
- Vessels of Decay (1425180) — Headup (69688)
- Soccerboy vs Aliens (3562500) — Red Marmoset (169300)
- Cold Response (3831420) — Eternal Minds (350400)
- Primal Echo (2394180) — Feral Flame (200248)

**Reply guidance (Robert, 2026-07-13):** do NOT proactively raise the konkurs or the Asset Transfer
Agreement in the reply — only mention if Valve asks.

Thank you - happy to provide anything you need to move this forward.

Best,
Robert Bäckström
Director, Creation Zero Point Holding AB (dba Aurora Punks)
robert@aurorapunks.com

---

## B. Letter of Consent (attachment, if Valve wants it - mirrors the Microsoft one)

Letter of Consent - Steam Product Ownership Transfer

Creation Zero Point Holding AB (org. nr 559182-7471)
Bondegatan 31, 116 33 Stockholm, Sweden
[DATE]

Creation Zero Point Holding AB ("CZP") has acquired the assets of Aurora Punks Development Services AB (org. nr 559320-7466), including the Steam titles listed below, from the bankruptcy estate of Aurora Punks Development Services AB. CZP therefore holds the right to consent to the transfer set out below.

I, Robert Bäckström, signing as Director and authorised signatory of Creation Zero Point Holding AB, consent to the transfer of ownership of the following Steam applications to Creation Zero Point Holding AB:
- Tears of Adria (app 2561500)
- BlockEm! (app 1529220)
- Chenso Club (app 1454730)
- Ooglians (app 2162070)
- [confirm additional titles]

Signed,
Robert Bäckström
Director, Creation Zero Point Holding AB

---

## Channel & sequencing (confirmed 2026-06-23)
- **Filing channel:** Steamworks support system, submitted from inside the EXISTING APDS Steamworks account. No Valve email channel exists. Existing account is accessible (Steam login "stagisaurus" + others: Winston, Hektor, Christian).
- **Receiving account:** new dedicated CZP Steam account (Robert's choice) - created via live Playwright session AFTER Valve confirms the approach.
- **Open question for Valve:** whether they handle this as (a) a company-info/payee update on the SAME account (legal name -> CZP, new bank, new W-8BEN-E) or (b) an app-by-app transfer to a new CZP account. The konkurs may force (b). We ask before doing anything.

## URGENT side-finding
- As of the 28 Apr 2026 payment notice, Valve is still paying revenue to "Aurora Punks Development Services AB" (the bankrupt entity). Post-acquisition revenue belongs to CZP. Flag payee redirection to CZP as part of the same request.

## Open items before sending
1. **Confirm the app list** - which titles actually sit under the APDS Steamworks account. Known live: Ooglians (2162070), Tears of Adria (2561500), BlockEm! (1529220), Chenso Club (1454730). Sir Whoopass (1240590) is the separate Atomic Elbow track - exclude.
2. **CZP registered office address** - Bondegatan 31, 116 33 Stockholm, Sweden (registered address per Robert 2026-07-15; the earlier Brännkyrkagatan 10b was superseded).
3. **Attach** the signed APDS-estate Asset Transfer Agreement.
