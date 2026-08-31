---
project: kng
status: open
priority: high
updated: 2026-08-31
created: 2026-08-31
type: task
owner: DevOps
---

## Connect Robert's Dropbox to the VPS (Fatshark art-direction archive)

Robert chose "give the VPS Dropbox access" (2026-08-31) so the ArtDirector agent can learn art
direction from the old **Fatshark art-direction docs** held there. Confirmed on 2026-08-31 that
there are **no Fatshark art docs on Drive**: the `Fatshark` folder on the Projects shared drive
(`1yHsHOWT43IlgG_LPM1qM_71rSRXRw1k1`) contains only `Legal/Service Agreement_WLBS_Final.pdf`.
Dropbox is the only known source.

**Why durable, not per-session:** per [[feedback_long_term_solutions]] this should be a
VPS-hosted connector with a refresh token in the VPS env, indexed into RAG like gdrive, not a
one-off link fetch. Mirrors the gdrive setup in [[reference_gdrive_service_account]].

**Blocked on:** the OAuth consent flow needs an interactive session. Cannot be completed from a
non-interactive run.

**Definition of done:**
1. Dropbox OAuth app registered, refresh token in VPS env, documented in the secrets registry.
2. Read access verified against the Fatshark art-direction folder.
3. Folder added to the RAG indexer so `rag_search(source=...)` reaches it.
4. Reference memory written so the next agent does not re-derive the setup.

Once live, the docs feed `skills/art_direction_critique.md` section 5 (currently the largest
known gap in the grimdark reference corpus).
