# Adapter: Midjourney

Facts from docs.midjourney.com, verified 2026-11-24 (`research/sources.md`). Default version at that date: V8.2. Parameters change between versions — check the Version page when unsure.

## Prompt form: short descriptive text, then parameters

Midjourney docs: short, simple prompts typically work best; describe what you want; long lists of instructions are not followed well. Useful content: subject, medium, environment, lighting, colour, mood, composition.

Shape:

```
<subject and action>, <setting>, <medium/style>, <light>, <mood/colour>, <composition> --ar W:H [--raw] [other parameters]
```

- Typical length: 10-40 words before parameters; up to ~60 for complex scenes.
- Commas or short sentences both work. Avoid paragraph-long instructions.
- Use numbers and collective nouns ("three cats", "a flock of birds").

## Parameters (put at the very end)

| Parameter | Use |
|---|---|
| `--ar W:H` | aspect ratio; integers only (`--ar 16:9`, not `1.78:1`); V8.x up to 14:1 |
| `--raw` | less Midjourney house style; more literal and photographic. Use for realistic and phone-photo looks |
| `--no x, y` | exclude objects only when the user asks to exclude something |
| `--c 0-100` | chaos: more varied grid; use for exploration requests |
| `--sref <url or code>` + `--sw 0-1000` | style reference and its strength |
| `--v 8.2` | version; omit unless the user needs a specific version |
| `--s 0-1000` | stylisation; lower = closer to the prompt |

- Multi-prompts `::` and weights: the docs state these work on versions up to 6.1 only; do not use them for V8.x.
- Do not use FLUX/SD syntax (`(word:1.2)`, negative prompt sections).

## Rules

1. Keep the user's subject first.
2. Realism: add `--raw` and describe a real camera context ("candid phone photo"). Do not stack "photorealistic, hyper-realistic, 8K".
3. Text in images: possible on recent versions but less reliable for long or non-Latin text; quote short text; warn about Thai text.
4. Artist names: avoid living artists; describe the traits instead.

## Editing

V8.x replaces Omni Reference / Character Reference with the **Edit Model**: up to 4 reference images, instruction-style prompts ("Change the jacket to red leather, keep the person and background the same"). On Discord: `--edit <image urls>`. In the web editor use the Edit tools and write the instruction as the prompt.

## Example

User: "Cozy rainy Bangkok café, film photo vibe, for my IG"

```
a cozy small café in Bangkok on a rainy afternoon, raindrops on the front window, a young woman reading by the glass with an iced latte, warm tungsten lamps inside, wet street and blurred tuk-tuk outside, 35mm film photo, soft grain, muted warm colours --ar 4:5 --raw
```
