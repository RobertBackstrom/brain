---
name: reference_infra_billing_entity
description: "All infra/SaaS subscriptions are billed to CZP via the Pleo card, even when labelled 'Runatyr'; CZP's registered address per Bolagsverket 2026-02-04."
metadata: 
  node_type: memory
  type: reference
  originSessionId: fe4d2437-91da-445c-9e48-b2b0e08a9aad
  modified: 2026-07-23T08:29:11.509Z
---

**All infrastructure and SaaS subscriptions belong to and are paid by Creation Zero Point Holding AB (CZP)** - confirmed by Robert 2026-07-23. This holds even where the secrets registry or a vendor account labels something "Runatyr Infra": that label is organisational shorthand, not the paying entity. Payment instrument is the **Pleo expense card + Pleo account** (see `assistant/pleo-login.js`).

Robert has flagged that infra *may* move to Runatyr or Aurora Punks later, but as of 2026-07-23 nothing has moved. Until he says otherwise, any vendor account, invoice address, VAT field, or new subscription defaults to CZP.

**Canonical CZP billing details** (Bolagsverket registreringsbevis, ärende 67465/2026, created 2026-02-04 - that ärende was specifically a *postadress* change, so it supersedes older records):

- Företagsnamn: **Creation Zero Point Holding AB**
- Org.nr: **559182-7471**
- VAT: **SE559182747101**
- Postadress: **c/o NeCo Software, Brännkurkogatan 10b, 118 20 Stockholm, Sweden**
- Säte: Stockholms län, Stockholm kommun

**Two stale addresses are still circulating - do not use either:**
1. `Timmermansgatan 43, 118 55 Stockholm` - that is Aurora Punks' address, and it appears on a Nov 2024 CZP invoice-details mail by mistake.
2. `c/o Robert Bäckström, Lästringevägen 10, 125 43 Älvsjö` - CZP's *previous* postadress. It is still on Fortnox invoice headers as recently as 2026-06-03, so **Fortnox has not been updated** and outgoing CZP invoices are carrying a stale address. Worth a CorpBot pass.

Note the org register also lists Lästringevägen 10 as Robert's *personal* styrelseledamot address - that is correct there and should not be "fixed".

Related: [[reference_company_structure]], [[reference_secrets_registry]] equivalents, [[project_czp_finances]].
