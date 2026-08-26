// Teef Chinatown-gate concepts via fal.ai Flux.dev (REST). FAL_KEY from assistant/.env.
import fs from 'node:fs';
import path from 'node:path';

const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
if (!FAL_KEY) throw new Error('FAL_KEY not found in assistant/.env');

const OUT = '/home/assistant/projects/teef/art/concepts/flux';
fs.mkdirSync(OUT, { recursive: true });

const TAIL = `stylized 2.5D isometric video game environment, semi-stylized 3D render of a premium mobile game, elevated three-quarter camera, heavy volumetric atmospheric fog with strong depth falloff, desaturated teal-green night gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), punctuated by warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, faint neon magenta (#b03cff) signage glow, subtle orange (#ff7a1a) gameplay target rings on wet cobblestone (#3a3d40), single dramatic low-key key light, deep soft shadows, faint white graffiti tags on shutters, cinematic, high detail, soft ambient occlusion, painterly stylized textures, no text, no watermark`;

const SCENES = {
  v1_wide: `The ornate Chinatown paifang gate, a grand traditional Chinese archway with upturned tiled roofs and carved beams marking the entrance to Soho Chinatown London, centered and flanked by narrow London brick townhouses with bay windows, a red British phone box and a red double-decker bus half-swallowed by fog behind, glowing red paper lanterns strung across the street, isometric establishing shot. ${TAIL}`,
  v2_hero: `The ornate Soho Chinatown paifang gate dominant in frame, upturned tiled roofs and intricately carved beams, dense fog behind it dissolving the London street into depth, glowing red paper lanterns and neon Chinese shop signage as the warm accents, one orange gameplay target ring glowing on the wet cobbles below, dramatic atmospheric hero shot. ${TAIL}`,
  v3_gloom: `The Soho Chinatown paifang gate pushed deep into thick green-teal fog, an ornate Chinese archway emerging from the gloom, very few warm lights, a single distant brazier fire as the only orange glow, sparse red lanterns, maximum atmospheric depth falloff and moody negative space, brick London townhouses as dim silhouettes. ${TAIL}`,
};

const SEEDS = [73419, 250688];

async function gen(label, prompt, seed) {
  const res = await fetch('https://fal.run/fal-ai/flux/dev', {
    method: 'POST',
    headers: { 'Authorization': `Key ${FAL_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, image_size: 'landscape_16_9', num_images: 1, seed, num_inference_steps: 30, guidance_scale: 3.5 }),
  });
  if (!res.ok) { console.error(`[${label}:${seed}] HTTP ${res.status} ${(await res.text()).slice(0,200)}`); return null; }
  const j = await res.json();
  const url = j.images?.[0]?.url;
  if (!url) { console.error(`[${label}:${seed}] no image url`); return null; }
  const img = Buffer.from(await (await fetch(url)).arrayBuffer());
  const file = path.join(OUT, `${label}_${seed}.jpg`);
  fs.writeFileSync(file, img);
  console.log(`[${label}:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`);
  return file;
}

const jobs = [];
for (const [label, prompt] of Object.entries(SCENES))
  for (const seed of SEEDS) jobs.push(gen(label, prompt, seed));
const out = (await Promise.all(jobs)).filter(Boolean);
console.log(`\nDONE: ${out.length}/6 images in ${OUT}`);
