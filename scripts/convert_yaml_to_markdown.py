#!/usr/bin/env python3
"""
Convert YAML files to individual markdown files with frontmatter.
This script transforms the monolithic YAML structure into modular markdown files.
"""

import yaml
import frontmatter
from pathlib import Path
from typing import Dict, List, Any
import click

def write_frontmatter_file(filepath: Path, frontmatter_data: Dict, content: str):
    """Write a file with frontmatter and content, handling encoding properly"""
    # Create the frontmatter string
    frontmatter_str = "---\n"
    for key, value in frontmatter_data.items():
        if isinstance(value, list):
            frontmatter_str += f"{key}:\n"
            for item in value:
                frontmatter_str += f"  - {item}\n"
        else:
            frontmatter_str += f"{key}: {value}\n"
    frontmatter_str += "---\n\n"

    # Combine frontmatter and content
    full_content = frontmatter_str + content

    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)

def convert_characters_to_markdown(characters_data: List[Dict], output_dir: Path):
    """Convert character YAML data to individual markdown files"""
    print("Converting characters to markdown...")

    for char_data in characters_data:
        char_id = char_data['id']
        filename = f"{char_id.lower().replace('-', '_')}.md"
        filepath = output_dir / filename

        # Create frontmatter
        frontmatter_data = {
            'id': char_data['id'],
            'name': char_data['name'],
            'type': char_data['type'],
            'role': char_data['role'],
            'status': char_data['status'],
            'first_appearance': char_data['first_appearance']
        }

        # Create markdown content
        content = f"""# {char_data['name']}

## Overview
{char_data.get('role', '')}

## Traits
"""
        for trait in char_data.get('traits', []):
            content += f"- {trait}\n"

        content += "\n## Goals\n"
        for goal in char_data.get('goals', []):
            content += f"- {goal}\n"

        content += "\n## Relationships\n"
        for rel_id, rel_desc in char_data.get('relationships', {}).items():
            content += f"- **{rel_id}**: {rel_desc}\n"

        content += f"\n## Backstory\n{char_data.get('backstory', '')}\n"

        if 'narrative_function' in char_data:
            content += f"\n## Narrative Function\n{char_data['narrative_function']}\n"

        # Write file with frontmatter
        write_frontmatter_file(filepath, frontmatter_data, content)

        print(f"SUCCESS: Created {filename}")

def convert_locations_to_markdown(world_data: Dict, output_dir: Path):
    """Convert location YAML data to individual markdown files"""
    print("Converting locations to markdown...")

    locations = world_data.get('locations', [])
    for loc_data in locations:
        loc_id = loc_data['id']
        filename = f"{loc_id.lower().replace('-', '_')}.md"
        filepath = output_dir / filename

        # Create frontmatter
        frontmatter_data = {
            'id': loc_data['id'],
            'name': loc_data['name'],
            'region': loc_data.get('region', ''),
            'significance': loc_data.get('significance', '')
        }

        # Create markdown content
        content = f"""# {loc_data['name']}

## Overview
{loc_data.get('description', '')}

## Region
{loc_data.get('region', '')}

## Significance
{loc_data.get('significance', '')}

## Connected Locations
"""
        for connected in loc_data.get('connected_to', []):
            content += f"- {connected}\n"

        # Write file with frontmatter
        write_frontmatter_file(filepath, frontmatter_data, content)

        print(f"SUCCESS: Created {filename}")

def convert_themes_to_markdown(themes_data: List[Dict], output_dir: Path):
    """Convert theme YAML data to individual markdown files"""
    print("Converting themes to markdown...")

    for theme_data in themes_data:
        theme_id = theme_data['id']
        filename = f"{theme_id.lower().replace('-', '_')}.md"
        filepath = output_dir / filename

        # Create frontmatter
        frontmatter_data = {
            'id': theme_data['id'],
            'name': theme_data['name']
        }

        # Create markdown content
        content = f"""# {theme_data['name']}

## Description
{theme_data.get('description', '')}

## Examples
"""
        for example in theme_data.get('examples', []):
            content += f"- {example}\n"

        content += f"\n## Significance\n{theme_data.get('significance', '')}\n"

        # Write file with frontmatter
        write_frontmatter_file(filepath, frontmatter_data, content)

        print(f"SUCCESS: Created {filename}")

