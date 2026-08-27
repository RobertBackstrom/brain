import test from 'node:test';
import assert from 'node:assert/strict';
import { HmacVerifier, NonceCache, sign } from '../src/auth.js';

const SECRET = 'test-secret';

function verifierAt(nowRef) {
  return new HmacVerifier({
    secret: SECRET,
    clockSkewSeconds: 60,
    nonceCache: new NonceCache(300),
    now: () => nowRef.value,
  });
}

function signedRequest({ timestamp, nonce, body = '{"a":1}', path = '/v1/grant/currency', secret = SECRET }) {
  return {
    method: 'POST',
    path,
    rawBody: body,
    headers: {
      'x-mlc-timestamp': String(timestamp),
      'x-mlc-nonce': nonce,
      'x-mlc-signature': sign(secret, 'POST', path, timestamp, nonce, body),
      'x-mlc-steam-id': '76561198000000007',
    },
  };
}

test('a correctly signed request passes and reports an unproven identity', () => {
  const now = { value: 1_700_000_000 };
  const v = verifierAt(now);
  const res = v.verify(signedRequest({ timestamp: now.value, nonce: 'n1' }));
  assert.equal(res.ok, true);
  assert.equal(res.caller.identityProven, false, 'hmac asserts identity, it does not prove it');
});

test('a tampered body invalidates the signature', () => {
  const now = { value: 1_700_000_000 };
  const v = verifierAt(now);
  const req = signedRequest({ timestamp: now.value, nonce: 'n2' });
  req.rawBody = '{"a":2}';
  assert.equal(v.verify(req).error, 'bad_signature');
});

test('a replayed nonce is refused even with a valid signature', () => {
  const now = { value: 1_700_000_000 };
  const v = verifierAt(now);
  const req = signedRequest({ timestamp: now.value, nonce: 'n3' });
  assert.equal(v.verify(req).ok, true);
  assert.equal(v.verify(req).error, 'nonce_replayed');
});

test('a stale timestamp is refused', () => {
  const now = { value: 1_700_000_000 };
  const v = verifierAt(now);
  const req = signedRequest({ timestamp: now.value - 3600, nonce: 'n4' });
  assert.equal(v.verify(req).error, 'timestamp_outside_window');
});

test('the wrong secret does not sign', () => {
  const now = { value: 1_700_000_000 };
  const v = verifierAt(now);
  const req = signedRequest({ timestamp: now.value, nonce: 'n5', secret: 'other' });
  assert.equal(v.verify(req).error, 'bad_signature');
});

test('nonces expire out of the cache so it cannot grow without bound', () => {
  const cache = new NonceCache(10);
  assert.equal(cache.claim('a', 100), true);
  assert.equal(cache.claim('a', 105), false);
  assert.equal(cache.claim('b', 200), true);
  assert.equal(cache.size, 1, 'the expired nonce was swept');
});
