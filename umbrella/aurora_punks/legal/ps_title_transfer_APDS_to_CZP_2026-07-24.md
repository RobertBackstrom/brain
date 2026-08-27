# PlayStation title transfer - APDS (konkurs) to CZP

**Date:** 2026-07-24
**Ticket:** apb-015 (PS Partners case CS0157316, auto-closed - needs reopening)
**Sibling:** apb-026 (the Steam equivalent, in flight)
**Transferring partner:** Aurora Punks Development Services AB (559320-7466), konkurs 2025-12-12. PlayStation Company ID **38001**.
**Receiving partner:** Creation Zero Point Holding AB (559182-7471, VAT SE559182747101, dba "Aurora Punks"), Bondegatan 31, 116 33 Stockholm.
**Scope decision (Robert, 2026-07-24):** everything under the org, no exclusions.

---

## 1. Headline: this is NOT the Steam process

| | Steam | PlayStation |
|---|---|---|
| Mechanism | Self-serve **Transfer Tool** | **Help Center ticket**, executed by SIE |
| Who runs it | Actual Authority user | SIE, after both partners confirm on one ticket |
| Lead time | Days | **~3 months** (Sony's own stated standard) |
| Paperwork | SDA on receiving account | Transfer agreement + **Title_Transfer_Form** (2 sheets) |

Ticket routing: **Category = Partner accounts and app access → Secondary = Mergers and acquisitions**, subject "Title Transfer".

## 2. What SIE requires (Title Transfer Process Guidelines v1.2)

1. **Evidence of agreement between partners** (PDF). Must state (a) title(s) transferred, (b) date of transfer, (c) signatures of representatives of both partners. Any format; need not be addressed to SIE; English or Japanese. **The transfer process does not start until this is confirmed.**
2. **Title_Transfer_Form** - both the "Title Transfer" sheet and the "Title ID List" sheet.
3. **Contact name + email** for the other partner, added as ticket watcher.

**Prerequisites on the CZP side (all currently unmet, as far as we know):**
1. CZP must have signed a **GDPA** with SIE and have PlayStation Partners application access.
2. CZP must be added as a **collaborating partner** on each concept. Without this SIE *cannot* change Concept Lead or Publisher Store Name, and CZP cannot create a PAR. Can be requested inside the title-transfer ticket.
3. CZP must complete **bank account registration** (separate ticket - not accepted in the transfer ticket). Payee cannot change until done.

## 3. Mandatory steps and who owns them

| Step | Owner | Application |
|---|---|---|
| Terminate existing PAR | **Transferring** (APDS) | Content Pipeline |
| Create new PAR | **Receiving** (CZP) | Content Pipeline |
| Publisher Store Name | SIE | Content Pipeline |
| TPRnet / Certification Center | SIE | - |
| **Set access rights to DevNet products** | **Transferring** (APDS) | **DevNet** |
| Sales data view rights (post-transfer) | SIE | Analytics |
| Payee change | SIE | Finance |

**Unchanged by transfer:** SPID, NP Title ID, Product ID, and the PlayStation Store URL. Store pages and existing owners survive.

**Not eligible:** all PS3 and PS Vita products; themes and avatars (cannot be transferred at all - only the transferring partner can terminate those).

## 4. DevNet audit - what is actually there (verified live 2026-07-24)

Read directly from DevNet with the session built today.

**PS5 DevNet - zero titles accessible.**
> "There are currently no titles visible to you. Please be sure you have permission to see your company's products before creating a new one."

Under *"Other Aurora Punks Development Services AB Titles - The owners have not yet given you access to these products"*:
- 1 entry, **title name restricted**, owner **Johannes Fornaeus**, created ~9 months ago, comprising 1 App Server (Client Credential) + 1 Back Office Server.

**PS4 DevNet - one title, Robert is Owner.**
- **1993 Shenandoah** → product "1993 Shenandoah PS4 US", **CUSA27230_00** (App). Role: **Owner**.
- Almost certainly the same IP as *1993 Space Machine* on Steam (appids 373480 / 1236440), under its original name.

**Read this carefully:** the PlayStation footprint under APDS is *far* smaller than the Steam one (10 products / 20 appids). Robot Lord Rising, Chenso Club, Ooglians, IRON EVIL etc. are **not** visible under this company on DevNet. They are either not on PlayStation, or sit under a different partner (e.g. Headup publishes Vessels of Decay). "Everything under the org" therefore currently resolves to a very short list.

## 5. Blockers

1. **Robert is org-admin but not product-owner.** He can edit the org's IP allowlist (proven today) yet cannot see the PS5 product. Sony's guidelines §2-5 require *"the collaborator designated as the owner of the DevNet products of the transferring partner"* to grant the receiving partner Owner access. For the PS5 product that owner is **Johannes Fornaeus**, not Robert. Until that is resolved, the DevNet half of the transfer cannot be performed by us at all.
2. **CS0157316 auto-closed** and was never reopened (apb-015, backlog since 2026-05-28).
3. **CZP's PlayStation status is unverified** - GDPA, application access, SPID and bank registration all unknown. Item 1 of the advance-preparation checklist.
4. **Konkurs framing.** On Steam, Robert's standing call was to frame the request as technical, not legal, and to keep the bankruptcy out of the filing unless asked. Sony will nonetheless require signatures of representatives of *both* partners on the agreement document - and APDS's signatory position is complicated by the estate. The ATA with the estate that backs the Steam transfer is the natural evidence document to reuse.

## 6. Recommended sequence

1. Confirm CZP's PlayStation Partners status (GDPA signed? SPID? bank registered?). Cheapest first step, and item 1 on Sony's checklist.
2. Resolve DevNet product ownership - get Johannes Fornaeus to grant Owner access, or ask SIE to reassign inside the transfer ticket.
3. Confirm the true title list. Establish whether anything beyond 1993 Shenandoah is actually on PlayStation under APDS.
4. Reopen CS0157316 (or file fresh under Mergers and acquisitions) with the Title_Transfer_Form + reused ATA.
5. Set the contractual transfer date **at least 3 months out** from filing.

## 7. Tooling built

- [assistant/devnet-ip-allowlist.js](../../assistant/devnet-ip-allowlist.js) - login (password + auto mail-MFA), allowlist read/add.
- [assistant/devnet-titles.js](../../assistant/devnet-titles.js) - read-only catalogue enumeration. **Known limitation:** the row scraper targets `<tr>` and the Titles page is a div/list layout, so it returns 0 rows; the data above was read from the full-page screenshots. Worth fixing if the list ever grows.

Deliberately **not** automated: the DevNet collaborator/Owner grant. That is a write against a partner org, gated on blocker 1, and is a prerequisite step rather than something to script blind.

---

## 8. Update (same day) - org sweep + the real blocker: application entitlement

**All three orgs sit under one company.** Reached via "Related organizations" on the WLBS org page (`/account/orgs/` itself returns *"You are not permitted to view the organization list"*):

| Org | Org ID | Short name | Company |
|---|---|---|---|
| White Lines Black Spaces AB | 40816 | `w_lines_b_spaces` | 38001 |
| Aurora Punks Development Services AB | 44810 | `ed1aa0010e6a787a` | 38001 |
| Sir Whoppass | 44823 | `y402e9c553a04976` | 38001 |

DevNet's Titles page is scoped to the **company**, so it was already aggregating all three. Switching org context reveals nothing further. The near-empty result in §4 was not an org-selection mistake.

**Correction to §4's conclusion.** "The PS catalogue is tiny" was drawn from the wrong system. **DevNet holds *development* products** (App Servers, Back Office Servers, dev title IDs) - which is why the one visible PS5 entry is infrastructure, not a game. The **sellable catalogue lives in Content Pipeline** (Concepts, Product Groups, Products, PARs, Publisher Store Name). Sony's own form confirms it: the Title_Transfer_Form's SPID field is sourced from *"Content Pipeline > Administrator page"*. Nothing about the commercial catalogue can be settled from DevNet.

**THE BLOCKER (verified, decisive).** `accounts.develop.playstation.net/account/home/` states plainly:

> "Welcome to the SIE Developer Network! You have access to the following support websites: **PS4 DevNet, PS5 DevNet**"

That is the complete list for `Robert@aurorapunks.com`. **No Content Pipeline. No Analytics. No TPRnet. No Certification Center.** This is an **entitlement** problem, not a login or scraping problem - no amount of tooling gets past it. Consequences:

1. The sellable catalogue **cannot be enumerated** by us today.
2. **SPIDs cannot be read**, so the Title_Transfer_Form cannot be completed.
3. **Sales/royalty data is out of reach** - Analytics is not granted either.
4. Combined with the §5 finding that Robert is org-admin but not *product* owner, we currently hold DevNet-shaped access to a problem that is entirely Content-Pipeline-shaped.

**Route to fix.** Sony announced on 2026-07-15 ("Team Admin Role Now Available") and 2026-07-16 ("Team Admin Role Expanding to Manage PlayStation Partners Application Access") that **application access is now managed by a Team Admin on the company**. So either a Team Admin on company 38001 grants Robert Content Pipeline + Analytics, or it goes in as a Help Center request. Candidate holders, unconfirmed: **Johannes Fornaeus** (owns the restricted PS5 product) and **Hektor Andreasson** (ran the 2024 Curve Games Sony title transfer and was APDS's Actual Authority on Steam).

**Revised next step (supersedes §6 item 1):** secure Content Pipeline + Analytics access for a CZP-side and an APDS-side user *before* any further transfer work. Everything else is blocked behind it.

---

## 9. THE REAL CATALOGUE - Content Pipeline (verified live 2026-07-24)

**Correction to §4 and §8.** Content Pipeline is at **`https://publish.playstation.net/`** and Robert **does** have access. My §8 conclusion ("no Content Pipeline entitlement") was **wrong** - it rested on `accounts.develop.playstation.net/account/home/`, which lists *DevNet support websites only*, not the Partners application suite. §4's "the PS catalogue is tiny" was likewise wrong: DevNet holds dev infrastructure, not the sellable catalogue.

Session bootstrapped with the same Okta mail-MFA flow (`devnet-ip-allowlist.js --login --target https://publish.playstation.net/ --state .devnet/publishState.json`).

**Total concepts visible: 12.** APDS owns 4; the other 8 belong to third parties.

### APDS-owned - the actual transfer scope
**Partner:** Aurora Punks Development Services AB · **partnerId 10006419** · **SPID `UB1314`**

| Concept | conceptId | Platforms | Status | Regions |
|---|---|---|---|---|
| Block'Em! | 10012216 | PS5 / PS4 | ACTIVE | SIEE, SIEJA-ASIA, SIEA, SIEJA-JAPAN |
| Chenso Club | 10005000 | PS5 / PS4 | PUBLISHED | SIEE, SIEA |
| 1993 Shenandoah | 10002510 | PS4 | PUBLISHED | SIEE, SIEJA-ASIA, SIEA, SIEJA-JAPAN |
| DO NOT USE | 10006927 | PS5 / PS4 | **SUSPENDED** | SIEE, SIEA |

### NOT APDS - must be excluded from any transfer
| Concept | Partner | SPID |
|---|---|---|
| Distant Bloom, Go Fight Fantastic! | Kinda Brave Entertainment Group AB | JB0701 |
| Garden of the Sea, Budget Cuts Ultimate | Neco Software | EP5210 |
| KreatureKind | Valiant Game Studio AB | EB1749 |
| Strike Force Heroes | Yaozuo Games Ltd | UP8419 |
| Backpack Hero | Pretty Soon S.A. | UP7793 |
| Kingdom Two Crowns | RAW FURY | UP2320 |

**This is exactly the trap the Steam audit caught.** The instruction was "everything under the org, no exclusions" - taken literally against this view it would have swept **8 third-party titles** belonging to Kinda Brave, Neco, Valiant, Yaozuo, Pretty Soon and RAW FURY into an APDS→CZP transfer. **Filter on `partnerId = 10006419`.**

### Open questions on scope
1. **"DO NOT USE" (SUSPENDED)** - almost certainly a scrapped/duplicate concept. Confirm whether it transfers or is left to die with APDS.
2. **Robot Lord Rising, Ooglians, IRON EVIL, Aurora, Innsmouth, JETZNAB, Massive Attax** (all on the Steam transfer list) have **no PlayStation concept at all**. The PS transfer is genuinely a 3-4 title job, not a 10-title one.
3. **Sir Whoopass** has a DevNet org but **no concept** under this account - consistent with it being handled separately.

### Still needed for the Title_Transfer_Form
`titleReferences` is **empty at concept level** - NP Title IDs (CUSA/PPSA) hang off **products**, not concepts. The "Title ID List" sheet therefore needs a second pass over each concept's products. Not yet done.

### How the data was obtained (for whoever maintains this)
Content Pipeline is a SPA whose grid is divs (`span.row-cell-content`), not a table, and it virtualises pagination - DOM scraping produced collapsed/duplicate rows. Direct navigation to `/api/v1/concepts` returns `ERR_HTTP_RESPONSE_CODE_FAILURE` and an in-page `fetch()` returns empty (missing the headers the app sends). **What works:** let the SPA issue its own request and use `page.route()` to rewrite `limit=10` to `limit=500`, then read the response. Endpoints: `GET /api/v1/concepts?limit=N` and `GET /api/v1/concepts/count`.

---

## 10. Transfer scope LOCKED (Robert, 2026-07-24)

**Receiving entity:** CZP Holding AB. **Transfer these 3 concepts (partnerId 10006419, SPID `UB1314`):**

| Concept | conceptId | Platforms | NP Title ID(s) |
|---|---|---|---|
| Block'Em! | 10012216 | PS5 / PS4 | *pending product-level pull* |
| Chenso Club | 10005000 | PS5 / PS4 | *pending product-level pull* |
| 1993 Shenandoah | 10002510 | PS4 | **CUSA27230_00** (from DevNet) |

**Explicitly EXCLUDED — stays with APDS:** "DO NOT USE" (conceptId 10006927, SUSPENDED). Robert: purpose unknown, leave it in APDS.
**Not on PlayStation at all** (so not in scope): Robot Lord Rising, Ooglians, IRON EVIL, Aurora, Innsmouth, JETZNAB, Massive Attax.

### Title ID List — status
Sony's "Title ID List" sheet wants every product's NP Title ID. We have 1993 Shenandoah's (CUSA27230_00) from DevNet. Block'Em! and Chenso Club's product-level IDs are **not yet pulled**: the Content Pipeline concept-*list* API (`/api/v1/concepts`) returns summary records with `titleReferences`/`spids`/`productReferences` all EMPTY, and the per-concept detail route hasn't been found — `/api/v1/concepts/{id}` (and `/products`, `/product-groups` variants) all 404, and the div-grid rows don't expose an `id`-bearing link to click through the SPA router. **This is a known gap, not done.** It is also low-urgency: Sony explicitly allows filing the ticket first and supplying the completed Title ID List afterward. The two missing IDs can be read by opening each concept in the portal manually (2 min) or by resuming the endpoint hunt later.

### What's ready to act on now
1. Transfer scope, receiving entity, SPID and conceptIds — all confirmed.
2. Process, ticket routing, required documents, lead time — all documented (§1-3).
3. The blocking prerequisite is **CZP-side**: GDPA signed? PS Partners app access? bank registered? None verified. This gates the whole transfer and is the cheapest next step.

---

## 11. Sales / promotions — discovery + draft plan (read-only, 2026-07-24)

**Scope (Robert):** the 3 transfer titles only — Block'Em!, Chenso Club, 1993 Shenandoah. **Timing:** on APDS now. **Gate retained:** draft for approval before anything is submitted live.

### What "regional and timed sales" actually are
PS Store discounts are not free-form. They are **Sony-curated campaigns** the partner opts titles into, each split into **4 regional promotions** (SIEA, SIEE, SIEJ, SIEAsia), type "Price Discount / Percentage". Promotions Manager holds **158 total**, but **142 are EXPIRED**. Only **4 campaigns are open/live** right now:

| Campaign | Start | State | Regions |
|---|---|---|---|
| Gamescom | 2026-08-26 | IN_PROGRESS (editable) | ×4 |
| Ready Set Play | 2026-08-12 | SONY_FINALIZING | ×4 |
| Summer Sale pt two | 2026-07-27 | PUBLISHED | ×4 |
| Summer Sale pt one | 2026-07-15 | **LIVE now** | ×4 |

So "apply to all regional and timed sales" resolves to: opt the 3 titles into each open campaign, across its 4 regions. **Gamescom (IN_PROGRESS) is the one still cleanly editable**; SONY_FINALIZING/PUBLISHED/LIVE are progressively locked.

### "Same discount as last discount"
Discount % lives **per product, per promotion**. The natural "last discount" reference is the most recent campaign each title took part in (Summer Sale, or the prior expired campaign). Reading each title's exact last % per region is the one remaining read-only pull; not yet done.

### HARD GATE before any write
Opting titles into a promotion **writes discount pricing to the live PS Store**. This is a publish action, it is revenue-affecting, and until the transfer completes the **payee is the APDS konkurs estate** — so any sale run now earns money for the estate, not CZP. I will draft the exact opt-in plan (title × campaign × region × %) for sign-off and will **not** submit anything to Sony without explicit approval.

### Workstream A blocker confirmed
`/api/v1/partners` on this account returns **exactly one partner: APDS (10006419)**. **CZP is not a PlayStation partner on this account.** "List CZP as developer" therefore cannot be done yet — CZP must first be onboarded (GDPA + app access) or added by SIE inside the transfer ticket. Unchanged: the read-only prep (Title Transfer Form + agreement PDF) can proceed.

---

## 12. AKTIVERAT 2026-08-26 — beviskravet är uppfyllt, CZP-sidan är hela blockeraren

Robert gav klartecken 2026-08-26 att köra plattformsflyttarna i ordningen Nintendo, PlayStation,
Xbox. Ingen advokatgenomlysning ska inväntas.

### Det som ändrades

Sonys krav 1 i Title Transfer Process Guidelines v1.2, **"evidence of agreement between partners"**,
är nu uppfyllt. Kravet är att handlingen anger (a) vilka titlar som överlåts, (b)
överlåtelsedatum och (c) underskrifter från båda parters företrädare. Vi har hela kedjan:

| Handling | Täcker (a) | Täcker (b) | Täcker (c) |
|---|---|---|---|
| `Rörelseöverlåtelseavtal` APDS konkursbo -> Bright Gambit, Scrive `09222115557567493495` | Ja, bilaga 2 namnger 17 poster inkl. Block'Em, Chenso Club och 1993 | 2026-01-18 | BankID: Nils Åberg (förvaltare) + Tim Browne (BG) |
| `Asset_Transfer_Agreement_BrightGambit_CreationZeroPoint`, DocuSign `C1FE07CC-...` | Generiskt "all assets", lutar sig mot bilagan ovan | 2026-02-16 | Andreea Chifu (BG) + Robert Bäckström (CZP) |

Drive: `10ZN-_9YckcvVJDBGV-5szGsAlaI_f-SQ` respektive `1nYJ_Vp7rnxcrJrWqMQ-43lHPKwLmpsBz`.
Skicka **båda**, i den ordningen. Det första bär titelnamnen, det andra bär CZP som part.
Ingen av dem ensam uppfyller (a) och (c) för CZP samtidigt.

### Ordningen är inte förhandlingsbar, och den börjar inte hos Sony

Det frestande är att öppna om CS0157316 direkt eftersom bevisningen äntligen finns. Det vore fel
drag. `/api/v1/partners` returnerar exakt en partner, APDS. **CZP är inte PlayStation-partner alls.**
Sony kan inte byta Concept Lead eller Publisher Store Name till en entitet som inte existerar i
deras system, och ledtiden på tre månader börjar först när de kan agera.

1. **GDPA för CZP.** Ansökan till SIE om Global Developer and Publisher Agreement plus
   PlayStation Partners-applikationsaccess. Detta är den enda punkten som gatar allt annat, och
   den har längst egen ledtid. **Börja här.**
2. **Bankregistrering för CZP.** Eget ärende hos SIE, tas uttryckligen **inte** emot i
   transferärendet. Payee kan inte ändras förrän det är klart. Kan köras parallellt med punkt 1.
   Samma uppgifter som Steam-onboardingen använde: SEB, IBAN `SE9650000000052661032177`, BIC
   `ESSESESS`.
3. **Öppna om CS0157316**, kategori `Partner accounts and app access` -> `Mergers and
   acquisitions`, ämne "Title Transfer". Begär i samma ärende att CZP läggs till som
   **collaborating partner** på de tre concepten. Bifoga båda avtalen.
4. **Title_Transfer_Form**, båda flikarna. NP Title ID för Block'Em! och Chenso Club är fortfarande
   inte utdragna, men Sony tillåter uttryckligen att listan kompletteras efter att ärendet öppnats.
   Två minuter i portalen per titel, eller återuppta endpoint-jakten i avsnitt 9.
5. **APDS-sidans egna steg** när Sony är redo: avsluta befintlig PAR i Content Pipeline och sätta
   access rights på DevNet-produkterna. Båda ägs av den avlämnande parten, alltså av oss.

### Omfattning, oförändrad

Block'Em! (concept 10012216), Chenso Club (10005000), 1993 Shenandoah (10002510, NP Title ID
CUSA27230_00). Exkluderad: "DO NOT USE" (10006927, suspended).

**Formulering, en sak att inte slarva med.** Bilaga 2 anger AP AB som IP-ägare till både Block'Em
och Chenso Club. Skriv därför att CZP förvärvat rörelsen med tillhörande publicerings- och
distributionsrättigheter, inte att CZP äger IP:t. Sony ska flytta ett konto och en
publiceringsposition, och det är precis vad handlingarna belägger. Se
`umbrella/aurora_punks/legal/apds_entity_transfer_master_2026-08-26.md` avsnitt 2.

### Verktygsläget

`DEVNET_PASS` finns i `assistant/.env` och `devnet-ip-allowlist.js` kör redan Playwright mot
DevNet, så portalläsning är möjlig. Punkt 4 ovan kan alltså köras utan att blockera på något.
