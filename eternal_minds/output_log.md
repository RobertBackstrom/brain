# Eternal Minds AB — Output Log

**Project:** Eternal Minds AB (org.nr 559527-5719)  
**Owner:** Robert  
**Type:** Internal / Corporate Governance

---

## 2026-04-20

**Deliverables created (4am sweep — CorpBot):**

1. **CHECKLIST_2026-04-20.md**
   - 7 open questions Robert must confirm before proceeding
   - Suppleant name/ssn, bolagsordning sections, EGM date/time/place, chairman/scrutineers, ansvarsfrihet relevance
   - Status: Waiting for Robert input

2. **TIMELINE_KRITISKA_DATUM.md**
   - Critical date tracking and deadline visualization
   - ABL 8:13 14-day filing deadline clearly marked
   - Recommended workflow phases (planning → docs → EGM → signatures → filing)
   - Risk mitigation strategies

3. **Activity log updated** (`assistant/followups/em-001-board-vd-change-bolagsverket.md`)
   - Status: NEEDS_INPUT
   - Blocker: Roberts confirmation of 7 checklist items needed before document updates

**Next phase (pending Robert):**
- Confirm checklist items
- Update all docs (01–07) with confirmed data
- Convert .md → Google Docs
- Upload to CZP/Deliverables/Eternal Minds AB/
- Set up DocuSeal signing queues
- Execute EGM by 2026-04-27 latest
- File ändringsanmälan to Bolagsverket within 14 days of EGM

**Notes:**
- Original docs dated 2026-04-13 (already passed) — requires refresh with actual EGM date
- Deadline is firm: no flexibility on 14-day window per ABL 8:13
- Package includes 8 documents total (all drafted, awaiting data)

---

## 2026-04-20 (continued, evening session)

**Robert bekräftade:**
- Per capsulum-format (inget fysiskt/digitalt möte, alla aktieägare signerar protokoll)
- Beslutsdatum 2026-04-23
- Robert kvarstår själv som suppleant (ingen ny person)
- Ingen bolagsordningsändring (befintlig BO tillåter 1+1)
- Ansvarsfrihet struken (inget avslutat räkenskapsår med årsredovisning)

**Deliverables produced:**

1. **Omarbetat dokumentpaket** (`eternal_minds/bolagsverket_2026-04-23/`)
   - 7 dokument (ner från 8; 02 ny BO + 06 samtycke ny suppleant togs bort)
   - Per capsulum-format
   - Klart för signering

2. **GDrive-mappstruktur skapad** under CZP Projects_2 (`1CAS46jrj9qsPip9tMYnlxL6otLysoqL7`)
   - `Eternal Minds AB/` (1 15oamkTpcy-dnYTPsgqlCHbNv5Vnw6lVq)
     - Agreements/
     - Meeting Notes/
     - Financials/
     - Deliverables/Bolagsverket 2026-04-23 — Styrelsebyte/

