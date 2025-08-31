#!/usr/bin/env python3
"""
Generate theme analysis from theme markdown files.
This script analyzes themes and their connections to characters, locations, and events.
"""

import frontmatter
from pathlib import Path
from typing import Dict, List, Set
import click

def load_theme_data(theme_file: Path) -> Dict:
    """Load theme data from markdown file"""
    try:
        with open(theme_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Extract content from markdown body
        content = post.content
        sections = {}

        # Parse markdown sections
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

        return {
            'id': post.get('id', ''),
            'name': post.get('name', ''),
            'description': post.get('description', ''),
            'overview': sections.get('Overview', ''),
            'key_concepts': sections.get('Key Concepts', ''),
            'examples': sections.get('Examples', ''),
            'significance': sections.get('Significance', ''),
            'content': content
        }
    except Exception as e:
        print(f"ERROR: Failed to load {theme_file.name}: {e}")
        return {}

def load_character_data(char_id: str, repo_root: Path) -> Dict:
    """Load character data from markdown file"""
    char_file = repo_root / "canon" / "characters" / f"{char_id.lower().replace('-', '_')}.md"
    if char_file.exists():
        with open(char_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return {
                'name': post.get('name', char_id),
                'type': post.get('type', 'unknown'),
                'role': post.get('role', '')
            }
    return {'name': char_id, 'type': 'unknown', 'role': ''}

def analyze_theme_connections(theme_data: Dict, repo_root: Path) -> Dict:
    """Analyze how themes connect to other elements"""
    analysis = {
        'character_connections': [],
        'location_connections': [],
        'event_connections': [],
        'theme_relationships': []
    }

    # Extract examples and look for connections
    examples = theme_data.get('examples', '')
    if examples:
        lines = examples.split('\n')
        for line in lines:
            if line.strip().startswith('- '):
                example = line.strip()[2:]
                # Look for character references
                if 'C-' in example:
                    char_id = example.split('C-')[1].split()[0] if 'C-' in example else ''
                    if char_id:
                        char_data = load_character_data(f"C-{char_id}", repo_root)
                        analysis['character_connections'].append({
                            'character': char_data['name'],
                            'connection': example
                        })

    return analysis

def generate_theme_summary(themes: List[Dict]) -> str:
    """Generate a summary of all themes"""
    summary = "# Westworld Themes Analysis\n\n"
    summary += "## Theme Overview\n\n"

    for theme in themes:
        if not theme:
            continue

        name = theme.get('name', 'Unknown Theme')
        description = theme.get('description', '')
        overview = theme.get('overview', '')

        summary += f"### {name}\n\n"
        if description:
            summary += f"**Description**: {description}\n\n"
        if overview:
            summary += f"{overview}\n\n"
        summary += "---\n\n"

    return summary

def generate_theme_connections(themes: List[Dict], repo_root: Path) -> str:
    """Generate analysis of theme connections"""
    connections = "## Theme Connections\n\n"

    for theme in themes:
        if not theme:
            continue

        name = theme.get('name', 'Unknown Theme')
        analysis = analyze_theme_connections(theme, repo_root)

        connections += f"### {name}\n\n"

        if analysis['character_connections']:
            connections += "**Character Connections**:\n"
            for conn in analysis['character_connections']:
                connections += f"- {conn['character']}: {conn['connection']}\n"
            connections += "\n"

        connections += "---\n\n"

    return connections

def generate_theme_significance(themes: List[Dict]) -> str:
    """Generate analysis of theme significance"""
    significance = "## Theme Significance\n\n"

    for theme in themes:
        if not theme:
            continue

        name = theme.get('name', 'Unknown Theme')
        sig_text = theme.get('significance', '')

        if sig_text:
            significance += f"### {name}\n\n"
            significance += f"{sig_text}\n\n"
            significance += "---\n\n"

    return significance

def process_theme_files(repo_root: Path, output_dir: Path):
    """Process all theme files and generate analysis"""
    themes_dir = repo_root / "canon" / "themes"

    if not themes_dir.exists():
        print("ERROR: Themes directory not found")
        return

    # Load all themes
    theme_files = list(themes_dir.glob("*.md"))
    themes = []

    for theme_file in theme_files:
        if theme_file.name == "index.md":
            continue
        theme_data = load_theme_data(theme_file)
        if theme_data:
            themes.append(theme_data)

    print(f"SUCCESS: Loaded {len(themes)} themes")

    # Generate different theme analyses
    theme_summary = generate_theme_summary(themes)
    theme_connections = generate_theme_connections(themes, repo_root)
    theme_significance = generate_theme_significance(themes)

    # Combine into full analysis
    full_analysis = theme_summary + "\n" + theme_connections + "\n" + theme_significance

    # Write output
    output_file = output_dir / "westworld_themes_analysis.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_analysis)

    print(f"SUCCESS: Generated theme analysis in {output_file}")

@click.command()
@click.option('--output-dir', default='generated/summaries', help='Output directory for theme analysis')
@click.option('--repo-root', default='.', help='Repository root directory')
def main(output_dir: str, repo_root: str):
    """Generate theme analysis from theme markdown files"""
    repo_path = Path(repo_root)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    print("Generating theme analysis...\n")

    process_theme_files(repo_path, output_path)

    print(f"\nSUCCESS: Theme analysis generated in {output_path}")


if __name__ == "__main__":
    main()
