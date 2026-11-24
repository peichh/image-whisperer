# Image editing

For requests that change an existing image (EDIT mode, conversational revisions, retouching, restoration, background swap, outfit change, object removal).

## 1. Write two lists first

- **Change**: exactly what must be different. One verb per item: replace, remove, add, recolour, relight, restyle, extend, move.
- **Keep**: what must stay the same. Always consider: identity (face, age, body shape, skin tone), pose, expression, clothing, proportions, camera angle and perspective, composition and framing, lighting direction and colour, background, text, style, image quality/grain.

Ask only if the target is ambiguous ("change her shirt" when there are two women → "the woman on the left").

## 2. Instruction shape

```
<Verb> <target, located precisely> <to/with result>. Keep <keep list> exactly the same. <Optional: match the existing light, perspective and grain so the change blends in.>
```

Examples:

- "Replace the grey sky with a clear late-afternoon blue sky. Keep the people, their faces, poses and clothes, the building and the camera angle exactly the same, and adjust the light on the people only slightly to match the brighter sky."
- "Remove the man in the red shirt in the background on the right and fill the space with the continuing brick wall. Keep everything else unchanged."
- "Change the text on the mug to read exactly "สวัสดี" in the same font style and size. Do not change anything else."

## 3. Rules

- Point to things by position, colour and type, not pronouns ("the cup on the left", not "it").
- For identity preservation say "keep the same face and identity" — do not describe the face anew (re-description invites drift).
- For style transfer say which parts of the original must survive (composition, pose, layout).
- Use a sequence of small edits instead of one huge edit when changes are many; models drift less.
- Retouching real photos: subtle, natural; keep pores, wrinkles and moles unless the user asks to remove them.
- Restoration of old photos: repair damage, keep the original era, clothing and faces; colourisation should use plausible period colours; say it may not match the real colours.
- Mark the edited area if the model supports it (masks, Seedream arrows/boxes, FLUX 3 bounding boxes).

## 4. Adapter notes

Each adapter has an "Editing" section with model syntax. Short summary:

| Model | Edit form |
|---|---|
| Gemini | Conversational: "Using the provided image, change… Keep…". Multi-turn works best for iterative changes. |
| FLUX 3 / FLUX.1 Kontext | Instruction on reference image(s); explicitly preserve; references by "image 1", "image 2". |
| Qwen-Image-Edit | Instruction prompt; strong for text edits and consistency; multi-image input. |
| Seedream | Concise instruction, explicit keep list, optional marks on the image. |
| Midjourney | Edit Model (V8.x) with up to 4 references; instruction-style prompt. |
| SDXL | Inpainting with a mask; prompt describes the masked area only, plus negative prompt. |
