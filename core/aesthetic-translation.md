# Aesthetic translation

Goal: get the **look and feel** the user wants, not just the right objects. A picture that contains everything asked for but in the wrong style has failed.

Style labels ("premium anime", "cinematic", "masterpiece", a studio's name) are not reliable instructions: each model maps them to its own average look, and that average is often a generic, polished AI style (see `research/sources.md`, aesthetic section). Gemini's own docs say to "be specific about the visual detail (bold lines, colors, etc.)". So translate style words into **visible, checkable traits**.

## 1. Decompose the target aesthetic

Fill only the axes that define the style (usually 5-9). Each value must be something you could point at in an image.

| # | Axis | Describe | Example values |
|---|---|---|---|
| 1 | line | weight, variation, colour, confidence | "thin, tapering ink lines that thicken in shadow"; "no outlines, edges defined by colour" |
| 2 | shape language | dominant shapes, simplification | "angular, sharp silhouettes"; "soft rounded masses" |
| 3 | anatomical stylisation | proportions, exaggeration | "realistic 7.5-head adults, slightly long legs"; "compact 3-head chibi" |
| 4 | facial design | eyes, nose, mouth, individuality | "medium-size eyes with small irises and a single catchlight, simple line nose, distinct faces per character" |
| 5 | shading | technique and number of tones | "two-tone hard cel shadow"; "soft painterly blending"; "hatching" |
| 6 | colour grading | palette, saturation, temperature, contrast | "muted desaturated greens and warm greys, lifted blacks" |
| 7 | lighting behaviour | source, logic, how light is rendered in this style | "warm sunset rim light painted as one solid orange band" |
| 8 | material rendering | how surfaces are treated | "fabric folds drawn with 2-3 lines, no texture"; "realistic metal reflections" |
| 9 | compositional hierarchy | focal point, placement, framing | "subject small in the lower third, wide empty sky" |
| 10 | perspective | camera height, lens feel, flatness | "low angle, mild wide-angle distortion"; "flat orthographic" |
| 11 | atmospheric depth | haze, value shift with distance | "background washed out to pale blue, foreground dark" |
| 12 | visual density | amount of detail, where it is concentrated | "detail only on faces and hands, loose background" |
| 13 | motion representation | how movement is shown | "speed lines and smear frames"; "frozen, still" |
| 14 | texture treatment | paper, grain, brush, digital clean | "visible watercolour paper grain"; "subtle film grain" |
| 15 | artistic imperfection | human traces that make it feel made | "slight line wobble, colour bleeding past lines, uneven fill" |
| 16 | emotional expression | how emotion is shown in faces, bodies, colour | "restrained: small mouth, lowered eyes, quiet pose" |

Sources for the values (in this order): the user's reference images → their aesthetic profile (`core/aesthetic-profile.md`) → their words → the style file in `styles/` → neutral defaults. Never fill an axis with praise ("beautiful lines").

## 2. Translate words into visual results

| User says | Do not write only | Write the visible result instead (adapt) |
|---|---|---|
| premium / high-end anime | "premium anime, masterpiece" | "theatrical anime film look: fine variable-weight lines, painted backgrounds with atmospheric depth, restrained 2-tone shading, natural non-neon colour, characters with individual faces" |
| cinematic | "cinematic" | name the frame: "wide 2.39:1 framing, subject off-centre, motivated light from a single practical lamp, deep shadows, muted teal-green grade" |
| high quality / detailed | "8K, ultra detailed" | say where detail goes: "fine detail on the hands and fabric, simpler background" |
| like [studio / artist] | the name alone | the traits that make it recognisable (axes above). Use the name only if the user insists, the host allows it, and the model is known to respond to it; always add traits too |
| aesthetic / vibe | "aesthetic" | palette + light + texture + composition in concrete words |
| not AI-looking | "not AI" | the specific fixes from `knowledge/anti-generic-aesthetics.md` |

Rules:

- **Replace, don't stack.** Swap a vague word for 1-2 concrete phrases. Do not make the prompt longer just to add style words. A good translation is often the same length.
- **Spend words on the axes that differ from the model's default.** If Gemini already draws clean flat icons, do not describe that; describe what it gets wrong (see adapter "Aesthetic translation" section).
- **Prefer references.** If the user has an image of the style, use it as a style reference (Gemini 3 Pro Image: up to 3 style images; FLUX 3 / Qwen-Image-Edit / Seedream multi-reference; Midjourney `--sref`) and still name 2-3 key traits in words.
- **One style.** If two style descriptions conflict, choose by the user's priority and drop the other.
- **Keep the user's intended "generic".** If they ask for a mobile-game look, thick outlines, neon or a centred symmetric poster, that is the target style, not a defect.

## 3. Cross-model translation

The same visual target needs different words per model. Write the **target aesthetic once** (axes), then compile per adapter:

- Narrative models (Gemini, FLUX, Seedream, Qwen, Z-Image): one sentence "The style: …" with the 4-6 most defining traits, after the subject and scene.
- Midjourney: 4-8 short style phrases + `--sref` if a reference exists; `--raw` when the house style would override the target; lower `--s` to stay closer to the described style.
- SDXL: a few style phrases early in the prompt, plus negative terms for the specific generic traits to avoid (only for SD-family models).
- Comparing models: keep the axes identical and change only wording and syntax; that makes differences in results attributable to the model.

## 4. Check

Before answering, confirm: the style is described by at least the key axes; no axis is only a praise word; the description does not contradict the subject; nothing generic was added that the user did not want. After an image is visible, score it with the three axes in `core/quality-critic.md` section E.

## Example

User: "ภาพอนิเมะพรีเมียมแบบหนังโรง เด็กหญิงยืนรอรถเมล์ตอนฝนตก" (Gemini)

Decomposition (internal): line = fine, variable weight; shading = restrained 2-tone; colour = cool desaturated blue-grey with warm signal lights; light = overcast with reflections; composition = girl small, right third; atmosphere = rain haze; density = detail in the background painting, simple character fill; texture = painted background, slight grain; emotion = quiet waiting.

```
An anime film still of a schoolgirl waiting alone at a small roadside bus stop in heavy rain at dusk, holding a closed umbrella. The style: a theatrical anime film look rather than a game illustration — fine, slightly varying line work, restrained two-tone cel shading on the character, and a richly hand-painted background. Cool, desaturated blue-grey palette broken by the warm glow of a traffic light reflected on the wet road. The girl stands small in the right third of a wide 16:9 frame, rain haze softening the distant houses, faint painted texture and grain. Her face is quiet and simple, eyes lowered, not glossy or doll-like.
```
