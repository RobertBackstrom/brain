---
name: project_aurorapunks_website
description: "aurorapunks.com + robotlordrising.com fully migrated Wix→Cloudflare (site, DNS, mail, registrar); end state + reusable gotchas"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7e2c3ca1-d5dc-4014-8628-ee0406b4b1e3
---

Both **aurorapunks.com** and **robotlordrising.com** were migrated off Wix (which had gone down) onto Cloudflare + the VPS, completed 2026-06-16. Cloudflare is now registrar + DNS + edge for both; sites self-hosted on the VPS behind the deathboard tunnel. Wix and Websupport accounts cancelled by Robert afterward. Ticket: `apw-001`.

**End state (2026-06-16):**
- **aurorapunks.com** — site = VPS-hosted static clone (`aurorapunks_site/site/`, served by `assistant/aurorapunks-server.js` :3784 via tunnel); mail = Google Workspace (`MX → aspmx.l.google.com`) + SPF + DKIM (`google._domainkey`) + DMARC; registrar = Cloudflare (exp 2027-07-07).
- **robotlordrising.com** — apex+www 301-redirect to its Steam page (app 1420120) via `assistant/robotlordrising-server.js` :3785; mail preserved (`MX 10/20 → mail.robotlordrising.com`, `mail A → 195.74.38.202`, DNS-only); registrar = Cloudflare (exp 2027-07-13).
- Both NS = `dina`/`marvin.ns.cloudflare.com`. Build source + go-live runbook in `aurorapunks_site/` (GO-LIVE-PLAN.md).

**Reusable gotchas (for the next migration):**
- Registrar topology = **Websupport** (portal) → **Ascio** (wholesale, IANA 106) → Loopia (sister brand). Transfer-away FOA from `null@ascio.com`, approve at `approval.ascio.com` ("I accept" = minutes vs 5-day auto).
- **DNSSEC**: Websupport panel showed "Aktiverad" but no DS was published in `.com` (verify via `dig DS @1.1.1.1`) — so NS flips were safe with no 24h wait. Don't trust the panel toggle; check the real parent DS.
- Cloudflare's onboarding **scan imported stale Wix records and proxied the RLR mail A** — always review; mail/MX A records must be DNS-only (grey), never proxied.
- Apex CNAME flattens to CF edge IPs only once the zone is **active** (post-NS-flip); empty apex A on a pending zone is normal, not a bug.
- Websupport login is passkey/WebAuthn + reCAPTCHA — not automatable; human-driven + screenshots.
- AP hero video self-hosts fine (`video.wixstatic.com` CDN kept serving even with the Wix site down).
- **HTTP/3 after cert rotation**: a CF edge cert rotation can leave the QUIC/HTTP-3 cert lagging while HTTP/2 picks up the new cert immediately → browsers fail with `ERR_QUIC_PROTOCOL_ERROR` while every VPS HTTP/2 check stays green. Tell: `alt-svc: h3` present but QUIC handshake fails. Fix: toggle HTTP/3 off on the zone; clients must clear cached alt-svc (24h ma). Re-enable after ~48h. (Incident 2026-06-17, apw-001; full detail in DevOps learnings.)

**Future:** client-facing RAG/wiki ("wiki page for AP" was stale) — separate project Robert wants help with.

Related: [[feedback_vps_operating_environment]], [[project_aurora_punks]] (AP AB governance), [[project_rlr_ip_dispute]].
