# Aurora Punks Static Site - Output Log

## 2026-06-18 - DevOps - clients.runatyr.games moved to client.aurorapunks.com (subdomain migration #2)

Same pattern as the pitch move below. `clients.runatyr.games` = the per-client prospect tracker (db-163/168), serving `/<secret-token>` -> sanitized single-project deal-wiki view + comment box; root 404s by design. **2 live tokenized client links** in the wild at move time: Elias Audio (`elias`) + Blue Scarab Entertainment (`blue_scarab`).

Changes:
1. Proxied CNAME `client.aurorapunks.com` (singular, per Robert) -> deathboard tunnel.
2. Tunnel route `client.aurorapunks.com` -> `http://localhost:3780` (ingress now 15 entries).
3. Origin 301 in `assistant/clients-server.js` (Host-check, env `CLIENTS_CANONICAL_HOST`, `/healthz` exempt). `clients.service` restarted (user scope).

Verified: both live client tokens 200 on new host; old host 301s preserving the token path; follow-chain lands 200; `/healthz` 200 both hosts; root still 404 (no client-listing leak). Tokens are host-agnostic so the same link works on either host - existing shared links unbroken.

`sign.runatyr.games` (OpenSign) deliberately deferred: Robert wants to wait until the current signature batch is signed, then move the docs to the new domain (avoids breaking in-flight signing links + Parse callback mid-batch).

## 2026-06-18 - DevOps - pitch.runatyr.games moved to pitch.aurorapunks.com (subdomain migration, pattern proof)

First of a planned set of subdomain moves off `runatyr.games` onto `aurorapunks.com` (Robert: consolidate brand surfaces; `.se` was considered but not registered, so using the `.com` we already own). Pitch done as the lowest-risk proof of the pattern.

Changes (all via scoped CF API token + origin edit, no dashboard):
1. New proxied CNAME `pitch.aurorapunks.com` -> deathboard tunnel (zone aurorapunks.com).
2. Added tunnel published-route `pitch.aurorapunks.com` -> `http://localhost:3778` (same origin as old pitch host; ingress now 14 entries incl catch-all).
3. Origin 301 in `assistant/pitches-server.js`: Host-based redirect `pitch.runatyr.games/*` -> `https://pitch.aurorapunks.com/*`, preserving path+query. `/healthz` exempt so monitoring stays green on both hosts. Gated by env `PITCHES_CANONICAL_HOST` (default `pitch.aurorapunks.com`) - reversible by unsetting + restart. `pitches.service` restarted (user scope).

Verified: new host serves live slugs (200); old host 301s with path+query preserved; full chain lands 200; `/healthz` 200 on both. Live prospect links (/1993, /tcg-shop, /tears-of-adria, /blockem) unbroken.

Why origin-redirect not CF Redirect Rule: the scoped token (`CLOUDFLARE_API_TOKEN`) lacks Rulesets/Zone-Settings edit (same limitation as the 2026-06-17 HTTP/3 entry) - and both hosts hit the same origin anyway, so an origin Host-check is cleaner, version-controlled, and reversible.

Remaining in this workstream: `clients.runatyr.games` -> `client.aurorapunks.com` (:3780), `sign.runatyr.games` -> `sign.aurorapunks.com` (:3782, OpenSign - more delicate: already-issued signing links + Parse callback reconfig). Separate workstream: merge board/hive into Death Board (canonical) + retire Plane (needs sudo-docker data check first).

## 2026-06-17 - DevOps - aurorapunks.com ERR_QUIC_PROTOCOL_ERROR resolved (HTTP/3 disabled)

Robert reported the site unreachable in incognito (desktop) and on mobile data: `ERR_QUIC_PROTOCOL_ERROR` / "Webbplatsen kan inte nås".

Diagnosis (site was never actually down):
- HTTP/2 path fully healthy throughout: 12/12 rapid requests `200`, apex+www, http+https, `x-apw-prod:1`, TLS cert valid (reissued Jun 16). All services up (`aurorapunks-site.service`, cloudflared tunnel).
- Failure was isolated to the HTTP/3 (QUIC) edge path. Edge was advertising `alt-svc: h3=":443"; ma=86400`; browsers tried to upgrade to QUIC and the handshake failed (across two networks, so not local). Root cause: QUIC/edge cert provisioning lagged the Jun 16 cert rotation - TCP+TLS got the new cert, QUIC did not.

