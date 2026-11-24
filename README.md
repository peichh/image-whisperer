# Image Whisperer

**[ภาษาไทย](README.th.md)**

A free, open-source Agent Skill that turns casual image requests (Thai or English) into prompts the target image model can actually follow. It is Gemini-first (Nano Banana, Gemini app, Gemini CLI, Gemini API), and also has adapters for FLUX, Midjourney, Stable Diffusion/SDXL, Qwen-Image, Z-Image, Seedream and unknown models.

It is not an image generator, a website or a trained model. It is a set of Markdown instructions. No backend, no API key, no cost.

## What it does

- Works out what the image is **for** and keeps everything you said: counts, text, style, people as they are.
- Adds only the details the image needs (light, setting, framing) and tells you what it assumed.
- Checks the scene makes physical sense (one light logic, contact shadows, believable poses).
- Writes the prompt in the form **each model** reads best: prose for Gemini/FLUX/Seedream, short text plus `--parameters` for Midjourney, compact phrases plus a negative prompt for SDXL. It does not add unsupported syntax or negative prompts by default.
- Handles edits ("change X, keep Y"), reference images, critique of finished images, prompt clean-up and side-by-side model comparison. You do not need to name a mode.
- Gets the **look** right, not just the objects: translates vague style words ("premium anime", "cinematic", a studio name) into visible traits on 16 axes (line, shading, colour grading, light, composition, texture, imperfection, emotion…), counters generic AI looks (mobile-game art, generic anime faces, neon overload) unless you asked for them, and can learn your taste as a reusable **aesthetic profile**.
- Loads knowledge (anatomy, photography, lighting, materials, composition, colour, "AI look" fixes, 20 styles) only when the request needs it.

## Install

| Where | How |
|---|---|
| Gemini app (personal accounts) | Upload [`dist/image-whisperer.zip`](dist/image-whisperer.zip) under **Skills → New skill → Upload** |
| Gemini Gems (work/school) | Paste [`integrations/standalone/image-whisperer-instructions.md`](integrations/standalone/image-whisperer-instructions.md) as instructions |
| Gemini CLI | `gemini skills install https://github.com/peichh/image-whisperer.git` |
| Antigravity | copy to `.agents/skills/image-whisperer/` |
| Claude Code and other Agent Skills hosts | `git clone https://github.com/peichh/image-whisperer.git ~/.claude/skills/image-whisperer` |
| Any chat assistant | paste the standalone instructions |
| Your own Gemini API agent | [`integrations/gemini-api/`](integrations/gemini-api/README.md) |

Details: [`integrations/`](integrations/README.md). Thai guide: [`docs/install.th.md`](docs/install.th.md).

## Example

Request: "ขอรูปยายกับหลานทำขนมครกหน้าบ้าน ถ่ายด้วยมือถือ" (Gemini)

```
A candid smartphone photo of a Thai grandmother, around 70, and her granddaughter, about 8, making khanom krok together at a small charcoal griddle in front of their wooden house in the late afternoon. The grandmother pours coconut batter into the dimpled cast-iron pan while the girl leans in, watching closely. Natural warm side light, a bit of smoke from the charcoal, everyday clothes, plastic stools and potted plants around them. Shot at eye level with a phone's wide main camera, slightly imperfect framing, realistic skin and natural phone HDR.
```

Not added: studio light, model looks, "cinematic", "8K". More in [`examples/`](examples/README.md).

## Benchmark (prompt-level only)

111 cases (56 Thai, 55 English) across 31 categories and 8 target models, comparing the raw request (A), a typical quality-tag enhancer (B) and this skill (C). Full report: [`benchmarks/REPORT.md`](benchmarks/REPORT.md).

| Metric | A raw | B conventional | C Image Whisperer |
|---|---|---|---|
| Intent preservation | 89.2% | 89.5% | 100.0% |
| Unrequested additions per prompt | 0.00 | 8.07 | 0.00 |
| Scene specificity | 16.7% | 56.5% | 83.3% |
| Model compatibility | 27.9% | 82.0% | 100.0% |

A second set of 24 style-fidelity cases checks that the look is described in visible terms: a content-only prompt (S) covers 4% of the defining style axes and fails every case, label stacking (B) relies on style labels alone in 88% of cases, and the skill (C) covers 100% of the axes and passes every case. Report: [`benchmarks/style-fidelity/REPORT.md`](benchmarks/style-fidelity/REPORT.md).

**No images were generated.** These are lexical checks on prompt text, written by the same project as the skill prompts. They are a regression baseline, not proof of better images. See [`benchmarks/README.md`](benchmarks/README.md) and [`docs/limitations.md`](docs/limitations.md).

## Repository layout

```
SKILL.md            entry point (mode detection, routing)
core/               intent, visual reasoning, scene, aesthetic translation, aesthetic profile, compiler, critic, editing, references
knowledge/          anatomy, physical realism, photography, lighting, materials, composition, colour, anti-AI look, anti-generic aesthetics
styles/             20 style modules (smartphone, anime, Thai art, product, graphic design, ...)
adapters/           gemini, flux, midjourney, sdxl, qwen-image, z-image, seedream, universal
schemas/            scene and benchmark JSON Schemas
examples/           worked examples for every mode
integrations/       Gemini app, Gems, CLI/Antigravity, API, other hosts, standalone
benchmarks/         cases, runner, report, visual test protocol
tests/              validation tests (stdlib only)
research/           sources with verified / inferred / unknown tags
docs/               architecture, maintenance, limitations, roadmap, Thai guides
dist/               upload-ready zip
```

## Development

```bash
python3 tests/test_skill.py                                   # validation
python3 benchmarks/run.py --report benchmarks/REPORT.md       # benchmark
python3 benchmarks/style_fidelity.py --report benchmarks/style-fidelity/REPORT.md
python3 scripts/build_dist.py                                 # rebuild the zip
```

How to improve the skill and keep model facts current: [`docs/maintaining.md`](docs/maintaining.md).

## License

MIT. Model names are trademarks of their owners; this project is not affiliated with Google, Black Forest Labs, Midjourney, Stability AI, Alibaba, ByteDance or OpenAI.
