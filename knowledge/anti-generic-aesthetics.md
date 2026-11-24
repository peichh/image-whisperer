# Anti-generic aesthetics

Load when a style matters (illustration, anime, concept art, posters, character art, stylised 3D) and the user wants a distinctive or premium look, or complains that results look "generic", "like a mobile game", "AI art", "ดูเป็น AI", "ดูราคาถูก". For realistic photos use `knowledge/anti-ai-appearance.md` instead (or both).

**Never remove a trait the user asked for.** If they want a mobile-game look, neon, thick outlines or a centred symmetrical poster, that is the target.

## Generic traits → concrete counter-instructions

| Generic trait | How to recognise it | Counter-instruction (describe the wanted result) |
|---|---|---|
| generic anime face | huge glossy eyes with multiple sparkles, tiny chin, same face for everyone, blush on every character | "eyes of moderate size with one simple catchlight, distinct face shapes per character (a round face, a long face), small natural blush only if embarrassed" |
| repetitive character design | identical hairstyles, bodies, outfits across a group | give each character one silhouette difference (height, hair shape, posture) and one clothing difference |
| mobile-game illustration look | glossy gradients everywhere, rim light on every edge, sparkles, busy ornate costume, centred hero pose, saturated purple-blue palette | "matte colour fills, light only from the stated source, plain practical clothing, natural relaxed pose, limited palette of …" |
| overly thick outlines | uniform heavy black outline around everything | "thin, varying line weight; lighter coloured lines on distant objects" (or "no outlines" for painterly) |
| flat lighting | no light direction, every surface equally lit | name the source and direction; "shadows fall to the left; one side of each face in shadow" |
| artificial poses | stiff T-poses, hero stance, everyone facing camera | give an action and a gaze target; asymmetric weight; "caught mid-movement" |
| excessive neon saturation | purple/cyan glow without sources | "colour only from visible sources; mostly neutral tones with one accent colour" |
| centred symmetric composition | subject dead centre, mirrored layout | "subject in the left third, looking into the open space"; uneven spacing |
| artificial expressions | wide open smile with teeth, generic surprise | a specific small expression tied to the situation ("tired half-smile", "biting her lip while reading") |
| unmotivated visual effects | floating particles, lens flares, glowing auras, bokeh balls with no cause | remove them; add effects only with a cause ("dust in the beam of window light") |
| genre-default setting or costume | an unrequested setting or gear the genre stereotypically implies (assassin → neon cyberpunk rain, fingerless gloves, thigh straps, forearm guards, pouches; wizard → glowing ruins) | a quiet setting that supports the character, chosen on purpose and listed as an assumption |
| over-polished digital surfaces | plastic-smooth skin and fabric, airbrushed gradients, no texture | a texture treatment ("visible brush strokes", "paper grain", "slight colour bleeding") and an imperfection ("slightly uneven line, hand-made feel") |

## Workflow

1. Detect: from the user's complaint, a shown image, or the target model's known tendencies (adapter section "Aesthetic translation").
2. Pick at most 3 counter-instructions — the most visible problems. More makes the prompt fight itself.
3. Write them as the target look in the style sentence, not as a list of "no …" (except SD-family negative prompts).
4. Re-check that the counter-instructions do not contradict the user's requested style.

## Why this happens (for explaining to users)

Image models are trained and tuned so their outputs appeal to a broad audience (ViPer, arXiv:2407.17365). Average taste tends toward polished, saturated, centred, symmetrical images; vague style words fall back to that average. Concrete visual traits and reference images move the result away from it. A prompt cannot guarantee a model can produce a given style; some styles may stay out of reach for a given model.
