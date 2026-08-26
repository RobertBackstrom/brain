# aurorapunks.com — Production Go-Live Cutover Runbook

**Project:** apw (Aurora Punks static site) | **Author:** DevOps agent | **Date:** 2026-06-15
**Status:** PLAN ONLY — nothing here has been executed. The DNS/nameserver flip is destructive to the live Wix site and to mail; do not run any step without Robert.

---

## Current state (verified live 2026-06-15)

| Fact | Value |
|---|---|
| Registrar / control panel | **Websupport** (`admin.websupport.se`) — confirmed by 2026-06-16 renewal mail for `aurorapunks.com`. Wholesale registrar = Ascio (IANA 106); Loopia is a sister brand on the same backend. NOT Wix, NOT Loopia. NS change is made at **Websupport**. |
| Current nameservers | `ns4.wixdns.net`, `ns5.wixdns.net` (Wix DNS) |
| Root A (Wix) | `185.230.63.107 / .171 / .186` |
| www | CNAME → Wix (`cdn1.wixdns.net` etc.) |
| **MX (mail)** | `1 aspmx.l.google.com.` — **Google Workspace. MUST NOT BREAK.** |
| SPF / DKIM / DMARC | **None published** (no TXT, no `_dmarc`, no `google._domainkey`) |
| **DNSSEC** | **ENABLED at Websupport** (DS for Wix's keys published in `.com`) — **MUST be disabled + propagated BEFORE the NS flip, or the domain SERVFAILs globally (site + mail dark)** |
| Websupport DNS zone | A dormant/legacy parallel zone exists at Websupport (old Unbounce A `54.84.104.245`, `www → unbouncepages.com`, legacy Websupport mail hosts `109.235.175.x`). **NOT authoritative** (Wix is). Ignore it — do not migrate these records, do not click the "Ställ in" quick-setup cards. |
| Domain expiry | **2026-07-07**, but **auto-renews ~2026-06-23 via Websupport saved card** (299 SEK) — no manual renewal needed |
| VPS public IP | `89.167.23.168` |
| Tunnel | `deathboard` (`769d4523-1a04-46b3-959d-8fdc90899f6b`), remote-managed, editable via the scoped `CLOUDFLARE_API_TOKEN` |
| Cloudflare account | `b7cba53cd3bd57c5ab76be89010c78a7` (runatyr.games lives here; aurorapunks.com zone is "pending" per secrets registry) |

**Preview already live:** https://aurorapunks-preview.runatyr.games/ (served by `assistant/aurorapunks-preview-server.js` on loopback :3783, fronted by the tunnel). Production reuses this serving stack.

---

## Serving model decision

The preview origin is **loopback-only** (`127.0.0.1:3783`) — the cloudflared tunnel is the sole public path; nothing is exposed on the VPS public IP. **Recommended for production: keep this model.** aurorapunks.com (and www) become **proxied CNAMEs to the tunnel** (`<tunnel-id>.cfargotunnel.com`), exactly like board/pitch/hive. This means:

- **No nginx vhost and no public A record are actually required** if we ride the tunnel (cleaner, keeps the origin private, matches existing runatyr.games pattern).
- The task brief mentions an "A record → VPS" + nginx; that is the *alternative* model (expose port 80/443 on the VPS public IP behind Cloudflare proxy). It works but exposes the origin and needs nginx + a firewall rule. **Recommend the tunnel-CNAME path; nginx steps below are the fallback only.**

A dedicated production server process (separate from the preview) is cleanest so the preview URL can stay or be retired independently. Reuse `aurorapunks-preview-server.js` as the template, new port (e.g. 3784), new systemd unit, tunnel ingress `aurorapunks.com` + `www.aurorapunks.com` → `http://localhost:3784`.

---

## Ordered cutover — mail-safe, near-zero site downtime

### Phase 0 — Prep on the VPS (DevOps, autonomous, no DNS impact, reversible)

1. **[DevOps] Self-host the hero video.** It currently points at Wix CDN and dies with Wix.
   - URL: `https://video.wixstatic.com/video/0a9405_78e3acfe53d4459c8328fbfed83c909c/1080p/mp4/file.mp4`
   - `curl -L -o aurorapunks_site/site/assets/hero-bg.mp4 "<url>"`
   - Edit `site/index.html` line ~1094 `<source src=...>` → `assets/hero-bg.mp4`.
   - Also self-host the Google Fonts (Barlow Condensed + Chakra Petch) OR accept the external dependency (fonts.googleapis.com survives Wix death — it's Google, not Wix — so this is optional, lower priority than the video).
2. **[DevOps] Production server process.** Copy `aurorapunks-preview-server.js` → `aurorapunks-server.js`, root = `aurorapunks_site/site/`, port 3784. Add `aurorapunks-site.service` user unit (mirror the preview unit), `systemctl --user enable --now`. Verify `curl -sI http://127.0.0.1:3784/` = 200.
3. **[DevOps] favicon** — add `site/favicon.ico` (currently missing) so the production tab icon isn't broken.

### Phase 1 — Recreate the zone in Cloudflare BEFORE touching nameservers (Robert + DevOps)

> **Critical ordering rule:** every record that exists at Wix today must exist in Cloudflare *before* the nameserver flip, especially MX. When NS switches, CF instantly becomes authoritative; any missing record = that service goes dark. Mail is the highest-stakes item.

4. **[Robert] Add aurorapunks.com to the Cloudflare account** (Dashboard → Add a site → aurorapunks.com → Free plan). CF will auto-scan existing Wix records — **review the scan, do not assume it caught everything.** It assigns the nameserver pair (expected `dina.ns.cloudflare.com` + `marvin.ns.cloudflare.com`). Once the zone exists, DevOps can finish the records via API (the scoped token already has zone DNS edit; secrets registry notes the token was provisioned anticipating exactly this aurorapunks.com migration).
5. **[DevOps, after zone exists] Create / verify these records in the CF zone** (via `CLOUDFLARE_API_TOKEN`):
   - **MX:** `aurorapunks.com  MX 1 aspmx.l.google.com` — **DNS-only (grey cloud), never proxied.** This is mail; double-check it lands before anything else.
   - **Site (recommended, tunnel model):** `aurorapunks.com  CNAME  769d4523-...cfargotunnel.com` **proxied (orange)**, and `www.aurorapunks.com  CNAME  769d4523-...cfargotunnel.com` proxied. Add tunnel ingress `aurorapunks.com` + `www.aurorapunks.com` → `http://localhost:3784` via the tunnel configurations API (same method used for the preview).
     - *Fallback (nginx model, only if not using the tunnel):* `aurorapunks.com  A  89.167.23.168` proxied + www CNAME; stand up an nginx vhost `server_name aurorapunks.com www.aurorapunks.com; root /home/assistant/projects/aurorapunks_site/site;` and open the firewall. **This needs sudo DevOps may not have — see Boundaries.** Prefer the tunnel.
   - **Email auth (new — none exist today; add while we're authoritative to improve deliverability):**
     - **SPF:** `aurorapunks.com  TXT  "v=spf1 include:_spf.google.com ~all"`
     - **DKIM:** generate in Google Admin (Apps → Google Workspace → Gmail → Authenticate email) → publish the `google._domainkey` TXT it produces. **[Robert]** must generate the key in Workspace admin; DevOps publishes the TXT.
     - **DMARC:** `_dmarc.aurorapunks.com  TXT  "v=DMARC1; p=none; rua=mailto:hello@aurorapunks.com"` (start at `p=none` monitor-only; tighten to `quarantine`/`reject` after a few weeks of clean reports).
   - **Any other Wix records the CF scan surfaced** (verification TXTs, subdomains). Replicate anything still needed; drop Wix-internal ones.
6. **[Robert + DevOps] Verify the CF zone resolves correctly while NS is still Wix.** Query the CF nameservers directly without flipping: `dig @dina.ns.cloudflare.com aurorapunks.com MX +short` and `... aurorapunks.com +short`, `... www +short`. Confirm MX = aspmx and the site answer points at the tunnel/VPS. **Do not proceed to the flip until this is green.**

### Phase 2 — Disable DNSSEC, then the nameserver flip (Robert, at Websupport — destructive)

> **⚠ DNSSEC GOTCHA (confirmed enabled 2026-06-16):** aurorapunks.com has **DNSSEC ACTIVE** at Websupport — a DS record for Wix's signing keys is in the `.com` parent zone. Switching nameservers to Cloudflare while that DS is live makes every validating resolver return **SERVFAIL → site AND mail dark globally.** DNSSEC must be turned off (DS removed) and allowed to propagate *before* the nameserver change. This step is mandatory and ordering-critical.

7. **[Robert] Disable DNSSEC at Websupport FIRST.** Panel → DNS → **Namnservrar** → DNSSEC section → red **"Inaktivera DNSSEC"** button. This removes the DS record from `.com`. **Wait for it to clear before the NS flip** — allow up to ~24h (the DS TTL). Verify: `dig DS aurorapunks.com +short` returns empty. Do NOT proceed until the DS is gone. (Optional, same window: lower TTLs if Wix's editor allows, for faster propagation.)
8. **[Robert] Change the nameservers at Websupport** (`admin.websupport.se` → DNS → **Namnservrar** → **"Anpassad namnserver"** tab — already selected, custom NS confirmed supported). Replace the two Wix entries (`ns4`/`ns5.wixdns.net`) with:
   - `dina.ns.cloudflare.com`
   - `marvin.ns.cloudflare.com`
   - Leave **GLUE-pekare (GLUE records) OFF** — only needed for in-domain nameservers. Click **"Anpassat"** to save. Websupport is the *registrar*; Wix only ran *DNS*. Wix loses DNS authority once propagation completes (minutes to ~24–48h depending on TTL).
9. **[DevOps] Monitor propagation:** loop `dig NS aurorapunks.com +short` until it returns the CF pair, then `curl -sI https://aurorapunks.com/` = 200 with `x-apw-preview`-style origin header, and `dig MX aurorapunks.com +short` still = aspmx. Confirm mail flow with a test send/receive to a `@aurorapunks.com` address.
10. **[DevOps] Enable HTTPS hardening in CF** once live: SSL/TLS mode = Full (strict) is N/A for a tunnel origin (tunnel is already encrypted) — use **Full**; turn on Always Use HTTPS + Automatic HTTPS Rewrites.
    - **[Robert, optional] Re-enable DNSSEC the right way** once Cloudflare is authoritative and stable: turn on DNSSEC in Cloudflare (DNS → Settings → Enable DNSSEC), copy the DS record CF generates, and add it back at Websupport (DNS → Namnservrar → DNSSEC). Restores DNSSEC protection under Cloudflare's keys. Do NOT do this until CF is confirmed serving — re-introducing a DS before the zone is stable just re-arms the same SERVFAIL risk.

### Phase 3 — Registration renewal decision (Robert, before 2026-07-07)

11. **[Robert] Renewal is already handled — domain auto-renews ~2026-06-23 via the Websupport saved card** (299 SEK), so the 2026-07-07 expiry is not a risk and no manual renewal is needed. Two paths going forward:
    - **(A) Leave registration at Websupport** (simplest): let it auto-renew, just repoint nameservers to Cloudflare. Keeps the registrar split from DNS. Nothing else to do.
    - **(B) Transfer registration to Cloudflare Registrar** (consolidation): after the zone is on CF and ≥60 days since last transfer/registration, transfer from Websupport to Cloudflare Registrar — adds a year, at-cost pricing, lets the Websupport account be decommissioned. Requires unlocking + auth/EPP code from Websupport. **If going this route, cancel the Websupport auto-renew first** so you don't pay for a year right before a transfer (which adds its own year). Don't start an inter-registrar transfer in the days around the 06-23 auto-renew / 07-07 expiry — do it after, with runway.

### Phase 4 — Future / non-blocking (DevOps, post-launch)

12. **[DevOps] Real contact-form backend.** Form is currently `mailto:hello@aurorapunks.com`. Replace with a POST endpoint:
    - Cheapest VPS-native option: a small route on the existing infra that builds a MIME and sends via the Gmail REST path (`require('./gmail-api')` → `sendRawMessage`, work account = robert@aurorapunks.com — same pattern used elsewhere; there is no SMTP on the VPS). Add a tunnel route or reuse an existing one, plus a Turnstile/honeypot to stop spam.
    - Lower-effort alternative: a third-party form service (Formspree/Basin) — no backend, but external dependency.

---

## Who does what

- **Robert (cannot be automated):** add aurorapunks.com to the CF account (step 4); generate the Google Workspace DKIM key (step 5); the nameserver change at Websupport (step 8); the registration-transfer decision (step 11 — renewal is automatic).
- **DevOps (autonomous, has the scoped CF API token):** video self-hosting (1), prod server + unit (2), favicon (3), all CF DNS records + tunnel ingress once the zone exists (5), propagation verification (6, 9), CF SSL/HTTPS settings (10), contact-form backend (12).
- **Needs sudo DevOps may NOT have:** the *nginx fallback* (step 5 fallback) needs `apt`/nginx config + firewall = root. **Avoid by using the tunnel model**, which needs no sudo (`systemctl --user` + CF API only). If the nginx path is ever required, flag it to Robert as a sudo dependency.

## Rollback

If the site breaks after the flip, the fastest recovery is at Cloudflare (we're now authoritative): fix/point the CNAME or A record in the CF zone — propagation is fast since CF is the edge. A full revert means changing nameservers back to Wix at Websupport (slow, only if CF zone is fundamentally wrong). **Mail has no quick rollback** — which is exactly why MX is recreated and verified (step 5/6) *before* the flip.
