# Narrative Generation Instructions

## For AI Agents

When asked to generate narrative prose from scenes:

1. Run `python scripts/generate-narrative.py`
2. Check generated files in `site/src/content/narratives/`
3. Commit the generated narratives
4. The site will auto-deploy to Vercel

## To improve a narrative

1. Locate the scene in `story/scenes/`
2. Enhance the scene data (add dialogue, actions, emotions)
3. Re-run the narrative generator
4. Commit and push changes

## Feedback workflow

Users will create issues like:
- "Improve narrative for scene S01E01-001"
- "Add more sensory details to ranch scenes"
- "Generate full episode narrative"

Respond by updating scenes and regenerating narratives.

## Example scene enhancement

```yaml
# Before
synopsis: "Dolores wakes up in the morning"
characters: ["dolores"]

# After  
synopsis: "Dolores slowly opens her eyes as golden morning light streams through her window, stretching her arms above her head with a contented sigh"
characters: ["dolores"]
dialogue:
  - "Good morning, beautiful"
actions:
  - "She rises gracefully from her bed"
  - "Her bare feet touch the cool wooden floor"
  - "She walks to the window and gazes out at the ranch"
emotions: ["contentment", "anticipation"]
```

## Running the generator

```bash
# From project root
cd scripts
python generate-narrative.py

# Or from site directory
npm run generate
```

## Viewing results

Generated narratives appear in `site/src/content/narratives/` as Markdown files.
Each file contains the scene title and generated prose narrative.
