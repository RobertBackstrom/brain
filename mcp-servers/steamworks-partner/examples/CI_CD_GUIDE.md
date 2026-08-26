# CI/CD Integration Guide

This guide shows how to integrate the Steamworks Partner MCP Server into your continuous integration and deployment pipelines.

## Overview

The Steamworks MCP provides two main ways to deploy builds:

1. **API-based deployment** (`set_app_build_live`) - Switch an existing build to live
2. **SteamCMD-based deployment** - Upload new builds from CI/CD

## Prerequisites

### Required Credentials

1. **Steamworks Publisher API Key**
   - Get from: https://partner.steamgames.com/doc/webapi_overview/auth
   - Used for: Verifying builds, querying status

2. **Steam Account Credentials**
   - Username and password for build uploads
   - **Steam Guard:** First-time SteamCMD login requires a Steam Guard code
   - Consider creating a dedicated CI/CD Steam account

3. **App Configuration**
   - Steam App ID
   - Depot ID(s) for your game
   - Branch names (e.g., `default`, `beta`, `staging`)

### Install SteamCMD

**Ubuntu/Debian:**
```bash
sudo add-apt-repository multiverse
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install steamcmd
```

**macOS:**
```bash
brew install steamcmd
```

**Windows:**
Download from: https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip

## Workflow Options

### Option 1: API-Only (Existing Builds)

If you upload builds manually or via another process, use the MCP to just switch builds live:

```typescript
// Using the MCP tool
{
  "name": "set_app_build_live",
  "arguments": {
    "appid": 123456,
    "buildid": 987654,
    "branch": "default"
  }
}
```

**When to use:**
- Builds are uploaded by developers manually
- You want to automate just the "go live" step
- Testing or staged rollouts

### Option 2: Full Upload Pipeline

Upload new builds directly from CI/CD:

1. Build your game in CI
2. Generate VDF script with MCP
3. Upload with SteamCMD
4. Verify via API

See `github-actions-upload.yml` and `gitlab-ci-upload.yml` for examples.

## Security Best Practices

### Protecting Credentials

**GitHub Actions:**
```yaml
# Use repository secrets
env:
  STEAM_USERNAME: ${{ secrets.STEAM_USERNAME }}
  STEAM_PASSWORD: ${{ secrets.STEAM_PASSWORD }}
```

**GitLab CI:**
```yaml
# Use protected CI/CD variables (Settings → CI/CD → Variables)
# Mark as "Masked" and "Protected"
variables:
  STEAM_USERNAME: $STEAM_USERNAME
  STEAM_PASSWORD: $STEAM_PASSWORD
```

### Steam Guard Challenges

**Problem:** SteamCMD requires Steam Guard code on first login from new machine.

**Solutions:**

1. **Pre-authorize CI runner** (recommended for self-hosted runners)
   - Run SteamCMD login once manually on the runner
   - Steam Guard files persist in `~/.steam/`

2. **Disable Steam Guard** (not recommended)
   - Only for dedicated CI accounts
   - High security risk

3. **Use environment variable**
   ```bash
   steamcmd +login "$USERNAME" "$PASSWORD" "$GUARD_CODE" +quit
   ```
   - Requires manual intervention on each new machine

## Example: GitHub Actions

```yaml
name: Deploy to Steam

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build game
        run: |
          # Your game build commands
          ./build.sh

      - name: Install SteamCMD
        run: |
          sudo apt install -y steamcmd

      - name: Upload to Steam
        env:
          STEAM_USERNAME: ${{ secrets.STEAM_USERNAME }}
          STEAM_PASSWORD: ${{ secrets.STEAM_PASSWORD }}
        run: |
          # Generate VDF script (using MCP)
          node generate-script.js
          # Upload
          steamcmd +login "$STEAM_USERNAME" "$STEAM_PASSWORD" \
            +run_app_build ./app_build.vdf \
            +quit
```

See `github-actions-upload.yml` for complete example.

## Example: GitLab CI

```yaml
stages:
  - build
  - deploy

deploy_steam:
  stage: deploy
  script:
    - steamcmd +login "$STEAM_USERNAME" "$STEAM_PASSWORD" \
        +run_app_build ./app_build.vdf \
        +quit
  only:
    - tags
```

See `gitlab-ci-upload.yml` for complete example.

## Common Patterns

### Staged Rollout

Deploy to beta branch first, then promote to default:

```yaml
# Step 1: Deploy to beta
- steamcmd +login ... +run_app_build ./app_build_beta.vdf +quit

# Step 2: Test beta build
# (Manual or automated testing)

# Step 3: Promote to default via MCP
- curl -X POST mcp-endpoint \
    -d '{"tool":"set_app_build_live","args":{"appid":123,"buildid":456,"branch":"default"}}'
```

### Multi-Platform Builds

Upload different depots for Windows/Mac/Linux:

```yaml
- name: Upload Windows build
  run: steamcmd +run_app_build ./windows_build.vdf +quit

- name: Upload Linux build
  run: steamcmd +run_app_build ./linux_build.vdf +quit

- name: Upload Mac build
  run: steamcmd +run_app_build ./mac_build.vdf +quit
```

### Rollback on Failure

Use the MCP to switch back to previous build if deployment fails:

```yaml
- name: Deploy new build
  id: deploy
  run: steamcmd +run_app_build ./app_build.vdf +quit
  continue-on-error: true

- name: Rollback on failure
  if: steps.deploy.outcome == 'failure'
  run: |
    # Switch back to last known good build
    node -e "
    const mcp = require('./steamworks-mcp');
    mcp.setAppBuildLive(123456, LAST_GOOD_BUILD_ID, 'default');
    "
```

## Verification

After deployment, verify the build:

```bash
# Check latest build via API
curl "https://partner.steam-api.com/ISteamApps/GetAppBuilds/v1?key=$API_KEY&appid=$APP_ID" \
  | jq '.response.builds[0]'

# Or using MCP tool
{
  "name": "get_app_builds",
  "arguments": { "appid": 123456 }
}
```

## Troubleshooting

### SteamCMD hangs on login
- Check Steam Guard setup
- Verify credentials are correct
- Look for `~/.steam/error.log`

### Build upload fails
- Check depot configuration in Steamworks partner site
- Verify content root path is correct
- Check file permissions

### Build uploaded but not visible
- Wait 5-10 minutes for Steam to process
- Check Steamworks partner dashboard
- Verify branch name matches

## Next Steps

- Review `TESTING.md` for manual testing
- Set up monitoring with Phase 3 tools (review alerts, sales tracking)
- Consider Death Board integration for automated notifications

## Resources

- [SteamCMD Wiki](https://developer.valvesoftware.com/wiki/SteamCMD)
- [Steamworks Build Upload](https://partner.steamgames.com/doc/sdk/uploading)
- [VDF Script Reference](https://partner.steamgames.com/doc/sdk/uploading#3)
