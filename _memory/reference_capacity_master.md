---
name: reference-capacity-master
description: "VPS-native capacity/allocation tracker - who on the AP dev pool is assignable when (person x project x month x %), with a heatmap that flags over-allocation"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c28d5302-c7a3-4180-aa75-742e4450ada9
---

# Capacity Master (team allocation tracker)

Canonical answer to **"who can we assign, and when."** Lives at `assistant/capacity/`.
Tracks the AP assignable dev pool (not client teams) as **person x project x month x %-allocation**.

- **Edit** `assistant/capacity/allocations.json`, then run `node assistant/capacity/render.js`.
- Outputs `capacity.html` (visual heatmap + conflicts) and `CAPACITY.md` (RAG-indexed summary).
- Query current allocations via `rag_search` on `CAPACITY.md`, or read it directly.

**Update protocol (do this, don't let it rot):**
- **BizDev:** quoting a deal that names people -> add `confidence: "proposed"` entries. Deal won/lost -> promote to `high` or delete.
- **PM:** sprint/milestone changes who is on what -> update the `active` entries.
- **CorpBot/Lawyer:** a subcontractor contract that fixes an FTE = a `high`-confidence entry (contractually committed).

**Known standing conflicts (2026-07, if Teef wins):**
- **Oskar Hansen is the biggest Teef chokepoint** - already 100% (K2C 80% / 4 days + WMY 20% / 1 day), so the Teef platform/UI seat puts him at 200% Oct-Nov. Likely replace him on Teef with **Petter or Basil**.
- **Fredrik Laurent** contracted 80% to K2C through Dec 31 (Ark Island) + proposed Teef TL 100% = 180% Oct-Nov, but K2C is fixed-fee and Robert expects Fredrik to have **more leeway from October**, so this may soften. Teef timeline is flexible, which absorbs it.
- **Robert** is chronically >100% (K2C 70 + BADASS 20 + Hooja/ToA oversight + Teef 50). Hooja + ToA are AI-built (Fable 5), costing Robert's oversight time, not a human dev seat.

Home decided VPS-native over Jira (internal-vs-client convention, agent-queryable, durable) - Robert 2026-07-15. Death Board UI wiring is a DevOps follow-up. Related: [[project_k2c_sands_of_duat]], [[project_teef]] (if present), [[reference_rate_card]], [[feedback_devops_tooling]].
