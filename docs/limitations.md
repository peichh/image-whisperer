# Limitations

- **A prompt cannot add model capability.** If a model cannot render Thai text, exact hands or a specific person, better words help only a little.
- **No visual testing was done.** The benchmark is prompt-level only. We make no claim that images look better; see `benchmarks/README.md`.
- **Self-authored benchmark.** The skill-arm prompts and the checks come from the same project, so the numbers are a regression baseline, not independent evidence.
- **Thai text inside images** is unreliable on every model listed; Thai is not in Gemini's documented best-performance language list.
- **Time-sensitive facts.** Model names, reference-image limits, parameters and app features were checked on 2026-11-24 and will change.
- **Host behaviour varies.** Whether a host loads extra files, can see images, or can generate images inside a skill depends on the host (e.g. the Gemini app skills page lists tools that do not work in skills yet).
- **Unverified areas**: Seedream 5.x prompt differences; Midjourney text rendering quality; live Gemini API path in `integrations/gemini-api/whisper.py` (only the dry run is tested).
- **Safety** is the host model's job; the skill adds basic rules (no sexualised minors, respect for real people) but is not a safety filter.
