# Prompt compiler

Turns the scene into text (and settings) for one target model. Read this, then the target adapter. The adapter overrides anything here.

## 1. Pick the prompt form from the adapter

| Form | Models | Shape |
|---|---|---|
| Narrative | Gemini, FLUX 2/3, Seedream, Qwen-Image, Z-Image, universal | Full sentences, subject first, then action, setting, light, camera/style |
| Short descriptive + parameters | Midjourney | One or two short sentences or phrases, then `--parameters` at the end |
| Weighted tags or short phrases + negative prompt | SD 1.5 / SDXL (A1111, ComfyUI) | Compact comma-separated phrases, important first; separate negative prompt |
| Edit instruction | any model with editing | "Change X to Y. Keep A, B, C unchanged." |
| Structured (JSON) | FLUX.2 / FLUX 3 when the user wants precise control | JSON object per adapter |

## 2. Order of content (narrative form)

1. **Image type + purpose** in one phrase: "A candid smartphone photo of…", "A flat vector icon of…", "A product photo for an online shop of…".
2. **Main subject** with the details that identify it.
3. **Action / pose / expression / relationships.**
4. **Setting** (place, time, weather, culture).
5. **Composition** (shot size, angle, placement, empty space).
6. **Light.**
7. **Style / medium / camera look** — only what is relevant.
8. **Text** to render, in quotes, with placement.
9. **Exclusions** rewritten as positives ("an empty beach" not "no people") unless the model has a real negative prompt *and* the user asked to exclude something.

Put the most important information first. Front-loading matters for every model, and is critical for CLIP-based models.

## 3. Wording rules

- Concrete nouns and visible facts over abstract praise. "Soft window light from the left" beats "beautiful lighting".
- One adjective that matters beats five that do not. Delete: masterpiece, best quality, ultra-detailed, 8K, award-winning, hyper-realistic, trending — unless the adapter says the model benefits (SD 1.5 community models sometimes do).
- Keep counts as numbers ("three cats").
- Name positions ("on the left", "behind her").
- Describe culture-specific items visually.
- Do not mix incompatible styles.
- Use camera terms only for photos, and only the ones that change the picture (see `knowledge/photography.md`).

## 4. Length

Use the adapter's band. General guide:

| Image | Words (narrative models) |
|---|---|
| Simple object / icon | 15-40 |
| Portrait / product | 40-90 |
| Complex multi-subject scene | 80-160 |
| Infographic / poster with layout | 80-200, structured by section |

Shorter is better when it says everything that matters. Longer is fine when every sentence adds a visible constraint.

## 5. Settings outside the prompt

Put aspect ratio, size, seed, steps, guidance and negative prompts in **settings**, not in prose, when the platform has a setting for them (Gemini API `aspect_ratio`, Midjourney `--ar`, SD negative prompt field). In chat apps without settings (Gemini app), write the aspect ratio in words: "vertical 9:16 image".

## 6. Unknown model

Use `adapters/universal.md`: narrative form, no parameters, no weights, no negative prompt, aspect ratio in words.

## 7. Self-check

Run the prompt checklist in `core/quality-critic.md` before showing the result.
