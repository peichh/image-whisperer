# Worked examples

Each example shows the request, the hidden reasoning in short, and the final answer. These are prompt examples only; no images were generated for this repository.

## 1. AUTO / PROMPT ONLY — vague Thai request (Gemini app)

**User:** "ขอรูปหมาน่ารักๆ"

**Reasoning:** purpose unknown → neutral; "cute dog" with no breed → pick a common, friendly-looking choice and say so; photo is the most likely type.

**Answer:**
```
A sweet, natural photo of a fluffy cream-coloured Pomeranian puppy sitting on a sunny wooden floor, head tilted slightly, looking up at the camera with bright eyes. Soft morning window light, a few toys blurred in the background, warm and cosy mood.
```
Assumed: Pomeranian puppy, photo style, indoor. Want a different breed, a cartoon, or a specific use (wallpaper, sticker)?

## 2. Keeping a person ordinary (Gemini)

**User:** "Photo of my dad, 58, fixing his motorbike in front of our house in Chiang Mai, real look, not too pretty"

```
A candid smartphone photo of a 58-year-old Thai man squatting beside an old red Honda Wave motorbike in front of a simple two-storey house in Chiang Mai, tightening a bolt with a spanner, focused expression. He wears a faded polo shirt, shorts and rubber sandals; grease on his fingers. Late-morning sun, a concrete driveway, potted plants and a parked bicycle around. Natural skin with wrinkles and sun spots, everyday colours, slightly off-centre framing at eye level.
```
Not added: studio light, model looks, "cinematic", 8K.

## 3. EDIT — keep identity (Gemini)

**User:** (uploads graduation photo) "เปลี่ยนพื้นหลังเป็นหน้าหอประชุมจุฬาฯ ไม่ต้องเปลี่ยนหน้า"

**Changes:** background → front of Chulalongkorn University's Auditorium.  
**Keep unchanged:** face, identity, gown and sash, pose, bouquet, camera angle, lighting on the person.

```
Using the provided photo, replace only the background with the front of the Chulalongkorn University Auditorium in Bangkok on a clear sunny morning, with its traditional Thai-style roof and steps. Keep the graduate's face, identity, hairstyle, gown, sash, bouquet, pose and framing exactly the same, and match the background light direction to the light on the person.
```

## 4. CRITIQUE (any host that can see the image)

**User:** "ทำไมรูปนี้ดูเป็น AI" (a portrait with glossy skin, orange glow, perfect symmetry)

1. Skin looks airbrushed → ask for "natural skin texture with visible pores and small imperfections".
2. Strong orange "golden hour" glow on an indoor scene → name the real light: "soft daylight from a window on the left".
3. Perfectly centred, stiff pose → "candid, slightly off-centre framing, mid-laugh".

Edit instruction:
```
Keep the same person, clothes and room, but make the skin look natural with visible pores and small imperfections, replace the orange glow with soft neutral daylight from the window on the left, and reframe slightly off-centre as a candid moment.
```

## 5. OPTIMIZE — bloated prompt (FLUX.2)

**User prompt:** "masterpiece, best quality, 8k, ultra detailed, beautiful woman, coffee shop, cinematic lighting, bokeh, trending on artstation, no ugly, no bad hands"

**Improved:**
```
A woman in her late twenties sitting by the window of a small neighbourhood coffee shop, both hands around a ceramic latte cup, smiling at someone off-camera. Rainy afternoon outside, soft grey window light on her face, warm pendant lamps behind her, background softly out of focus. Natural photo, shot on a 50mm lens, true-to-life colours.
```
What changed: removed quality tags (no effect on FLUX); removed negative phrases (FLUX has no negative prompt) and gave the hands a simple task instead; added a real light source; replaced "beautiful" with a concrete moment.

## 6. REFERENCE — product + model (Gemini 3 Pro Image / Nano Banana 2.1)

```
Use image 1 for the woman's face and identity, and image 2 for the skincare bottle. Create a bright, clean lifestyle photo of the woman from image 1 in a white bathroom holding the bottle from image 2 near her cheek, smiling softly. Keep her face exactly as in image 1 and the bottle's shape, colour and label text exactly as in image 2. Soft daylight from a frosted window, vertical 4:5.
```

## 7. COMPARE — one idea, three models

**User:** "Floating market at dawn, for a travel blog header"

