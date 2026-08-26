---
name: vps-security-posture
description: "Verified security state of board.runatyr.games (the Assistant VPS) — Cloudflare Access policy, firewall, SSH config, GitHub repo exposure. Facts that are expensive to re-derive (needed sudo + the CF API); check here before assuming."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 97f74fe7-f75c-40af-ae78-50db2ed7985f
  modified: 2026-08-16T18:26:33.050Z
---

Verified 2026-07-22 during the four-way security audit (`assistant/followups/ops-security-audit-2026-07-22.md`). These are measured facts, not assumptions - several required sudo or the Cloudflare API to establish, so re-deriving them is expensive. Re-verify if the date is stale.

**Cloudflare Access** - `board.runatyr.games` and `hive.runatyr.games` both carry a single policy, **"Robert Only"**, whose only include is `email: robert@aurorapunks.com`. Not a group, not a domain. So anything reachable "behind Access" is reachable by Robert alone - which caps the severity of internal-surface findings and means the realistic attacker on those hosts is a **prompt-injected agent via the localhost bypass**, not the open internet. Three paths bypass the origin JWT check (`CF_JWT_BYPASS_PATHS` in `server.js`, formerly `UNAUTH_PATHS`): `/webhook/atlassian`, `/webhook/docuseal`, `/webhook/plane` - each does origin-side signature auth.

**Firewall** - UFW is **active**, `default deny (incoming)`, and **only `22/tcp` is open**. Consequence worth remembering: `server.js` binds `*:3777` (all interfaces), but **port 3777 is NOT reachable from the internet** - UFW stops it. The weekly T1 sweep flagged "public bind + unknown firewall" as a compound critical for 13 weeks; the unknown half was correctly configured the whole time.

**SSH** - `PermitRootLogin no` (set 2026-07-22; root had logged in exactly once ever, 2026-04-08). `PubkeyAuthentication yes`, `PermitEmptyPasswords no`, `MaxAuthTries 6`. **`PasswordAuthentication yes` - deliberately kept by Robert**, with `fail2ban` installed as the compensating control (it banned 3 IPs on first start; brute-force traffic against port 22 is live and ongoing). Robert's key is `ssh-ed25519 robert@aurorapunks.com` in `~/.ssh/authorized_keys` (0600), so disabling passwords remains a low-risk option if he ever wants it.

**GitHub** - all three repos (`RobertBackstrom/assistant`, `projects`, `cc-hive`) are **private**, sole collaborator `RobertBackstrom`, **zero deploy keys, zero forks**. This is what caps the severity of secrets found in git history (notably the Discord bot token, still unrotated as of 2026-07-22).

## Addendum 2026-08-16 (sec-020) — Cloudflare API reach, and the one thing we cannot audit

**What the CF token can do.** `CLOUDFLARE_API_TOKEN` (in `assistant/.env`, 53 chars, `cfut…`) is
active and covers **all three zones**: `aurorapunks.com` (cb4386a8…), `runatyr.games` (02701bea…),
`robotlordrising.com` (7e026725…). Zone read **and DNS write** both verified 2026-08-16 by creating
and immediately deleting a throwaway TXT. So **DNS-based domain verification (Google Search Console,
etc.) is an agent step, not a Robert step** — he only has to paste the token value. Helper:
`assistant/gsc-verify-txt.js`.

**What no token can do: read Cloudflare Access logs.**
`/accounts/<id>/access/logs/access_requests` returns `10000 Authentication error` for **both**
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCESS_API_TOKEN`. Consequence during an incident: we can
prove the DNS zone is clean, the content unchanged and the logins unknown-free, but **we cannot
answer "who authenticated to our internal surfaces"** without the Zero Trust dashboard. Tracked as
`sec-022` (needs an Access: Read scoped token). Also worth resolving whether
`CLOUDFLARE_ACCESS_API_TOKEN` is dead config.

**Access-gated hosts (all behind the single "Robert Only" policy):** `board.runatyr.games`,
`code.runatyr.games`, `hive.runatyr.games`, `kanban.aurorapunks.com`, `internal.aurorapunks.com`,
routed through the `runatyr.cloudflareaccess.com` IdP. Every one of them serves a Cloudflare Access
login page unauthenticated, which is **structurally a phishing signature** (cross-domain hop, login
form, Google branding, ~900-char opaque JWT) and is what Chrome's real-time classifier has now
flagged twice. See [[project_security_automation]].

**Zone inventory (2026-08-16):** aurorapunks.com 11 records, runatyr.games 7, robotlordrising.com 3.
All CNAMEs point at our own tunnel `769d4523-1a04-46b3-959d-8fdc90899f6b`. **No rogue or dangling
records.** `runatyr.games` apex has **no DNS record at all** (only subdomains resolve). A full zone
enumeration via the CF API is the single highest-value first check when asked "were we attacked" —
a rogue subdomain is the most likely real finding behind a domain-reputation hit.

**Read-only verification without general sudo** - `/etc/sudoers.d/010-security-readonly` grants NOPASSWD for `ufw status verbose` and `sshd -T`. Use these rather than reading config files directly: `/etc/ssh/sshd_config.d/` is root-only, so the *readable* config and the *effective* config differ. That gap is exactly why password auth sat undetected for months while the sweep reported on SSH every week. See [[feedback_security_defaults]] and [[project_security_automation]].
