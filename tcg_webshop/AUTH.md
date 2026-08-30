# Auth for the pre-grade API

Written 2026-08-30 (tcg-002, item 3). **Decision needed from Robert.** Nothing
here is implemented; the API still runs one shared bearer token.

## What is wrong with what we have

`EXPO_PUBLIC_API_TOKEN` is inlined into the JS bundle by Expo, by design. That
is what the prefix means. Anyone holding the IPA holds the token, and there is
no build configuration that changes it. Three consequences:

1. **Rotation costs a build.** Changing the token means a new TestFlight build
   and every installed copy stops working until it updates. So in practice the
   token never rotates, which is the failure mode a rotation policy exists to
   prevent.
2. **There is one principal.** The API cannot tell the app from a script from
   whoever pulled the token out of the bundle. Rate limiting, per-user quotas
   and revoking one device are all impossible because there is nothing to
   attach them to.
3. **It does not survive the App Store.** Public distribution means handing the
   token to everyone who installs. Every vision pass is a paid Claude call
   against Robert's account, so the exposure is not "someone reads a report",
   it is "someone spends money".

Today's blast radius is small and worth stating plainly: the TestFlight group
is one internal tester, the token gates a pre-grade engine and nothing else,
and the API writes only into `intake/` and `reports/`. This is a
launch blocker, not an incident.

## The three options

### A. Cloudflare Access service token

Put the hostname behind Access and give the app a service token
(`CF-Access-Client-Id` / `CF-Access-Client-Secret`), the same gate
`board.runatyr.games` already uses.

- **For:** no origin code to write, revocation is a dashboard click, and it
  matches the platform pattern already in use.
- **Against:** it is still one shared credential baked into the bundle. It
  makes rotation cheap and revocation possible, but it does not create a
  per-user identity, and `sec-022` records that we currently cannot read Access
  logs, so "who used it" stays unanswerable.
- **Effort:** hours. **Fixes:** rotation, revocation. **Does not fix:** identity.

### B. Per-device enrollment

First launch generates a keypair on the device, posts the public key to
`/api/devices` with a short enrollment code Robert issues, and the API stores
it. Requests carry a signature; the server keeps a device list it can revoke
per row.

- **For:** real per-device identity with no accounts, no passwords and no
  personal data. Quotas and revocation become per-device. Nothing secret ships
  in the bundle. It fits a tool whose entire user base is a small known group.
- **Against:** the most code, and enrollment codes need somewhere to live and
  expire.
- **Effort:** a day or two. **Fixes:** rotation, revocation, identity, quotas.

### C. Sign in with Apple

Real accounts. The app gets an identity token, the API verifies it against
Apple's JWKS and issues its own session.

- **For:** the only option that survives an actual public launch with strangers
  in it, and on iOS it is the login users expect. Apple requires it anyway if
  the app ever offers third-party sign-in.
- **Against:** most moving parts, and it introduces user accounts to a tool
  that has no other reason to have them. Also brings App Store account-deletion
  obligations.
- **Effort:** several days. **Fixes:** everything, at the cost of a user system.

## Recommendation

**B, and only if the app stays internal. C if it goes public.**

The question that decides it is not technical: it is whether this tool is ever
handed to people outside the group. If it stays Robert plus a few known
collectors, per-device enrollment gives real identity for a fraction of C's
cost and adds no account system to maintain. If the App Store is genuinely on
the roadmap, B is throwaway work and C should be built once.

A is worth doing regardless, this week, as a stopgap: it takes hours, makes the
credential rotatable, and does not conflict with either B or C later.

## Also worth fixing whichever way this goes

- **`/api/health` is unauthenticated on purpose** so monitors can probe it. It
  leaks only `{ok, service, auth}`. That is fine, but it should stay that thin.
- **No rate limiting anywhere.** A leaked credential today means unbounded paid
  vision calls. A per-day cap on `/analyze` is cheap and independent of the
  auth choice. Recommend doing this alongside A.
- **`grade.aurorapunks.com` has no Access policy at all right now.** The bearer
  token is the only gate. Verified by curl on 2026-08-30: every route except
  `/api/health` answers 401 unauthenticated, and a wrong bearer also 401s, so
  it does fail closed. But there is no second layer.
