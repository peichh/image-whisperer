# Scene representation

An internal, model-neutral description of the image. Fill only the fields the image needs; leave the rest out. JSON Schema: `schemas/scene.schema.json`.

## Fields

| Field | Content | Needed when |
|---|---|---|
| `purpose` | use of the image | always |
| `image_type` | photo / illustration / anime / 3d / graphic / painting / mixed | always |
| `style` | named style or medium, if any | style matters |
| `subjects[]` | `{id, description, count, pose, expression, action, clothing, position}` | there are subjects |
| `relationships[]` | `{from, to, relation}` e.g. holding, facing, behind | 2+ subjects or props |
| `environment` | place, time of day, weather, season, culture | almost always |
| `layers` | `{foreground, midground, background}` | depth matters |
| `composition` | framing, shot size, angle, subject placement, negative space, aspect ratio | always (short) |
| `camera` | device type, lens feel, depth of field, motion blur | photo styles only |
| `lighting` | key source, direction, quality, colour, secondary light | always (short) |
| `color` | palette, brand colours (hex if given), contrast | colour matters |
| `materials[]` | important surfaces and how they look | close-ups, products, realism |
| `physics` | contact, gravity, wind, liquids, cloth | realism, action |
| `text[]` | `{content, language, placement, style}` exact text to render | text appears in image |
| `hierarchy` | main subject → secondary → background | busy scenes |
| `exclusions[]` | things that must not appear, as positive statements where possible | user asked to exclude |
| `edit` | `{source, changes[], keep[]}` | EDIT mode |
| `references[]` | `{id, use: identity/style/layout/product/pose, notes}` | REFERENCE mode |
| `assumptions[]` | choices not given by the user | always (report to user) |

## Depth guide

- Icon, logo, sticker: purpose, image_type, style, subject, color, text.
- Product shot: + materials, lighting, composition, environment.
- Portrait: + camera, lighting, expression, clothing, environment.
- Multi-person or action scene: everything, especially relationships, positions and physics.

## Example (compact)

```json
{
  "purpose": "Facebook post for a small cafe",
  "image_type": "photo",
  "subjects": [{"id": "drink", "description": "iced Thai milk tea in a clear plastic cup", "count": 1, "position": "centre, slightly right"}],
  "environment": {"place": "wooden cafe counter by a window", "time": "morning"},
  "composition": {"shot": "close-up", "angle": "slightly above eye level", "aspect_ratio": "4:5", "negative_space": "top left for a caption"},
  "camera": {"device": "smartphone", "depth_of_field": "moderate, background softly blurred"},
  "lighting": {"key": "soft window light from the left", "quality": "diffuse"},
  "materials": [{"surface": "cup", "look": "condensation droplets, ice cubes visible through orange tea"}],
  "assumptions": ["morning window light", "wooden counter"]
}
```
