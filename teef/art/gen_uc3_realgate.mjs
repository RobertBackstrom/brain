// Teef Chinatown — REAL ornate London gate + phone box on the SIDE, UC detail, locked aerial. Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait. High aerial drone camera looking steeply down at about 55 degrees over a dense Soho Chinatown district in London at night. The clear focal landmark is a large, highly ornate and colourful real London Chinatown paifang gate modelled on the Wardour Street gate: three tiered green and gold glazed pagoda roofs with sharply upswept eaves and dragon finials, richly painted red, gold, blue and green carved beams and dougong brackets, a central gold signboard with red Chinese characters, red lanterns hanging beneath, spanning the main street. Around it rooftops and a grid of narrow streets between brick townhouse blocks fill the frame, thin foggy haze at the top. Dense gritty Urban Cyber detail: tangled overhead electric and telecom cables, rusty fire escapes, rooftop water tanks, AC units, satellite dishes and antennas, tall neon vertical Chinese and Japanese signs glowing magenta red and cyan, street signs and traffic lights, graffiti on shutters, market stalls and clutter on wet cobbles. A single red British telephone box standing on the pavement at the left side of the street, against the buildings, not in the middle of the road, realistic human-and-a-half height. Small realistic hooded figures along the street below, a couple inside a glowing orange target ring (#ff7a1a). Heavy volumetric fog, depth falloff, desaturated teal-green night gloom with warm amber and neon accents, dramatic low-key cinematic light, wet reflections, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game, high detail, no text, no UI, no watermark`;

const SEEDS=[11902, 33027, 51884, 90233];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:36,guidance_scale:3.7})});
  if(!res.ok){console.error(`[uc3:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`uc3_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[uc3:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/4`);
