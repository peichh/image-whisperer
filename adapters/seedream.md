# Adapter: Seedream (ByteDance)

Covers Seedream 4.0 / 4.5 and newer (5.0, Dola Seedream 5.5) on BytePlus ModelArk, Volcengine Ark, Doubao/Jimeng and third-party hosts. Prompt guidance verified from the official Seedream 4.0-4.5 prompt guide (`research/sources.md`); 5.x-specific differences not yet verified.

## Prompt form: coherent natural language

Official guide: describe **subject + action + environment** in clear natural language, then add style, colour, lighting and composition. Avoid piles of comma-separated keywords and stacks of ornate adjectives; Seedream 4.x needs less description than 3.0 and favours concise, precise prompts.

- 30-120 words typical.
- State the use case: "Design a logo for a gaming company…", "Make a product poster for…".
- English and Chinese both well supported; for Thai requests write English and quote Thai text.

## Rules

1. Text to render goes in double quotes.
2. Be specific about style, colour and light, not generic praise.
3. No weight syntax; no negative prompt in the official guide — describe positively.
4. Multi-image output (story sets, variations, sticker sets) is supported: state the number and what differs between images ("Generate 4 images showing the same cat in spring, summer, autumn and winter").
5. Size/ratio are API parameters.

## Editing

From the official guide:

- Concise, unambiguous instruction; no vague pronouns ("the man in the blue jacket", not "him").
- Say explicitly what stays unchanged.
- Visual marks on the input (arrows, boxes, doodles) can indicate regions and positions.
- Multi-image input: refer to "image 1", "image 2" and give each a job (subject, style, background).

## Example

User: "ทำสติกเกอร์ไลน์แมวส้ม 4 ท่า"

```
Generate a set of 4 cute LINE-style sticker images of the same chubby orange tabby cat, each on a plain white background with a thick white outline: 1) waving hello, 2) laughing with eyes closed, 3) crying dramatically with big tears, 4) sleeping curled up. Flat 2D cartoon style, bold clean outlines, soft pastel shading, consistent character design in all four.
```
