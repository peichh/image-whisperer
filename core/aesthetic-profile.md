# User aesthetic profile

A reusable record of what this user likes and dislikes, stored as **visual traits on the 16 axes** of `core/aesthetic-translation.md` — not as style names. Method based on ViPer (arXiv:2407.17365): collect the user's reasons for liking or disliking images, infer structured liked/disliked attributes, and apply them to new prompts.

Schema: `schemas/aesthetic-profile.schema.json`. Example: `examples/aesthetic-profile.example.json`.

## When to use

- The user shows images they like or dislike, compares two images, gives feedback on a result ("too glossy", "ชอบลายเส้นแบบนี้"), or says "remember my style", "จำสไตล์ฉันไว้".
- A profile already exists (in host memory or pasted/uploaded as a file) → apply it to every new request unless the user asks for something different.

## Learning

| Signal | What to extract |
|---|---|
| liked image | 3-6 traits that most define it, on named axes |
| disliked image | the 1-3 traits the user objects to (ask "what bothers you most?" if unclear) |
| reference image | traits to reuse; note which are tied to that project only |
| A vs B comparison | the axes where A and B differ; the chosen side's values become likes, the other side's dislikes |
| feedback text | map words to axes ("ดูแข็ง" → pose/anatomy; "สีจัดไป" → colour saturation) |

Rules:

1. Record **traits, not names**: "fine tapering lines, muted palette, painted skies" — not "Ghibli". A name may be kept only as a `label` beside the traits.
2. Keep each trait with its source and a confidence (`low` after one signal, `medium` after two consistent signals, `high` when the user states it as a rule).
3. Do not generalise from one image to all work: tie narrow traits to a `scope` — a project ("children's book project") or an image type ("portraits").
4. Conflicts: newer explicit statements beat older inferred ones; ask if two explicit rules conflict.
5. Show the user the extracted traits in plain language and let them correct before saving.

## Applying

1. Request-specific instructions win over the whole profile, including `hard_rules`: if the user asks for a conflicting style this time ("ignore my style", "this time neon"), suspend the conflicting rules for this request only and keep the profile unchanged.
2. Otherwise use `hard_rules` always; use `likes` to fill axes the request leaves open; use `dislikes` as counter-instructions (via `knowledge/anti-generic-aesthetics.md` style wording).
3. Use `model_notes` for the current target model (e.g. "on Gemini, say 'not a mobile-game illustration' explicitly").
4. Mention briefly that the profile was applied ("ใช้สไตล์ที่บันทึกไว้: เส้นบาง สีหม่น").

## Storing (always with permission)

- **Host has persistent memory** (e.g. Gemini app "saved info"/memory, Claude memory, agent memory files): ask "Save this aesthetic profile for future images?" Save only after a yes. Save the compact form (hard rules + top likes/dislikes), keeping every trait's `scope`: a trait scoped to a project or an image type (e.g. "portraits") is saved with its scope tag and applied only to requests in that project or of that image type.
- **No persistent memory**: give the profile as a JSON block or file named `image-whisperer-profile.json` and tell the user to paste or upload it next time.
- Never store images of real people or personal data in the profile; store only visual traits.
- The user can ask to show, edit, export or delete the profile at any time.

## Compact form (for memory or chat)

```
Aesthetic profile "<name>": ALWAYS <hard rules>. LIKES line: …; colour: …; light: …; composition: …; texture: …. AVOID <dislikes>. ONLY FOR <scope>: <scoped traits>. On <model>: <note>.
```

Traits without a scope apply to all work; traits under `ONLY FOR <scope>` apply only when the request belongs to that scope (that project, or that image type in any project).
