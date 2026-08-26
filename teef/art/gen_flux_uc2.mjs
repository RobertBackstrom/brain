// Teef Chinatown — UC detail, GATE prominent, no bus words, scaled phone box. Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait. High aerial drone camera looking steeply down at about 55 degrees over a dense Soho Chinatown district in London at night. A large ornate Chinatown paifang gate, a traditional Chinese archway with upturned tiled roofs and carved beams, arches across the main street in the mid-ground as the clear focal landmark. Around it, rooftops and a grid of narrow streets between brick townhouse blocks fill the frame, thin foggy haze only at the top. Dense gritty Urban Cyber detail: tangled overhead electric and telecom cables strung between buildings, rusty fire escapes, rooftop water tanks, AC units, satellite dishes and antennas, tall neon vertical Chinese and Japanese signs glowing magenta red and cyan, street signs and traffic lights, graffiti on shutters, market stalls, bins and clutter on wet cobbles. A few sparse red paper lanterns. One correctly-scaled red British telephone box on the pavement near the gate, realistic human-and-a-half height proportions. Small realistic hooded figures along the streets below, a couple standing inside glowing orange target rings (#ff7a1a). Heavy volumetric fog, depth falloff, desaturated teal-green night gloom with warm amber and neon accents, dramatic low-key cinematic light, wet reflections, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game, high detail, no text, no UI, no watermark`;

const SEEDS=[83014, 11902, 33027, 70215];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:36,guidance_scale:3.7})});
  if(!res.ok){console.error(`[uc2:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`uc2_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[uc2:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/4`);
