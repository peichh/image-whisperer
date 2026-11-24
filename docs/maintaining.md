# Maintaining and improving the skill

## Self-improvement loop

1. **Collect failures**: a user report, a bad image, a critique result, or a new official doc page.
2. **Turn it into a benchmark case** (`benchmarks/cases.jsonl`): the request, what was lost (`must_keep`), what was wrongly added (`must_not_add`), the target model, and the corrected prompt.
3. **Fix the smallest module** that caused it (an adapter rule, a style file, a knowledge table). Do not grow `SKILL.md` unless the routing itself was wrong.
4. **Run** `python3 tests/test_skill.py`, `python3 benchmarks/run.py --report benchmarks/REPORT.md` and `python3 benchmarks/style_fidelity.py --report benchmarks/style-fidelity/REPORT.md`; a style complaint ("looks generic") becomes a `benchmarks/style-fidelity/cases.jsonl` case; rebuild `python3 scripts/build_dist.py`.
5. **Record sources**: any new model fact goes into `research/sources.md` with [V]/[I]/[U] and the date.

## Official documentation checks (every release, or monthly)

| Model | Page to re-check |
|---|---|
| Gemini | https://ai.google.dev/gemini-api/docs/image-generation , Gemini app skills help |
| FLUX | https://docs.bfl.ai/guides/prompting_summary |
| Midjourney | Version, Parameter List and Edit pages on docs.midjourney.com |
| Qwen-Image | https://github.com/QwenLM/Qwen-Image |
| Z-Image | https://github.com/Tongyi-MAI/Z-Image |
| Seedream | BytePlus ModelArk Seedream prompt guide |
| SDXL / Diffusers | Diffusers prompting docs |

Model names, limits and parameters are the most time-sensitive facts; adapters keep them in one table at the top so they are easy to update.

## Adding a model

Copy `adapters/universal.md`, fill each section from official docs only, add a length band in `benchmarks/run.py` (`BANDS`), add at least 5 cases, and add the row to `adapters/README.md` and the routing table in `SKILL.md`.
