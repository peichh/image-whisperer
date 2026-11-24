# Research notes and sources

Retrieved 2026-11-24. Every claim below is tagged:

- **[V]** verified: stated in the linked official documentation or model card at retrieval time.
- **[I]** inference: our reading or extrapolation; treat as a hypothesis to test.
- **[U]** unknown: not publicly documented; do not claim.

Model docs change fast. Re-check a source before changing an adapter (see `docs/maintaining.md`).

## Agent Skills format

Source: https://agentskills.io/specification

- [V] A skill is a folder with `SKILL.md` (YAML frontmatter + Markdown body). Optional `scripts/`, `references/`, `assets/`.
- [V] `name`: 1-64 chars, lowercase a-z, 0-9, hyphen; no leading/trailing/double hyphen; must match the folder name.
- [V] `description`: 1-1024 chars; say what it does and when to use it, with trigger keywords.
- [V] Optional `license`, `compatibility` (<=500 chars), `metadata` (string map), `allowed-tools` (experimental).
- [V] Progressive disclosure: metadata (~100 tokens) at startup; body (<5000 tokens recommended, <500 lines) on activation; other files on demand. Keep file references one level deep from SKILL.md.
- [V] Validator: the `skills-ref` package (`pip install skills-ref`, command `agentskills validate <dir>`; verified with v0.1.1).

## Gemini surfaces

### Gemini app (gemini.google.com): Gems are being replaced by skills

Sources: https://support.google.com/gemini/answer/15146780 , https://support.google.com/gemini/answer/18560919 , https://support.google.com/gemini/answer/17094296

- [V] Personal accounts (18+): from 2026-11-17 Gems become read-only and transition to skills; on 2026-12-17 Gems are removed. Work accounts March 2027, education June 2027.
- [V] Gemini app skills: available in Gemini web, mobile and Mac app. Create from a template, manually, with Gemini's help, or by **uploading a `SKILL.md`, a folder, or a `.zip` with `SKILL.md` in its root**.
- [V] Skill name must be lowercase-hyphen; total upload <= 100 MB; plain-text files (.md, .json, .yaml, .txt, .py ...) supported; .ts/.tsx not supported; scripts cannot reach the internet.
- [V] Gemini applies a relevant skill automatically, or the user types `/` (soon `@`) + skill name. Skills stack.
- [V] Most default Gem tools (Create video, Create music, Canvas, Deep Research, Guided learning) do not work inside skills yet. The page does not say whether image generation works inside a skill. [U] → our package must also work as plain instructions when the host cannot generate images.
- [V] Google's tips for skills: define when to use it, keep it concise, give examples.
- [I] Work/school accounts still have Gems until 2027, so we keep a Gem-instructions version too.

### Gemini CLI and Antigravity

Sources: https://geminicli.com/docs/cli/skills/ , https://geminicli.com/docs/extensions/ , https://antigravity.google/docs/skills

- [V] Gemini CLI implements the Agent Skills standard. Discovery tiers: built-in, extension, user (`~/.gemini/skills/` or `~/.agents/skills/`), workspace (`.gemini/skills/` or `.agents/skills/`).
- [V] `gemini skills install <git-url> [--path <subdir>] [--scope user|workspace]`; `/skills list|link|enable|disable|reload`.
- [V] Activation: model calls `activate_skill`; the user confirms; SKILL.md body and folder listing are injected and the folder becomes readable.
- [V] Extensions can bundle skills; install with `gemini extensions install <github-url>`.
- [V] Banner on geminicli.com: "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026."
- [V] Antigravity (app, CLI, IDE) reads skills from `<workspace>/.agents/skills/<name>/` and `~/.gemini/config/skills/<name>/`; `description` is required, `name` defaults to the folder name.
- [V] Gemini CLI itself does not ship an image-generation tool in these docs. [I] Image generation from the CLI needs an MCP server or a script that calls the Gemini API with the user's own key; we document it as optional and never required.

### Gemini API native image generation ("Nano Banana")

Source: https://ai.google.dev/gemini-api/docs/image-generation

