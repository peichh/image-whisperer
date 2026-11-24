#!/usr/bin/env python3
"""Build dist/image-whisperer.zip: the runtime skill only (for Gemini app / Claude upload).

Deterministic: fixed file order and timestamps, so the zip only changes when content changes.
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ["SKILL.md", "LICENSE", "core", "knowledge", "adapters", "styles", "schemas", "examples"]
OUT = ROOT / "dist" / "image-whisperer.zip"


def runtime_files():
    for entry in RUNTIME:
        p = ROOT / entry
        if p.is_file():
            yield p
        else:
            yield from sorted(x for x in p.rglob("*") if x.is_file())


def build(out: Path = OUT) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in runtime_files():
            info = zipfile.ZipInfo(str(f.relative_to(ROOT)), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes())
    return out


if __name__ == "__main__":
    p = build(Path(sys.argv[1]) if len(sys.argv) > 1 else OUT)
    print(p, p.stat().st_size, "bytes")
