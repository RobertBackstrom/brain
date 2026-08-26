---
name: K2C epic/sprint structure convention
description: K2C Jira breakdown conventions — separate shapes for FEATURE epics and CAMPAIGN island epics
type: project
originSessionId: fa2f1009-25a5-4f75-a000-2c6fd10ad031
modified: 2026-08-02T11:09:18.457Z
---
K2C uses two distinct epic shapes depending on whether the work is a discrete feature or a campaign island.

## Shape A — FEATURE epics (Banner, Apesh, STG, Demolisher, Monarch rework)

- **Pre-prod design task** → labelled `pre-prod-design`, placed in the current sprint column ("To Do This Sprint")
- **Prod-design / art / code tasks** → sibling Tasks under the epic (NOT subtasks of pre-prod), labelled `prod-design` / `art` / `code`, live in BACKLOG until pre-prod design clears
- Plus the four Sprint A prototype tickets (KAN-281 STG, KAN-282 Banner, KAN-283 Visual benchmark, KAN-284 Build pipeline) that prove the feature in-engine before MS1

**Why:** Robert wants design visibly gated — pre-prod design must complete before the prod/art/code chain begins. Putting pre-prod in-sprint and the rest in BACKLOG makes the dependency visible on the board and prevents art/code from starting before design lock.

## Shape B — CAMPAIGN island epics (KAN-5..11, Islands A..G)

Each island epic has FIVE child tasks with consistent owners and labels:

| Subtask | Owner | fixVersion | Notes |
|---|---|---|---|
| Design spec (pre-prod) | Tim | MS1 | Lives under island for traceability but delivers as part of pre-prod (MS1) |
| Level Scripting | Tim | parent epic's MS | Implement design in engine, first pass of balancing, ensure island plays end-to-end |
| Feature implementation (needed) | Fredrik | parent epic's MS | Features the island NEEDS to function (banner system, branching save, mounts already in play) |
| Feature unlocks | Fredrik | parent epic's MS | Features the island UNLOCKS (mount, divine item, hermit, statue, tech tier) — preferably delivered with island, can slip if scope is tight |
| Level Art | Imi | parent epic's MS | Biome and island-specific assets — traditional waterfall, final art does not need to land with the production milestone, polish continues afterwards |

**Sequencing rule (locked 2026-04-27):** No new iteration of any island until ALL 7 islands have completed a first pass through the production stack above. Broad-and-shallow before deepening any single island, so we surface scope and balancing issues across the whole DLC before polishing anything.

## Shape C — CONTENT-ITEM Tasks (added 2026-05-22)

Single content items under the umbrella epics (KAN-13 ABILITIES, KAN-15 BLESSINGS, KAN-14 ENEMIES variants without feature-epic wrappers, KAN-12 MOUNTS individual mounts). Each content-item Task has THREE Subtasks:

- `<item>: design` — label `prod-design`
- `<item>: art` — label `art`
- `<item>: implementation` — label `code`

Several pre-existing content items already had a single subtask carrying the design content in its summary (e.g. KAN-149 "Reuse from base game / average stats" under KAN-148 Standard Horse). When topping these up, leave the existing summary alone — that spec content is useful in place — and add the art + implementation siblings alongside.

Subtasks inherit the parent Task's Sprint and parent Epic; no need to assign sprints to subtasks directly.

Why a third shape: FEATURE epics (banner, monarch rework) use sibling Tasks because each discipline is substantial. CONTENT items (one ability, one mount) are small enough that one parent + three subtasks fits — Subtasks roll up under the parent on the board and stay legible at backlog scale.

Applied 2026-05-22 to: KAN-164, 166, 168, 305 (abilities), KAN-178, 180 (blessings), KAN-174, 176, 218 (enemies), KAN-148, 150, 152, 154, 156, 158, 160, 162 (mounts). Skipped: KAN-170 Lurker greed and KAN-172 Apesh (already covered by FEATURE epic siblings KAN-261 + KAN-257).

## Shape D — Reskin Task (added 2026-06-01)

Egyptian-setting reskins of existing player units (citizens, pikeman, others to be added) are grouped under **one** Task — KAN-354 "Egyptian unit reskins" — rather than per-unit tickets. Per-asset state continues to live in the K2C New Asset List on Confluence (page id 98338).

**Why one ticket:** reskins are not new features; they're visual refreshes of existing player units. Splitting them per unit creates ticket noise without adding tracking value, since the asset list already itemizes them.

**When to use:** existing player unit getting an Egyptian visual variant only (no new behavior, no new feature epic). Distinct from FEATURE epics like KAN-349 Javelinist, which IS a new player-controlled unit (not a reskin) and gets the full sibling-Task shape.

## Milestoning rule for CONTENT ITEMS (Robert, 2026-07-31)

**Mounts, items of power, blessings and bosses are milestoned by the ISLAND that unlocks them**, not by a blanket "current milestone" or "next milestone" call. Robert's words: *"both mounts and items of power are connected to specific Islands."* Each stays one Task per feature (Shape C), and its `fixVersion` follows its island's milestone from the finalized island→MS map.

Derived mapping as applied 2026-07-31:

| Island (MS) | Mount | Item of power | Boss / blessing |
|---|---|---|---|
| A Ra (MS2) | Standard Horse KAN-148, War Horse KAN-150 | Staff of Ra KAN-164 ✅ | Ra blessing / day cycle KAN-178 |
| B Bata (MS3) | Large Black Cat KAN-156 ✅ | Flail of Anubis KAN-168 (Path A) | — |
| C Sobek (MS4) | Crocodile KAN-154 | — | Farm boost KAN-180 |
| D Sphinx (MS5) | Camel KAN-152 | — | Greed-headed Sphinx KAN-174 |
| E Osiris (MS5) | Chariot KAN-162 | Scepter of Khonsu KAN-305 | — |
| F Anubis/Apesh (MS4) | Scarab KAN-158 | Flail of Anubis (Path B fallback) | Apesh turtle boss KAN-172 |
| G Set (MS5) | Scorpion KAN-160 | Book of the Dead KAN-166 | Set + Greed Queen |

**Not island-connected**, so the rule does not decide them and they need a separate call: per-island greed variants KAN-176 (spans all), Greed Mask upgrades KAN-218, War Room KAN-182, Bulk Buy KAN-184.

**Caveat carried forward:** the Ra mounts (KAN-148/150) are still open on MS4 despite Ra having shipped at MS2 — both are "reuse from base game", so they are probably closeable but were not closed without evidence.

## Across all shapes

- Epic `fixVersion` = milestone where the epic actually delivers (NOT milestone-prior). This was revised on 2026-04-23 — the older "milestone prior" rule conflicted with delivery-driven Timeline tracking.
- Epic `duedate` = the same milestone's release date, so Releases page and Timeline view agree.
- Tasks under the epic carry their own fixVersions matching their individual delivery milestones (Design spec subtasks under campaign islands always go to MS1).
- Applies to the KAN project on aurorapunks.atlassian.net.
