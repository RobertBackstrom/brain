# pitches/

Static HTML one-pagers served at `pitch.aurorapunks.com/<slug>`.

> **Host migrated 2026-06-18 (apw):** canonical is `pitch.aurorapunks.com`. The old `pitch.runatyr.games` still resolves but permanently 301-redirects here. Both hostnames reach the same origin via the deathboard tunnel.

## Slug convention

Each pitch is its own folder. Slug = the URL path segment.

```
pitches/
├── 1993/
│   ├── index.html
│   └── steam-media/    (or assets/)
├── sir-whoopass/
│   └── index.html
└── ...
```

Access: `https://pitch.aurorapunks.com/<slug>` → renders `pitches/<slug>/index.html`.

Extensionless routing: `pitch.aurorapunks.com/1993` → `pitches/1993/index.html` (Express `express.static` serves the folder index automatically).

## Adding a new pitch

1. BizDev drafts copy + UIbot builds HTML in `drafts/<ticket-id>/`
2. When approved, `cp -r drafts/<ticket-id>/ pitches/<slug>/`
3. URL is immediately live — no deploy needed, no server restart needed (Express serves fresh on every request)
4. Update the LinkedIn message or email with `https://pitch.aurorapunks.com/<slug>`

## Conventions

- **Pages are public.** Default per [`feedback_deck_format_publish_web.md`](../../.claude/projects/-home-assistant-projects/memory/feedback_deck_format_publish_web.md). Don't drop sensitive financials or pre-release contract terms in here.
  - **Exception: gated slugs.** A slug listed in `assistant/pitch-auth.json` is behind HTTP Basic Auth and may carry commercials or financials. `owners` (the AP shareholder update) is one of these and holds live P&L figures. Check `pitch-auth.json` before assuming a slug is public, and never move a gated page's content to an ungated slug.
- **Slug = URL.** Keep slugs short, readable, no underscores — use hyphens if you must (`sir-whoopass`, not `sir_whoopass`).
- **Self-contained assets.** Reference local media via relative paths (`./steam-media/...`). Don't hotlink to Steam CDN.
- **Mobile-friendly.** LinkedIn opens links in their in-app browser; check narrow-viewport rendering before ship.

## Infrastructure

Served by `assistant/pitches-server.js` (Express static on port 3778), fronted by cloudflared ingress `pitch.aurorapunks.com → localhost:3778`. See [db-042](../assistant/followups/db-042-pitch-runatyr-games-hosting.md) for the deploy.
