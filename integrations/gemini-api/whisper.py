#!/usr/bin/env python3
"""Image Whisperer for Gemini API agents.

Step 1: a Gemini text model rewrites a casual request into a Gemini image prompt,
        using the standalone Image Whisperer instructions and the Gemini adapter.
Step 2 (only with --generate): a Gemini image model renders the prompt.
"""
import argparse
import base64
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INSTRUCTIONS = ROOT / "integrations" / "standalone" / "image-whisperer-instructions.md"
ADAPTER = ROOT / "adapters" / "gemini.md"

OUTPUT_RULE = (
    "Target model: Gemini image generation (API). Return only the final image prompt as plain text, "
    "with no code fences, no settings and no commentary."
)


def build_input(request: str) -> str:
    instructions = INSTRUCTIONS.read_text(encoding="utf-8").split("\n---\n", 1)[-1].strip()
    adapter = ADAPTER.read_text(encoding="utf-8")
    return f"{instructions}\n\n# Gemini adapter\n\n{adapter}\n\n{OUTPUT_RULE}\n\nUser request:\n{request}"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("request")
    p.add_argument("--text-model", default="gemini-3.8-flash")
    p.add_argument("--image-model", default="gemini-nano-banana-2.1")
    p.add_argument("--generate", action="store_true", help="also create the image (paid)")
    p.add_argument("--aspect-ratio", default=None)
    p.add_argument("--size", default=None, choices=[None, "512px", "1K", "2K", "4K"])
    p.add_argument("--out", default="image-whisperer.png")
    p.add_argument("--dry-run", action="store_true", help="print the requests, call nothing")
    a = p.parse_args()

    text_req = {"model": a.text_model, "input": build_input(a.request)}
    response_format = {"type": "image"}
    if a.aspect_ratio:
        response_format["aspect_ratio"] = a.aspect_ratio
    if a.size:
        response_format["image_size"] = a.size

    if a.dry_run:
        print(json.dumps({"step1": {"model": text_req["model"], "input_chars": len(text_req["input"])},
                          "step2": {"model": a.image_model, "response_format": response_format} if a.generate else None},
                         ensure_ascii=False, indent=2))
        return 0

    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        print("Set GEMINI_API_KEY (your own key) or use --dry-run.", file=sys.stderr)
        return 2

    from google import genai  # pip install google-genai

    client = genai.Client()
    prompt = client.interactions.create(**text_req).output_text.strip()
    print(prompt)

    if a.generate:
        img = client.interactions.create(model=a.image_model, input=prompt, response_format=response_format)
        Path(a.out).write_bytes(base64.b64decode(img.output_image.data))
        print(f"saved {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
