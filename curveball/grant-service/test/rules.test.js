import test from 'node:test';
import assert from 'node:assert/strict';
import {
  splitCurrencies, clampSoftCurrency, validateAssetGrant, validateCurrencyGrant,
  validateProgressionGrant, assertWithinCaps, assertMatchGrantable, RuleError, KIND,
} from '../src/rules.js';

const limits = {
  softCurrencyId: 'SOFT',
  softCurrencyCap: 6000,
  maxCurrencyPerMatch: 500,
  maxAssetsPerMatch: 4,
  maxProgressionPerMatch: 1000,
  windowSeconds: 3600,
  maxCurrencyPerWindow: 3000,
  maxAssetsPerWindow: 20,
  maxProgressionPerWindow: 6000,
  minMatchSeconds: 30,
  maxMatchSeconds: 3600,
  maxPlayersPerMatch: 16,
  allowedCurrencyIds: [],
  allowedProgressionKeys: [],
  allowedAssetIds: [],
};

test('duplicate currency entries are summed, credits and debits separated', () => {
  const { credit, debit } = splitCurrencies([
    { currencyId: 'SOFT', amount: 100 },
    { currencyId: 'SOFT', amount: 50 },
    { currencyId: 'HARD', amount: -20 },
    { currencyId: 'HARD', amount: -5 },
    { currencyId: 'NOOP', amount: 0 },
  ]);
  assert.deepEqual(credit, [{ currencyId: 'SOFT', amount: 150 }]);
  assert.deepEqual(debit, [{ currencyId: 'HARD', amount: 25 }]);
});

test('soft currency is clamped to the cap, never negative', () => {
  const atCap = clampSoftCurrency([{ currencyId: 'SOFT', amount: 500 }], { SOFT: 5800 }, limits);
  assert.equal(atCap[0].amount, 200);
  assert.equal(atCap[0].clamped, true);

  const overCap = clampSoftCurrency([{ currencyId: 'SOFT', amount: 500 }], { SOFT: 6500 }, limits);
  assert.equal(overCap[0].amount, 0);

  const other = clampSoftCurrency([{ currencyId: 'HARD', amount: 999999 }], { HARD: 0 }, limits);
  assert.equal(other[0].amount, 999999, 'only the soft currency is capped');
});

test('progression rejects zero, matching AddProgressionForPlayer', () => {
  assert.throws(() => validateProgressionGrant({ progressionKey: 'xp', amount: 0 }, limits), RuleError);
  assert.deepEqual(
    validateProgressionGrant({ progressionKey: 'xp', amount: -50 }, limits),
    { progressionKey: 'xp', amount: -50 },
  );
});

test('asset grants reject duplicates and non-positive ids', () => {
  assert.throws(() => validateAssetGrant([1, 1], limits), /duplicate_assets/);
  assert.throws(() => validateAssetGrant([0], limits), /bad_asset_id/);
  assert.throws(() => validateAssetGrant([], limits), /no_assets/);
  assert.deepEqual(validateAssetGrant([651820, 651824], limits), [651820, 651824]);
});

test('allow lists are enforced when configured, ignored when empty', () => {
  const locked = { ...limits, allowedCurrencyIds: ['SOFT'] };
  assert.throws(() => validateCurrencyGrant([{ currencyId: 'HARD', amount: 1 }], locked), /currency_not_allowed/);
  assert.doesNotThrow(() => validateCurrencyGrant([{ currencyId: 'HARD', amount: 1 }], limits));
});

test('caps count what the ledger already holds, so splitting does not help', () => {
  const matchTotals = { currency: 400, assets: 0, progression: 0 };
  const windowTotals = { currency: 400, assets: 0, progression: 0 };
  assert.doesNotThrow(() => assertWithinCaps({ kind: KIND.CURRENCY, amount: 100, matchTotals, windowTotals, limits }));
  assert.throws(
    () => assertWithinCaps({ kind: KIND.CURRENCY, amount: 101, matchTotals, windowTotals, limits }),
    /match_cap_exceeded/,
  );
});

test('window cap catches a host farming across matches', () => {
  const matchTotals = { currency: 0, assets: 0, progression: 0 };
  const windowTotals = { currency: 2900, assets: 0, progression: 0 };
  assert.throws(
    () => assertWithinCaps({ kind: KIND.CURRENCY, amount: 200, matchTotals, windowTotals, limits }),
    /window_cap_exceeded/,
  );
});

test('a match that just opened cannot already have produced rewards', () => {
  const now = 1_000_000;
  assert.throws(() => assertMatchGrantable({ opened_at: now - 5, closed_at: null }, limits, now), /match_too_young/);
  assert.throws(() => assertMatchGrantable({ opened_at: now - 60, closed_at: now }, limits, now), /match_closed/);
  assert.throws(() => assertMatchGrantable(null, limits, now), /unknown_match/);
  assert.doesNotThrow(() => assertMatchGrantable({ opened_at: now - 120, closed_at: null }, limits, now));
});
