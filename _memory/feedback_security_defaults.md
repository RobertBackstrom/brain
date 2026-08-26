---
name: Security defaults for platform work
description: Hard defaults when building/reviewing Death Board or any Robert-owned VPS code — cover the six failure modes that the 2026-04-23 audit caught
type: feedback
originSessionId: 82050791-0030-4319-adc0-4a0ea51cedfd
---
When writing or reviewing any server/platform code for Robert (Death Board, cc-hive, trackers, webhook handlers), apply these as non-negotiable defaults. Don't wait for a security review to catch them.

1. **Verify public exposure before trusting auth claims.** If someone (Robert, another agent, a ticket, me) says a hostname is "behind Cloudflare Access" or any similar gate, curl it from outside the VPS first. Don't reason from the assumption.
2. **Fail closed when a signature secret is missing.** Any webhook handler that verifies HMAC signatures must refuse the request if its secret env var is unset (return 503). Never "warn and accept" — the unconfigured state is the one an attacker exploits.
3. **Never interpolate user input into shell strings.** Use `execFile(cmd, [args])` or `spawn(cmd, [args])`. `exec(string)` with any variable part is a shell-injection vulnerability regardless of escaping.
4. **HTTP-settable author/actor fields must be hardcoded or namespaced.** If any downstream code treats `author === "Claude"` (or any trusted name) as a trust signal, the HTTP endpoint that writes that field must force the author to a distinct value (e.g. `Robert`) — never accept author from the request body verbatim.
5. **Secrets must never be readable from an unauthenticated endpoint.** Not `GET /api/*/totp`, not `GET /api/*/token`, not even behind Cloudflare Access as sole protection. If headless auth is needed, keep it server-internal; expose only the action that uses the secret, not the secret itself.
6. **Sanitize user-controlled slugs at BOTH input and write boundaries when they flow to the filesystem.** IPC files, upload paths, ticket IDs — restrict to `^[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}$` at the HTTP endpoint AND defensively inside any function that writes via `path.join(dir, slug + ext)`. Defense in depth; an attacker who plants a bad slug in a markdown file still can't escape.

**Why:** the 2026-04-23 security audit of Robert's platform (see `assistant/followups/ops-security-audit-2026-04-23.md`) found 5 criticals + 5 highs, every one rooted in one of these six patterns. The umbrella issue — `hive.runatyr.games` and `board.runatyr.games` being on the open internet with no auth — was masked for weeks by the assumption that Cloudflare Access was on them like it was on `code.runatyr.games`. `/api/steam/totp` was leaking live Steam Guard codes to anyone who asked. Ticket creation + execute-now was a 2-POST-to-RCE chain. Robert had to rotate Steam Guard + change the Steam account password as a consequence.

**How to apply:** Any time I'm writing a new endpoint, webhook, tracker, or IPC path — or reviewing one — walk this list mentally before declaring done. Especially aggressive about #1 whenever the word "public", "internet-facing", "behind Access", or "tunneled" appears. Especially aggressive about #5 whenever code touches `process.env.*_SECRET`, `*_TOKEN`, or anything resembling a credential.
