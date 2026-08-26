---
name: Aurora Punks
description: AP AB (559256-9718) governance, cap table, board, investor relations — CorpBot-owned
type: project
originSessionId: e7068c11-9a0a-46d5-88dd-e538820e2ade
modified: 2026-08-04T19:45:03.407Z
---
# Aurora Punks AB

- **Prefix:** `apb` (AP Board)
- **Folder:** `/home/assistant/projects/aurora_punks/`
- **Agent owner:** CorpBot
- **Company narrative / pitch history (2019→now, verticals, portfolio, IP slate, team, the raise):** `aurora_punks/ap_history_dossier.md` — built 2026-06-22 by reading the AP pitch decks directly (Corporate 2025, Portfolio Master, Back Catalog). Use it for "what is AP / what have we done" context; this memory stays governance/cap-table only.
- **Entity:** Aurora Punks AB, org nr 559256-9718 (NOT the bankrupt Development Services AB)
- **Epic ticket:** `apb-000-epic` (AP Board governance, board members, P&L sheets)
- **AP P&L ticket:** `apb-002-pnl` (board P&L 2026, includes K2C IC; folded apb-001 + former czp-000 P&L scope on 2026-04-29)

## Board (5 ledamöter, korrigerat 2026-05-03)
- Mattias Wiking (ordf) — mattias@mattiaswiking.com
- Alexander Bergendahl — alexander@lootlocker.com
- Andreea Chifu — andreeachifu@gmail.com (preferred, för signering/kontakt; tidigare andreea@aurorapunks.com) (avgick som VD under 2025, kvar i styrelsen)
- Karl-Magnus Troedsson — km@behold.vc
- Robert Bäckström — robert@aurorapunks.com (inofficiell ställföreträdande VD efter Andreeas VD-avgång)
- **Firmateckning:** två i förening (förslagsvis Mattias + Robert)
- **Konkursförvaltare APDS:** Nils Åberg på Carler (Ulrika Mattsson handläggare)

## Cap table (fully diluted, post WISE 2, 2024-06-13)
Total 396 173 shares. Top holders:
- Behold Ventures 0 AB: 32,26%
- Creation Zero Point Holding AB (Robert): 30,14%
- Alexander Bergendahl: 12,07%
- Loot Spawn AB: 11,39%
- Remaining 14,14% across 7 smaller holders

### Konto 1350, AP:s innehav i ANDRA bolag (kanonisk källa)
Sheet **"Aurora Punks AB - Aktieinnehav"** (`10mAz2jYAYBYh1DhfbYDivSpNP4hZMHTNjtM3FL_jbfk`) är registret över vad AP äger i andra bolag, med årsvisa saldon 2020-2025 och SHA-länk per rad: Upstream Arcade (15 %), LootLocker (avyttrat 2023), Runatyr, Red Marmoset (15 %), Eddaheim-konvertibler (löpte ut), Northify, No89 (sålt 2025-04-24). Revisorn efterfrågar den här vid varje bokslut, och frågan "dokumentation som styrker konto 1350" gäller **detta**, inte AP:s egen aktiebok. **Obs avstämningsglapp:** saldo 2024-12-31 2 972 945 kr minus enda 2025-rörelsen −999 267 kr ger 1 973 678 kr, men liggaren anger 0 kr per 2025-12-31, trolig omklassning till 1310/1315 som aldrig skrevs in. Stäm av med Amer före leverans till revisorn.

## Key external contacts
- **Marc Harris** — Dangoor Associates, corporate legal, holds authoritative cap table xlsx
- **Karl Magnus Troedsson (KM)** — Behold Ventures, largest external shareholder
- **Magnus Kenneby** — Behold finance, source of transaction queries
- **Amer Alsalek** — Book It AB, amer@book-it.se — redovisning/bokslut för AP (tog över från Sifferrådet juni 2026; Henrik Franzén/Sifferrådet gör CZP, inte AP). Se [[reference_entity_accountants]]
- **Jacob Biderholt** — Parameter Revision AB, auktoriserad revisor, signerar revisionsberättelsen
- **Christine Lef** — Parameter Revision, gör själva granskningen under Jacob

## Cap table model conventions (from Marc's xlsx 2024-06-18)
- EV = pre-money throughout (verified: 45M EV / 294 709 pre-shares = 152 SEK/share)
- No anti-dilution or liq pref in the base model (must be verified against actual AA/WISE agreements if triggered)
- WISE 2 converted 2024-07-01 at floor EV 40M (Behold +46 101 shares)
- Authoritative xlsx: `uploads/Calculations AP Issuances and Conversions (2024-05-20 - additional discount version).xlsx`

