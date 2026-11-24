# Adapter: Qwen-Image and Qwen-Image-Edit

Covers Qwen-Image (20B MMDiT, Apache-2.0) and Qwen-Image-Edit (2511 and later), local (Diffusers, ComfyUI) or hosted (Qwen Chat, Alibaba Cloud Model Studio). Sources: Qwen-Image GitHub, model cards, technical report arXiv:2508.02324 (`research/sources.md`).

## Prompt form: detailed narrative

Qwen-Image's strengths per its docs: complex text rendering (especially Chinese, also English), and precise editing. It reads detailed natural-language descriptions. The Qwen repo recommends a prompt-enhancement step for short prompts — this skill is that step.

- Write full sentences: subject, action, setting, light, style, then text.
- 50-200 words; longer is fine for posters and layouts with many text elements.
- English or Chinese prompts both work. For Thai requests write English; keep Thai text quoted (Thai rendering is not a documented strength; warn the user).

## Rules

1. **Text**: Qwen-Image is the best choice in this list for posters with several text blocks. Quote every text exactly, give each block a position, size and font feel.
2. **Negative prompt**: the pipeline has a `negative_prompt` field (true CFG; official examples pass `" "` with `true_cfg_scale=4.0`). Leave it as a single space unless the user wants exclusions; if so, keep it short.
3. Use no weight syntax.
4. Aspect ratio/resolution: pipeline settings (`width`, `height`), not in the prompt.

## Editing (Qwen-Image-Edit)

- Instruction form: "Change the sign text to "ร้านป้าแดง", keep the font style, colour and everything else unchanged."
- 2511 improves consistency for single and multiple people, product identity, multi-image input (combine people/products from several images) and has built-in lighting and new-viewpoint LoRAs.
- For identity: "keep the person's face and identity unchanged".
- Text edits: name the exact old and new text.

## Example

User: "โปสเตอร์ร้านชาไข่มุก เปิดใหม่ ลด 20% สีพาสเทล"

```
A cheerful pastel promotional poster for a new bubble tea shop. In the centre, a tall clear cup of brown sugar milk tea with chewy tapioca pearls and condensation, surrounded by floating pearls and soft clouds on a mint and peach gradient background. At the top, a large rounded bold headline "GRAND OPENING"; below the cup a badge reading "20% OFF"; at the bottom small text "เปิดใหม่ ซอยอารีย์ 1". Clean flat graphic design with soft shadows, plenty of breathing space, cute and friendly mood.
```
Note to user: Thai lines may render imperfectly; the English lines are more reliable.
