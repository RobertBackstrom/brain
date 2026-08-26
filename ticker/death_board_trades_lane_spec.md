# Death Board "Trades" Lane - Integration Spec

**Owner:** DevOps + UIbot  
**Status:** Not yet implemented (pending this spec)  
**Purpose:** Dedicated execution-decision channel for Ticker, separate from daily catch-up cards

## Why a Dedicated Lane

Execution decisions (go/no-go on a trade) must be **visually and notification-wise separate** from the daily digest cards. Robert needs to see them prominently and respond fast - burying them in the general queue means they get lost.

## Requirements

### 1. New Card Type: `trade-decision`

Structured fields (beyond the generic follow-up fields):

```json
{
  "type": "trade-decision",
  "project": "tkr",
  "ticker_symbol": "AAPL",
  "thesis": "Earnings beat + pullback to support - entry setup",
  "entry_price": 150.00,
  "target_price": 165.00,
  "stop_price": 145.00,
  "recommended_size_sek": 3500,
  "recommended_pct": 35,
  "invalidation": "Close below $145 or negative analyst revisions",
  "horizon": "position",
  "side": "Buy",
  "quantity": 23,
  "uic": 211,
  "account_key": "...",
  "created_at": "2026-06-17T08:30:00Z",
  "expires_at": "2026-06-17T20:00:00Z",
  "status": "awaiting_confirm | confirmed | rejected | expired | filled | cancelled"
}
```

### 2. UI Presentation

- **Dedicated column** in the kanban view, or a **separate tab/view** labeled "Trades" or "Execution Queue"
- Card shows:
  - Big symbol (e.g., **AAPL**)
  - Thesis (1-2 lines)
  - Entry / Target / Stop (formatted as prices)
  - Recommended size (SEK + %)
  - Horizon badge (swing / position / thesis)
  - Countdown timer if `expires_at` is set
  - Clear **CONFIRM** and **REJECT** actions (big buttons, not buried in a menu)

### 3. Confirmation Flow

When Robert clicks **CONFIRM**:
- Optionally prompt for final size adjustment (default = recommended)
- On confirm, the card's `status` → `confirmed`
- Trigger: `POST /api/ticker/execute` with the card data + Robert's final size
  - This endpoint calls `node assistant/saxo.js place-order <params>`
  - Returns order ID on success
- Card updates with order ID, shows "Order placed - awaiting fill"

When Robert clicks **REJECT**:
- Card's `status` → `rejected`
- Move to a "Rejected" or "Closed" section
- Log rejection to `ticker/trades_log.csv` (action: `rejected`)

### 4. Expiry Handling

If `expires_at` passes and status is still `awaiting_confirm`:
- Auto-transition to `expired`
- Move to "Expired" section
- No order placed

### 5. Fill Notification (webhook from Saxo or polling)

When Saxo reports a fill:
- Card's `status` → `filled`
- Show fill price + timestamp
- Log to `ticker/trades_log.csv` (action: `filled`, include fill_price)
- Move to "Filled" or "Done" section

### 6. Notifications

- **Discord ping** when a new trade-decision card is created (separate webhook or channel)
- **Discord ping** on fill or rejection
- Optional: SMS if Robert wants belt-and-suspenders for execution confirmations

### 7. Access Control

- Only Robert can confirm/reject (not other users if the board becomes multi-user later)
- Read-only view for auditing OK

## Technical Notes

- The `/api/ticker/execute` endpoint doesn't exist yet - DevOps builds it as part of `server.js`
- It should:
  1. Verify the card is `trade-decision` type and status is `awaiting_confirm`
  2. Check Robert's session/auth
  3. Load `ticker/risk_limits.json` and enforce caps
  4. Call `saxo.js place-order` with params from the card
  5. Update the card with order ID and new status
  6. Return success/error to the UI

- Card creation: Ticker agent can create these via the Death Board API (`POST /api/followups` with the right structure)
  
## Example Card Flow

1. **Ticker daily digest** runs at 06:00, spots a setup on AAPL
2. Ticker creates a `trade-decision` card:
   ```json
   {
     "type": "trade-decision",
     "title": "AAPL position entry",
     "ticker_symbol": "AAPL",
     "thesis": "Earnings beat + pullback to 21 EMA support",
     "entry_price": 150.00,
     "target_price": 165.00,
     "stop_price": 145.00,
     "recommended_size_sek": 3500,
     "expires_at": "2026-06-17T20:00:00Z"
   }
   ```
3. Discord pings Robert: "New trade decision: AAPL position entry - confirm by 20:00"
4. Robert opens the Trades lane, reviews, clicks **CONFIRM**, optionally adjusts size to 3000 SEK
5. Backend calls `saxo.js place-order`, gets order ID `ORD12345`
6. Card updates: "Order ORD12345 placed at $150.00 limit, awaiting fill"
7. (Later) Saxo reports fill at $150.25
8. Card → `filled`, Discord pings "AAPL filled @ $150.25"
9. Card moves to "Done"

## See Also

- [execution_spec_saxo.md](execution_spec_saxo.md) - full execution architecture
- [risk_limits.json](risk_limits.json) - caps and guardrails
- [trades_log.csv](trades_log.csv) - audit trail
