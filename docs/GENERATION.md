# Westworld Content Generation Pipeline

## Overview

The Westworld framework now uses a markdown-based content system with an automated generation pipeline. This document describes how to use the generation scripts and how the system works.

## Architecture

### Content Structure

- **Source Content**: Individual markdown files in `canon/` and `story/` directories
- **Generation Pipeline**: Python scripts that process markdown and create enriched content
- **Output**: Generated content in `generated/` directory

### Directory Structure

```
canon/
├── characters/          # Character markdown files
├── locations/           # Location markdown files  
├── themes/              # Theme markdown files
└── timeline/            # Timeline event files

story/
└── scenes/              # Scene markdown files

generated/
├── narratives/          # Generated scene narratives
└── summaries/           # Enriched profiles, timeline, themes

scripts/
└── generate/            # Generation scripts
    ├── narrative_from_scene.py
    ├── enrich_character_profile.py
    ├── timeline_visualization.py
    └── theme_analysis.py
```

## Generation Scripts

### 1. Scene Narrative Generator

**Script**: `scripts/generate/narrative_from_scene.py`

**Purpose**: Converts scene markdown files into flowing narrative prose

**Usage**:
```bash
# Generate narrative for specific scene
python scripts/generate/narrative_from_scene.py --scene-id S01E01-001

# Generate narratives for all scenes
python scripts/generate/narrative_from_scene.py
```

**Input**: Scene markdown files in `story/scenes/s01e01/`
**Output**: Narrative prose in `generated/narratives/`

**Features**:
- Extracts Synopsis, Characters, Actions, Emotions, Dialogue, etc.
- Loads character and location details
- Creates immersive narrative descriptions
- Maintains thematic connections

### 2. Character Profile Enricher

**Script**: `scripts/generate/enrich_character_profile.py`

**Purpose**: Analyzes character relationships and generates insights

**Usage**:
```bash
# Enrich specific character
python scripts/generate/enrich_character_profile.py --character-id C-DOLORES

# Enrich all characters
python scripts/generate/enrich_character_profile.py
```

**Input**: Character markdown files in `canon/characters/`
**Output**: Enriched profiles in `generated/summaries/`

**Features**:
- Analyzes relationship networks
- Categorizes relationship types (romantic, creation, family, etc.)
- Generates character insights based on type and goals
- Provides comprehensive character analysis

### 3. Timeline Visualizer

**Script**: `scripts/generate/timeline_visualization.py`

**Purpose**: Creates chronological and thematic timeline views

**Usage**:
```bash
python scripts/generate/timeline_visualization.py
```

**Input**: Timeline event files in `canon/timeline/`
**Output**: Timeline analysis in `generated/summaries/westworld_timeline.md`

**Features**:
- Chronological summary by period
- Narrative period breakdown
- Character-focused timelines
- Event significance analysis

### 4. Theme Analyzer

**Script**: `scripts/generate/theme_analysis.py`

**Purpose**: Analyzes themes and their connections to other elements

**Usage**:
```bash
python scripts/generate/theme_analysis.py
```

**Input**: Theme files in `canon/themes/`
**Output**: Theme analysis in `generated/summaries/westworld_themes_analysis.md`

**Features**:
- Theme overview and descriptions
- Character connections to themes
- Theme significance analysis
- Cross-theme relationships

## Master Generation Script

### Run All Generators

**Script**: `scripts/generate_all.py`

**Purpose**: Orchestrates the entire generation pipeline

**Usage**:
```bash
python scripts/generate_all.py
```

**What it does**:
1. Runs scene narrative generation
2. Enriches all character profiles
3. Creates timeline visualizations
4. Generates theme analysis
5. Provides comprehensive status report

## Content Format Requirements

### Scene Files

