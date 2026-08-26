---
name: Security Automation Pipeline
description: VPS security screening — weekly T1 + monthly T2 + 2-week soak check, bash+Claude hybrid via systemd user timers, writes DB tickets with sec-* prefix
type: project
originSessionId: c9076dd0-2de4-41ef-9b47-45a8a385e9a0
modified: 2026-08-16T18:26:50.365Z
---
# Security Automation Pipeline

Set up 2026-04-24 after the ops security hardening rollout. Three scheduled jobs running locally on the VPS via systemd user timers (NOT remote /schedule routines — those run in Anthropic cloud and can't see the VPS).

## Where things live

- **Scripts + prompts:** `/home/assistant/projects/.security/` — `t1.sh`, `t2.sh`, `soak-check.sh`, `prompt-t1.md`, `prompt-t2.md`, `prompt-soak.md`, `gitleaks.toml` (auto-created)
- **State + baselines:** same dir — `last-run-t1`, `last-run-t2`, `systemd-user-baseline.txt`, `t2-baseline-users.txt`, `t2-baseline-timers.txt`, `t2-baseline-ssh-keys.txt`, raw reports as `t1-raw-<ts>.txt` etc.
- **Synthesis logs:** same dir — `t1-synthesis-<ts>.log`, `t2-synthesis-<ts>.log`, `soak-<ts>.log`
- **Systemd units:** `~/.config/systemd/user/security-{t1,t2,soak}.{service,timer}`
- **Output tickets:** `assistant/followups/sec-NNN-<slug>.md` (project: ops)

## Schedule

- **T1 weekly:** `OnCalendar=Sun *-*-* 05:00:00 Europe/Stockholm` — quick screening, baselines diff against last week
- **T2 monthly:** `OnCalendar=*-*-15 05:00:00 Europe/Stockholm` — deep audit, full git history secret sweep, transitive dep audit, user/key/timer baselines diff
- **Soak check (one-shot):** `OnCalendar=2026-05-08 09:00:00 Europe/Stockholm` — 2-week verification of the CF Access hardening rollout

## Architecture

Hybrid pattern: systemd timer → `t*.sh` bash collector dumps raw data to `t*-raw-<ts>.txt` → `claude --model sonnet -p` reads the report + writes the DB ticket. Bash handles cheap mechanical things (gitleaks, ss, journalctl, npm audit, perms); Claude handles judgment (priority tiers, recommendations, narrative summary). LLM is invoked once per run, not for the data collection loop.

## Ticket conventions

- Prefix: `sec-` (matches `^[a-z]{2,6}-\d{3}(-[a-z0-9-]+)?$` ticket ID regex)
- Slug embeds run date: `sec-NNN-weekly-YYYYMMDD`, `sec-NNN-monthly-YYYYMMDD`, `sec-NNN-soak-check-YYYYMMDD`
- Priority tiers: `low` (clean), `medium` (minor findings), `critical` (new secrets, loose creds, unexpected ports, SSH config drift, JWT reject spike, git fsck errors)
- Critical priority also pings `DISCORD_HEALTHZ_WEBHOOK`

## Allowlist

`/home/assistant/projects/.security/gitleaks.toml` allowlists files that legitimately contain secrets: `.env`, `secrets_registry.md`, `.claude/.credentials.json`, `.claude/.gdrive-server-credentials.json`, `.claude/.atlassian-credentials.json`, `.claude/.gcal-credentials.json`. Any new secret outside these → reported.

## Manual runs

- T1: `systemctl --user start security-t1.service` (or `bash /home/assistant/projects/.security/t1.sh` for direct invocation with stdout)
- T2: `systemctl --user start security-t2.service`
- Soak: `systemctl --user start security-soak.service`
- Status: `systemctl --user list-timers --all | grep security`
- Disable a timer: `systemctl --user disable --now security-t1.timer`

## Fourth scheduled job (added 2026-08-11, extended 2026-08-16) — Safe Browsing monitor

Not part of the T1/T2/soak bash+Claude pipeline above; a standalone Node job, but it is a **weekly
security job filing `sec-NNN` tickets**, so treat it as part of this pipeline.

- **Script:** `assistant/safebrowsing-monitor.js` · **Timer:** `safebrowsing-monitor.timer` (weekly, Mon 05:02)
- **State:** `assistant/logs/safebrowsing-state.json` · **History:** `safebrowsing-history.jsonl`
- **Covers 18 hostnames** across all three zones (was 12; audited against live Cloudflare DNS
  2026-08-16, which found 7 unmonitored hosts including all of `robotlordrising.com`).
  Re-run that diff whenever a hostname is added.

**It emits two independent signals. Do not conflate them:**

1. **Safe Browsing verdict** — Google's *reputation* view, via the Transparency Report. Files a
   `sec-NNN` on a clean→flagged edge only, never re-files while a host stays flagged.
2. **Page shape** — what a classifier actually *sees* at our origin right now. Alerts **only on a
   change**, never on the steady state, because every Access-gated host permanently looks like a
   login page and alerting on that would be pure noise. A change is a real signal: a static page
   that gained a password field is content injection; a gated host that stopped requiring auth is a
   broken Access policy.

**The trap this exists to cover:** the Transparency Report knows only *standing blocklist entries*,
while Chrome also issues **real-time verdicts that never become a persistent record**. So
`status=1 clean` while Chrome shows the red interstitial is the **expected** reading, not a bug and
not a stale monitor. When they disagree, read the shape, not the verdict.
Ad-hoc during an incident: `node assistant/safebrowsing-monitor.js --shape [host…]`.

**Open, blocked on Robert (`sec-020`, since 2026-08-11):** the `aurorapunks.com` apex carries a
standing deceptive-content flag. Clearing it requires a Search Console security review, which has
**no API** — property creation is automatable (`assistant/gsc-verify-txt.js`, and we hold DNS write),
but the review click is his. The flag is bleeding into Access-gated subdomains via real-time
verdicts, so it degrades over time rather than staying put.

## Status caveat (2026-07-22 audit) — the collector works, the loop does not

A four-way security audit (`assistant/followups/ops-security-audit-2026-07-22.md`) found this
pipeline is currently **closer to process theatre than control**. Do not trust a green sec-* ticket
as evidence that findings were resolved:

1. **Tickets are born `status: done`.** `prompt-t1.md` / `prompt-t2.md` hardcode it, and the Death
   Board `pending_close` sweep then auto-closes them after 4 days — sec-012 through sec-015 were all
   marked completed while carrying unresolved criticals.
2. **A critical went unactioned for 13 consecutive weeks** (`PermitRootLogin yes`, finally fixed
   2026-07-22). 13 identical Discord alerts produced alarm fatigue, not action.
3. **The 2026-07-05 run failed silently** (three zero-byte artifacts, no ticket, no alert) and nobody
   noticed for 17 days. Neither service has an `OnFailure=` directive.
4. **~95% of the gitleaks signal is `rag.db-wal` noise**, and the ~20 real hits have never been
   triaged. Separately, that finding means secrets are landing inside the RAG database.
5. **It tests for none of the current threat model** — no prompt-injection check, no MCP/agent-config
   drift, no permission-allowlist monitoring. It also pipes its own untrusted report into a
   `Bash,Read,Write,Edit` Claude call with no untrusted-content delimiter.
6. **It measures readable state, not effective state.** `sshd_config.d/` is root-only, so the sweep
   reported on SSH weekly for months without ever seeing `PasswordAuthentication yes`. A NOPASSWD
   entry now exists (`/etc/sudoers.d/010-security-readonly`) for `ufw status verbose` and `sshd -T`
   — wire T1 to use it. See [[reference_vps_security_posture]].