**Gemini**
```
A wide travel-blog header photo of Damnoen Saduak floating market at dawn: wooden boats loaded with tropical fruit and vegetables, vendors in wide-brimmed straw hats paddling along a narrow canal, soft pink-orange early light and light mist on the water, traditional wooden houses on both banks. Wide 16:9 composition with calm sky in the upper third for a title. Natural, true-to-life colours.
```
**Midjourney**
```
Damnoen Saduak floating market at dawn, wooden boats full of tropical fruit, vendors in straw hats, misty canal, soft pink morning light, travel photography, calm sky for title space --ar 16:9 --raw
```
**SDXL**
```
travel photo, Thai floating market at dawn, wooden boats loaded with tropical fruit, vendors in straw hats paddling, narrow canal with light mist, soft pink morning light, wooden houses on both banks, wide shot, natural colours
Negative prompt: oversaturated, cartoon, blurry, text, watermark
```
Differences: Gemini gets purpose and layout in prose; Midjourney gets a short prompt with `--ar` and `--raw`; SDXL gets compact phrases and a short negative prompt.

## 8. Conversational revision

Turn 1 prompt: example 1 (Pomeranian).  
**User:** "ขอเป็นแนวการ์ตูน แต่ตัวเดิม"

```
Turn the same fluffy cream-coloured Pomeranian puppy into a cute flat cartoon illustration: same pose with head tilted, big bright eyes, simple rounded shapes, soft pastel background, clean outlines.
```
Only the style changed; the subject and pose stayed.

## 9. Aesthetic translation — "premium" without the generic look (Gemini)

**User:** "ภาพอนิเมะพรีเมียมแบบหนังโรง เด็กหญิงยืนรอรถเมล์ตอนฝนตก"

**Reasoning:** "premium" and "หนังโรง" are labels; Gemini may turn them into generic illustration. Translate to visible traits: fine varied lines, restrained 2-tone shading, painted background, desaturated palette with one warm accent, small off-centre subject, rain haze, quiet face.

```
An anime film still of a schoolgirl waiting alone at a small roadside bus stop in heavy rain at dusk, holding a closed umbrella. The style: a theatrical anime film look rather than a game illustration — fine, slightly varying line work, restrained two-tone cel shading on the character, and a richly hand-painted background. Cool, desaturated blue-grey palette broken by the warm glow of a traffic light reflected on the wet road. The girl stands small in the right third of a wide 16:9 frame, rain haze softening the distant houses, faint painted texture and grain. Her face is quiet and simple, eyes lowered, not glossy or doll-like.
```

## 10. Aesthetic profile from an A/B choice

**User:** (shows two images) "ชอบรูป A มากกว่า รูป B ดูเป็นเกมมือถือ จำไว้ด้วย"

**Answer:** "From your choice I see you like: matte shading instead of glossy gradients, a painted background with haze, a muted palette, the character off-centre. You dislike: big sparkly eyes, neon glow without a source. Save this as your style for next time?" → on yes, save to host memory; otherwise give `image-whisperer-profile.json` (format: `examples/aesthetic-profile.example.json`).

## 11. Undescribed person — natural, not plain, with a moment (Gemini)

**User:** "สร้างรูปผู้ชายเอเชียที่ริมหาด ถ่ายด้วยกล้องไอโฟน"

**Reasoning:** no specific person → natural, pleasant-looking, not a model and not "ordinary". Photo story: a friend takes it on holiday → candid moment, a few metres away, chest height (natural proportions), vertical 3:4.

```
A candid iPhone photo of a Thai man in his mid-20s walking barefoot along the water's edge on a tropical beach in the late afternoon, taken by a friend a few metres away. His slightly messy black hair is lifted by the sea breeze; he laughs while pushing it back with one hand, glancing along the shoreline instead of at the camera. He wears an open light linen shirt over swim shorts; small waves wash over his feet and the wet sand reflects the sun. Vertical 3:4, full body, shot at chest height on the 1x main camera so his proportions look natural, slightly off-centre with the sea and a green headland behind him. Warm low side light, natural skin with a light tan, natural iPhone HDR colours.
```
Assumed: Thai, mid-20s, linen shirt over swim shorts. Say "หล่อแบบนายแบบ" or "ถอดเสื้อ" if you want that look.

