#!/usr/bin/env node
/**
 * In-place update of an existing Google Slides file from a local .pptx,
 * keeping the same fileId (and therefore the same share link).
 * Reuses Robert's OAuth creds the same way gdrive-upload.js does.
 *
 * Usage: node update_slides.js <fileId> <local.pptx>
 */
const fs = require('fs');
const path = require('path');

const HOME = process.env.HOME || process.env.USERPROFILE;
const CREDS_FILE = path.join(HOME, '.claude', '.gdrive-server-credentials.json');
const KEYS_FILE = path.join(HOME, '.claude', 'gcp-oauth.keys.json');

const PPTX_MIME = 'application/vnd.openxmlformats-officedocument.presentationml.presentation';

function loadKeys() { return JSON.parse(fs.readFileSync(KEYS_FILE, 'utf-8')).installed; }
function loadCreds() { return JSON.parse(fs.readFileSync(CREDS_FILE, 'utf-8')); }
function saveCreds(c) { fs.writeFileSync(CREDS_FILE, JSON.stringify(c, null, 2)); }

async function refreshToken(keys, creds) {
  const params = new URLSearchParams({
    client_id: keys.client_id,
    client_secret: keys.client_secret,
    refresh_token: creds.refresh_token,
    grant_type: 'refresh_token',
  });
  const res = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', body: params });
  const data = await res.json();
  if (data.error) throw new Error(`Token refresh failed: ${data.error_description}`);
  const updated = { ...creds, access_token: data.access_token, expiry_date: Date.now() + data.expires_in * 1000 };
  saveCreds(updated);
  return updated;
}

async function getToken() {
  const keys = loadKeys();
  let creds = loadCreds();
  if (creds.expiry_date && Date.now() > creds.expiry_date - 60000) {
    creds = await refreshToken(keys, creds);
  }
  return creds.access_token;
}

async function main() {
  const [fileId, pptxPath] = process.argv.slice(2);
  if (!fileId || !pptxPath) { console.error('Usage: node update_slides.js <fileId> <local.pptx>'); process.exit(1); }
  const abs = path.resolve(pptxPath);
  if (!fs.existsSync(abs)) { console.error('File not found:', abs); process.exit(1); }

  const token = await getToken();
  const content = fs.readFileSync(abs);

  // Multipart update: metadata keeps native-Slides mimeType so Drive re-converts
  // the uploaded pptx into the SAME presentation file (same id, same link).
  const metadata = { mimeType: 'application/vnd.google-apps.presentation' };
  const boundary = 'update_boundary_' + Date.now();
  const header = `--${boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n${JSON.stringify(metadata)}\r\n--${boundary}\r\nContent-Type: ${PPTX_MIME}\r\n\r\n`;
  const footer = `\r\n--${boundary}--`;
  const body = Buffer.concat([Buffer.from(header), content, Buffer.from(footer)]);

  const url = `https://www.googleapis.com/upload/drive/v3/files/${fileId}?uploadType=multipart&supportsAllDrives=true&fields=id,name,mimeType,webViewLink,modifiedTime`;
  const res = await fetch(url, {
    method: 'PATCH',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': `multipart/related; boundary=${boundary}` },
    body,
  });
  const result = await res.json();
  if (result.error) { console.error('Update failed:', JSON.stringify(result.error)); process.exit(1); }
  console.log('Updated in place!');
  console.log('  ID:', result.id);
  console.log('  Name:', result.name);
  console.log('  Type:', result.mimeType);
  console.log('  Modified:', result.modifiedTime);
  console.log('  Link:', result.webViewLink);
}

main().catch(e => { console.error('Error:', e.message); process.exit(1); });
