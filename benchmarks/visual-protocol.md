# Visual evaluation protocol (optional, needs real image generation)

Not run for this repository. Use it if you have generation access and want evidence about images, not just prompts.

1. Pick at least 30 cases from `cases.jsonl` across categories; fix the target model and version.
2. Generate A, B and C prompts with the same settings (seed if available, same aspect ratio). At least 2 images per prompt.
3. Blind the images (shuffle, hide which arm made them).
4. For each image, answer the case's question list (from `must_keep` plus coherence questions in `core/quality-critic.md`) with yes/no, and rate 1-5: intent match, realism or style fidelity, unrequested changes, overall preference.
5. Use at least 2 raters; report agreement. Optionally add an automatic VQA score (e.g. VQAScore, arXiv:2404.01291).
6. Report per category and per model with the number of images. Publish the prompts, settings and raw ratings.
7. Do not generalise to other models or versions.

Cost: every image may be billed. Get approval before running.
