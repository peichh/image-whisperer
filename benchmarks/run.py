#!/usr/bin/env python3
"""Prompt-level benchmark: A raw request vs B conventional enhancement vs C Image Whisperer.

No images are generated. All metrics are lexical heuristics over prompt text; see benchmarks/README.md.
Usage: python3 benchmarks/run.py [--report benchmarks/REPORT.md] [--json benchmarks/results.json]
"""
import argparse
import json
import re
import statistics as st
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases.jsonl"

# B: a typical "prompt enhancer" — the request plus a generic quality-tag suffix.
CONVENTIONAL_SUFFIX = (", masterpiece, best quality, ultra detailed, 8k, hyperrealistic, "
                       "cinematic lighting, sharp focus, award-winning, trending on artstation")

# Words that push style without being asked (counted only if absent from the request).
BLOAT = [r"masterpiece", r"best quality", r"ultra[- ]?detailed", r"\b8k\b", r"\b4k\b", r"hyper-?realistic",
         r"award[- ]winning", r"trending on artstation", r"cinematic", r"breathtaking", r"stunning",
         r"flawless", r"perfect (skin|face)", r"\bordinary\b", r"average-looking", r"octane render", r"unreal engine"]

SLOTS = {
    "setting": r"\b(in|at|on|inside|outside|by|beside|street|room|kitchen|beach|market|shop|house|office|background|studio|city|park|temple|forest|table|garden|road|cafe|café|field|sky)\b",
    "light": r"\b(light|lit|lighting|sun|sunlight|shadow|shadows|glow|lamp|daylight|overcast|neon|flash|dusk|dawn|golden hour|backlit|softbox|night)\b",
    "composition": r"\b(close-up|wide|medium shot|full[- ]body|overhead|top-down|eye level|eye-level|low angle|high angle|centred|centered|left|right|foreground|background|framing|vertical|horizontal|\d+:\d+|--ar|portrait orientation|flat lay|space for)\b",
    "medium": r"\b(photo|photograph|illustration|anime|painting|watercolou?r|render|3d|vector|poster|logo|infographic|sketch|manga|comic|drawing|sticker|icon|graphic|cartoon|concept art|mural)\b",
}

BANDS = {  # target words in the main prompt (excluding parameters / negative prompt)
    "gemini": (25, 260), "flux": (15, 140), "midjourney": (6, 70), "sdxl": (12, 90),
    "qwen-image": (30, 260), "z-image": (40, 260), "seedream": (20, 170), "universal": (20, 170),
}


def words(s):
    return len(re.findall(r"\w+", s))


def strip_params(p):
    return re.sub(r"\s--\w+.*$", "", p.strip(), flags=re.S)


def lint(target, prompt, negative, mode="prompt_only"):
    """Return list of model-compatibility violations."""
    v = []
    main = prompt
    if target != "midjourney" and re.search(r"(^|\s)--[a-z]+", main):
        v.append("midjourney-style parameters")
    if target != "sdxl" and re.search(r"\([^()]+:\s*\d(\.\d+)?\)", main):
        v.append("weight syntax")
    if "::" in main and target != "midjourney":
        v.append(":: multi-prompt")
    if target == "midjourney":
        if "::" in main:
            v.append(":: not supported on V7+")
        tail = re.split(r"\s--", main, maxsplit=1)
        if len(tail) > 1 and re.search(r"[.,]\s*\w+\s*$", tail[1]) and not re.search(r"--no\s", main):
            v.append("text after parameters")
    if re.search(r"negative prompt", main, re.I):
        v.append("negative prompt inside prompt text")
    if negative and target in {"gemini", "flux", "seedream", "universal", "midjourney"}:
        v.append("negative prompt for a model without one")
    lo, hi = BANDS[target]
    if mode in ("edit", "critique"):
        lo = 8  # edit instructions are short by design
    n = words(strip_params(main))
    if not lo <= n <= hi:
        v.append(f"length {n} outside {lo}-{hi}")
    return v


def score(case, arm, prompt, negative=""):
    req = case["request"].lower()
    text = prompt.lower()
    keep = case["must_keep"]
    kept = sum(1 for k in keep if re.search(k, text, re.I))
    added = [b for b in case["must_not_add"] + BLOAT if re.search(b, text, re.I) and not re.search(b, req, re.I)]
    slots = sum(1 for r in SLOTS.values() if re.search(r, text, re.I))
    violations = lint(case["target"], prompt, negative, case["mode"])
    skill_missing = [k for k in case.get("skill_checks", []) if not re.search(k, text, re.I)]
    return {
        "intent": kept / len(keep) if keep else 1.0,
        "assumptions": len(added),
        "added": added,
        "specificity": slots / len(SLOTS),
        "compat": 0 if violations else 1,
        "violations": violations,
        "words": words(strip_params(prompt)),
        "skill_missing": skill_missing,
    }


