// Teef — 3 mood-piece landscape concepts for the pitch Voice section. Flux.dev REST.
// Street-level cinematic vignettes in the established Teef cyber-London palette.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/mood';
fs.mkdirSync(OUT, { recursive: true });

const TAIL = `cinematic street-level game key art, semi-stylized 3D render of a premium mobile crime game set in London, desaturated grey London stone and brick, wet reflective streets, moody low-key cinematic lighting, punctuated by lantern red (#d22a2a) and faint green (#3aff8a) neon accents, cool night-blue shadow (#14202e), light atmospheric haze with depth (not heavy fog), Lock Stock cockney London crime mood, gritty believable, Unreal Engine 5 cinematic, high detail, painterly stylized textures, no text, no UI, no watermark`;

const SCENES = [
  { key: 'lift',    prompt: `A sharply dressed businessman in a suit stands at a London bus stop at dusk, absorbed in his phone, wallet visible in his back pocket; a hooded figure in dark streetwear drifts past close behind him, hand low, about to lift it. A red British phone box and a red double-decker bus behind, Soho brick townhouses, neon shop signage reflecting on wet pavement. ${TAIL}` },
  { key: 'recruit', prompt: `Behind a greasy London cafe at night, a glowing neon cafe sign over a narrow brick back-alley, steam rising from a street vent; a wiry teenage figure in a tracksuit faces an older hooded gang member sizing him up, two figures, tense quiet moment, wet cobbles, a single black cab parked at the alley mouth. ${TAIL}` },
  { key: 'fence',   prompt: `Interior of a dim London railway-arch lock-up workshop at night, a heavy gold chain and stolen jewellery glinting under a single hanging work-lamp on a cluttered workbench, a stocky older fence in a flat cap examining a piece through a jeweller's loupe, shelves of crates and bric-a-brac in shadow behind, warm lamp pool against cold dark. ${TAIL}` },
];
const SEEDS = [250688, 44120];

async function gen(scene, seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:scene.prompt,image_size:'landscape_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.5})});
  if(!res.ok){console.error(`[${scene.key}:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[${scene.key}:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`${scene.key}_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[${scene.key}:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const jobs=[]; for(const s of SCENES) for(const seed of SEEDS) jobs.push(gen(s,seed));
const out=(await Promise.all(jobs)).filter(Boolean);
console.log(`\nDONE ${out.length}/${jobs.length}`);
