// Append-only ledger of every match and every grant, on node:sqlite (no dependencies).
//
// Two jobs beyond bookkeeping:
//   1. Idempotency. The game's LootLockerApiQueue retries failed server calls, so the
//      same grant will arrive twice. Keyed on request_id, the second call returns the
//      first call's result instead of granting again.
//   2. It is the evidence for the plausibility rules. Per-match and per-window totals
//      are read back out of here, so a host cannot get around a cap by splitting a
//      grant into pieces.

import { DatabaseSync } from 'node:sqlite';
import fs from 'node:fs';
import path from 'node:path';

const SCHEMA = `
CREATE TABLE IF NOT EXISTS matches (
  id            TEXT PRIMARY KEY,
  host_steam_id TEXT,
  mode          TEXT,
  opened_at     INTEGER NOT NULL,
  closed_at     INTEGER,
  player_count  INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS match_players (
  match_id  TEXT NOT NULL,
  player_id INTEGER NOT NULL,
  ulid      TEXT,
  steam_id  TEXT,
  PRIMARY KEY (match_id, player_id)
);
CREATE TABLE IF NOT EXISTS grants (
  request_id      TEXT PRIMARY KEY,
  match_id        TEXT NOT NULL,
  player_id       INTEGER NOT NULL,
  kind            TEXT NOT NULL,
  amount          INTEGER NOT NULL DEFAULT 0,
  currency_id     TEXT,
  progression_key TEXT,
  asset_count     INTEGER NOT NULL DEFAULT 0,
  request_json    TEXT NOT NULL,
  applied_json    TEXT NOT NULL,
  identity_proven INTEGER NOT NULL DEFAULT 0,
  created_at      INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS grants_by_player_time ON grants (player_id, created_at);
CREATE INDEX IF NOT EXISTS grants_by_match ON grants (match_id, player_id);
`;

export class Ledger {
  constructor(dbPath) {
    if (dbPath !== ':memory:') fs.mkdirSync(path.dirname(dbPath), { recursive: true });
    this.db = new DatabaseSync(dbPath);
    this.db.exec('PRAGMA journal_mode = WAL;');
    this.db.exec(SCHEMA);
  }

  close() {
    this.db.close();
  }

  openMatch({ id, hostSteamId, mode, players, now }) {
    this.db.prepare(
      'INSERT INTO matches (id, host_steam_id, mode, opened_at, player_count) VALUES (?, ?, ?, ?, ?)',
    ).run(id, hostSteamId, mode ?? null, now, players.length);
    const ins = this.db.prepare(
      'INSERT INTO match_players (match_id, player_id, ulid, steam_id) VALUES (?, ?, ?, ?)',
    );
    for (const p of players) ins.run(id, p.playerId, p.ulid ?? null, p.steamId ?? null);
  }

  closeMatch(id, now) {
    this.db.prepare('UPDATE matches SET closed_at = ? WHERE id = ? AND closed_at IS NULL').run(now, id);
  }

  getMatch(id) {
    const row = this.db.prepare('SELECT * FROM matches WHERE id = ?').get(id);
    if (!row) return null;
    const players = this.db.prepare('SELECT * FROM match_players WHERE match_id = ?').all(id);
    return { ...row, players };
  }

  isPlayerInMatch(matchId, playerId) {
    const row = this.db.prepare(
      'SELECT 1 AS ok FROM match_players WHERE match_id = ? AND player_id = ?',
    ).get(matchId, playerId);
    return Boolean(row);
  }

  findGrant(requestId) {
    const row = this.db.prepare('SELECT * FROM grants WHERE request_id = ?').get(requestId);
    return row ? { ...row, applied: JSON.parse(row.applied_json) } : null;
  }

  recordGrant(entry) {
    this.db.prepare(`
      INSERT INTO grants (request_id, match_id, player_id, kind, amount, currency_id,
                          progression_key, asset_count, request_json, applied_json,
                          identity_proven, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).run(
      entry.requestId, entry.matchId, entry.playerId, entry.kind, entry.amount ?? 0,
      entry.currencyId ?? null, entry.progressionKey ?? null, entry.assetCount ?? 0,
      JSON.stringify(entry.request), JSON.stringify(entry.applied),
      entry.identityProven ? 1 : 0, entry.now,
    );
  }

  // Positive totals only. A debit does not buy back headroom under a cap, otherwise
  // a host could credit, debit and credit again to walk past it.
  totalsForMatch(matchId, playerId) {
    const row = this.db.prepare(`
      SELECT
        COALESCE(SUM(CASE WHEN kind = 'currency'    AND amount > 0 THEN amount END), 0) AS currency,
        COALESCE(SUM(CASE WHEN kind = 'progression' AND amount > 0 THEN amount END), 0) AS progression,
        COALESCE(SUM(asset_count), 0) AS assets
      FROM grants WHERE match_id = ? AND player_id = ?
    `).get(matchId, playerId);
    return { currency: row.currency, progression: row.progression, assets: row.assets };
  }

  totalsInWindow(playerId, sinceEpoch) {
    const row = this.db.prepare(`
      SELECT
        COALESCE(SUM(CASE WHEN kind = 'currency'    AND amount > 0 THEN amount END), 0) AS currency,
        COALESCE(SUM(CASE WHEN kind = 'progression' AND amount > 0 THEN amount END), 0) AS progression,
        COALESCE(SUM(asset_count), 0) AS assets
      FROM grants WHERE player_id = ? AND created_at >= ?
    `).get(playerId, sinceEpoch);
    return { currency: row.currency, progression: row.progression, assets: row.assets };
  }
}

export default Ledger;
