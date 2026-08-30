// K&G Fiverr scout — 2026-08-30 4am sweep (unattended).
// Bounded run per skills/fiverr_scout_playwright.md: one search query, top gigs,
// throttled 2-4s, STOP on captcha/block (no solving, no blind retries).
import { chromium } from '/home/assistant/projects/assistant/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';

const OUT = '/home/assistant/projects/knives_and_gutters/art/logo/fiverr';
const QUERY = 'hand painted fantasy game logo illustration';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = () => sleep(2000 + Math.floor(Math.random() * 2000));

function blocked(title, body) {
  const t = (title + ' ' + body.slice(0, 4000)).toLowerCase();
  return ['access denied', 'captcha', 'human verification', 'are you a human', 'perimeterx', 'press & hold', 'blocked', 'attention required'].some((s) => t.includes(s));
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
  viewport: { width: 1440, height: 900 },
  locale: 'en-US',
});
const page = await ctx.newPage();
const result = { query: QUERY, status: 'unknown', gigs: [] };

try {
  await page.goto('https://www.fiverr.com/search/gigs?query=' + encodeURIComponent(QUERY), { waitUntil: 'domcontentloaded', timeout: 45000 });
  await sleep(4000);
  const title = await page.title();
  const body = await page.evaluate(() => document.body?.innerText || '');
  await page.screenshot({ path: path.join(OUT, '_search_page.png'), fullPage: false });

  if (blocked(title, body)) {
    result.status = 'blocked';
    result.page_title = title;
    console.log('BLOCKED at search page — stopping per anti-bot rule. Title:', title);
  } else {
    result.status = 'search-ok';
    // Gig cards: anchor hrefs matching /<seller>/<gig-slug> under the listings container.
    const gigs = await page.evaluate(() => {
      const seen = new Set();
      const out = [];
      for (const a of document.querySelectorAll('a[href*="/gigs/"], a[href^="/"][href*="?context_referrer"]')) {
        const href = a.getAttribute('href') || '';
        const m = href.match(/^\/([a-z0-9_]+)\/([a-z0-9-]+)\?/i);
        if (!m || seen.has(m[0])) continue;
        const card = a.closest('div');
        const text = card ? card.innerText.slice(0, 400) : '';
        seen.add(m[0]);
        out.push({ seller: m[1], url: 'https://www.fiverr.com' + href.split('?')[0], cardText: text });
        if (out.length >= 15) break;
      }
      return out;
    });
    result.gigs = gigs;
    console.log('search page ok, extracted', gigs.length, 'gig links');

    // Visit up to 5 gig pages for detail + portfolio screenshot
    for (const gig of gigs.slice(0, 5)) {
      await jitter();
      try {
        await page.goto(gig.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await sleep(3500);
        const gtitle = await page.title();
        const gbody = await page.evaluate(() => document.body?.innerText || '');
        if (blocked(gtitle, gbody)) {
          gig.status = 'blocked';
          console.log('blocked at gig page:', gig.url);
          result.status = 'partial-blocked';
          break;
        }
        const dir = path.join(OUT, gig.seller);
        fs.mkdirSync(dir, { recursive: true });
        await page.screenshot({ path: path.join(dir, '01_top.png') });
        await page.evaluate(() => window.scrollBy(0, 900));
        await sleep(1500);
        await page.screenshot({ path: path.join(dir, '02_mid.png') });
        gig.detail = await page.evaluate(() => {
          const txt = (sel) => document.querySelector(sel)?.innerText?.trim() || '';
          return {
            h1: txt('h1'),
            rating: txt('[data-testid="rating-score"], .rating-score, [class*="rating"]').slice(0, 40),
            price: (document.body.innerText.match(/(?:From\s+)?[$€]\s?\d[\d,.]*/g) || []).slice(0, 4),
            bodyHead: document.body.innerText.slice(0, 1500),
          };
        });
        gig.status = 'captured';
        console.log('captured:', gig.seller, '—', gig.detail.h1.slice(0, 60));
      } catch (e) {
        gig.status = 'error: ' + e.message.slice(0, 120);
        console.log('gig error:', gig.seller, e.message.slice(0, 120));
      }
    }
    if (result.status === 'search-ok') result.status = 'done';
  }
} catch (e) {
  result.status = 'error';
  result.error = e.message;
  console.log('fatal:', e.message);
} finally {
  fs.writeFileSync(path.join(OUT, '_scout_raw.json'), JSON.stringify(result, null, 2));
  await browser.close();
}
console.log('final status:', result.status);
