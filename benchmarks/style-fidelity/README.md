# Style fidelity benchmark

Tests the Aesthetic Translation Engine (`core/aesthetic-translation.md`, `knowledge/anti-generic-aesthetics.md`, `core/aesthetic-profile.md`).

## Prompt level (automated, `style_fidelity.py`)

`cases.jsonl` (schema `schemas/style-fidelity-case.schema.json`) has four kinds of case:

| Kind | Checks |
|---|---|
| translate | vague or label-style requests ("premium anime", "cinematic", "อาร์ตๆ") become visible traits |
| intentional_generic | the user asks for a "generic" look (gacha, synthwave neon, thick outlines); it must be kept, not "fixed" |
| profile | `examples/aesthetic-profile.example.json` is applied, or overridden when the request says so |
| cross_model | one aesthetic target compiled for Gemini, Midjourney, SDXL and FLUX with the same axes |

Arms: A raw request, B label stacking (request + "premium art style, masterpiece, cinematic…"), S semantic-only (good content prompt without style traits), C aesthetic translation.

Per prompt: semantic coverage (`keep`), share of the case's defining style axes described (`axes`), label-only reliance (labels present and < 50% axes), unwanted generic traits (`avoid`, ignoring negated phrases such as "not glossy"), adapter lint. A C prompt passes only if semantic = 100%, axes ≥ 80%, no label-only reliance, no unwanted traits and no lint errors. The S arm exists to show that a complete content prompt still fails when the style is not described.

## Image level (manual protocol, not run)

For each image score 1-5, separately: **semantic accuracy**, **aesthetic fidelity** (per defining axis, yes/no questions), **artistic execution**. Verdict rule (`verdict()` in `style_fidelity.py`, tested by `rubric-fixtures.jsonl`): success needs semantic ≥ 4, aesthetic ≥ 4, execution ≥ 3. An image with every object but the wrong style is `content_correct_style_off`, never success. Use blind A/B pairs (e.g. Gemini vs another model, S vs C prompt) with at least 2 raters; follow `benchmarks/visual-protocol.md` for setup and costs.
