# Aurora Punks Static Site

**Project:** aurorapunks.com static rebuild
**Prefix:** apw
**Owner:** Aurora Punks / Robert

## Context
Replacing the Wix-hosted aurorapunks.com with a self-hosted static site on the VPS (nginx). Wix + Loopia accounts being decommissioned.

## Scope
- Phase 1 (complete): Landing page (homepage) faithful static clone
- Phase 2 (future): Sub-pages - Game Publishing and Marketing, Co-Development, Full Cycle Development, About Us, Blog
- DevOps task: nginx vhost setup + Cloudflare DNS cutover (separate ticket)
- DevOps task: Form handler endpoint for contact form (currently mailto)

## Structure
- `wix-refs/` - Reference screenshots + INVENTORY.md from Wix capture (2026-06-15)
- `assets/` - Source image assets downloaded from Wix CDN
- `site/` - Built static site (deploy this directory)
  - `index.html` - Homepage
  - `assets/` - Images used by the site

## Design System
See `wix-refs/INVENTORY.md` for full color/font/layout spec.
Key colors: #0c0c1c (bg), #65ede8 (teal-bright H1), #1ab1ab (teal-mid H2), #ffffff (body text)
Fonts: Barlow Condensed (display, substitute for Wix madefor-display-extrabold), Chakra Petch (body/nav)

## Deploy
Site lives at `aurorapunks_site/site/` - serve this directory via nginx.
No build step required - pure static HTML/CSS.

## Open Items
- [ ] DevOps: nginx vhost config for aurorapunks.com -> this VPS
- [ ] DevOps: Cloudflare DNS cutover + Loopia decommission
- [ ] DevOps: Form handler endpoint (replace mailto fallback)
- [ ] Phase 2: Sub-page builds using wix-refs/ screenshots as reference
- [ ] favicon.ico not yet added
- [ ] Video asset: hero-bg video hosted on Wix CDN (wixstatic), will die with Wix - should be self-hosted