def convert_timeline_to_markdown(timeline_data: List[Dict], output_dir: Path):
    """Convert timeline YAML data to individual markdown files"""
    print("Converting timeline events to markdown...")

    events = timeline_data.get('events', [])
    for event_data in events:
        event_id = event_data['id']
        filename = f"{event_id.lower().replace('-', '_')}.md"
        filepath = output_dir / filename

        # Create frontmatter
        frontmatter_data = {
            'id': event_data['id'],
            'title': event_data['title'],
            'date': event_data.get('date', ''),
            'period': event_data.get('period', ''),
            'episode_reference': event_data.get('episode_reference', '')
        }

        # Create markdown content
        content = f"""# {event_data['title']}

## Overview
{event_data.get('description', '')}

## Date
{event_data.get('date', '')}

## Period
{event_data.get('period', '')}

## Characters Involved
"""
        for char_id in event_data.get('characters_involved', []):
            content += f"- {char_id}\n"

        content += f"\n## Significance\n{event_data.get('significance', '')}\n"

        if 'episode_reference' in event_data:
            content += f"\n## Episode Reference\n{event_data['episode_reference']}\n"

        # Write file with frontmatter
        write_frontmatter_file(filepath, frontmatter_data, content)

        print(f"SUCCESS: Created {filename}")

def convert_scenes_to_markdown(scenes_dir: Path, output_dir: Path):
    """Convert scene YAML files to markdown"""
    print("Converting scenes to markdown...")

    scene_files = list(scenes_dir.glob("*.yml"))
    for scene_file in scene_files:
        if scene_file.name == "TEMPLATE.yml":
            continue

        with open(scene_file, 'r', encoding='utf-8') as f:
            scene_data = yaml.safe_load(f)

        scene_id = scene_data['id']
        filename = f"{scene_id.lower().replace('-', '_')}.md"
        filepath = output_dir / filename

        # Create frontmatter
        frontmatter_data = {
            'id': scene_data['id'],
            'episode': scene_data['episode'],
            'title': scene_data['title'],
            'location': scene_data.get('location', ''),
            'timestamp': scene_data.get('timestamp', ''),
            'themes': scene_data.get('themes', [])
        }

        # Create markdown content
        content = f"""# {scene_data['title']}

## Synopsis
{scene_data.get('synopsis', '')}

## Characters
"""
        for char_id in scene_data.get('characters', []):
            content += f"- {char_id}\n"

        content += "\n## Themes\n"
        for theme_id in scene_data.get('themes', []):
            content += f"- {theme_id}\n"

        if 'reveals' in scene_data:
            content += "\n## Reveals\n"
            for reveal in scene_data['reveals']:
                content += f"- {reveal}\n"

        if 'conflicts' in scene_data:
            content += "\n## Conflicts\n"
            for conflict in scene_data['conflicts']:
                content += f"- {conflict}\n"

        if 'dialogue' in scene_data:
            content += "\n## Key Dialogue\n"
            for line in scene_data['dialogue']:
                content += f"- \"{line}\"\n"

        if 'emotions' in scene_data:
            content += "\n## Emotions\n"
            for emotion in scene_data['emotions']:
                content += f"- {emotion}\n"

        if 'actions' in scene_data:
            content += "\n## Actions\n"
            for action in scene_data['actions']:
                content += f"- {action}\n"

        if 'connections' in scene_data:
            content += "\n## Connections\n"
            for connection in scene_data['connections']:
                content += f"- {connection}\n"

        # Write file with frontmatter
        write_frontmatter_file(filepath, frontmatter_data, content)

        print(f"SUCCESS: Created {filename}")

