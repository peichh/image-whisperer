# Benchmarks

## What is measured

`cases.jsonl` holds 112 prompt-level cases (Thai and English) across 31 categories and all 8 adapters: vague and detailed requests, people, groups, complex poses, smartphone looks, anime and other styles, products, architecture, graphics with text, edits, references, conversational revisions, optimisation, critique and cross-model comparison. Schema: `schemas/benchmark-case.schema.json`.

Each case compares three prompts:

- **A raw**: the user's request as typed.
- **B conventional enhancement**: the request plus the generic quality-tag suffix many prompt enhancers add (`masterpiece, best quality, ultra detailed, 8k, hyperrealistic, cinematic lighting…`), defined in `run.py`.
- **C Image Whisperer**: a prompt written by following `SKILL.md` for the stated target model.

Metrics (`run.py`, no dependencies):

| Metric | How |
|---|---|
| Intent preservation | share of `must_keep` regexes found (each locked detail from the request; Thai and English alternatives) |
| Unrequested additions | count of `must_not_add` regexes and generic style-push words found that were not in the request |
| Specificity | share of 4 scene slots (setting, light, composition, medium) mentioned |
| Model compatibility | adapter lint: no foreign syntax (`--ar` outside Midjourney, `(x:1.2)` outside SD, `::` on V7+), no negative prompt for models without one, word count inside the adapter's band |
| Skill checks | optional `skill_checks` regexes for behaviour the user did not state (a person's moment, camera height); must pass for C, not counted as intent |
| Context awareness | intent preservation on revision cases that carry earlier-turn context |
| Efficiency | mean words (reported, not scored) |

Run: `python3 benchmarks/run.py --report benchmarks/REPORT.md`

## What is NOT measured

- **Image quality.** No images were generated. Nothing here shows that images get better.
- **Independence.** C prompts and the checks come from the same project. Lexical checks can be gamed. Treat the numbers as a regression baseline: a change to the skill should not make them worse.
- Instruction following inside real models, which differs per model and version.

For real image tests use `visual-protocol.md`.

## Adding cases

Add a JSON line, run `python3 tests/test_skill.py` (schema and coverage checks) and the benchmark. Failed real-world prompts are the best new cases: add the request, what was lost (`must_keep`) or wrongly added (`must_not_add`), and the corrected C prompt.
