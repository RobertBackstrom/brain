// Teef — showcase camera-relative transparency / distance fade. Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait, three-quarter game camera at about 45 degrees over a Soho Chinatown street at night. A tall brick London building in the immediate foreground that would block the view is rendered SEMI-TRANSPARENT and ghosted, faded to a faint translucent glassy x-ray with glowing cyan wireframe edges, so the player character and a glowing orange circular target ring (#ff7a1a) on the wet cobbled street directly behind it are clearly visible straight through the transparent building. The buildings toward the left and right edges and into the far distance fade out softly into fog, becoming translucent and dissolving. Down the street stands the ornate colourful London Chinatown paifang gate with green and gold tiered roofs. Urban Cyber detail: neon vertical Chinese signs, overhead cables, fire escapes, red lanterns. Desaturated teal-green night gloom with red and amber neon accents, volumetric fog, realistic stylized Unreal Engine game render, high detail, no text, no UI, no watermark`;

const SEEDS=[11902, 40771, 88560];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:36,guidance_scale:3.8})});
  if(!res.ok){console.error(`[fade:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`fade_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[fade:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/3`);