Scene markdown files must have these sections:
```markdown
---
id: S01E01-001
episode: S01E01
title: Scene Title
location: L-LOCATION-ID
timestamp: Dawn
themes: [T-THEME-1, T-THEME-2]
---

# Scene Title

## Synopsis
Scene description...

## Characters
- C-CHARACTER-1
- C-CHARACTER-2

## Actions
- Action 1
- Action 2

## Emotions
- Emotion 1
- Emotion 2

## Key Dialogue
- "Dialogue line 1"
- "Dialogue line 2"

## Reveals
- Revelation 1
- Revelation 2

## Conflicts
- Conflict 1
- Conflict 2

## Connections
- Connection to other scenes/events
```

### Character Files

Character files must have these sections:
```markdown
---
id: C-CHARACTER-ID
name: Character Name
type: host|human
role: Character role
status: active|deceased
---

# Character Name

## Overview
Character description...

## Traits
- Trait 1
- Trait 2

## Goals
- Goal 1
- Goal 2

## Relationships
- **Character Name**: Relationship description
- **Another Character**: Another relationship

## Backstory
Character history...

## Narrative Function
Character's role in the story...
```

### Timeline Event Files

Timeline files must have these sections:
```markdown
---
id: TE-EVENT-ID
title: Event Title
date: 2052
period: Present Day
episode_reference: S01E10
---

# Event Title

## Overview
Event description...

## Characters Involved
- C-CHARACTER-1
- C-CHARACTER-2

## Significance
Why this event matters...
```

## Adding New Content

### 1. Create New Character

1. Create `canon/characters/character-name.md`
2. Follow character format requirements
3. Run character enrichment: `python scripts/generate/enrich_character_profile.py --character-id C-NEW-CHARACTER`

### 2. Create New Scene

1. Create `story/scenes/episode/scene-id.md`
2. Follow scene format requirements
3. Run narrative generation: `python scripts/generate/narrative_from_scene.py --scene-id SCENE-ID`

### 3. Create New Timeline Event

1. Create `canon/timeline/te-event-id.md`
2. Follow timeline format requirements
3. Run timeline generation: `python scripts/generate/timeline_visualization.py`

### 4. Create New Theme

1. Create `canon/themes/theme-name.md`
2. Follow theme format requirements
3. Run theme analysis: `python scripts/generate/theme_analysis.py`

## Validation

### Markdown Validation

The system includes validation scripts in `checks/`:
```bash
python checks/validate_markdown.py
```

This validates:
- Frontmatter requirements
- Required markdown sections
- Content structure
- ID consistency

## Benefits of the New System

### For Agents

- **Clear Structure**: Each content type has defined format
- **Incremental Updates**: Can add/update individual files
- **Automated Generation**: Scripts handle complex analysis
- **Consistent Output**: Standardized generation pipeline

### For Humans

- **Easy Review**: Markdown files are human-readable
- **Git-Friendly**: Clear diffs for changes
- **No Build System**: GitHub Pages renders natively
- **Modular**: Easy to find and update specific content

### For Development

- **Scalable**: Easy to add new content types
- **Maintainable**: Clear separation of concerns
- **Testable**: Each generator can be tested independently
- **Extensible**: New generation scripts can be added easily

## Troubleshooting

### Common Issues

1. **Script Not Found**: Ensure you're running from the repository root
2. **Missing Sections**: Check that markdown files have required sections
3. **Path Issues**: Verify file paths and directory structure
4. **Encoding Issues**: Ensure files are saved as UTF-8

### Debug Mode

Add print statements to generation scripts to see what's happening:
```python
print(f"Processing file: {file_path}")
print(f"Extracted content: {content[:100]}...")
```

## Future Enhancements

### Planned Features

- **Relationship Graph Generator**: Visual character relationship maps
- **Location Analysis**: Geographic and thematic location analysis
- **Episode Summaries**: Automated episode summary generation
- **Character Arc Analysis**: Character development tracking over time

### Custom Generators

You can create custom generation scripts by following the pattern:
1. Load markdown files using `frontmatter.load()`
2. Parse content sections
3. Generate analysis or output
4. Write to `generated/` directory

## Conclusion

The markdown-based generation pipeline provides a robust, scalable foundation for the Westworld framework. It enables autonomous agents to create and update content while maintaining human readability and reviewability. The system is designed to grow with your needs and can be easily extended with new content types and generation capabilities.

