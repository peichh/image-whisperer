#!/usr/bin/env python3
"""Validation tests for Image Whisperer. Standard library only: python3 tests/test_skill.py"""
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "benchmarks"))
sys.path.insert(0, str(ROOT / "scripts"))
import run as bench  # noqa: E402
import build_dist  # noqa: E402


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "missing YAML frontmatter"
    fm, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^\S[^:]*:", line):
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            fm[key] = val.strip('"') if val else {}
        elif key and isinstance(fm[key], dict):
            k, _, v = line.strip().partition(":")
            fm[key][k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


class SkillSpec(unittest.TestCase):
    """Agent Skills specification (agentskills.io/specification)."""

    def setUp(self):
        self.text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.fm, self.body = frontmatter(self.text)

    def test_name(self):
        n = self.fm["name"]
        self.assertRegex(n, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(n), 64)
        self.assertEqual(n, "image-whisperer")

    def test_description(self):
        d = self.fm["description"]
        self.assertTrue(1 <= len(d) <= 1024, len(d))
        for word in ("Gemini", "prompt", "edit"):
            self.assertIn(word, d)

    def test_optional_fields(self):
        self.assertLessEqual(len(self.fm.get("compatibility", "")), 500)
        self.assertEqual(self.fm.get("license"), "MIT")
        self.assertIsInstance(self.fm.get("metadata"), dict)

    def test_body_size(self):
        self.assertLess(len(self.text.splitlines()), 500)
        self.assertLess(len(self.body.split()), 3500)  # ~<5000 tokens

    def test_referenced_files_exist(self):
        for ref in sorted(set(re.findall(r"`((?:core|knowledge|adapters|styles|schemas|examples|research)/[\w./-]+)`", self.text))):
            self.assertTrue((ROOT / ref).exists(), ref)

    def test_all_modes_documented(self):
        for mode in ("AUTO", "PROMPT ONLY", "EDIT", "CRITIQUE", "OPTIMIZE", "REFERENCE", "COMPARE"):
            self.assertIn(mode, self.body)


class Modules(unittest.TestCase):
    def test_every_markdown_link_resolves(self):
        for md in ROOT.rglob("*.md"):
            if ".git" in md.parts or "research_raw" in md.parts:
                continue
            for ref in re.findall(r"`((?:core|knowledge|adapters|styles|schemas|integrations|benchmarks|docs|examples|research|dist|tests|scripts)/[\w./-]+\.(?:md|json|py|zip|jsonl))`", md.read_text(encoding="utf-8")):
                self.assertTrue((ROOT / ref).exists(), f"{md.relative_to(ROOT)} -> {ref}")

    def test_adapters_have_sections(self):
        for name in ("gemini", "flux", "midjourney", "sdxl", "qwen-image", "z-image", "seedream", "universal"):
            t = (ROOT / "adapters" / f"{name}.md").read_text(encoding="utf-8")
            for sec in ("## Prompt form", "## Rules", "## Editing", "## Example"):
                self.assertIn(sec, t, f"{name}: {sec}")
            self.assertIn(name, bench.BANDS)

    def test_styles_have_sections_and_index(self):
        index = (ROOT / "styles" / "README.md").read_text(encoding="utf-8")
        for f in (ROOT / "styles").glob("*.md"):
            if f.name == "README.md":
                continue
            t = f.read_text(encoding="utf-8")
            for sec in ("## When", "## Key traits", "## Prompt words", "## Avoid", "## Model notes"):
                self.assertIn(sec, t, f"{f.name}: {sec}")
            self.assertIn(f"styles/{f.name}", index)

    def test_schemas_are_valid_json(self):
        for f in (ROOT / "schemas").glob("*.json"):
            s = json.loads(f.read_text(encoding="utf-8"))
            self.assertIn("$schema", s)

    def test_no_unsupported_syntax_in_adapter_examples(self):
        """Gemini/FLUX/Seedream/universal examples must not contain Midjourney or SD syntax."""
        for name in ("gemini", "flux", "seedream", "universal", "qwen-image", "z-image"):
            t = (ROOT / "adapters" / f"{name}.md").read_text(encoding="utf-8")
            for block in re.findall(r"```\n(.*?)```", t, re.S):
                self.assertNotRegex(block, r"\s--(ar|v|raw|no)\b", name)
                self.assertNotRegex(block, r"\([^()]+:\d\.\d\)", name)


class Benchmark(unittest.TestCase):
    def setUp(self):
        self.cases = bench.load()
        self.schema = json.loads((ROOT / "schemas" / "benchmark-case.schema.json").read_text(encoding="utf-8"))

    def test_count_and_coverage(self):
        self.assertGreaterEqual(len(self.cases), 100)
        langs = {c["lang"] for c in self.cases}
        self.assertEqual(langs, {"th", "en"})
        targets = {c["target"] for c in self.cases}
        self.assertEqual(targets, set(bench.BANDS))
        cats = {c["category"] for c in self.cases}
        for need in ("vague", "detailed", "people", "multi_person", "complex_pose", "smartphone", "anime",
                     "product", "architecture", "graphic", "edit", "reference", "revision", "optimize", "critique", "compare"):
            self.assertIn(need, cats)
        modes = {c["mode"] for c in self.cases}
        self.assertTrue({"edit", "reference", "optimize", "critique", "compare"} <= modes)

    def test_schema_fields(self):
        props, req = self.schema["properties"], self.schema["required"]
        ids = set()
        for c in self.cases:
            for k in req:
                self.assertIn(k, c, c.get("id"))
            for k in c:
                self.assertIn(k, props, f"{c['id']}: unknown field {k}")
            self.assertRegex(c["id"], props["id"]["pattern"])
            self.assertIn(c["target"], props["target"]["enum"])
            self.assertIn(c["mode"], props["mode"]["enum"])
            self.assertNotIn(c["id"], ids)
            ids.add(c["id"])
            for r in c["must_keep"] + c["must_not_add"]:
                re.compile(r)

    def test_skill_arm_has_no_regressions(self):
        rows = bench.run()
        bad = [(r["id"], r["C"]) for r in rows if r["C"]["intent"] < 1 or r["C"]["assumptions"] or not r["C"]["compat"]]
        self.assertEqual(bad, [])

    def test_report_is_current(self):
        self.assertEqual((ROOT / "benchmarks" / "REPORT.md").read_text(encoding="utf-8"), bench.report(bench.run()))

    def test_lint_catches_known_errors(self):
        self.assertTrue(bench.lint("gemini", "a cat on a mat in soft light, photo --ar 16:9 " + "word " * 30, ""))
        self.assertTrue(bench.lint("flux", "a cat " * 20, "blurry"))
        self.assertTrue(bench.lint("midjourney", "a cat :: 2 dog --v 8", ""))
        self.assertFalse(bench.lint("midjourney", "a grey cat asleep on a sunny windowsill --ar 3:2 --raw", ""))


class Distribution(unittest.TestCase):
    def test_zip_is_current_and_runtime_only(self):
        with tempfile.TemporaryDirectory() as d:
            fresh = build_dist.build(Path(d) / "x.zip")
            committed = ROOT / "dist" / "image-whisperer.zip"
            self.assertTrue(committed.exists(), "run python3 scripts/build_dist.py")
            self.assertEqual(fresh.read_bytes(), committed.read_bytes(), "dist zip outdated: run python3 scripts/build_dist.py")
        names = zipfile.ZipFile(ROOT / "dist" / "image-whisperer.zip").namelist()
        self.assertIn("SKILL.md", names)
        self.assertFalse([n for n in names if n.startswith(("tests/", "benchmarks/", "research/", "docs/"))])
        self.assertLess((ROOT / "dist" / "image-whisperer.zip").stat().st_size, 100 * 1024 * 1024)

    def test_standalone_instructions(self):
        t = (ROOT / "integrations" / "standalone" / "image-whisperer-instructions.md").read_text(encoding="utf-8")
        self.assertIn("\n---\n", t)
        self.assertLess(len(t.split()), 2000)
        for model in ("Gemini", "FLUX", "Midjourney", "SDXL", "Qwen", "Z-Image", "Seedream", "Unknown model"):
            self.assertIn(model, t)

    def test_gemini_api_dry_run(self):
        out = subprocess.run([sys.executable, str(ROOT / "integrations" / "gemini-api" / "whisper.py"), "แมว", "--dry-run", "--generate", "--size", "2K"],
                             capture_output=True, text=True, check=True).stdout
        data = json.loads(out)
        self.assertEqual(data["step2"]["response_format"]["image_size"], "2K")


if __name__ == "__main__":
    unittest.main(verbosity=1)
