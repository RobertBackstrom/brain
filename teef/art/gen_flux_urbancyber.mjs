// Teef Chinatown — locked aer camera + Urban Cyber detail, fewer lanterns, phone box (no bus). Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait. High aerial drone camera looking steeply down at about 55 degrees over a dense Soho Chinatown district in London at night, across rooftops and a grid of narrow streets between brick townhouse blocks, the district filling the frame, thin foggy haze only at the very top. The ornate Chinatown paifang gate as one landmark. Dense gritty Urban Cyber detail: tangled overhead electric and telecom cables strung between buildings, rusty fire escapes, rooftop water tanks, AC units and satellite dishes, neon vertical Chinese and Japanese signs glowing magenta red and cyan, street signs and traffic lights, graffiti on shutters, bins and clutter on wet cobbles. Only a few sparse red paper lanterns over one street. A single correctly-scaled red British telephone box on the pavement (realistic proportions, about 2.5 metres tall). No bus, no double-decker. Small realistic hooded figures along the streets below, a couple inside glowing orange target rings (#ff7a1a). Heavy volumetric fog, depth falloff, desaturated teal-green night gloom with warm amber and neon accents, dramatic low-key cinematic light, wet reflections, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game, high detail, no text, no UI, no watermark`;

const SEEDS=[83014, 11902, 47711, 65230];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:36,guidance_scale:3.7})});
  if(!res.ok){console.error(`[uc:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`uc_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[uc:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/4`);
