// Teef Chinatown gate — FAITHFUL to the live prototype: red-monochrome extruded OSM city. Flux.dev.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Monochrome red-and-black stylized 3D video game map, a Soho London city district built entirely from bright crimson red (#e21414) extruded blocks shaped like giant letterforms and brutalist geometric shapes, pure black streets and pure black background as negative space, hard graphic high-contrast look, an ornate red 3D Chinatown paifang gate archway standing as a recognisable landmark among the red extruded blocks, small glowing green cylinder pickup markers (#22dd44) scattered across the streets, a single small white capsule player token, tilted three-quarter top-down camera at a dramatic low angle looking across the city, OpenStreetMap extruded buildings aesthetic, bold minimal graphic game art, clean, no fog, sharp shadows, no text, no watermark, no UI`;

const SEEDS = [73419, 250688, 51234, 90871];
async function gen(seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'landscape_16_9',num_images:1,seed,num_inference_steps:32,guidance_scale:4.0})});
  if(!res.ok){console.error(`[proto:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[proto:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`proto_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[proto:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`\nDONE ${out.length}/${SEEDS.length}`);
