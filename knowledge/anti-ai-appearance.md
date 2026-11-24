# Anti-AI appearance

Load when the user wants a real-looking photo, complains that an image "looks AI", or when realism is the main goal. Do not apply to stylised art where these traits are the style.

## Common "AI look" traits and the prompt fix

| Trait | Cause (typical) | Fix in the prompt |
|---|---|---|
| plastic, airbrushed skin | beauty defaults, "flawless", "perfect" | "natural skin texture with visible pores and small imperfections"; remove "flawless", "perfect", "beautiful" |
| everyone looks like a model | idealised default faces | give real age, body type, ordinary clothing, specific everyday expression |
| over-saturated, HDR glow | quality tags, "vibrant", "cinematic" | "natural, realistic colours", name the actual light; remove "8K, HDR, vibrant" |
| perfectly centred, symmetric posing | default composition | candid framing, off-centre subject, mid-action moment |
| uniform dramatic golden/orange light | "cinematic", golden hour default | name the real light: "flat overcast daylight", "office fluorescent light" |
| too clean environments | missing clutter | add place-appropriate everyday details: cables, stains, worn paint, receipts |
| impossibly shallow blur on phone photos | DSLR defaults | "phone camera, most of the scene in focus" |
| glossy shiny surfaces everywhere | sheen default | name matte materials where real |
| text gibberish | model limits | quote short exact text; for long text generate text first (Gemini docs) or add text later in an editor |
| extra/merged fingers | hands are hard | give hands a simple task, fewer visible hands |
| identical faces in groups | same-face syndrome | different ages, hairstyles, expressions, clothing for each person |
| floating objects, missing shadows | weak physics | contact shadows, name supports (`knowledge/physical-realism.md`) |
| style drift to illustration | ambiguous medium | start with "A photo of…" / "A candid smartphone photo of…" |

## Negative prompts

- Gemini, FLUX 2/3, Seedream, Midjourney (mostly): describe the wanted result positively. Midjourney's `--no` is for excluding objects, not for quality.
- SD/SDXL, Qwen-Image, Z-Image base: a short negative prompt is supported. Keep it relevant ("plastic skin, oversaturated, extra fingers") — not a 100-word list.
- Z-Image-Turbo runs with guidance 0: negative prompts have no effect.

## Restraint

"Real" is not "more detail". Remove words before adding words. The best realism fix is often to delete "cinematic, 8K, masterpiece, perfect".
