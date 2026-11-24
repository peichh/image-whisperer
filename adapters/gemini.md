# Adapter: Gemini native image generation (Nano Banana)

Covers the Gemini app (gemini.google.com, mobile, Mac), Gemini API / Vertex AI, Google AI Studio, and agents that call Gemini image models. Facts verified 2026-11-24 from https://ai.google.dev/gemini-api/docs/image-generation (see `research/sources.md`). Model names and limits change; re-check before relying on numbers.

## Models (API names)

| Model | Notes from docs |
|---|---|
| `gemini-nano-banana-2.1` (Nano Banana 2.1) | recommended default for new projects; Flash speed, better text, multi-turn consistency, Search grounding; 1K/2K/4K; extra ratios 1:4, 4:1, 1:8, 8:1; up to 10 object + 4 character references |
| `gemini-3.1-flash-image` (Nano Banana 2) | previous Flash generation; `512px`-`4K`; same reference limits as 2.1 |
| `gemini-3-pro-image` (Nano Banana Pro) | premium; "Thinking" for complex instructions, brand consistency and high-fidelity text; up to 6 object + 5 character + 3 style references |
| `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) | fastest/cheapest; not optimised for multiple references or multi-turn editing |
| `gemini-2.5-flash-image` (Nano Banana) | legacy; works best with up to 3 input images |

All Nano Banana models: up to 14 reference images in total.

In the Gemini app the model is chosen by Google; the user may pick a mode (e.g. Fast vs Thinking/Pro). Do not tell app users to type model names or parameters.

## Prompt form: narrative

Gemini is a language model that draws. It reads full sentences, purpose and context better than keyword lists.

Template (adapt, do not fill mechanically):

```
[Image type and purpose] of [main subject with identifying details], [action / pose / expression], [setting: place, time, weather, culture]. [Composition: shot size, angle, placement, empty space]. [Light: source, direction, quality]. [Style or camera look, only if relevant]. [Text: exact words in quotes, placement, font feel].
```

Google's own photoreal pattern: "A photorealistic [shot type] of [subject] in [setting]. [Light]. Shot from [camera angle] with a [lens type]."

### Rules

1. **Lead with purpose and type**: "A YouTube thumbnail of…", "A minimalist logo for a Thai coffee brand…", "A candid phone photo of…". Purpose is one of Google's top tips.
2. **Narrative, specific, relevant**: 40-150 words for most images; up to ~250 for infographics, multi-panel or multi-reference compositions. Every sentence should add something visible.
3. **Semantic negatives**: no negative-prompt field. Say what you want instead ("an empty, quiet street at dawn", not "no cars, no people"). A short "Do not add any text or logos" is fine when text drift is a known risk.
4. **Complex scenes step by step**: for many elements, write "First…, then…, finally…" or a short numbered list of elements with positions.
5. **Camera words when useful**: wide-angle, macro, low angle, 85mm portrait, shallow depth of field. Skip them for illustrations.
6. **English final prompt**: Thai is not in Google's best-performance language list. Write the prompt in English, keep Thai only inside quotes for rendered text, and explain the prompt to the user in Thai. In the Gemini app a Thai prompt also works; English is the safer default for detail.
7. **Aspect ratio and size**: API → config (`response_format.aspect_ratio`, e.g. `1:1`, `5:4`, `16:9`; check the docs for the full list per model; default matches the input image or 1:1; `image_size`: `1K` default, `2K`, `4K`, uppercase K). Gemini app → write it in words at the start or end: "Vertical 9:16 image." / "ภาพแนวตั้ง".
8. **Counts**: the model may not return the exact number of separate images requested. For "4 variations", either run 4 separate requests or ask for "a 2×2 grid of four variations in one image" if a grid is acceptable.
9. **Grounding**: Gemini 3 image models can use Google Search. For current events, real places, weather or real products, say "use Google Search to check how … looks" in API/agent setups that enable the tool. Do not rely on this in the app unless the user confirms it works for them.
10. **Thinking**: 3 Pro / 3.1 Flash think by default. Long checklists are not needed to make it "reason"; give clear facts and goals.

## Text in images

- Quote exact text: `the headline "SALE 50%" in bold white sans-serif at the top`.
- Keep text short. For longer copy, Google suggests generating the text first in chat, then asking for the image with that text.
- Thai script: keep to a few words; specify "Thai script"; check results; offer a blank area as a fallback.
- Infographics: list sections with exact labels and numbers; Gemini 3 Pro Image is the strongest Gemini option for dense text.

## Aesthetic translation

- [V] Google's guidance for stylised images: "Describe the artistic style, subject, and medium. Be specific about the visual detail (bold lines, colors, etc.)". Template: "A [style] of a [subject] doing [activity]. The design features [visual qualities] and [color/background preference]."
- [I, user-reported] Gemini can match every object but render "premium" anime or illustration requests as generic AI illustration or mobile-game artwork. Counter it by naming the visible traits (`core/aesthetic-translation.md`) and, when that look is a risk, one contrast phrase: "a theatrical anime film look rather than a mobile-game illustration".
- Put one sentence starting "The style:" after the scene with the 4-6 defining traits (line, shading, palette, light, texture, composition). Replace style labels; do not add them on top.
- Strongest control: style reference images. Gemini 3 Pro Image takes up to 3 style references; say what to take from them ("use only the line work and colour palette of the style images").
- In multi-turn edits, fix style one axis at a time: "Keep everything the same, but make the shading flat two-tone instead of glossy gradients."

## Editing (conversational)

- Upload/attach the image and say: "Using the provided image, change … to …. Keep … exactly the same."
- Multi-turn: "Keep everything the same, but make the lighting warmer." Change one thing per turn for best control.
- Identity: "Keep the person's face, identity, hairstyle and expression unchanged."
- Region by description: "the blue mug on the left side of the table".
- Style transfer: "Turn this photo into a watercolour painting, keeping the same composition and people."

## References (multi-image)

Name each image by order and job: "Use the woman from the first image, the dress from the second image and the beach from the third image." Respect the limits in the table above. For character consistency across a series, reuse the same reference images each time and repeat the identity sentence.

## What not to send

- No `--ar`, `--v`, weights `(word:1.3)`, `::`, or "negative prompt:" sections.
- No "8K, masterpiece, best quality, trending on ArtStation" — they add no documented benefit and push style.
- No requests for unsafe content; Gemini has its own safety filters and will refuse.

## Output notes for the user

- All generated images carry an invisible SynthID watermark.
- If the result misses something, use the critic loop (`core/quality-critic.md`) with a short edit instruction rather than regenerating from scratch.

## Examples

**Thai request → Gemini app (PROMPT ONLY)**

User: "อยากได้โปสเตอร์งานวัด ปีนี้มีชิงช้าสวรรค์ แนวย้อนยุค ภาพแนวตั้ง"

```
A vertical 3:4 retro Thai temple-fair poster in the style of 1970s Thai movie posters: a hand-painted illustration of a colourful Ferris wheel lit with bulbs at night, food stalls with lanterns, and families walking in the foreground. Bold hand-lettered Thai title "งานวัดประจำปี" across the top in red and yellow with a dark outline. Slightly faded printed-paper texture, warm red, yellow and teal palette, visible halftone grain.
```

**English request → Gemini API (settings separated)**

User: "Product shot of our matcha tin for Shopee, white background."

```
prompt: A clean e-commerce product photo of a matte green cylindrical matcha tin with a white paper label, centred on a seamless pure-white background. The whole tin is visible, label facing the camera and sharp. Soft diffused light from the front-left with a gentle contact shadow under the tin. No other props.
config: aspect_ratio="1:1", image_size="2K"
```
(With the real tin photo: add "Use the tin from the provided image exactly as it is, including the label text and colour.")

**Edit**

```
Using the provided photo, replace the cloudy grey sky with a clear blue afternoon sky. Keep the family, their faces, clothes and poses, the temple building and the camera angle exactly the same, and slightly brighten the light on the people to match the new sky.
```
