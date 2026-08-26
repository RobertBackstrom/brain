#!/usr/bin/env node
/* Create a Gmail draft WITH a PDF attachment, on an existing thread.
 * Reuses the OAuth creds from gmail-draft.js / gmail-archive.js. */
const fs = require('fs');
const path = require('path');
const HOME = process.env.HOME;
const CREDS_FILE = path.join(HOME, '.claude', '.gmail-archive-credentials.json');
const KEYS_FILE = path.join(HOME, '.claude', 'gcp-oauth.keys.json');

const TO = 'tom@experimentation.group';
const SUBJECT = 'Re: Aurora Punks * Teef Brief';
const THREAD_ID = '19ebb4a5e69ab2ab';
const PDF = '/home/assistant/projects/teef/pdf/Teef_Proposal_Summary.pdf';
const BODY = `Hi Tom,

Had a proper look at the updated brief. Revised proposal is in - living doc updated at the same link (password as before): https://pitch.aurorapunks.com/teef/ and a fresh one-page summary attached.

TL;DR: tighter scope, one number, price down to EUR 85k.

The scope cut collapses the two options into one. Mayfair is out and Soho is built to read as London rather than street-accurate, so the old A/B split falls away - single quote now. Four missions in Soho, around 60 minutes, five-week build.

EUR 85k, down from 110k. Build EUR 69k + independent functional and compliance QA via Northify (EUR 8k) + a 10 percent contingency against the fixed end-Q4 date. Everything else stands: senior team, pass-through at cost, Unity engine license with you, 30/40/20/10 milestones, and you own all code, art and audio on delivery.

The systems carry over largely unchanged, so the saving is in content and map art. Gameplay code and UI are still the heavy part, and we have weighted the quote there.

Happy to jump on a call whenever suits.

Cheers,
Robert`;

async function getToken() {
  const keys = JSON.parse(fs.readFileSync(KEYS_FILE, 'utf-8')).installed;
  let creds = JSON.parse(fs.readFileSync(CREDS_FILE, 'utf-8'));
  if (!creds.expiry_date || creds.expiry_date < Date.now() + 60000) {
    const params = new URLSearchParams({ client_id: keys.client_id, client_secret: keys.client_secret, refresh_token: creds.refresh_token, grant_type: 'refresh_token' });
    const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', body: params });
    const d = await r.json();
    if (d.error) throw new Error(d.error_description);
    creds = { ...creds, access_token: d.access_token, expiry_date: Date.now() + d.expires_in * 1000 };
    fs.writeFileSync(CREDS_FILE, JSON.stringify(creds, null, 2));
  }
  return creds.access_token;
}

function b64(s) { return Buffer.from(s, 'utf-8').toString('base64'); }
function enc(v) { return /[^\x00-\x7F]/.test(v) ? `=?UTF-8?B?${b64(v)}?=` : v; }

function buildRaw() {
  const B = '==TEEF_BOUNDARY_8f3a==';
  const pdf = fs.readFileSync(PDF).toString('base64').replace(/(.{76})/g, '$1\r\n');
  const msg = [
    `To: ${enc(TO)}`,
    `Subject: ${enc(SUBJECT)}`,
    'MIME-Version: 1.0',
    `Content-Type: multipart/mixed; boundary="${B}"`,
    '',
    `--${B}`,
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: base64',
    '',
    b64(BODY).replace(/(.{76})/g, '$1\r\n'),
    `--${B}`,
    'Content-Type: application/pdf; name="Teef_Proposal_Summary.pdf"',
    'Content-Disposition: attachment; filename="Teef_Proposal_Summary.pdf"',
    'Content-Transfer-Encoding: base64',
    '',
    pdf,
    `--${B}--`,
    ''
  ].join('\r\n');
  return Buffer.from(msg, 'utf-8').toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

(async () => {
  const token = await getToken();
  const res = await fetch('https://gmail.googleapis.com/gmail/v1/users/me/drafts', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: { raw: buildRaw(), threadId: THREAD_ID } })
  });
  if (!res.ok) throw new Error(await res.text());
  const d = await res.json();
  console.log('Draft created:', d.id, 'msg:', d.message && d.message.id);
})().catch(e => { console.error(e.message); process.exit(1); });