Fix:
- Robert toggled OFF **HTTP/3 (with QUIC)** in CF dashboard (zone aurorapunks.com). Verified from VPS: `alt-svc` header now gone, HTTP/2 `200` clean.
- Residual failure after toggle was browser-cached `alt-svc` (24h ma). Cleared via Chrome QUIC flag / full browser restart. Confirmed working by Robert.

Note: my CF API token (`CLOUDFLARE_API_TOKEN`, scoped DNS/tunnel) returns `9109 Unauthorized` on zone settings - could not flip via API. Open follow-ups: (1) DevOps to mint a CF token with Zone Settings:Edit; (2) add an HTTP/3-path monitor so QUIC-only failures alarm. Leave HTTP/3 off ~48h, then safe to re-enable once edge re-provisions QUIC cert.


## 2026-06-16 - DevOps - Cloudflare pre-flip prep + production serving (AP + RLR)

Wix down (both aurorapunks.com + robotlordrising.com 404). Prepped CF zones for the manual NS flip at Websupport (Robert's step). CF-side only - no NS/Websupport/Wix changes.

### aurorapunks.com (CF zone already existed, status=pending)
- Assigned CF nameservers: `dina.ns.cloudflare.com` + `marvin.ns.cloudflare.com`.
- Deleted 3 stale Wix apex A records (185.230.63.107/.171/.186) + www->cdn1.wixdns.net (scan imports).
- Added proxied CNAME apex + www -> tunnel (`769d4523...cfargotunnel.com`).
- Kept MX `1 aspmx.l.google.com` (DNS-only, Google Workspace - PRESERVED).
- Added SPF `v=spf1 include:_spf.google.com ~all` + DMARC `p=none rua=mailto:hello@aurorapunks.com`.
- Left `git.aurorapunks.com A 192.168.50.106` (private RFC1918 from Wix scan - non-routable, harmless; flag to Robert to delete).
- DKIM NOT added - Robert must generate in Google Admin.
- Verified via `dig @dina.ns.cloudflare.com`: MX/www/SPF/DMARC all correct. Apex A empty pre-activation (CNAME flattening only fires once zone goes active post-flip - confirmed against active runatyr zone behavior).

### robotlordrising.com (NOT yet in CF account)
- Token LACKS zone-create permission. Robert must add via dashboard "Add a site". BLOCKER.
- Ready-to-run script: `robotlordrising_site/cf-setup-rlr.sh` (recreates MX 10/20 -> mail.robotlordrising.com, A mail=195.74.38.202 CRITICAL, apex+www proxied CNAME -> tunnel). Re-verified all RLR live facts via dig.
- Placeholder page built: `robotlordrising_site/site/index.html` ("Robot Lord Rising - coming soon").

### Production serving (both, tunnel model, no nginx/sudo)
- `assistant/aurorapunks-server.js` (:3784, root aurorapunks_site/site) + `aurorapunks-site.service`.
- `assistant/robotlordrising-server.js` (:3785, root robotlordrising_site/site) + `robotlordrising-site.service`.
- Both systemd --user units, Restart=always, enabled + active. Loopback bind, tunnel = sole public path.
- Tunnel ingress added (4 hostnames) before catch-all via CF API.

### AP hero video
- Self-hosted: downloaded Wix CDN mp4 (19MB, HTTP 200 - Wix static CDN still up even though pages 404) to `site/assets/hero-bg.mp4`, repointed `<source>` in index.html. Poster fallback (assets/hero-bg.jpg) already present for graceful degrade.


## 2026-06-16 - UIbot - Split hero + console-porting removal

### Changes delivered
- **Change 1 - Split hero:** Replaced the old full-bleed background-image hero with a 50/50 CSS grid split. Video (Wix CDN, same source) on the left; hero intro copy ("BUILD IT. SHIP IT. EVOLVE IT." + paragraphs) on the right against `--dark-bg2`. Mobile breakpoint (<900px) collapses to single column: video panel on top (height capped to `56vw`, min 220px, max 360px), text panel below.
- **Change 2 - Console porting removed:** Deleted the `.console-section` HTML block and all its CSS (`.console-section`, `.console-image`, `.console-text`), plus the orphaned mobile overrides for those classes. No layout gaps remain.
- **Old video section removed:** The standalone `<section class="video-section">` (mid-page) was also removed - video now lives exclusively in the split hero.

### Verification (all pass)
- Desktop 1440px: 720px / 720px grid columns, video left + text right rendered correctly
- Mobile 390px: single column, video above text, both full-width
- Console porting: no `.console-section` in DOM, no matching CSS rules, porting text absent from HTML
- Services, business models, footer: all intact (3 service items, 2 model cards, footer present)

### Screenshots
- `aurorapunks_site/screenshots/desktop-1440-hero.png` (full page)
- `aurorapunks_site/screenshots/desktop-1440-viewport-only.png` (viewport only, hero detail)
- `aurorapunks_site/screenshots/mobile-390-hero.png` (full page)

## 2026-06-15 - DevOps - Preview URL live + go-live plan written

### Preview (Part 1 - executed)
- Live: **https://aurorapunks-preview.runatyr.games/** (verified HTTP/2 200, page + assets render, `x-apw-preview` origin header confirms our serving stack)
- Served by `assistant/aurorapunks-preview-server.js` (zero-dep Node static server, mirror of pitches-server.js) on loopback `127.0.0.1:3783`
- systemd user unit `aurorapunks-preview.service` (enabled, Restart=always); logs at `assistant/logs/aurorapunks-preview.log`
- Fronted via the `deathboard` cloudflared tunnel: added ingress route (`aurorapunks-preview.runatyr.games -> http://localhost:3783`) + proxied CNAME to `cfargotunnel.com`, both via the scoped `CLOUDFLARE_API_TOKEN` (NOT local config.yml — the tunnel is remote-managed)
- Hero video still points at Wix CDN (`video.wixstatic.com/.../file.mp4`), fonts at Google Fonts — fine for preview, flagged for production self-hosting

### Go-live plan (Part 2 - plan only, NOT executed)
- Written to `aurorapunks_site/GO-LIVE-PLAN.md`: mail-safe ordered cutover (recreate MX→aspmx + add SPF/DKIM/DMARC in CF before NS flip), tunnel-CNAME serving (recommends over nginx/A-record), NS flip at Loopia (dina/marvin.ns.cloudflare.com), renewal-before-2026-07-07 + CF Registrar transfer option, contact-form backend future item
- Verified live facts: NS=Wix, MX=aspmx.l.google.com, no SPF/DKIM/DMARC, root A=Wix IPs

## 2026-06-15 - UIbot - Phase 1 complete: reference capture + homepage build

### Reference Capture
- Navigated full Wix site (10 pages attempted)
- 4 live pages: homepage, game-publishing-and-marketing, co-development, full-cycle-development
- 6 dead pages (Wix 404): post-launch-updates, ugc-platforms, branded-experience, gamification, about-us, blog
- Screenshots: desktop (1440px) + mobile (390px) for each page
- Full text captured via Playwright accessibility snapshots
- Computed styles extracted: fonts, colors, hex values
- All image assets downloaded to assets/
- INVENTORY.md written with full design system spec

### Homepage Build
- `site/index.html` - complete static faithful clone
- Sections: nav, hero, CTA banner, console porting, what we do, video, business models, contact form, footer
- All copy verbatim from live site (via accessibility snapshot)
- Colors: #0c0c1c bg, #65ede8/#1ab1ab/#5bbeba teal palette, white body text
- Fonts: Google Fonts Barlow Condensed (replaces Wix proprietary madefor-display-extrabold) + Chakra Petch
- Responsive: desktop + mobile breakpoints at 900px and 480px
- Form: mailto:hello@aurorapunks.com (DevOps item for proper endpoint)
- Video: links to Wix CDN (DevOps item: self-host before cutover)
- Social links: Twitter, YouTube, LinkedIn, Discord - all correct URLs

### Verification
All checklist items passed (see summary for checklist).

### Open Items (carried to CLAUDE.md)
- nginx vhost config
- Cloudflare DNS cutover
- Form handler endpoint
- Hero video self-hosting
- Phase 2 sub-pages
- favicon
