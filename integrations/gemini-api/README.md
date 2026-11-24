# Gemini API agents

Use Image Whisperer inside your own code. Two steps: a text model writes the prompt with the skill's instructions; then (optionally) an image model renders it. You need **your own** Gemini API key; the skill itself is free and needs no key.

`whisper.py` uses the official `google-genai` SDK and the Interactions API calls shown in https://ai.google.dev/gemini-api/docs/image-generation.

```bash
pip install google-genai
export GEMINI_API_KEY=...            # your key

# show what would be sent, no API call, no key needed
python3 whisper.py "ขอรูปตลาดน้ำตอนเช้า สำหรับหัวบล็อก" --dry-run

# write the prompt only (text model, low cost)
python3 whisper.py "ขอรูปตลาดน้ำตอนเช้า สำหรับหัวบล็อก"

# write the prompt and generate an image (image model, paid per image)
python3 whisper.py "ขอรูปตลาดน้ำตอนเช้า สำหรับหัวบล็อก" --generate --aspect-ratio 16:9 --size 2K
```

Model names are flags (`--text-model`, `--image-model`) because Google renames models often; check the models page before use.

Status: the dry-run path is tested in CI. The live API path was not run by the maintainers (no key was used when building this repository).
