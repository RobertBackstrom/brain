---
name: Secrets registry convention
description: All infra secrets are tracked in /home/assistant/projects/secrets_registry.md by stable `<domain>.<purpose>` ID, values in VPS .env + LastPass backup
type: feedback
originSessionId: 1ad5f5c9-0e2d-42d9-8dc7-b9b21d66dce4
modified: 2026-08-16T18:26:15.436Z
---
All infra secrets (API keys, webhook secrets, tokens) must be tracked in `/home/assistant/projects/secrets_registry.md` using a stable `<domain>.<purpose>` ID (e.g. `atlassian.webhook`, `discord.bot-token`). Values live in VPS `/home/assistant/projects/assistant/.env` (runtime) and LastPass under `Runatyr Infra` folder (backup, Robert owns). The registry file itself holds metadata only — never values.

**Why:** Robert asked for a system where he and Claude can both refer to secrets unambiguously across sessions and tools. Without IDs, conversations about "the webhook secret" get ambiguous when more than one exists.

**Reading a secret: never `source .env`.** Read the single value you need directly:

```bash
TOKEN=$(grep -m1 '^CLOUDFLARE_API_TOKEN=' assistant/.env | cut -d= -f2- | tr -d '"'"'"' \r\n')
```

**Why (measured 2026-08-16, sec-020):** one unquoted value containing shell metacharacters is a
**syntax error that aborts sourcing**, so every variable declared *below it* is silently left unset.
On this box a single line 47 password left **38 of 58 secrets empty** for every shell consumer. The
failure mode is an empty string, not an error, so the API call returns "invalid Authorization header"
and reads exactly like a revoked token — the trap is that you go and rotate a perfectly good secret.
`${#VAR}` = 0 is the tell. (The file was fixed, but read directly regardless: it is immune either way,
and the same class of line can reappear on any new secret.)

Note the same file parses **differently for three consumers**: systemd `EnvironmentFile` and Node's
`dotenv` both handle it correctly, only bash aborts. So services can be perfectly healthy while every
agent shell silently sees nothing. If you change `.env` quoting, verify across all three.

**How to apply:**
- When creating a new secret: generate the value, append to VPS `.env` with a comment line naming the ID, add a metadata entry in `secrets_registry.md`. Tell Robert to mirror it into LastPass under the same ID.
- **Quote any value containing spaces or shell metacharacters** (`< > ( ) & ; | $ \` ! * ? [ ] { } #`) when writing it to `.env`, single quotes preferred.
- When referencing a secret in conversation, tickets, or docs: use the ID (`atlassian.webhook`) not a description (`the Atlassian webhook secret`).
- Never put values in git, CLAUDE.md, memory files, plan files, or ticket bodies.
- Never touch LastPass — that's Robert's boundary.
- See skill `[[secrets_registry]]` for the full convention.
