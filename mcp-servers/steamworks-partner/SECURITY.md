# Security Considerations

## API Key Management

### Never Commit Keys
- API keys should **never** be committed to version control
- `.gitignore` includes `.env` to prevent accidental commits
- Use `.env.example` as a template (keys removed)

### Key Storage
- Store keys in `.env` file (local development)
- For production/CI: use environment variables or secret management (GitHub Secrets, AWS Secrets Manager, etc.)
- For Claude Desktop: keys go in the `env` section of `claude_desktop_config.json`

### Key Types
1. **Publisher Key** — General Steamworks API access (apps, builds, news)
2. **Financial Key** — Revenue/sales data access (requires separate approval)

Both keys grant access to **sensitive publisher data**. Treat them like passwords.

## Key Rotation

If a key is compromised:
1. Immediately revoke it in Steamworks Partner dashboard
2. Generate a new key
3. Update `.env` or config files
4. Restart the MCP server / Claude Desktop

## API Permissions

### Read-Only Tools (Safe)
- `get_partner_apps`
- `get_sales_data`
- `get_wishlist_data`
- `get_news`
- `get_app_details`
- `get_reviews`
- `get_app_builds`
- `get_app_betas`

### Write Tools (Use Carefully)
- `set_app_build_live` (Phase 2) — Changes which build is live on a branch
  - **Risk:** Could accidentally push wrong build to production
  - **Mitigation:** Add confirmation prompt, implement dry-run mode

### Future Considerations
- SteamCMD integration (Phase 2) requires Steam Guard credentials
  - Use app-specific password if possible
  - Store TOTP secret securely (not in plain text)

## Rate Limiting

Steamworks API has rate limits (exact limits not publicly documented).

**Best practices:**
- Don't poll endpoints in tight loops
- Cache results where appropriate
- Implement exponential backoff on 429 responses
- Respect `Retry-After` headers

## Data Privacy

### What This Server Accesses
- Sales revenue and units sold
- Wishlist data (aggregated by country/language)
- User reviews (public data, but includes playtime)
- Build history and descriptions

### Who Can Access This Data
- Anyone with access to the MCP server logs
- Claude (or other MCP client) during conversations
- Any system where the MCP server is installed

**Recommendation:** Don't run this server on shared/public systems.

## Logging

The current implementation does **not** log API responses to disk.

If you add logging:
- Never log API keys
- Redact sensitive data (revenue numbers, user IDs)
- Rotate logs regularly
- Secure log files (chmod 600)

## Dependencies

This project uses npm packages. **Security risks:**
- Supply chain attacks (compromised packages)
- Vulnerable dependencies

**Mitigation:**
- Run `npm audit` regularly
- Keep dependencies up to date
- Review dependency changes before upgrading
- Use `package-lock.json` for reproducible builds

## Network Security

### HTTPS
Both Steamworks Partner API and Store API use HTTPS. Axios verifies SSL certificates by default.

### Environment
If running on a VPS or shared host:
- Use firewall rules to restrict access
- Don't expose the MCP server on public ports (stdio transport only)
- Use SSH tunneling if remote access is needed

## Vulnerability Reporting

If you discover a security issue:
1. **Do not** open a public GitHub issue
2. Email: robert@aurorapunks.com
3. Include: description, steps to reproduce, impact assessment
4. Allow reasonable time for a fix before public disclosure

## Compliance

### Steamworks API Terms of Service
Review [Steamworks API Agreement](https://partner.steamgames.com/doc/api/agreement) before using in production.

Key points:
- Don't use API data to compete with Steam
- Don't scrape data en masse
- Respect user privacy
- Don't redistribute API access

### GDPR / Data Protection
If handling EU user data (reviews, playtime):
- User reviews are public data (low risk)
- Aggregate wishlist data (no personal info)
- Sales data is business metrics (not personal data)

**Recommendation:** No special GDPR compliance needed for Phase 1 tools.

## Security Checklist

Before deploying to production:
- [ ] API keys stored securely (not in code)
- [ ] `.env` in `.gitignore`
- [ ] Dependencies audited (`npm audit`)
- [ ] Rate limiting implemented
- [ ] Error messages don't leak sensitive data
- [ ] Logging doesn't include API keys or credentials
- [ ] Access restricted to authorized users only
- [ ] Steamworks API ToS reviewed and complied with

---

**Last Updated:** 2026-04-17  
**Reviewed By:** GameDev Agent
