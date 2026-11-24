# Adapter: Stable Diffusion family (SD 1.5, SDXL, SD3.x) and community UIs

Covers SDXL base/refiner and fine-tunes, SD 1.5 checkpoints, SD 3.x, run through ComfyUI, AUTOMATIC1111/Forge, Diffusers, InvokeAI and similar. Sources: SDXL model card, Diffusers prompting guide (`research/sources.md`).

## Prompt form: compact, important first, plus a separate negative prompt

- Diffusers guidance: Subject → Style → Context; a structured narrative works better than random keyword piles on modern models.
- CLIP text encoders read 77-token chunks; UIs chunk longer prompts but weight early tokens more. Keep the key content in the first ~40 words. Typical length 25-75 words.
- Comma-separated descriptive phrases are fine and common for SD-family models; SD3.x (T5 encoder) also understands full sentences.

Shape:

```
<image type>, <subject with details>, <action>, <setting>, <light>, <style/medium>, <camera look if photo>
Negative prompt: <short list of relevant unwanted traits>
```

## Rules

1. **Negative prompt is supported** and useful here. Keep it short and relevant to the request (5-15 items). Generic realism set: "plastic skin, oversaturated, cartoon, extra fingers, deformed hands, blurry, watermark, text". For illustrations remove "cartoon"; for text-free images keep "text, watermark".
2. **Weights** `(word:1.2)` work in A1111/ComfyUI (and Compel in Diffusers). Use at most 1-3 weights, values 1.1-1.4, only for elements the model keeps missing.
3. **Checkpoint matters**: anime fine-tunes (Pony, Illustrious, NoobAI types) expect booru-style tags and their own quality tags; photo fine-tunes respond to "photo, 35mm". If the user names a checkpoint, follow its model card; otherwise use plain descriptive phrases.
4. **Resolution**: SDXL is trained around 1024×1024 total area (e.g. 832×1216, 1216×832); put size in settings, not prompt.
5. **Text rendering** is weak on SD 1.5/SDXL; recommend adding text afterwards. SD3.x is better but still limited.
6. **Thai**: CLIP encoders handle Thai poorly. Always write the prompt in English.

## Aesthetic translation

- The checkpoint and LoRAs decide most of the aesthetic; say which style traits to emphasise in the first phrases.
- Negative prompt can target the generic traits the user dislikes ("glossy, airbrushed, neon glow, generic anime face"), kept short.
- Concrete style phrases beat quality tags; use at most one weight on the defining trait if it keeps being ignored.

## Editing

- img2img with denoise 0.3-0.6 for style/colour changes keeping layout.
- Inpainting with a mask for local changes: prompt describes only what should appear in the masked area, plus the general style.
- ControlNet (pose, depth, canny) or IP-Adapter for structure/identity — mention only if the user's UI has them.

## Settings (suggested defaults, tune per checkpoint)

SDXL: 25-35 steps, CFG 5-7, DPM++ 2M Karras or Euler a, 1024-area resolution. These are common community defaults, not official requirements.

## Example

User: "anime girl reading in a library, soft light" (target: SDXL general model)

```
anime illustration, a teenage girl with short brown hair reading a thick book at a wooden library table, tall bookshelves behind her, soft afternoon light from a tall window, warm dust in the air, clean line art, cel shading, calm mood
Negative prompt: photorealistic, 3d render, extra fingers, deformed hands, blurry, text, watermark
```
