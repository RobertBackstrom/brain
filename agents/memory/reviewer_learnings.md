# The Reviewer — Learnings

Cross-project learnings for the [[reviewer]] agent. Append inline after every pass, with date +
lens + project tag. When a learning is a durable failure mode or a criterion the rubric should
have had, also fold it into the matching `skills/review/lens_*` file so future passes inherit it.

Format per entry:
- **[YYYY-MM-DD] [lens] [project]** — the learning (what the review missed, or flagged wrongly),
  and the calibration takeaway. Category: `false_negative` (missed, Robert caught it) /
  `false_positive` (cried wolf) / `rubric_gap` / `process` / `tooling`.

Never manufacture a finding to look thorough — calibration beats volume. If Robert stops trusting
the memos, the whole tool is dead weight.

---

## Entries

- **[2026-07-22] [security/measurement] [the_assistant / VPS]** — **Measure effective state, not
  readable state.** Two of the loudest findings in the VPS audit existed only because the weekly
  sweep reported on what it could read rather than what was true, and they failed in *opposite*
  directions: (1) `/etc/ssh/sshd_config` said nothing about passwords, but the root-only-readable
  drop-in `sshd_config.d/50-cloud-init.conf` had `PasswordAuthentication yes` - **worse** than
  reported, and invisible for 13 weeks; (2) the sweep flagged "port 3777 binds `*:3777` + firewall
  state unknown" as a compound critical every week, but UFW was `default deny incoming` with only
  22/tcp open the entire time - **better** than reported. Both are the same defect. When a check
  cannot read the authoritative source, it does not produce a weak signal, it produces a **wrong**
  one, and 13 weeks of confident weekly reporting on a guess is worse than no check. Fix pattern
  that worked: a narrow NOPASSWD sudoers entry for read-only verifiers (`ufw status verbose`,
  `sshd -T`) so the routine can measure ground truth without granting general sudo. Ask of any
  security check: "is this reading the authoritative source, or the one it happens to have
  permission for?" Also worth remembering: my own first `systemctl is-active | grep -q active`
  check reported all three brute-force daemons ACTIVE because "in**active**" contains "active" -
  a broken test that reports reassuring results is the same failure mode at small scale. None were
  installed; there was live brute-force traffic (3 IPs banned on fail2ban's first start).
- **[2026-07-22] [security/remediation] [the_assistant / VPS]** — Applying the audit taught more
  than writing it. **Three times the review's own recommendation was wrong or overstated, and only
  verification caught it:** (1) "apply `isValidTicketId` to every `:id` route" would have rejected
  **62 of 962 real tickets** (uppercase `W` in weekly-reflection ids, `ACTIVITY_LOG`, `db-*`
  without numbers) - the needed property was **path containment**, not a naming convention;
  (2) "`LEAN_MCP_ARGS` removes the full MCP fleet" - it removes **only whatsapp**; gdrive write,
  `linkedin-sd send_message` and jira write remain; (3) "require `approved_to_execute` on the 4am
  path" would have **silently disabled the autonomous sweep**, since that flag is single-use and
  cleared on fire - the right fix was making `scoreTicket` asymmetric (downgrades read everything,
  grants read only author-controlled text). **Lesson: a Reviewer memo is a hypothesis list, not a
  patch list. Every fix must be tested against the real data population before it ships** - and
  when the fix is wrong, correct the audit document too, don't silently deviate.
  **Second lesson, bigger:** I drafted a Discord registration wall, then checked actual usage and
  found a non-Robert K2C collaborator using the feature routinely with **0 registered users** - the
  "security fix" would have broken a live client workflow. **Before gating any capability, grep the
  logs for who actually uses it.** Scope the gate to where the risk really is (the community-shared
  guild), not to the whole surface. Also: a broad env scrub looked obviously right until I checked
  whether scripts load dotenv themselves - most do not, so it would have broken every shell-out.
  **Verify the blast radius of the fix as adversarially as the finding.**
- **[2026-07-22] [security] [the_assistant / VPS]** — First fan-out pass: four parallel Fable
  Reviewers (agent autonomy / platform code / secrets / the security routines themselves) + a
  synthesis pass, threat model = prompt injection via indexed untrusted content. Output:
  `assistant/followups/ops-security-audit-2026-07-22.md`. **The fan-out shape earned its cost:**
  no single layer saw a kill chain: the mail-injection entry (layer A), the missing env/MCP scrub
  on the execute spawn (layer B), the `EnvironmentFile` in the systemd unit (layer C) and the
  auto-closing sweep tickets (layer D) are one chain, and only the synthesis saw it. **Lesson:
  for any review where the risk is compositional rather than local, fan out by layer and always
  add a synthesis pass whose explicit job is to trace chains across memos** - do not just merge
  finding lists. Second lesson: the synthesis **disagreed with two layers' severities and said so**
  (raised the unattended 4am path to Critical since it is gated on nothing; dropped PermitRootLogin
  to Medium since the effective config was never measured) - a synthesis that only aggregates is
  worth much less than one licensed to re-rank. Third: the most useful single output was not the
  finding list but the "70 minutes closes most of four chains" ordering by leverage-per-effort -
  **rank by what breaks the most chains per hour, not by severity**. Also confirmed the calibration
  rule pays: crediting the genuinely verified perimeter (CF Access enforced edge+origin, April
  remediations held) is what made the blunt "this part is theatre" verdict land. Cost: ~522k
  subagent tokens across 5 passes.
- **[2026-07-17] [business_case+legal] [aurora_punks / apb-029]** — First live pass: the "Erik
  Reynolds offer" ($1.5-2M into AP). High-value hits: (1) the artifact under review (summary
  email) had **already been sent** - the pass caught that the target moved from "edit before send"
  to "correct on the call", by checking live Gmail rather than trusting the draft's status. Lesson:
  **always verify send-status against live Gmail before reviewing an outgoing message** - a
  "draft" file may already be on the record. (2) "dismissed and ring-fenced" debt was false vs the
  live WLBS/APDS litigation ([[project_wlbs_apds_litigation]]) - grounding in the litigation memory
  + today's Lawyer PM caught a written misstatement to a prospective US investor (anti-fraud/
  securities exposure). (3) $89k/mo = gross dressed as net (~3x the confirmed 290K SEK/mo net
  anchor in the same data room) - cross-checking the email against the deal's own §2.1/§6 anchor
  is where the number broke. Process wins to fold into rubrics: for an *outgoing* artifact, check
  live send-status first; for financials, always diff the headline number against the producing
  team's own internal anchor doc; for "debt dismissed/clean" claims, always cross-check open
  litigation. Ran on Fable, ~132k tokens, 17 tool calls - within the bounded-cost expectation.
  Calibration held (credited the RLR correction + honest data room, didn't manufacture).
- **[2026-07-14] [process] [meta]** — Agent created, mirroring [[the_author]]: named agent
  (model: fable) + layered `skills/review/` corpus + registry routing note. Same token economy —
  cheap models produce, Fable critiques the short finished artifact. Four v1 lenses:
  business_case, legal, security, code, each grounded in an existing source of truth
  (rate card / `wiki/legal/` + [[lawyer]] / [[feedback_security_defaults]] / `/code-review`).
  Advisory only, never blocking, never edits the artifact. Death Board recommendation detector
  scoped as a DevOps handoff, not yet built.
