---
name: project_receipt_intake
description: "Kvitto-intake pipeline - one Drive folder Robert scans into from the phone, routed by card to Pleo/CZP/Runatyr/AP/Zenland bokföringsunderlag."
metadata: 
  node_type: memory
  type: project
  originSessionId: 709cbf46-cdbe-46d0-bdf0-723ca00fe35b
  modified: 2026-07-21T15:18:50.374Z
---

Built 2026-07-21 (db-279). Replaces the old `CZP_Expenses` + Runatyr expense drop folders,
both left in place as read-only legacy.

**Intake (bookmarked on Robert's phone):** `Kvitton_Inbox` `1xPRfNjgz9wQHEkdxWzpOwlREn4LJFYbJ`
in Robert's My Drive. Root = auto-classify; `PLEO/ CZP/ RUNATYR/ AP/ ZENLAND/` = explicit
override; `_needs_review/` = parked + Discord ping; `_processed/` = Pleo audit trail.

**Routing rule: the card on the receipt decides the entity.** Unrecognised card is never
guessed - it goes to review. Cadence per company: **CZP monthly, Runatyr quarterly, AP AB
quarterly, Zenland yearly (broken FY, ends 30 Jun)**. The period folder comes from the
purchase date, not the upload date.

Mail receipts run the same classifier (`mail-receipt-router.js`) - digital purchases are
**not** automatically Pleo, which is what the pre-2026-07-21 routine wrongly assumed.
Unclassifiable mail is left in the inbox, never archived.

Config is `assistant/receipt-routing.json` - edit that, not the code. Full doc in the
[[receipt_intake]] skill; build details and gotchas in devops learnings.

**Kortkartan (kanonisk - CorpBot behöver den vid avstämning):**

| Kort | Bolag |
|---|---|
| MasterCard **8786** | Pleo-kort, CZP |
| MasterCard **0844** | Pleo-kort, CZP (kontaktlöst) |
| MasterCard **6920** | Runatyr företagskort, SEB Commercial Debit |
| VISA **3081** | Robert privat - kan avse **vilket bolag som helst**, avgörs alltid manuellt |

VISA 3081 är mappad till sentinel-värdet `"review"`, inte utelämnad: kortet är känt men kan
aldrig ensamt avgöra bolag, så pingen frågar "vilket bolag ska det bokas mot?" istället för att
rapportera ett okänt kort som behöver konfigureras.

**Praktisk begränsning (skärpt 2026-07-24 efter skarpt test):** på **fotade papperskvitton**
läses kortet ofta inte alls, och när det läses är avläsningen icke-deterministisk - samma
Coop-foto gav `0844` i en körning och `null` i nästa, med belopp som också drev (378 / 378,09 /
378,89). Kortkartan bär alltså **PDF- och mailkvitton**; för papper är det override-mapparna och
periodavstämningen som gäller.

`receipt-reconcile.js` matchar därför på **beloppsintervall**, inte exakt belopp: minst 1,00 kr,
0,5 % på större belopp, tak 50 kr. Siffermissläsning faller utanför med flit, och två kandidater
i samma fönster rapporteras som tvetydiga i stället för att en väljs.

**Pleo dedupar inkommande kvitton själv** (Robert 2026-07-24). Ett kvitto som råkar
vidarebefordras två gånger till `forward@fetch.pleo.io` skapar alltså inget dubbelutlägg och
kräver ingen städning - jaga inte en dubblett som inte finns. Gäller **bara** Pleo-grenen:
en dubbelkörning mot Drive-grenarna skapar riktiga dubbletter i bokföringsunderlaget, där
inget dedupar. Båda routrarna har PID-lås sedan 2026-07-24.
