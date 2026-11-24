# Visual reasoning

Goal: make the scene physically and visually possible before writing the prompt. Models follow coherent descriptions better than contradictory lists.

## 1. Lay out the space

Decide, only as far as needed:

- **Camera position**: eye level, high, low, top-down, over-the-shoulder; distance (close-up, medium, full body, wide).
- **Planes**: what is in the foreground, midground, background.
- **Positions**: left/right/centre, in front of/behind, touching/not touching. Use these words explicitly for multi-subject scenes.
- **Scale**: real-world sizes must agree (a cup is smaller than a hand; a car fills a lane).
- **Focus**: what is sharp; what is blurred. Shallow depth of field only when the camera setup allows it (phones blur less than large-sensor cameras, except in portrait mode).

## 2. One light logic

- Pick one main light (sun, window, lamp, flash, screen, neon). Its direction sets shadow direction for every object.
- Add fill/rim only if there is a source for it (a wall, the sky, a sign).
- Colour of light must match the source (tungsten warm, overcast neutral-cool, neon coloured).
- Night scenes need a visible or implied light source.

## 3. Contact, weight and support

For every subject ask: what holds it up?

- Feet on ground with weight on one leg; a sitting person compresses the cushion; a hand holding a cup wraps around it.
- Objects on tables cast contact shadows.
- Liquids follow gravity; hair and fabric respond to wind and movement in one consistent direction.

## 4. Interaction check

For each action: can a real body do it with these props? Name the grip ("holding the phone in her right hand, thumb on the screen"). Two people hugging: arms around shoulders or waist, heads turned to the side. Keep hand-object interactions simple; complex finger poses are a frequent failure.

## 5. Visual hierarchy

- One clear main subject (or a clearly described group).
- Secondary elements support it and should not compete for attention.
- For text-bearing images: decide where text goes and leave clean space there.

## 6. Consistency checklist (run before compiling)

- [ ] Count of subjects/objects matches the request.
- [ ] Every subject has a location and, if relevant, an action.
- [ ] One main light; shadows and highlights agree with it.
- [ ] Time of day, weather and season agree with light and clothing.
- [ ] Scale and perspective consistent (horizon line, vanishing direction).
- [ ] Physical support and contact for every object and person.
- [ ] Style is one style (not "photo + watercolour" unless that mix is the point).
- [ ] Culture and location details agree (Thai street signs in Thai, left-side traffic in Thailand).
- [ ] Text has a surface and a size that can hold it.

Fix contradictions silently when the fix is obvious. If a contradiction is in the user's locked request and seems intentional (surreal art), keep it and describe it as intentional ("a surreal scene where…").
