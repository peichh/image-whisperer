# Intent understanding

Goal: know what the person wants to *see* and *use*, before thinking about words for the model.

## 1. Classify the request

| Field | Question | Examples |
|---|---|---|
| purpose | What will the image be used for? | Facebook post, product listing, slide, poster, wallpaper, gift, storyboard, character sheet, mood board |
| image_type | What kind of picture? | phone photo, pro photo, anime, illustration, painting, 3D render, logo, infographic, UI mockup |
| subject | Who/what is the image about? | "my cat", "a bowl of tom yum", "two friends" |
| action / relationship | What is happening, between whom? | "hugging", "selling", "arguing", "looking at the camera" |
| mood | What should it feel like? | cosy, tense, funny, premium, nostalgic |
| locked | What did the user say literally? | colours, counts, text, names, style, aspect ratio |
| audience / culture | Who will see it, what setting is implied? | Thai family, Japanese market, corporate |
| target model | Which model or host? | Gemini app, Midjourney, unknown |

If `purpose` is missing, infer it from context (platform words, tone). If it is truly unknown, choose the most neutral reading.

## 2. Separate four kinds of information

1. **Locked**: stated by the user. Never drop or change. If two locked items conflict, ask.
2. **Implied**: follows directly from locked items or purpose. Add it. (e.g. "Songkran" → water, summer daylight, Thai street; "for a menu" → food centred, clean background, appetising light.)
3. **Default**: a neutral choice the image needs but the user would not care about (time of day for a product shot, generic background). Add the *least surprising* option and keep it short.
4. **Risky**: a choice that would change the image a lot (identity, age, ethnicity, body type, style, text content, brand). Do not invent. Ask, or keep it neutral and list it under "Assumed".

## 3. Read the hidden constraints

- "Real photo", "ถ่ายจริง", "ไม่เอาแบบ AI" → realism goal: load `knowledge/anti-ai-appearance.md`.
- "From my phone", "ถ่ายมือถือ", "candid", "vlog" → phone look, not studio.
- "Cute", "น่ารัก" for a product → soft colours, rounded shapes; for a person → friendly expression, not sexualised.
- "Professional" for a headshot → clean background, soft light, natural retouch, not a magazine cover.
- "Like a poster/thumbnail" → bold composition, space for text, high contrast at small size.
- Brand or real person names → respect host policy; describe look rather than copying a protected design when needed.
- Age words: always keep people who are minors in non-sexual, age-appropriate contexts.

## 3b. People: described vs undescribed, and the photo story

- **Real or described person** ("my dad, 58", a reference photo, "a chubby guy"): keep exactly that look — age, body, face, skin. No idealising.
- **Undescribed person** ("an Asian man at the beach"): choose a natural, pleasant-looking real person — the way a photo of a friend looks on a good day. Do not idealise (model face, six-pack, glamour) and do not push the other way (never add "ordinary", "average-looking", "plain"). Pick age and nationality from context (Thai request → Thai person is a fair default) and list them under "Assumed".
- **Photo story**: decide who is taking the picture and why, because it sets distance, gaze and mood. A beach photo "on iPhone" is most likely taken by a friend or partner on holiday → candid moment, a few metres away, chest-to-eye height, relaxed and flattering. A selfie → arm's length, front camera. A stranger's street shot → farther, unaware subject.
- **Moment**: give the person something to do and somewhere to look (walking along the water, laughing, pushing hair back, glancing at the sea). A stiff "standing, facing the camera, arms down" pose reads as a record shot; use it only for ID-style, product-fit or when asked.

## 3c. Emotion words → visible face, pose and camera

Translate mood words (often Thai) into what can be seen; a single adjective is usually rendered as a generic expression.

| Word | Face | Body / camera |
|---|---|---|
| หยิ่ง, haughty, arrogant | chin raised, looking down the nose, half-lidded eyes, faint smug smirk | weight on one leg, relaxed shoulders; low camera angle so the subject looks down at the viewer |
| ดุ, fierce, angry | brows pulled down, eyes wide and fixed, jaw tight | forward lean, tense shoulders; eye-level or slightly low |
| เย็นชา, cold | neutral mouth, steady unblinking gaze, no smile | still, upright; eye-level, more distance |
| มั่นใจ, confident | small closed-mouth smile, direct gaze | open stance, hand on hip; slightly low angle |
| ขี้เล่น, playful | lopsided grin, one eyebrow up, wink | mid-movement, tilted head |
| เขิน, shy | eyes down or to the side, small smile, blush | shoulders in, hand near face; slightly high angle |
| เศร้า, sad | brows raised in the middle, mouth corners down, wet eyes | head lowered; high angle, more empty space |

Use the body/camera column only when the framing shows the body; for a face or portrait request change only the face. Never add props or actions (weapons, fists, a fight) the user did not ask for.

Keep the user's exact word in mind: "หยิ่ง" is not "ดุ". If two readings are possible, pick the one closest to the word and list it under "Assumed".

## 4. Do not over-interpret

Bad habits to avoid:

- Turning every person into a model with perfect skin.
- The opposite: making an undescribed person deliberately plain ("ordinary", "average-looking") or stiffly posed.
- Adding "cinematic lighting, 8K, masterpiece, trending on ArtStation" to everything.
- Making amateur photos look like studio photos.
- Adding photorealism to anime, cartoons or flat graphics.
- Making every scene dramatic, moody or golden hour.
- Adding extra people, text, logos or props the user did not ask for.
- Changing the requested count (3 cats stays 3 cats).

## 5. Revisions in a conversation

On a follow-up ("make it brighter", "เอาแมวออก", "ขอแนวตั้ง"):

1. Start from the previous prompt and scene.
2. Change only what the user asked. Keep everything else word-for-word where possible.
3. If the host keeps image context (Gemini, ChatGPT, Seedream, FLUX Kontext/3 with a reference), write an *edit instruction* ("Keep everything the same, but…") instead of a new prompt. See `core/image-editing.md`.
4. Remember rejections: if the user said "not so orange", do not bring orange back in later turns.

## 6. When to ask a question

Ask (one question, with 2-4 options) only if:

- a risky choice decides the whole image (which person, which product, what text), and
- a wrong guess would waste a generation.

Otherwise proceed and list assumptions. In AUTO mode with a free/included generator, a quick draft plus "want me to change X?" is usually better than a question.

## Thai language notes

- Thai requests often skip subjects and counts ("ขอรูปทำอาหาร"). Infer from context, keep neutral.
- Thai cultural items should be named in English with a short visual description so the model knows what they look like: "khanom krok (small round coconut pancakes cooked in a dimpled cast-iron pan)".
- Keep Thai text that must appear in the image in Thai script, in quotes, and keep it short. Many models render Thai script unreliably; warn the user once when text is long. See the adapter's text section.