## Steam storefront entity (2026-08-04)
The back catalogue's **Steamworks partner account is CZP, not AP AB and not APDS**. 18 appids (Block'Em!, Chenso Club, IRON EVIL, Ooglians, JETZNAB, Aurora, Innsmouth, Robot Lord Rising, Massive Attax, 1993 Space Machine + their demos/soundtracks) transferred APDS 301411 → **Creation Zero Point Holding AB 418393, effective 1 July 2026**; both parties agreed 2026-08-04, pending Valve's final approval. Tears of Adria (2561500) deliberately excluded. Full appid table + exclusions: `aurora_punks/ap_ip_ownership_canonical.md` §H. Ticket `apb-026`. Storefront ownership ≠ IP ownership — check both before answering an ownership question.

## Intercompany-reverser CZP → AP, 2026 (kanoniskt register)

Två separata kortfristiga, ovillkorade, räntefria aktieägarlån från Creation Zero Point Holding AB
(559182-7471) till Aurora Punks AB under 2026, samma upplägg per Amers rekommendation: ovillkorat
aktieägarlån, kort återbetalningstid, tydligt åtskilt från kapitaltillskott, avräknas mot
CZP↔AP-regleringen, bortre gräns **2026-12-31**. De ersätter INTE varandra — **100 000 SEK
sammanlagt** i utestående kortfristiga CZP→AP-lån per 2026-08-20. Robert signerar för CZP
(långivare); Wiking + KM två i förening för AP (Robert står ej på AP:s rad, ABL 8:23 jäv).

| Datum | Belopp | Syfte | OpenSign docId | Status (2026-08-20) | Ticket |
|---|---|---|---|---|---|
| 2026-07-06 | 50 000 SEK | AP:s löpande utgifter + en advokatkostnad | `1PgufGehIP` | Fullt signerad 2026-07-08, PDF arkiverad i AP:s Financial SD | `apb-031` |
| 2026-08-19 | 50 000 SEK | AP:s löpande utgifter + revisorskostnader | `AfWbAMb1nY` | Fullt signerad + arkiverad 2026-08-20 08:15 (samma Drive-mapp som julireversen, fil `1D4nxQq3dG3TB8OOi6UXcCsqGm-RGKp5J`) | `apb-047` |

Ett tidigare augustidokument (`XKRCivr0QV`, daterat 2026-08-18) voidades 2026-08-19 och ersattes av
`AfWbAMb1nY` efter en revidering av punkt 4-5 i reversen — ingen motpart avvisade, trots att
notismailet såg ut som en avvisning ("A signer DECLINED"); `voidDocument()` sätter samma flagga som
en riktig avvisning i OpenSign.

**Skiljs från:** det större ägarlånet på ca 1,25M SEK som ersatte Almi-lånet — separat facilitet,
se [[project_ap_ek_2025_almi_agarlan]]. Blanda inte ihop beloppen vid nästa bokslutsfråga.

## Ägarlån och reverser, status per revisionen 2026-08 (apb-052)

- **Deko Du AB**, org.nr 559096-5033, **200 000 kr, 0 % ränta**, revers undertecknad 2022-10-20 med
  slutbetalning senast 2023-10-20 (DocuSign, envelope 8F04C56E-E170-4C41-B9C7-5CE9AC17D1E3), signerad
  av **Andreea Chifu** för Deko Du och Robert för AP. **Fortfarande utestående.** Förfallodagen har
  passerat utan att någon skriftlig förlängning upprättats. Det är det enda ägarlånet från 2025 och
  tidigare som INTE omvandlades till equity. Närståendetransaktion, så den behöver upplysning.
  Handlingen ligger som `Revers_DekoDu_AB_200000kr_2022-10-20.pdf` i revisionsmappen. En äldre revers
  på 300 000 kr med förfall 2022-05-31 finns också i Drive, den föregår denna.
- **Loot Spawn AB** (Karl Magnus Troedsson), **50 000 kr, 2 % ränta**, revers 2025-11-11 på sex månader.
  **Reglerad inom 2025:** inbetald till AP 2025-11-17, återbetald 2025-12-05. Filen låg länge felnamngiven
  som DekoDu-reversen i revisionsmappen, heter nu `Revers_LootSpawn_AB_50000kr_2025-11-11.pdf`.
- Under november 2025 togs även kortfristiga lån från Deko Du (15 000) och Wiking Development (10 000)
  in, båda återbetalda 2025-12-05.

Revisionsmappen: `Aurora Punks Board/_deliverables_working`
`1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh`, se [[reference_drive_folders]].

## Notable open items
- Cap table above is the 2024 snapshot. Authoritative group ownership map (incl. AP's 15% stakes in Red Marmoset + Upstream Arcade, not reflected here): [[reference_company_structure]] / `wiki/company/structure_ownership.md`. Minority-holdings audit + cap-table refresh tracked in `apb-011`.
- Bolago shareholder register may need sync with Marc's latest cap table (2024 AGM thread noted this was hard to update)
- WISE 2 exact principal not explicit in xlsx; estimated 5,27M SEK from 40M floor convention — confirm with Marc if needed for precise investor IRR reporting
- AP VAT registration status (see db-045) — may affect invoicing structure
