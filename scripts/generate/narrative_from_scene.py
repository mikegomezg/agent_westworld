#!/usr/bin/env python3
"""
Generate narrative prose from scene markdown files.
This script takes scene data and creates flowing narrative text.
"""

import frontmatter
from pathlib import Path
from typing import Dict, List
import click

def load_character_data(char_id: str, repo_root: Path) -> Dict:
    """Load character data from markdown file"""
    char_file = repo_root / "canon" / "characters" / f"{char_id.lower().replace('-', '_')}.md"
    if char_file.exists():
        with open(char_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return {
                'name': post.get('name', char_id),
                'type': post.get('type', 'unknown'),
                'role': post.get('role', ''),
                'traits': post.get('traits', [])
            }
    return {'name': char_id, 'type': 'unknown', 'role': '', 'traits': []}

def load_location_data(loc_id: str, repo_root: Path) -> Dict:
    """Load location data from markdown file"""
    loc_file = repo_root / "canon" / "locations" / f"{loc_id.lower().replace('-', '_')}.md"
    if loc_file.exists():
        with open(loc_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            # Extract description from content
            content = post.content
            description = ""
            if "## Overview" in content:
                overview_section = content.split("## Overview")[1].split("##")[0]
                description = overview_section.strip()

            return {
                'name': post.get('name', loc_id),
                'description': description,
                'region': post.get('region', '')
            }
    return {'name': loc_id, 'description': '', 'region': ''}

def generate_narrative_prose(scene_data: Dict, repo_root: Path) -> str:
    """Generate narrative prose from scene data"""
    title = scene_data.get('title', 'Unknown Scene')
    location_id = scene_data.get('location', '')
    timestamp = scene_data.get('timestamp', '')
    themes = scene_data.get('themes', [])

    # Extract sections from content using a more reliable method
    content = scene_data.get('content', '')
    sections = {}

    # Split content into sections
    lines = content.split('\n')
    current_section = None
    current_content = []

    for line in lines:
        if line.startswith('## '):
            # Save previous section
            if current_section and current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            # Start new section
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    # Save last section
    if current_section and current_content:
        sections[current_section] = '\n'.join(current_content).strip()

    # Extract specific sections
    synopsis = sections.get('Synopsis', '')
    characters = []
    if 'Characters' in sections:
        char_lines = sections['Characters'].split('\n')
        characters = [line.strip()[2:] for line in char_lines if line.strip().startswith('- ')]

    actions = []
    if 'Actions' in sections:
        action_lines = sections['Actions'].split('\n')
        actions = [line.strip()[2:] for line in action_lines if line.strip().startswith('- ')]

    emotions = []
    if 'Emotions' in sections:
        emotion_lines = sections['Emotions'].split('\n')
        emotions = [line.strip()[2:] for line in emotion_lines if line.strip().startswith('- ')]

    dialogue = []
    if 'Key Dialogue' in sections:
        dialogue_lines = sections['Key Dialogue'].split('\n')
        dialogue = [line.strip()[2:] for line in dialogue_lines if line.strip().startswith('- ')]

    reveals = []
    if 'Reveals' in sections:
        reveal_lines = sections['Reveals'].split('\n')
        reveals = [line.strip()[2:] for line in reveal_lines if line.strip().startswith('- ')]

    conflicts = []
    if 'Conflicts' in sections:
        conflict_lines = sections['Conflicts'].split('\n')
        conflicts = [line.strip()[2:] for line in conflict_lines if line.strip().startswith('- ')]

    connections = []
    if 'Connections' in sections:
        connection_lines = sections['Connections'].split('\n')
        connections = [line.strip()[2:] for line in connection_lines if line.strip().startswith('- ')]

    # Load location details
    location = load_location_data(location_id, repo_root)

    # Load character details
    char_details = []
    for char_id in characters:
        char_data = load_character_data(char_id, repo_root)
        char_details.append(char_data)

    # Generate narrative
    narrative = f"# {title}\n\n"

    # Setting
    if timestamp and location['name']:
        narrative += f"The scene opens at {timestamp.lower()} in {location['name']}"
        if location['description']:
            narrative += f", {location['description'].lower()}"
        narrative += ".\n\n"
    elif location['name']:
        narrative += f"The scene takes place in {location['name']}"
        if location['description']:
            narrative += f", {location['description'].lower()}"
        narrative += ".\n\n"

    # Character introductions
    if char_details:
        narrative += "## Characters Present\n\n"
        for char in char_details:
            narrative += f"**{char['name']}** - {char['role']}"
            if char['traits']:
                narrative += f" ({', '.join(char['traits'][:2])})"
            narrative += "\n\n"

    # Main narrative
    if synopsis:
        narrative += "## Narrative\n\n"
        narrative += f"{synopsis}\n\n"

    # Add details from scene data
    if actions:
        narrative += "### Key Actions\n\n"
        for action in actions:
            narrative += f"- {action}\n"
        narrative += "\n"

    if emotions:
        narrative += "### Emotional Beats\n\n"
        for emotion in emotions:
            narrative += f"- {emotion}\n"
        narrative += "\n"

    if dialogue:
        narrative += "### Key Dialogue\n\n"
        for line in dialogue:
            # Remove quotes if they exist
            clean_line = line.strip('"')
            narrative += f"> \"{clean_line}\"\n\n"

    if reveals:
        narrative += "### Revelations\n\n"
        for reveal in reveals:
            narrative += f"- {reveal}\n"
        narrative += "\n"

    if conflicts:
        narrative += "### Conflicts\n\n"
        for conflict in conflicts:
            narrative += f"- {conflict}\n"
        narrative += "\n"

    # Themes
    if themes:
        narrative += "## Themes Explored\n\n"
        for theme_id in themes:
            narrative += f"- {theme_id}\n"
        narrative += "\n"

    # Connections
    if connections:
        narrative += "## Narrative Connections\n\n"
        for connection in connections:
            narrative += f"- {connection}\n"
        narrative += "\n"

    return narrative

def process_scene_file(scene_file: Path, repo_root: Path, output_dir: Path):
    """Process a single scene file and generate narrative"""
    try:
        with open(scene_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        scene_id = post.get('id', scene_file.stem)
        scene_title = post.get('title', 'Unknown Scene')

        # Get the full markdown content (everything after frontmatter)
        markdown_content = post.content

        # Create a scene_data dict that includes the parsed content
        scene_data = dict(post)
        scene_data['content'] = markdown_content

        # Generate narrative
        narrative = generate_narrative_prose(scene_data, repo_root)

        # Write output
        output_file = output_dir / f"{scene_id.lower().replace('-', '_')}_narrative.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(narrative)

        print(f"SUCCESS: Generated narrative for {scene_title}")

    except Exception as e:
        print(f"ERROR: Failed to process {scene_file.name}: {e}")

@click.command()
@click.option('--scene-id', help='Specific scene ID to process')
@click.option('--output-dir', default='generated/narratives', help='Output directory for narratives')
@click.option('--repo-root', default='.', help='Repository root directory')
def main(scene_id: str, output_dir: str, repo_root: str):
    """Generate narrative prose from scene markdown files"""
    repo_path = Path(repo_root)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    print("Generating narratives from scenes...\n")

    if scene_id:
        # Process specific scene
        scene_file = repo_path / "story" / "scenes" / "s01e01" / f"{scene_id.lower().replace('-', '_')}.md"
        if scene_file.exists():
            process_scene_file(scene_file, repo_path, output_path)
        else:
            print(f"ERROR: Scene file not found: {scene_file}")
            exit(1)
    else:
        # Process all scenes
        scenes_dir = repo_path / "story" / "scenes" / "s01e01"
        if not scenes_dir.exists():
            print("ERROR: Scenes directory not found")
            exit(1)

        scene_files = list(scenes_dir.glob("*.md"))
        for scene_file in scene_files:
            if scene_file.name == "index.md":
                continue
            process_scene_file(scene_file, repo_path, output_path)

    print(f"\nSUCCESS: Narratives generated in {output_path}")


if __name__ == "__main__":
    main()