3. **Alla 7 dokument uppladdade som Google Docs:**
   - [00 README](https://docs.google.com/document/d/1mtO8bBaGbcOUmQ2Z1-HtLWYhuljgyuDwRKoKPb6GKPE/edit)
   - [01 Underskrift per capsulum](https://docs.google.com/document/d/1Zg3CIT2hzP3inQlbEXqCKQ1MIgNNS0KMSAxSsgYBcf0/edit)
   - [03 Röstlängd](https://docs.google.com/document/d/1OlaCQQ8oor4wYtBkcWuq_5MSq3T8t5H3NdXlR2Pg8yE/edit)
   - [04 Stämmoprotokoll per capsulum](https://docs.google.com/document/d/1BmvqDYFjFDVc90jq8Ie1mFAnKaPwzRGC33HWcJfWvjM/edit)
   - [05 Konstituerande styrelseprotokoll](https://docs.google.com/document/d/1lZhi2Ks0Ee7UqMjrRbnO6QVqZTYfUgG2CNsA7YIbCd4/edit)
   - [07 Samtycke Robin VD](https://docs.google.com/document/d/17GE_AfqKauGAnJKmRjRxFGIXRpfS_UjWp82Kms50wwE/edit)
   - [08 Ändringsanmälan-instruktion](https://docs.google.com/document/d/1sJpWcyq1fS5MD8mSI2wg3beRa-Ce35_VaKufID7TDfY/edit)

**Blocker:** DocuSeal-integrationen är inte wirad (ingen API-nyckel i secrets_registry eller .env). Nästa steg måste göras manuellt av Robert eller handas till DevOps för VPS-integration.

---

## 2026-04-21 (4am sweep)

**CorpBot verification & next-steps guide:**

1. **Dokumentpaket verifierat** — alla 6 dokument är kompletta:
   - 01_underskrift_per_capsulum.md ✅
   - 03_rostlangd.md ✅
   - 04_stammoprotokoll.md (per capsulum) ✅
   - 05_konstituerande_styrelseprotokoll.md ✅
   - 07_samtycke_robin_vd.md ✅
   - 08_andringsanmalan_instruktion.md ✅

2. **Google Docs mapp verifierad:**
   - Deliverables/Bolagsverket 2026-04-23 (ID: 1eRr48v92fYO8zECRwiwG8ms9wqyTroWF)
   - Alla 6 dokument är uppe och tillgängliga för signering

3. **NÄSTA_STEG_2026-04-21.md skapad:**
   - Tvåvägsväg framåt: Option A (vänta på db-046 för automatiserad signering) eller Option B (manuell PDF-export + DocuSeal manuellt idag)
   - Kompletta instruktioner för båda vägar
   - Signeringskrav listade (9 totala signaturer från Bibbi, Robin, Robert)
   - Tidsplan bekräftad: 16 dagar kvar till deadline 2026-05-07 ✅

**Status:** 🟡 READY FOR SIGNATURES — Väntar på Roberts beslut om signering-path  
**Nästa:** Robert väljer Option A eller B och startar signeringflöde

**Deadline tracker:**
- EGM-beslut fattades: 2026-04-23
- Ändringsanmälan måste ske senast: 2026-05-07 (14 dagar, ABL 8:13)
- Tid kvar: 16 dagar (gott om tid för båda vägarna)

---

---

## 2026-04-22 — 4am Sweep: Signature Path Preparation

**Status:** ✅ Ready for Robert's path choice

**What was done:**

1. **Reviewed ticket state** — Documents complete, 6 Google Docs in GDrive ready, deadline 2026-05-07 (16 days away)
2. **Identified blockers:**
   - Email addresses for signers (Bibbi Wikman, Robin Hofström)
   - Path choice (Option A automated via db-046, or Option B manual via DocuSeal UI)
3. **Sent IPC question** to Robert requesting:
   - Signer email addresses
   - Path preference with reasoning for each option
4. **Created KÖRNINGSPLAN_2026-04-22.md** — detailed run guide with:
   - Option A: Automated (conditional on db-046 API key setup)
   - Option B: Manual (start immediately, 30 min setup + 1-2 days for signing)
   - Step-by-step instructions for both paths
   - Timeline and checkpoints
5. **Updated activity log** on em-001 ticket with IPC question and status

**Key findings:**
- Both paths fit the deadline (2026-05-07)
- Option B can start immediately
- Option A requires Robert to configure DocuSeal credentials (see db-046)
- 9 signatures total needed from 3 signers (Bibbi, Robin, Robert)

**Next step:** Robert reviews ticket, provides signer emails + path choice → CorpBot proceeds with chosen path

**Deadline buffer:** 16 days remaining ✅

---

## 2026-04-23 — Review round launched (Option B path)

**Context:** DocuSeal console API access requires a paid plan, so Robert rerouted from Option A (automated) to Option B (manual DocuSeal UI). Before sending for signatures, Robert wants Bibbi + Robin to review the docs first.

**What was done:**

1. **Shared Deliverables/Bolagsverket 2026-04-23 folder** (ID `1eRr48v92fYO8zECRwiwG8ms9wqyTroWF`) with:
   - bibbi@coldpx.com — commenter
   - hoffa@nethash.se — commenter
   - Google's default "folder shared" notification sent to both
2. **Created Gmail draft** from robert@aurorapunks.com to both (draftId `r-7899553000152317880`, thread `19db9abb591b4cb0`)
   - Swedish, explains each doc's purpose + why Bolagsverket needs it
   - No hard review deadline; asks "så snart ni kan"
   - Robert to review + send

**Status:** 🟡 Awaiting Robert to send the draft → review round opens
**Next step after reviewers OK:** Export 5 signing docs (01, 03, 04, 05, 07) to PDF → upload to DocuSeal UI → invite signers → collect signed PDFs → file via verksamt.se (900 kr)
**Deadline buffer:** 14 days remaining

---

## 2026-04-27 — Reviewer round closed, address fix applied, signing path switched to Drive eSignature

**Reviewer status:**
- ✅ Bibbi (2026-04-24): "Jag tycker att det ser bra ut, skicka ut för signering så vi kan signa idag." — approved
- ✅ Robin (2026-04-23): "Lämnade kommentar om min adress bara annars ser det bra ut!" — approved with one correction (address change)

**Robin's address comment:** Replace `Grindvägen 4 F LGH 1001, 761 62 Norrtälje` → `Roslagsgatan 20B, 761 31 Norrtälje` in [doc 07 Samtycke Robin VD](https://docs.google.com/document/d/17GE_AfqKauGAnJKmRjRxFGIXRpfS_UjWp82Kms50wwE/edit). Address only appears in doc 07 — all other docs reference Robin by name + personnummer only.

**Actions taken:**
1. **Patched doc 07 via Docs API** — `replaceAllText` batchUpdate, 1 occurrence changed. Gdoc URL preserved (no churn for Bibbi/Robin), address now correct. Robin's comment thread left unresolved so Robert can verify and resolve manually.
2. **Synced local source** — `bolagsverket_2026-04-23/07_samtycke_robin_vd.md` updated to match.
3. **Signing path switch: DocuSeal → Drive eSignature.** DocuSeal API is paid; Drive eSignature is free in Workspace Business Standard+ which the AP tenant has. New skill at [[google_drive_esignature]]. The 6 existing Gdocs in [Deliverables/Bolagsverket 2026-04-23](https://drive.google.com/drive/folders/1eRr48v92fYO8zECRwiwG8ms9wqyTroWF) are signable directly via Tools → eSignature in each doc.

**Table-formatting review (per Robert's question):** the existing 6 Gdocs were uploaded 2026-04-20 as raw `.md` (direct conversion), so they have Google's default Arial / symmetric-margins styling — not the canonical legal-doc styling baked into `md-to-docx.sh` (EB Garamond body / Calibri bold headings / asymmetric A4 margins, 1440 left for punch-bind). The only doc with an actual table is [03 Röstlängd](https://docs.google.com/document/d/1OlaCQQ8oor4wYtBkcWuq_5MSq3T8t5H3NdXlR2Pg8yE/edit) — content is correct (6 columns, bold-in-cell preserved, empty summary-row cells preserved), but borders / cell padding are Google defaults not house-style.

**Recommendation: ship as-is for this batch.** Re-rendering via the canonical pipeline would change every Gdoc URL (Bibbi's saved links break) for purely cosmetic gain on docs that will be PDF-exported and uploaded to verksamt.se anyway. Apply canonical styling on the **next** legal pack instead — the new [[contract_workflow]] makes this automatic.

**New CorpBot infrastructure delivered today:**
- `skills/google_drive_esignature.md` — replaces DocuSeal as default signing
- `skills/contract_workflow.md` — 5-step process (request → draft → review → partner round → sign → store) + 3-layer template storage model + external-source recommendations per doc type
- `skills/docuseal_integration.md` — deprecation note added at top
- `agents/admin.md` — tools field updated, Skills-to-Load list refreshed, Contracts & Legal domain rewritten
- `skills/_index.md` — new "Legal & Contracts" cluster
- `eternal_minds/legals/signed/` — local storage convention created

**Next step (Robert):**
1. Open [doc 07](https://docs.google.com/document/d/17GE_AfqKauGAnJKmRjRxFGIXRpfS_UjWp82Kms50wwE/edit), verify the new address, mark Robin's comment resolved.
2. For each of the 5 signing docs (01, 03, 04, 05, 07): Tools → eSignature → add signers (Bibbi `bibbi@coldpx.com`, Robin `hoffa@nethash.se`, you `robert@aurorapunks.com`) → Send. Doc 08 (instruction) doesn't need signing.
3. Once all 9 signatures collected, file via verksamt.se (900 kr) — instructions in [doc 08](https://docs.google.com/document/d/1sJpWcyq1fS5MD8mSI2wg3beRa-Ce35_VaKufID7TDfY/edit). Deadline 2026-05-07 (10 days).

**Deadline buffer:** 10 days remaining ✅

---

## 2026-04-27 (continued) — Bullet→numbered list fix + signature markers pre-placed

**Diagnosis (after Robert flagged "broken tables" on doc 01):** the actual table is structurally fine — 4 cols × 4 rows, all data correct, header + Totalt row bold preserved, empty summary cell intentional. The real broken-formatting issue was different: **numbered lists (`1. 2. 3.` in source markdown) rendered as plain bullets** after the 2026-04-20 direct .md → Gdoc upload. Root cause: `gdrive-upload.js --convert` on .md does not preserve list-style metadata; only the `md-to-docx.sh` pipeline (md → docx → Gdoc) carries numbered-list semantics through.

**Patches applied via Docs API `batchUpdate` (no Gdoc URL churn):**

| Doc | Bullet→number ranges | Signature markers inserted |
|-----|----------------------|----------------------------|
| 01 | 274–559 (Vi bekräftar att, 3 items), 593–995 (Ärenden, 5 items) | `{{SIG: Bibbi Wikman}}` @ 1343, `{{SIG: Robin Hofström}}` @ 1358 |
| 03 | (no list issues) | `{{SIG: Bibbi Wikman}}` @ 549, `{{SIG: Robin Hofström}}` @ 564 |
| 04 | (no list issues — source used `-` bullets) | `{{SIG: Bibbi Wikman}}` @ 2546, `{{SIG: Robin Hofström}}` @ 2588 |
| 05 | 828–1053 (§3 Firmateckning, 2 items) | `{{SIG: Robin Hofström}}` @ 1432, `{{SIG: Robert Bäckström}}` @ 1528 |
| 07 | (no list issues) | `{{SIG: Robin Hofström}}` @ 508 |

Method: `deleteParagraphBullets` + `createParagraphBullets {bulletPreset: NUMBERED_DECIMAL_NESTED}` over each range. `insertText {{SIG: <Name>}}\n` for each marker, sent in **descending position order** so each insert's index references original (pre-shift) positions. All 15 requests across 5 docs applied successfully on first try.

**Robert's eSignature workflow (now ~30 sec/doc instead of guessing where to drop fields):**

For each doc:
1. Open doc → Tools → eSignature → Request signature
2. Add signers (see signer matrix below)
3. The sidebar shows "Signature, Date, Initials, Text" fields. Drag the Signature field onto the `{{SIG: <Name>}}` placeholder line for each signer.
4. Optional: select the placeholder text and delete it (1 keystroke) — keeps the final signed PDF clean.
5. Click Send.

**Signer matrix:**

| Doc | Signers |
|-----|---------|
| 01 Underskrift per capsulum | Bibbi Wikman `bibbi@coldpx.com`, Robin Hofström `hoffa@nethash.se` |
| 03 Röstlängd | Bibbi `bibbi@coldpx.com`, Robin `hoffa@nethash.se` |
| 04 Stämmoprotokoll | Bibbi `bibbi@coldpx.com`, Robin `hoffa@nethash.se` |
| 05 Konstituerande styrelseprotokoll | Robin `hoffa@nethash.se`, Robert `robert@aurorapunks.com` |
| 07 Samtycke Robin VD | Robin only `hoffa@nethash.se` |

Total: 9 signatures across 5 docs. Doc 08 (verksamt.se instruction) is internal, no signature needed.

**Local .md sync:** address fix on doc 07 source already in sync. The `{{SIG: ...}}` markers are intentionally **not** added to the local .md — they're eSignature wizard placement cues that Robert deletes post-placement, not part of the source-of-truth content.

---

## 2026-04-27 (third pass) — Table column widths fixed (the actual "broken table")

**Diagnosis correction:** Robert's "broken tables" complaint was real — I missed it on the first review pass because the markdown export of doc 01 looked fine. The screenshots Robert shared showed every character in the Aktieägare table wrapping to its own line. Root cause: the `.md → Gdoc` upload set `widthType: EVENLY_DISTRIBUTED` with `width: undefined` on every column. In Drive's renderer and the eSignature/PDF preview that's interpreted as "fit to minimum content width" → each cell collapses to ~1 char wide.

**Fix via Docs API `updateTableColumnProperties` (no URL churn):**

| Doc | Table | Column widths set (FIXED_WIDTH, total ≤ 465pt for Letter usable) |
|---|---|---|
| 01 | Aktieägare (4 cols) | Namn 180, Personnummer 100, Antal aktier 95, Andel 90 |
| 03 | Röstlängd (6 cols) | Nr 25, Namn 175, Personnummer 85, Antal aktier 60, Antal röster 60, Andel av röster 60 |

Verified post-patch: all 10 columns now have explicit `FIXED_WIDTH` magnitudes. Reload the docs in browser to see the corrected layout.

**This is the third silent failure mode of `gdrive-upload.js --convert` on raw .md files** (same root cause family as the styling loss and numbered-list demotion patched earlier today). The combined evidence is now strong enough to make a hard rule: **never upload legal docs as raw `.md --convert` — always go through `md-to-docx.sh` first.** The intermediate .docx carries canonical styling, numbered-list semantics, AND explicit column widths through the conversion. Captured in [admin_learnings.md](../agents/memory/admin_learnings.md).

---

## 2026-04-27 (final pass) — Pipeline regen, new Gdoc set with canonical styling

**Why:** Even after the FIXED_WIDTH patch was applied via Docs API, Drive's renderer still showed the doc 01 table with characters wrapping per line (Robert flagged with screenshot). The Docs API confirmed the values were stored (180/100/95/90 PT) but visually they weren't being honored — likely a rendering quirk on docs that originated as raw `.md --convert` uploads. Surgical patches reach a point of diminishing returns; the right fix is to regenerate from source through the canonical pipeline.

**What was done:**
1. **Renamed all 7 existing Gdocs** with `[v1 2026-04-20] ` prefix (preserves Bibbi/Robin's existing comment threads + audit trail; sorts below new versions alphabetically)
2. **Ran `md-to-docx.sh` on all 7 source `.md` files** → `.docx` with canonical legal styling baked in (A4 portrait 595×842 PT, asymmetric margins L=72/R=54 PT, EB Garamond body 11pt, Calibri bold headings)
3. **Uploaded new `.docx` to the Deliverables folder** with `--convert` flag → 7 new native Gdocs
4. **Reallocated table column widths** on docs 01 + 03 via Docs API to fit the longest expected content per column (rather than html-to-docx's default evenly-distributed)
5. **Inserted `{{SIG: <Name>}}` markers** above each signer's name across all 5 signing docs

**New Gdoc set (canonical styling):**

| # | Name | Link | Tables | Sig markers |
|---|------|------|--------|-------------|
| 00 | README | https://docs.google.com/document/d/1esrulIWrf0oBE9O_XEDQ9pEqMrRccj3AXR23V_ZVvZE/edit | — | n/a |
| 01 | Underskrift per capsulum | https://docs.google.com/document/d/1jan4naTK4V_8mQVbCkhxLMJfRmr4mDSZgIogI7O24DI/edit | 195/90/90/90 PT | Bibbi @ 1343, Robin @ 1356 |
| 03 | Röstlängd | https://docs.google.com/document/d/1UtkmzUcAVbB4HeruA0DPrDmuFDEK2cq_fdpobd0_yb8/edit | 25/175/80/60/60/65 PT | Bibbi @ 549, Robin @ 562 |
| 04 | Stämmoprotokoll per capsulum | https://docs.google.com/document/d/1W-7MD5pqteIg3y7CWMFjZNSn6KgmeU-1p59I5UgD1FA/edit | — | Bibbi @ 2541, Robin @ 2581 |
| 05 | Konstituerande styrelseprotokoll | https://docs.google.com/document/d/1PfTCn5Ok8l1l09fIZKLRxCCS20eZTNptGNb1NVs-QKA/edit | — | Robin @ 1429, Robert @ 1523 |
| 07 | Samtycke Robin VD | https://docs.google.com/document/d/1hYcOYIFHe9Iy4PL8eNrtYYFPqxqO5OOHaRbtN4IECXM/edit | — | Robin @ 505 |
| 08 | Ändringsanmälan-instruktion | https://docs.google.com/document/d/1-zaQDTOZlH8IdR2cZrh72QdKFqRmmqCUPY-B04cPoAA/edit | — | n/a (instruction sheet) |

**Total markers placed:** 9 (Bibbi 3× + Robin 4× + Robert 2×) across 5 signing docs.

**Folder share:** [Deliverables/Bolagsverket 2026-04-23](https://drive.google.com/drive/folders/1eRr48v92fYO8zECRwiwG8ms9wqyTroWF) — Bibbi `bibbi@coldpx.com` and Robin `hoffa@nethash.se` already have commenter access at folder level, so they automatically see the new docs without re-share. The `[v1 2026-04-20]` versions remain in the same folder for their reference.

**Robert's eSignature flow per doc (~30 sec each, 5 docs):**
1. Open the new doc → **Tools → eSignature → Request signature**
2. Add signers from the matrix above
3. Drag the signature field onto each `{{SIG: <Name>}}` placeholder line
4. Optional: select the placeholder line, Backspace to keep the signed PDF clean
5. Send

**Pipeline observations (filed to admin_learnings):**
- HRs from the source `.md` (`___________________________` lines that markdown converts to `<hr>`) get dropped during html-to-docx conversion — the new docs no longer have the visible thin signature line above each name. Mitigation: the `{{SIG: <Name>}}` marker serves as the placement cue. For purely visual signature lines on printed copies, would need to switch from `___...` source to literal underscore strings escaped from markdown HR conversion.
- Markdown blockquotes (`> Notering: ...`) survive but lose the left-border styling through html-to-docx — render as plain indented text. Acceptable for this pack.
- Table column widths via html-to-docx default to evenly-distributed FIXED_WIDTH (page-usable / N cols). Post-fix via `updateTableColumnProperties` is the right pattern when content needs uneven distribution.

---

## 2026-04-28 — Format-pivot: per capsulum → digital stämma + Monowo AB-fix i röstlängden

**Trigger:** Robert flaggade två materiella fel efter v2-rundan:
1. **Verksamt accepterar inte per capsulam för komplexa frågor från 2025** — styrelse-/VD-byten kräver digital eller fysisk stämma. Hela paketet behövde retroanpassas till digital stämma (Google Meet-mötet 2026-04-23 17.00–18.00 där beslutet faktiskt diskuterades).
2. **Aktieägaren är Monowo AB, inte Bibbi Wikman privat.** Bibbi är ensam ägare och firmatecknare för Monowo AB (org.nr 559207-4933) och företräder bolaget i kraft av firmateckningsrätten — ingen separat fullmakt erfordras.

**Bedömning per doc:**
- 01 (per capsulum-underskrift) → **förkastas**, ersätts inte (digital stämma har inget motsvarande dokument)
- 03 (röstlängd) → **ny v3** med Monowo AB + digital format
- 04 (stämmoprotokoll) → **ny v3** som digital stämma med ordförande/sekr/just
- 05 (konstituerande styrelseprotokoll) → **ny v3** för konsistens (rad 6 + rad 9 hänvisade till per capsulam-stämma)
- 07 (samtycke Robin VD) → **orörd**, format-neutral
- 08 (instruktion) → **uppdaterad** för att referera till nya bilageuppsättningen

**Mötesdetaljer (bekräftat av Robert):**
- Tid: 2026-04-23, 17.00–18.00
- Plattform: Google Meet
- Ordförande: Johan Robert Bäckström (suppleant)
- Sekreterare: Robin Chris Tommy Hofström
- Justerare: Bibbi Wikman
- Robert närvarade som suppleant + valdes till mötets ordförande

**Nya Gdocs (v3 digital 2026-04-28) i [Deliverables/Bolagsverket 2026-04-23](https://drive.google.com/drive/folders/1eRr48v92fYO8zECRwiwG8ms9wqyTroWF):**

| # | Namn | Länk | Signers | SIG-markörer |
|---|------|------|---------|--------------|
| 03 | Röstlängd Monowo AB | [öppna](https://docs.google.com/document/d/1LL8vKTKL1UT72SLgZ2bAlLorOdfjnCC_Z4vnqDoksRU/edit) | Robert (ord), Bibbi (just) | 2 |
| 04 | Stämmoprotokoll digital stämma | [öppna](https://docs.google.com/document/d/1HFpL0uOKg62HdF4oxj7YvaX55nSgjgVFY4f_A75TTBc/edit) | Robert (ord), Robin (sekr), Bibbi (just) | 3 |
| 05 | Konstituerande styrelseprotokoll | [öppna](https://docs.google.com/document/d/1GS0E57wUQM3k4qIaW65Pkf8saJf_lE_gqu-2Iku_kbQ/edit) | Robin (led/VD), Robert (suppl) | 2 |
| 08 | Ändringsanmälan-instruktion (v2) | [öppna](https://docs.google.com/document/d/16BmzQNNXg1-pGJD-1YADKuAaX976c0B1XlorfRuIA88/edit) | n/a | n/a |

**Totalt nya signaturer:** 7 (ner från 9 i v2-paketet — 01 utgår, plus signers fördelas på 3 funktionsroller istället för aktieägare)

**Pipeline:** md-to-docx.sh på alla 4 källfiler → docx → upload med `--convert` → docs.batchUpdate `insertText` för SIG-markörer (anchors korrigerade efter att html-to-docx slog ihop "Namn\nRoll" till "Namn Roll" på samma rad).

**v2 (per capsulum) Gdocs lämnas orörda i samma mapp** — de är signerade men obsoleta. Inte renamed för att inte bryta Bibbi/Robins existerande länkar/bookmarks. Den nya `[v3 digital 2026-04-28]`-prefixen gör det visuellt tydligt vilka som är aktiva.

**Lärdom sparad:** [feedback_verksamt_per_capsulam.md](../../.claude/projects/-home-assistant-projects/memory/feedback_verksamt_per_capsulam.md) — Bolagsverket/verksamt accepterar inte per capsulam för styrelse-/VD-byten från 2025. Defaulta till digital stämma framöver.

**Robert's eSignature-flow (per doc, ~30 sek):**
1. Öppna doc → Tools → eSignature → Request signature
2. Lägg till signers per matrix ovan (bibbi@coldpx.com, hoffa@nethash.se, robert@aurorapunks.com)
3. Drag signaturfältet på `{{SIG: <Namn>}}`-markören för varje signer
4. Send

**Deadline:** 2026-05-07 — 9 dagar kvar ✅
