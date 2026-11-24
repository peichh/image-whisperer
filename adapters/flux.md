# Adapter: FLUX (Black Forest Labs)

Covers FLUX 3 Image, FLUX.2 ([max], [pro], [flex], [klein], [dev]) and FLUX.1 Kontext. Facts from docs.bfl.ai, verified 2026-11-24 (`research/sources.md`).

## Prompt form: narrative, important things first

FLUX reads natural language. Structure: **Subject + Action + Style + Context**. Word order matters: what comes first gets the most weight.

- FLUX 3: start short and specific; the model expands it. Add detail only where you need control. Typical 20-80 words.
- FLUX.2: 30-80 words is usually ideal; 80+ for complex scenes; 10-30 for quick concepts.
- FLUX.2 [klein]: write flowing prose, not keyword lists; the text goes to the model unchanged; append `Style: … Mood: …` at the end.

## Rules

1. **No negative prompts.** FLUX.2 and FLUX 3 do not support them. Rewrite exclusions as positives ("empty, deserted street" not "no people"). Do not send a `negative_prompt` field.
2. **Photorealism**: camera and film words work: "shot on a 35mm lens", "Kodak Portra 400 colours", "candid iPhone photo". Use one or two, not a list.
3. **Colours**: hex codes tied to objects work in FLUX.2/3 ("a vase in #2E5E4E green"). Add the colour name too.
4. **Text**: put exact text in quotes and say where and how ("the words "OPEN DAILY" in white serif letters on the awning"). Short text renders best.
5. **Language**: FLUX.2 can take many languages including Thai; English tends to be most precise. Default to English; keep rendered Thai text in quotes.
6. **No unsupported fields** for FLUX 3 API: no `negative_prompt`, `seed`, `prompt_upsampling`, `guidance` (unknown fields return HTTP 422). FLUX.2 [dev] local pipelines accept guidance/steps; use the defaults unless the user tunes them.
7. **Quality tags** ("8K, masterpiece") add nothing; remove.

## Structured prompts (FLUX.2 / FLUX 3)

When the user wants exact control (layout, many elements, brand colours), FLUX.2 accepts a JSON prompt, for example:

```json
{
  "scene": "a small Thai coffee shop counter in the morning",
  "subjects": [{"description": "iced Thai tea in a clear cup", "position": "centre"}],
  "style": "natural smartphone photo",
  "lighting": "soft window light from the left",
  "color_palette": ["#D9822B", "#F4EBDD"],
  "camera": {"angle": "slightly above eye level", "lens": "phone wide main camera"}
}
```

FLUX 3 also accepts an optional element table with bounding boxes `[top, left, bottom, right]` on a 0-1000 grid for precise placement. Use only when the user needs exact layout.

## Editing

- FLUX 3: reference images by position — "image 1", "image 2" (up to 10 references). Edit template from the docs: "Modify image 1 by replacing … with …. Keep the rest of the image exactly unchanged, preserving …."
- FLUX.1 Kontext: specific verbs ("change", "replace", "remove") and an explicit preservation clause ("while keeping the same facial features, pose and lighting").
- Name what stays: identity, pose, composition, camera angle, light.

## Settings

- Aspect ratio / width-height are API or UI fields; do not write them into the prompt unless the UI has no setting.

## Example

User: "ภาพสตรีทฟู้ดเยาวราชตอนกลางคืน สมจริง" (target: FLUX.2 [pro])

```
A realistic night street photo of Yaowarat Road in Bangkok's Chinatown: a busy seafood stall in the foreground with a cook tossing noodles in a flaming wok, steam and smoke rising, diners on plastic stools along the pavement. Behind them, glowing red and yellow Chinese and Thai neon signs over the crowded street and slow tuk-tuks. Shot on a 35mm lens at eye level, warm mixed street light, slight motion blur on passing people, natural colours.
```
