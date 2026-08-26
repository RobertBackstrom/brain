---
name: reference_entity_accountants
description: Which accounting firm handles books/payroll for each entity (CZP / AP / Runatyr)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 058f5b43-a6d6-4719-a71b-69523693a75d
---

Per-entity accountants (who to mail for bokföring / lön / bokslut):

- **Creation Zero Point Holding AB (CZP)** → **Sifferrådet** — Henrik Franzén, **henrik@sifferradet.se** (shared inbox, also staffed by Frida Swan / Caroline Eriksson; `hej@sifferradet.se` is a second shared inbox; tel 08-124 515 72). Colleague: **Emelie Andersson**, **hej@sifferradet.se** (spelled Emelie, not "Emilie") — she is the one who sends **lönebesked** to employees, so hand her the employee's email address as soon as someone is set up. Confirmed 2026-07-24 in the Carolina thread; Henrik also replies from the `hej@` inbox, so either address reaches both. **Payroll workflow:** Sifferrådet creates + attests the lön in Fortnox, then **Robert sends the payment to the bank (SEB)** himself — they do not pay out.
- **Aurora Punks AB (AP)** → **Amer Alsalek**, **amer@book-it.se** (bokslut / accounting).
- **Runatyr AB (559204-0728)** → **Amer Alsalek**, **amer@book-it.se** — samma person som gör AP:s
  bokslut. Stavas **Amer**, inte "Ameer": äldre noteringar hade båda stavningarna och antydde två
  olika personer. Det är en. Bekräftat 2026-07-17 (han gör Runatyrs ÅR 2025, `run-013`). Han har egen
  **SEB-access** och kollar Skatteverket själv. Bokföringen ligger i **Bokio** (2025/26) + Fortnox
  (tidigare år); Bokio kräver BankID → Robert exporterar. Se [[project_runatyr]].
- **Zenland Games AB** → **no external accountant. CorpBot is the in-house bookkeeping assistant** (Robert's directive 2026-07-08). To actually run it, CorpBot needs Zenland's basics: org.nr, Fortnox access (per [[reference_fortnox_access]]), bank, and where source receipts/invoices land in Drive. Zenland is its own company unit in the Drive restructure (db-256).

Do NOT conflate Amer (AP/Runatyr) with Sifferrådet (CZP). Amer och "Ameer" är samma person. Correction logged 2026-06-24 (earlier notes wrongly said Amer ran CZP payroll). First use: setting up Carolina Foghammar Nömtak's CZP visstid payroll, see [[project_k2c_sands_of_duat]].

## Revisorer (skild från redovisning ovan)

- **Aurora Punks AB (AP)** → **Parameter Revision AB** ("En del av Cedra", Sankt Eriksgatan 63B, Stockholm). **Jacob Biderholt** (auktoriserad revisor, jacob.biderholt@parameterrevision.se, 070-40 30 443) signerar revisionsberättelsen; **Christine Lef** (christine.lef@parameterrevision.se) gör granskningen med revisorsinlogg i Fortnox. Blanda INTE ihop revision (Parameter) med redovisning/bokslut (Amer, Book It). Etablerat 2026-07-15, se [[reference_vessels_of_decay]].