- [V] Models on the page: `gemini-nano-banana-2.1` (Nano Banana 2.1, recommended for new projects), `gemini-3.1-flash-image` (Nano Banana 2), `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite), `gemini-3-pro-image` (Nano Banana Pro), `gemini-2.5-flash-image` (Nano Banana, legacy). Imagen is listed as legacy.
- [V] Official prompting advice: describe the scene in narrative detail rather than keyword lists; give context and purpose ("a logo for a high-end minimalist skincare brand"); iterate conversationally ("keep everything the same, but ..."); for complex scenes give step-by-step instructions; use **semantic negative prompts** (describe the wanted absence positively: "an empty, deserted street"); control the camera with photographic terms (wide-angle, macro, low-angle).
- [V] Photoreal template from the docs: "A photorealistic [shot type] of [subject] in [setting]. [Light]. Shot from [camera angle] with a [lens type]."
- [V] `aspect_ratio` and `image_size` (`512px` only on 3.1 Flash Image, `1K` default, `2K`, `4K`; uppercase K required) are set in `response_format`/config, not in the prompt text. 3.1 Flash Image and Nano Banana 2.1 add 1:4, 4:1, 1:8, 8:1.
- [V] Reference images: up to 14 in total. Nano Banana 2.1 and 3.1 Flash Image: up to 10 high-fidelity objects and 4 characters; 3 Pro Image: 6 objects, 5 characters, 3 style references. 2.5 Flash Image works best with up to 3 inputs.
- [V] Gemini 3 image models use a thinking process by default and can use Google Search grounding.
- [V] Limitations: best languages listed are EN, ar-EG, de-DE, es-MX, fr-FR, hi-IN, id-ID, it-IT, ja-JP, ko-KR, pt-BR, ru-RU, ua-UA, vi-VN, zh-CN (**Thai is not listed**); the model may not return the exact number of images asked for; for text in images, generating the text first and then asking for the image works best; all outputs carry a SynthID watermark.
- [I] Because Thai is not in the best-performance list, the skill writes the final prompt in English and keeps Thai only for text that must appear in the image (quoted verbatim).
- [U] No negative-prompt field, seed or guidance parameters are documented for these models; we do not emit any.

## FLUX (Black Forest Labs)

Sources: https://docs.bfl.ai/guides/prompting_summary , https://docs.bfl.ai/guides/prompting_guide_flux2 , https://docs.bfl.ai/guides/prompting_guide_t2i_negative , https://docs.bfl.ai/guides/prompting_unified_reference

- [V] Current docs target **FLUX 3 Image**; FLUX.2 ([max], [pro], [flex], [klein], [dev]) and FLUX.1 Kontext still documented.
- [V] No negative prompts (FLUX.2, FLUX 3). Rewrite exclusions as positive opposites ("no people" → "empty, deserted").
- [V] FLUX.2 structure: Subject + Action + Style + Context; word order matters, most important first; 30-80 words usually ideal.
- [V] FLUX.2 supports JSON-structured prompts and hex colours tied to objects; quoted text for typography; camera/film names ("shot on Kodak Portra 400") for photoreal looks.
- [V] FLUX.2 [klein]: prose not keyword lists; "what you write is exactly what the model receives"; append `Style: ... Mood: ...`.
- [V] FLUX 3 Image: start short, it expands the prompt itself; add detail only where you need control; reference images by position "image 1"..; up to 10 references; optional element table with bbox `[top,left,bottom,right]` on a 0-1000 grid; edits as "Modify <ref_image_0> by replacing … with … Keep the rest of the image exactly unchanged, preserving …"; no `negative_prompt`, `seed`, `prompt_upsampling` or `guidance` fields (unknown fields → HTTP 422).
- [V] FLUX.2 can be prompted in many languages (Thai shown as an example); English tends to be most precise.
- [V] FLUX.1 Kontext edits: say what changes, state what is preserved, prefer specific verbs.

## Midjourney

Sources (via docs.midjourney.com): Prompt Basics, No, Multi-Prompts & Weights, Raw, Version, Style Reference, Edit Model, Aspect Ratio.

- [V] Default version V8.2 (since 2026-07-24). V8.1/V8.2 support HD 2048px; max aspect 14:1 (4:1 for HD).
- [V] Short, simple, descriptive prompts work best; avoid long lists of instructions; use specific numbers and collective nouns; describe what you want.
- [V] `--no x` excludes (equivalent to weight -0.5). Multi-prompts `::` and weights work only on versions up to 6.1 per the doc page.
- [V] `--ar W:H` (integers only), `--raw` (less house style, more literal/photographic), `--c 0-100` chaos/variety, `--sref <url|code>` + `--sw 0-1000`, `--v`.
- [V] V8.x: Edit Model replaces Omni Reference / Character Reference; up to 4 reference images; accepts instruction-style prompts; Discord `--edit <urls>`.
- [I] Parameters go at the end of the prompt; text inside the image is less reliable than Gemini/FLUX/Qwen (not benchmarked by us).

## Stable Diffusion XL / SD family

Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 , https://huggingface.co/docs/diffusers/using-diffusers/weighted_prompts

- [V] SDXL = base + optional refiner; two CLIP text encoders.
- [V] Diffusers guide: subject first, then style, then context; prefer a structured narrative over keyword lists for modern models.
- [V] Negative prompts and prompt weighting are supported in common SD tooling (diffusers, Compel, A1111/ComfyUI `(word:1.2)` syntax).
- [I] CLIP text encoders truncate at 77 tokens per chunk unless the UI chunks prompts, so the important content goes first and prompts stay compact.

## Qwen-Image

Sources: https://github.com/QwenLM/Qwen-Image , https://huggingface.co/Qwen/Qwen-Image , https://huggingface.co/Qwen/Qwen-Image-Edit-2511

- [V] 20B MMDiT foundation model; strong complex text rendering, especially Chinese; precise editing. Apache-2.0.
- [V] Qwen-Image-Edit-2511: better character and multi-person consistency, multi-image input, built-in lighting/viewpoint LoRAs, geometric reasoning. Example call uses `negative_prompt=" "` and `true_cfg_scale=4.0`.
- [V] Negative prompt is a pipeline field (true CFG).
- [I] Qwen's repo recommends prompt enhancement for short prompts; we treat a structured, specific English or Chinese prompt as best practice.

## Z-Image (Tongyi-MAI)

Sources: https://github.com/Tongyi-MAI/Z-Image , https://huggingface.co/Tongyi-MAI/Z-Image-Turbo , https://huggingface.co/Tongyi-MAI/Z-Image

- [V] 6B single-stream DiT family: Z-Image-Turbo (8 NFEs, `guidance_scale=0.0`), Z-Image (base, full CFG 3-5, 28-50 steps, 512²-2048² total area), Z-Image-Omni-Base, Z-Image-Edit.
- [V] Turbo: strong photorealism and accurate bilingual Chinese/English text rendering; a Prompt Enhancer adds reasoning.
- [V] Base: "robust negative control" — negative prompts work; Turbo runs with guidance 0, so a negative prompt has no effect there. [I]
- [V] Official example prompts are long, dense, comma-separated descriptive sentences (Chinese and English).

## Seedream (ByteDance)

Sources: https://docs.byteplus.com/en/docs/ModelArk/1829186 (Seedream 4.0-4.5 prompt guide), BytePlus ModelArk docs index (Dola Seedream 5.5, Seedream 5.0 pro/flash).

- [V] Use coherent natural language: subject + action + environment, then style, colour, light, composition. Avoid comma keyword piles.
- [V] State the use case ("Design a logo for a gaming company ...").
- [V] Put text that must appear in double quotes.
- [V] Editing: concise, unambiguous instructions, no vague pronouns, say explicitly what stays unchanged; arrows/boxes/doodles on the input can mark regions.
- [V] Seedream 4.x needs less description than 3.0; concise precise prompts beat stacked ornate adjectives.
- [V] Multi-image input and multi-image output (sets/series) supported.
- [U] We did not verify Seedream 5.5-specific prompting differences; adapter marks this.

## ChatGPT Images (OpenAI) — what is public

Sources: https://platform.openai.com/docs/guides/image-generation , https://cookbook.openai.com (image prompting guide).

- [V] ChatGPT/API image generation is natively multimodal and conversational: a chat model can call the image tool, and images can be edited over several turns with references.
- [I] The user-facing experience comes from the chat model rewriting short requests into a detailed image instruction before generation, plus multi-turn context. This is the behaviour this skill reproduces for other hosts.
- [U] Internal architecture, training data and any hidden prompt rewriting rules are not published. We do not claim to copy them.

## Research topics used for knowledge modules

These are general, stable craft knowledge (photography, anatomy, lighting, composition). The modules cite well-known references where specific numbers are used:

- Human proportions: the 7.5-8 head canon in figure drawing (e.g. Andrew Loomis, *Figure Drawing for All It's Worth*, 1943). [V for the book's content; artistic convention, not biology]
- Focal length / perspective: wider lenses exaggerate near features at close distance (perspective distortion depends on camera distance). [V standard optics]
- Smartphone main cameras are roughly 24-28 mm full-frame-equivalent wide lenses with small sensors and computational HDR/denoise. [V general; exact values vary per phone]
- Image quality assessment frameworks referenced for the critic rubric: TIFA (Hu et al., 2023, arXiv:2303.11897), DSG Davidsonian Scene Graph (Cho et al., 2024, arXiv:2310.18235), VQAScore (Lin et al., 2024, arXiv:2404.01291), GenEval (Ghosh et al., 2023, arXiv:2310.11513), T2I-CompBench / T2I-CompBench++ (Huang et al., arXiv:2307.06350). [V: arXiv IDs and titles checked 2026-11-24; these papers exist and propose question-based / compositional evaluation; we adapt the idea, we do not run their code]
- Prompt optimisation research referenced: "Optimizing Prompts for Text-to-Image Generation" / Promptist (Hao et al., 2022, arXiv:2212.09611); Qwen-Image Technical Report (arXiv:2508.02324); DALL·E 3 paper "Improving Image Generation with Better Captions" (Betker et al., OpenAI 2023) — descriptive synthetic captions improve prompt following, which motivates descriptive rewriting. [V papers exist; applying them here is I]

## Aesthetic translation and style fidelity (added 2026-11-24)

Problem reported by the project owner from their own tests [user observation, not verified by us]: with the same prompt, ChatGPT Images and Gemini both include the requested objects, but differ clearly in line quality, composition, light and mood; Gemini sometimes renders "premium" style requests as generic AI illustration or mobile-game artwork.

- [V] Gemini docs, "Stylized illustrations & stickers": "Describe the artistic style, subject, and medium. Be specific about the visual detail (bold lines, colors, etc.) for consistent results." Template: "A [style] of a [subject…] doing [activity]. The design features [visual qualities, e.g., bold outlines, cel-shading, etc.] and [color/background preference]." → official support for describing visible style traits rather than style labels.
- [V] Gemini 3 Pro Image accepts up to 3 images as style references (same page). → A reference image is the strongest way to pin a style on Gemini.
- [V] Somepalli et al., "Measuring Style Similarity in Diffusion Models" (arXiv:2404.01292): style is "a subjective property of an image that captures complex yet meaningful interactions of factors including but not limited to colors, textures, shapes"; proposes style descriptors separate from semantic content. → Supports evaluating style separately from content.
- [V] Gatys et al., "A Neural Algorithm of Artistic Style" (arXiv:1508.06576): content and style representations are separable in CNN features; style captured by texture/feature correlations. → Style lives largely in texture, stroke and colour statistics, which can be described independently of subject.
- [V] Pick-a-Pic / PickScore (arXiv:2305.01569), ImageReward (arXiv:2304.05977), HPS v2 (arXiv:2306.09341): preference models trained on many users' choices. [I] They predict *average* preference; optimising toward average taste plausibly pushes toward a polished, generic look — one reason individual profiles are needed.
- [V] ViPer (arXiv:2407.17365): models are "tuned to produce outputs that appeal to a broad audience"; ViPer asks users to comment on why they like/dislike a few images, infers structured liked/disliked visual attributes with an LLM, and uses them to guide generation; user studies show better alignment with individual preference. → Direct basis for the User Aesthetic Profile design (comments → structured attributes, not style names).
- [V] Visual Style Prompting (arXiv:2402.12974) and the multi-reference features of Gemini, FLUX 3, Qwen-Image-Edit, Midjourney (`--sref`) show reference images carry style more precisely than text. [I]
- [V] Formal analysis in art education (elements of art: line, shape, form, value, colour, texture, space; principles: balance, emphasis, movement, rhythm, unity) is the standard vocabulary for describing style in visible terms; our 16 axes extend it with stylisation-specific axes (anatomy, faces, imperfection, emotion).
- [U] How each model internally maps words like "premium anime" or studio names to visuals is not published. Adapter notes on this are hypotheses to test, marked [I].
