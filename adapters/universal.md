# Adapter: Universal (unknown or unlisted model)

Use when the target model is unknown, not listed, or a chat app whose image model is undocumented (e.g. ChatGPT Images, Copilot, Canva, Leonardo, Ideogram, Recraft, Grok). Goal: a prompt that works reasonably anywhere and breaks nowhere.

## Prompt form: plain narrative

```
[Image type and purpose] of [subject], [action], [setting]. [Composition]. [Light]. [Style]. [Text in quotes].
```

- 40-120 words.
- English, unless the host is known to prefer another language.
- Aspect ratio in words ("vertical 9:16 image").

## Rules

1. No parameters (`--ar`), no weights `(x:1.2)`, no `::`, no "Negative prompt:" section.
2. Exclusions as positive descriptions.
3. No quality-tag lists.
4. Quote exact text; keep it short.
5. If the user later names the model, recompile with that adapter.

## Editing

"Edit the provided image: <change>. Keep <keep list> exactly the same." Works in most chat-based editors.

## Example

User: "A cute poster for my kid's lemonade stand"

```
A cheerful hand-drawn poster for a child's lemonade stand, vertical 2:3. A smiling cartoon lemon wearing a straw hat pours lemonade into a cup next to a small wooden stand with a striped yellow-and-white awning. Big friendly rounded lettering at the top reads "LEMONADE 25¢". Bright yellow, sky blue and leaf green on a white background, crayon-like texture, simple and readable from a distance.
```
