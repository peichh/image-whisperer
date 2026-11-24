# Reference images

For REFERENCE mode: the user gives one or more images to borrow from.

## 1. Label each reference by its job

| Job | What to take | What to say |
|---|---|---|
| identity | face, hair, body, recognisable features | "the person in image 1 (keep the same face and identity)" |
| product | exact shape, colour, label, logo | "the bottle from image 2, unchanged, label readable" |
| style | medium, palette, line, texture, light mood | "in the visual style of image 3: …" (also describe 2-3 style traits in words) |
| layout | composition, poses, placement | "use the composition of image 1" |
| pose | body pose only | "in the same pose as the figure in image 2" |
| background | environment | "set in the room from image 4" |

Say what NOT to take when it matters ("take only the colour palette from image 3, not its subject").

## 2. Write the prompt

1. List references in order and give each a job.
2. Describe the new scene in narrative form.
3. Repeat the most important preservation rule at the end.

Example (Gemini):

"Use image 1 for the woman's face and identity and image 2 for the handbag. Create a candid street-style photo of the woman from image 1 walking past a Bangkok shophouse at dusk, carrying the handbag from image 2 on her left shoulder. Keep her face, hairstyle and the handbag's shape, colour and logo exactly as in the references."

## 3. Limits to respect (verify current numbers in the adapter)

- Gemini 3 image models: up to 14 references in total, with model-specific limits for characters and objects; 2.5 Flash Image works best with up to 3.
- FLUX 3: up to 10 references. Midjourney V8.x Edit Model: up to 4.
- More references = more risk of mixing. Use the fewest that do the job.

## 4. Describing a reference in text

If the user asks "write a prompt that makes something like this image" (no image input to the generator), describe: image type, subject, composition, light, palette, medium, camera look, mood. Do not guess the original prompt or the artist. Do not claim to identify real people.
