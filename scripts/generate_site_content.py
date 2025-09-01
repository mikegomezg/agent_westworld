#!/usr/bin/env python3
"""
Generate site content for GitHub Pages from story data.
Creates narrative markdown files from scene YAML data.
"""

import yaml
from pathlib import Path
import sys

def load_yaml_file(file_path):
    """Load and parse a YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: Failed to load {file_path}: {e}")
        return None

def load_characters():
    """Load character data for name resolution."""
    characters_file = Path('canon/characters.yml')
    if characters_file.exists():
        return load_yaml_file(characters_file)
    return {}

def get_character_name(char_id, characters):
    """Get character name from ID."""
    if not characters:
        return char_id

    for char in characters.get('characters', []):
        if char.get('id') == char_id:
            return char.get('name', char_id)
    return char_id

def generate_narrative_content(scene, characters):
    """Generate narrative content from scene data."""
    content = []

    # Title and metadata
    content.append(f"# {scene.get('title', 'Untitled Scene')}")
    content.append("")

    # Episode and location info
    episode = scene.get('episode', 'Unknown Episode')
    location = scene.get('location', 'Unknown Location')
    content.append(f"*Episode {episode} - Location: {location}*")
    content.append("")

    # Synopsis
    synopsis = scene.get('synopsis', 'No synopsis available.')
    content.append(f"## Synopsis")
    content.append(f"{synopsis}")
    content.append("")

    # Characters
    if 'characters' in scene:
        content.append("## Characters")
        for char_id in scene['characters']:
            char_name = get_character_name(char_id, characters)
            content.append(f"- {char_name}")
        content.append("")

    # Dialogue
    if 'dialogue' in scene:
        content.append("## Dialogue")
        for line in scene['dialogue']:
            content.append(f"> \"{line}\"")
        content.append("")

    # Themes
    if 'themes' in scene:
        content.append("## Themes")
        for theme in scene['themes']:
            content.append(f"- {theme}")
        content.append("")

    # Notes
    if 'notes' in scene:
        content.append("## Notes")
        content.append(f"{scene['notes']}")
        content.append("")

    return '\n'.join(content)

def generate_narrative_index(narratives_dir):
    """Generate index of all narratives."""
    output = Path('narratives.md')

    content = [
        "---",
        "layout: page",
        "title: Generated Narratives",
        "---",
        "",
        "# Scene Narratives",
        "",
        "This page displays AI-generated narrative content for all scenes.",
        "",
        "## Available Narratives",
        ""
    ]

    # Get all narrative files
    narrative_files = sorted(narratives_dir.glob('*.md'))

    if not narrative_files:
        content.append("*No narratives generated yet. Run the generation script to create narratives.*")
    else:
        for narrative_file in narrative_files:
            if narrative_file.name == 'index.md':
                continue

            # Try to extract title from the narrative file
            title = narrative_file.stem.replace('_', ' ').title()
            # Use directory-style links to match Jekyll pretty permalinks
            content.append(f"- [{title}](narratives/{narrative_file.stem}/)")

    content.extend([
        "",
        "## Generation Script",
        "To generate narratives, run:",
        "```bash",
        "python scripts/generate_site_content.py",
        "```",
        "",
        "## Raw Scene Data",
        "- [View All Scenes](story/scenes/)",
        "",
        "---",
        "",
        "*Narratives are generated using structured scene data and AI assistance to create coherent story content.*"
    ])

    with open(output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content) + '\n')

def generate_narratives():
    """Main function to generate all narratives."""
    scenes_dir = Path('story/scenes')
    narratives_dir = Path('narratives')

    # Create narratives directory
    narratives_dir.mkdir(exist_ok=True)

    # Load character data
    characters = load_characters()
    print("SUCCESS: Loaded character data")

    # Process each scene file
    scene_files = list(scenes_dir.glob('*.yml'))
    if not scene_files:
        print("WARNING: No scene files found in story/scenes/")
        return

    print(f"SUCCESS: Found {len(scene_files)} scene files")

    for scene_file in scene_files:
        if scene_file.name == 'TEMPLATE.yml':
            continue

        print(f"Processing: {scene_file.name}")

        # Load scene data
        scene = load_yaml_file(scene_file)
        if not scene:
            continue

        # Generate narrative content
        narrative_content = generate_narrative_content(scene, characters)

        # Create narrative file
        scene_id = scene.get('id', scene_file.stem)
        narrative_file = narratives_dir / f"{scene_id}.md"

        # Add Jekyll front matter
        front_matter = [
            "---",
            f"layout: page",
            f"title: {scene.get('title', 'Untitled Scene')}",
            "---",
            "",
            narrative_content
        ]

        with open(narrative_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(front_matter))

        print(f"SUCCESS: Generated {narrative_file.name}")

    # Generate narrative index
    generate_narrative_index(narratives_dir)
    print("SUCCESS: Generated narrative index")

    # Create narratives index file
    narratives_index = narratives_dir / 'index.md'
    index_content = [
        "---",
        "layout: page",
        "title: Narratives Index",
        "---",
        "",
        "# All Narratives",
        "",
        "Browse all generated narrative content:",
        ""
    ]

    # Add links to all narratives
    for narrative_file in sorted(narratives_dir.glob('*.md')):
        if narrative_file.name == 'index.md':
            continue

        scene_id = narrative_file.stem
        # Link to directory to support pretty permalinks
        index_content.append(f"- [{scene_id}]({scene_id}/)")

    with open(narratives_index, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content) + '\n')

    print("SUCCESS: Generated narratives index file")


if __name__ == "__main__":
    try:
        generate_narratives()
        print("SUCCESS: Site content generation completed!")
    except Exception as e:
        print(f"ERROR: Generation failed: {e}")
        sys.exit(1)
