# Next Steps for Steamworks Partner MCP Server

## Current Status

✅ **Phase 1 COMPLETE** — Core Analytics (8 read-only tools)  
✅ **Phase 2 COMPLETE** — Build Management (3 deployment tools + CI/CD examples)  
⏳ **Phase 3 IN PROGRESS** — Monitoring & Integration

## Immediate (Testing Phase 2)

1. **Test Build Management Tools**
   - [ ] Test `set_app_build_live` against ToA (switching beta builds, NOT production!)
   - [ ] Generate VDF scripts for ToA build
   - [ ] Test SteamCMD upload in safe environment (beta branch only)
   - [ ] Verify CI/CD examples work with ToA pipeline

2. **Security Review**
   - [ ] Audit WRITE operations for safety guardrails
   - [ ] Document rollback procedures
   - [ ] Test error handling for failed uploads
   - [ ] Verify Steam Guard handling

3. **Integration Testing**
   - [ ] Test full workflow: build → generate script → upload → verify → set live
   - [ ] Test with multiple branches (default, beta, staging)
   - [ ] Verify builds appear in Steamworks dashboard correctly
   - [ ] Document any discovered API quirks or Steam limitations

## Completed ✅

### Phase 1: Core Analytics
- [x] Scaffold MCP server (TypeScript, SDK)
- [x] Auth: Steamworks API key configuration
- [x] All 8 analytics tools implemented
- [x] Documentation complete

### Phase 2: Build Management
- [x] `set_app_build_live` tool implemented
- [x] SteamCMD wrapper module created
- [x] VDF build script generation
- [x] GitHub Actions example
- [x] GitLab CI example
- [x] CI/CD integration guide

## Phase 3: Monitoring & Integration

1. **Review Monitoring**
   - [ ] Add `monitor_reviews` tool (periodic pulls)
   - [ ] Sentiment analysis integration (OpenAI/Anthropic)
   - [ ] Flag negative reviews for response
   - [ ] Track review velocity and rating trends

2. **Wishlist Analytics**
   - [ ] Daily wishlist snapshot tracking
   - [ ] Trend detection (surges, drops)
   - [ ] Country/language breakdown visualization
   - [ ] Larry Loop integration for daily reports

3. **Sales Spike Detection**
   - [ ] Configurable threshold for "spike" definition
   - [ ] Daily sales comparison (today vs. 7-day avg)
   - [ ] Alert when threshold exceeded
   - [ ] Death Board auto-ticket creation

4. **Death Board Integration**
   - [ ] Auto-create follow-ups for review responses needed
   - [ ] Sales report cards on Death Board
   - [ ] Build deployment status updates
   - [ ] CCU monitoring with alerts

## Documentation & Community

1. **Battle-Test with ToA**
   - [ ] Use in production for 2-4 weeks
   - [ ] Collect real-world usage patterns
   - [ ] Document edge cases and gotchas
   - [ ] Refine tool descriptions based on usage

2. **Open Source Prep** (if decided)
   - [ ] Remove any ToA-specific references
   - [ ] Add CONTRIBUTING.md
   - [ ] Set up GitHub repo with Issues/Discussions
   - [ ] Write blog post announcing first Steamworks Partner MCP
   - [ ] Share on Reddit (r/gamedev, r/SteamDeck, r/ClaudeAI)
   - [ ] Submit to MCP directory/marketplace

3. **Advanced Features**
   - [ ] Support for multiple publishers (multi-key config)
   - [ ] Caching layer for frequently accessed data
   - [ ] WebSocket/SSE support for real-time monitoring
   - [ ] Integration with other game platforms (Epic, GOG)

## Security & Compliance

- [ ] Audit API key handling (never log keys)
- [ ] Document key rotation process
- [ ] Add security.md with vulnerability reporting
- [ ] Review Steamworks API Terms of Service for automation
- [ ] Add rate limiting to prevent abuse

## Known Issues to Address

1. Store API review pagination — need to handle cursor correctly
2. Financial API key approval process can take 1-2 days (document in README)
3. Some endpoints may return inconsistent JSON schemas (add error handling)
4. Build history may be large — consider adding limit parameter

---

**Current Status:** Phase 1 complete ✅  
**Priority:** Testing with real ToA data  
**Blocker:** Need Steamworks API keys from Robert
