# Adapter: Z-Image (Tongyi-MAI)

Covers Z-Image-Turbo, Z-Image (base), Z-Image-Omni-Base and Z-Image-Edit (6B single-stream DiT). Sources: Z-Image GitHub and Hugging Face model cards (`research/sources.md`).

## Prompt form: long, dense descriptive prose

Official example prompts are long, specific descriptions (often 80-200 words) in Chinese or English that list subject, clothing, setting, light, camera and text in detail. Z-Image-Turbo is documented for strong photorealism and accurate bilingual (Chinese/English) text rendering.

- Write English (or Chinese if the user writes Chinese). Thai text in images is not a documented strength; keep it short and quoted, or leave space.
- Be concrete: materials, light, camera look, small realistic details.

## Rules by variant

| Variant | Guidance / steps (from model cards) | Negative prompt |
|---|---|---|
| Z-Image-Turbo | `guidance_scale=0.0`, 8 NFEs (about 9 steps) | no effect (guidance 0) — do not write one |
| Z-Image (base) | CFG 3-5, 28-50 steps, 512²-2048² total area | supported, documented as robust; keep short |
| Z-Image-Edit | instruction editing | follow instruction form below |

- No weight syntax.
- Resolution is a pipeline setting.
- The project ships a Prompt Enhancer; this skill's output can replace it or be fed into it.

## Editing (Z-Image-Edit)

Instruction plus explicit keep-list, as in `core/image-editing.md`: "Replace the background with a snowy mountain view, keep the woman, her pose, clothes and lighting direction unchanged."

## Example

User: "Street portrait of an old fisherman in Phuket, very realistic" (target: Z-Image-Turbo)

```
A realistic close-up street portrait of a Thai fisherman in his late sixties standing on a wooden pier in Phuket at early morning. Deep sun-weathered wrinkles, short grey stubble, a faded blue cotton shirt with rolled sleeves, a coil of rope over his shoulder. Soft low sunlight from the right, gentle shadows on his face, small fishing boats and calm water softly blurred behind him. Natural skin texture, real colours, documentary photography style, 50mm lens at eye level, he looks slightly past the camera with a calm expression.
```
(No negative prompt: Turbo runs with guidance 0.)
