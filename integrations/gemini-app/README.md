# Gemini app (gemini.google.com, Android, iOS, Mac)

Google is moving Gems to **skills** in the Gemini app (personal accounts: from 17 Nov 2026; Gems removed 17 Dec 2026). Skills can be created by uploading a `SKILL.md`, a folder, or a `.zip` with `SKILL.md` at its root (max 100 MB total, text files only). Source: https://support.google.com/gemini/answer/17094296

## Install

1. Download `dist/image-whisperer.zip` from this repository (it contains only the files the skill needs: `SKILL.md`, `core/`, `knowledge/`, `adapters/`, `styles/`, `schemas/`, `examples/`).
2. Open Gemini → **Skills** → **New skill** → **Upload** and choose the zip.
3. Check that the name is `image-whisperer` and save.

## Use

- Just ask for an image ("ขอรูปแมวนอนบนโซฟา ถ่ายมือถือ"); Gemini applies the skill when it is relevant.
- Or call it directly: type `/image-whisperer` (Google says `@` will replace `/` later) and your request.
- If image creation is available in your chat, ask Gemini to create the image after it writes the prompt. If not, copy the prompt into a chat where image creation works.

## Notes

- Google's page lists tools that do not work inside skills yet (video, music, Canvas, Deep Research, Guided learning). It does not say whether image creation works inside a skill; if it does not in your account, use the prompt in a normal chat.
- Updating: download the new zip and upload it again (replace the old skill).
