# Adapters

One file per target model. Each has: prompt form, rules, text handling, negative-prompt policy, editing, settings and an example. Load only the target's adapter.

| Model | File | Negative prompt | Preferred form |
|---|---|---|---|
| Gemini (Nano Banana) | `gemini.md` | no (semantic positives) | narrative |
| FLUX 3 / FLUX.2 / Kontext | `flux.md` | no | narrative, optional JSON |
| Midjourney | `midjourney.md` | `--no` for objects only | short + parameters |
| SD 1.5 / SDXL / SD3 | `sdxl.md` | yes | compact phrases |
| Qwen-Image / Edit | `qwen-image.md` | field exists, default blank | detailed narrative |
| Z-Image | `z-image.md` | base: yes; Turbo: no effect | long descriptive |
| Seedream | `seedream.md` | no | concise narrative |
| Unknown | `universal.md` | no | plain narrative |

To add a model, copy `universal.md`, fill each section from official docs, add sources to `research/sources.md`, and add benchmark cases (see `docs/maintaining.md`).
