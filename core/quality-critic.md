# Quality critic

Two checks: one for prompts (always), one for images (only if you can see the image).

## A. Prompt checklist (always)

| # | Check | Fail example |
|---|---|---|
| 1 | Every locked constraint is present, unchanged | user said "3 dogs", prompt says "dogs" |
| 2 | Nothing contradicts | "night" + "harsh noon shadows" |
| 3 | No unrequested style or beautification | "cinematic, supermodel" for a family snapshot |
| 4 | Image type matches the request | photoreal words in an anime prompt |
| 5 | Only parameters the target supports | `--ar` in a Gemini prompt; negative prompt for FLUX |
| 6 | Length inside the adapter's band | 300-word Midjourney prompt |
| 7 | Text to render is quoted, exact, short, placed | "add some text saying sale" |
| 8 | Edits have an explicit keep-list | "make the sky pink" without "keep everything else unchanged" |
| 9 | Assumptions are listed for the user | silently chose a male subject |
| 10 | Safe and respectful: no sexualisation of minors, no deceptive real-person imagery, host policy respected | — |

Fix failures before answering.

## B. Image critique (when an image is visible)

Inspired by question-based evaluation (TIFA, Davidsonian Scene Graph, VQAScore; see `research/sources.md`): turn the scene into yes/no questions and check each one.

1. **Faithfulness questions** from the scene: "Are there exactly three cats?", "Is the woman holding the cup in her right hand?", "Does the sign read 'ร้านป้าแดง'?"
2. **Coherence questions**: light direction consistent? contact shadows? hands and fingers correct? perspective? text legible?
3. **Intent questions**: does it fit the purpose and mood? any unrequested style drift (too glossy, too dramatic, too perfect)?
4. **Artifacts**: see `knowledge/anti-ai-appearance.md` list.

Rank failures by how visible they are. Report at most 3.

## C. Correction loop

- Fix with the smallest change: an edit instruction ("Keep everything the same, but make the sign read exactly 'ร้านป้าแดง'") or one added sentence, not a full rewrite.
- One problem per round when the model supports conversational editing; group small ones.
- **Stop** when all faithfulness questions pass and no visible defect remains, or after 2 correction rounds, or when the remaining defect is a known model limit (tell the user).
- Never run extra paid generations without the user's permission. Never claim a fix worked without seeing the new image.

## D. Critique output format

```
1. <problem> → <fix>
2. ...
Fixed prompt / edit instruction:
<code block>
```

If the image is fine, say so. Do not invent problems.