def create_index_files(repo_root: Path):
    """Create index.md files that aggregate content"""
    print("Creating index files...")

    # Characters index
    chars_dir = repo_root / "canon" / "characters"
    char_files = list(chars_dir.glob("*.md"))

    chars_index = """# Characters

## Hosts
"""

    humans_index = "\n## Humans\n"

    for char_file in char_files:
        if char_file.name == "index.md":
            continue
        with open(char_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            char_type = post.get('type', 'unknown')
            char_name = post.get('name', char_file.stem)

            if char_type == 'host':
                chars_index += f"- [{char_name}]({char_file.name})\n"
            else:
                humans_index += f"- [{char_name}]({char_file.name})\n"

    chars_index += humans_index

    with open(chars_dir / "index.md", 'w', encoding='utf-8') as f:
        f.write(chars_index)

    print("SUCCESS: Created characters index")

    # Create other index files
    # Locations index
    locs_dir = repo_root / "canon" / "locations"
    if locs_dir.exists():
        loc_files = list(locs_dir.glob("*.md"))
        if loc_files:
            locs_index = "# Locations\n\n"
            for loc_file in loc_files:
                if loc_file.name == "index.md":
                    continue
                with open(loc_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    loc_name = post.get('name', loc_file.stem)
                    locs_index += f"- [{loc_name}]({loc_file.name})\n"

            with open(locs_dir / "index.md", 'w', encoding='utf-8') as f:
                f.write(locs_index)
            print("SUCCESS: Created locations index")

    # Themes index
    themes_dir = repo_root / "canon" / "themes"
    if themes_dir.exists():
        theme_files = list(themes_dir.glob("*.md"))
        if theme_files:
            themes_index = "# Themes\n\n"
            for theme_file in theme_files:
                if theme_file.name == "index.md":
                    continue
                with open(theme_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    theme_name = post.get('name', theme_file.stem)
                    themes_index += f"- [{theme_name}]({theme_file.name})\n"

            with open(themes_dir / "index.md", 'w', encoding='utf-8') as f:
                f.write(themes_index)
            print("SUCCESS: Created themes index")

    # Timeline index
    timeline_dir = repo_root / "canon" / "timeline"
    if timeline_dir.exists():
        timeline_files = list(timeline_dir.glob("*.md"))
        if timeline_files:
            timeline_index = "# Timeline Events\n\n"
            for timeline_file in timeline_files:
                if timeline_file.name == "index.md":
                    continue
                with open(timeline_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    event_title = post.get('title', timeline_file.stem)
                    event_date = post.get('date', '')
                    if event_date:
                        timeline_index += f"- [{event_title}]({timeline_file.name}) - {event_date}\n"
                    else:
                        timeline_index += f"- [{event_title}]({timeline_file.name})\n"

            with open(timeline_dir / "index.md", 'w', encoding='utf-8') as f:
                f.write(timeline_index)
            print("SUCCESS: Created timeline index")

    # Scenes index
    scenes_dir = repo_root / "story" / "scenes" / "s01e01"
    if scenes_dir.exists():
        scene_files = list(scenes_dir.glob("*.md"))
        if scene_files:
            scenes_index = "# Season 1 Episode 1 Scenes\n\n"
            for scene_file in scene_files:
                if scene_file.name == "index.md":
                    continue
                with open(scene_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    scene_title = post.get('title', scene_file.stem)
                    scene_id = post.get('id', '')
                    if scene_id:
                        scenes_index += f"- [{scene_title}]({scene_file.name}) - {scene_id}\n"
                    else:
                        scenes_index += f"- [{scene_title}]({scene_file.name})\n"

            with open(scenes_dir / "index.md", 'w', encoding='utf-8') as f:
                f.write(scenes_index)
            print("SUCCESS: Created scenes index")

@click.command()
@click.option('--repo-root', default='.', help='Repository root directory')
def main(repo_root: str):
    """Convert YAML files to markdown structure"""
    repo_path = Path(repo_root)

    print("Converting YAML to Markdown Structure\n")

    try:
        # Convert characters
        chars_file = repo_path / "canon" / "characters.yml"
        if chars_file.exists():
            with open(chars_file, 'r', encoding='utf-8') as f:
                chars_data = yaml.safe_load(f)
            convert_characters_to_markdown(chars_data['characters'], repo_path / "canon" / "characters")

        # Convert locations
        world_file = repo_path / "canon" / "world.yml"
        if world_file.exists():
            with open(world_file, 'r', encoding='utf-8') as f:
                world_data = yaml.safe_load(f)
            convert_locations_to_markdown(world_data, repo_path / "canon" / "locations")

        # Convert themes
        themes_file = repo_path / "canon" / "themes.yml"
        if themes_file.exists():
            with open(themes_file, 'r', encoding='utf-8') as f:
                themes_data = yaml.safe_load(f)
            convert_themes_to_markdown(themes_data['themes'], repo_path / "canon" / "themes")

        # Convert timeline
        timeline_file = repo_path / "canon" / "timeline.yml"
        if timeline_file.exists():
            with open(timeline_file, 'r', encoding='utf-8') as f:
                timeline_data = yaml.safe_load(f)
            convert_timeline_to_markdown(timeline_data, repo_path / "canon" / "timeline")

        # Convert scenes
        scenes_dir = repo_path / "story" / "scenes"
        if scenes_dir.exists():
            convert_scenes_to_markdown(scenes_dir, repo_path / "story" / "scenes" / "s01e01")

        # Create index files
        create_index_files(repo_path)

        print("\nSUCCESS: Conversion completed!")
        print("Check the generated markdown files in the new directory structure.")

    except Exception as e:
        print(f"\nERROR: Conversion failed: {e}")
        raise


if __name__ == "__main__":
    main()