def load():
    return [json.loads(l) for l in CASES.read_text(encoding="utf-8").splitlines() if l.strip()]


def run():
    out = []
    for c in load():
        a = c.get("a_raw") or c["request"]
        b = c.get("b_conventional") or (a.rstrip(" .") + CONVENTIONAL_SUFFIX)
        out.append({"id": c["id"], "lang": c["lang"], "category": c["category"], "target": c["target"],
                    "mode": c["mode"], "revision": bool(c.get("context")),
                    "A": score(c, "A", a), "B": score(c, "B", b),
                    "C": score(c, "C", c["c_skill"], c.get("c_negative", ""))})
    return out


def agg(rows, arm, key):
    return st.mean(r[arm][key] for r in rows)


def report(rows):
    L = ["# Prompt-level benchmark report", "",
         "Generated by `python3 benchmarks/run.py --report benchmarks/REPORT.md`. **No images were generated.** "
         "These numbers measure prompt text only, with simple lexical checks. They do not show that images look better. "
         "See `benchmarks/README.md` for method and caveats.", "",
         f"Cases: {len(rows)} ({sum(r['lang']=='th' for r in rows)} Thai, {sum(r['lang']=='en' for r in rows)} English), "
         f"{len({r['category'] for r in rows})} categories, {len({r['target'] for r in rows})} target models.", "",
         "## Overall", "",
         "| Metric | A raw | B conventional | C Image Whisperer | Better is |",
         "|---|---|---|---|---|"]
    def row(name, key, fmt, better):
        L.append(f"| {name} | " + " | ".join(fmt(agg(rows, a, key)) for a in "ABC") + f" | {better} |")
    pct = lambda x: f"{x*100:.1f}%"
    row("Intent preservation (must-keep items present)", "intent", pct, "higher")
    row("Unrequested additions per prompt", "assumptions", lambda x: f"{x:.2f}", "lower")
    row("Scene specificity (setting/light/composition/medium covered)", "specificity", pct, "higher")
    row("Model compatibility (no lint violations, length in band)", "compat", pct, "higher")
    row("Mean words", "words", lambda x: f"{x:.0f}", "—")
    rev = [r for r in rows if r["revision"]]
    if rev:
        L += ["", f"Context awareness (revision cases, n={len(rev)}): intent preservation "
              + ", ".join(f"{a} {agg(rev, a, 'intent')*100:.1f}%" for a in "ABC") + "."]
    for title, field in (("By target model", "target"), ("By category", "category"), ("By language", "lang")):
        g = defaultdict(list)
        for r in rows:
            g[r[field]].append(r)
        L += ["", f"## {title}", "", "| Group | n | Intent A/B/C | Additions A/B/C | Compat A/B/C |", "|---|---|---|---|---|"]
        for k in sorted(g):
            rs = g[k]
            L.append(f"| {k} | {len(rs)} | " + "/".join(f"{agg(rs,a,'intent')*100:.0f}" for a in "ABC") + " | "
                     + "/".join(f"{agg(rs,a,'assumptions'):.1f}" for a in "ABC") + " | "
                     + "/".join(f"{agg(rs,a,'compat')*100:.0f}" for a in "ABC") + " |")
    fails = [r for r in rows if r["C"]["intent"] < 1 or r["C"]["assumptions"] or not r["C"]["compat"] or r["C"]["skill_missing"]]
    L += ["", "## C cases with any failure", ""]
    if not fails:
        L.append("None.")
    for r in fails:
        L.append(f"- `{r['id']}`: intent {r['C']['intent']*100:.0f}%, added {r['C']['added']}, violations {r['C']['violations']}, skill checks missing {r['C']['skill_missing']}")
    L += ["", "## Reading these numbers", "",
          "- A (raw) often scores high on intent because it *is* the request; it loses on specificity and compatibility.",
          "- B shows the cost of generic enhancement: unrequested style words and lint failures, with no added scene information.",
          "- C prompts were written by following this skill; the same team wrote the checks, so treat the result as a regression baseline, not independent proof.",
          "- Visual quality is not measured. Use `benchmarks/visual-protocol.md` for real image tests."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--report")
    ap.add_argument("--json")
    a = ap.parse_args()
    rows = run()
    if a.json:
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    text = report(rows)
    if a.report:
        Path(a.report).write_text(text, encoding="utf-8")
    print(text)
