# Architecture

```
request ─► SKILL.md (mode detection, routing)
            │
            ├─ core/intent-understanding.md   purpose, locked / implied / default / risky details
            ├─ core/visual-reasoning.md       space, light logic, contact, consistency checklist
            ├─ core/scene-representation.md   model-neutral scene (schemas/scene.schema.json)
            ├─ knowledge/*.md, styles/*.md    loaded only when the scene needs them
            ├─ core/prompt-compiler.md        prompt form, order, length
            │    └─ adapters/<model>.md       model-specific syntax and rules
            ├─ core/image-editing.md, core/reference-images.md   EDIT / REFERENCE
            └─ core/quality-critic.md         prompt checklist, image critique, stop rules
```

Design choices:

- **Repository root = skill folder.** `gemini skills install <git-url>` and Agent Skills hosts work directly; `dist/image-whisperer.zip` holds only runtime files for app uploads.
- **Progressive disclosure.** `SKILL.md` is ~130 lines; every other file is one hop away and loaded on demand.
- **Adapters own model facts.** Core files stay model-neutral, so a model update touches one file.
- **Standalone instructions** (`integrations/standalone/`) compress the whole skill for hosts without file loading (Gems, custom GPTs, copy-paste).
