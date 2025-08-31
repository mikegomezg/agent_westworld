#!/usr/bin/env python3
"""
Enrich character profiles by analyzing relationships and generating insights.
This script takes character data and creates enriched profiles with additional analysis.
"""

import frontmatter
from pathlib import Path
from typing import Dict, List, Set
import click

def load_character_data(char_id: str, repo_root: Path) -> Dict:
    """Load character data from markdown file"""
    char_file = repo_root / "canon" / "characters" / f"{char_id.lower().replace('-', '_')}.md"
    if char_file.exists():
        with open(char_file, 'r', encoding='utf-8') as f:
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

            # Extract specific sections
            traits = []
            if 'Traits' in sections:
                trait_lines = sections['Traits'].split('\n')
                traits = [line.strip()[2:] for line in trait_lines if line.strip().startswith('- ')]

            goals = []
            if 'Goals' in sections:
                goal_lines = sections['Goals'].split('\n')
                goals = [line.strip()[2:] for line in goal_lines if line.strip().startswith('- ')]

            relationships = {}
            if 'Relationships' in sections:
                rel_lines = sections['Relationships'].split('\n')
                for line in rel_lines:
                    if line.strip().startswith('- **'):
                        # Parse relationship line like "- **Teddy**: Love interest"
                        parts = line.strip()[2:].split('**: ')
                        if len(parts) == 2:
                            rel_name = parts[0].strip()
                            rel_desc = parts[1].strip()
                            relationships[rel_name] = rel_desc

            backstory = sections.get('Backstory', '')
            narrative_function = sections.get('Narrative Function', '')

            return {
                'id': post.get('id', char_id),
                'name': post.get('name', char_id),
                'type': post.get('type', 'unknown'),
                'role': post.get('role', ''),
                'status': post.get('status', ''),
                'traits': traits,
                'goals': goals,
                'relationships': relationships,
                'backstory': backstory,
                'narrative_function': narrative_function
            }
    return {}

def analyze_relationships(char_data: Dict, repo_root: Path) -> Dict:
    """Analyze character relationships and create insights"""
    relationships = char_data.get('relationships', {})
    analysis = {
        'relationship_count': len(relationships),
        'relationship_types': {},
        'key_relationships': [],
        'relationship_insights': []
    }

    for rel_id, rel_desc in relationships.items():
        # Load related character data
        related_char = load_character_data(rel_id, repo_root)
        if related_char:
            # Categorize relationship type
            rel_type = 'unknown'
            if 'love' in rel_desc.lower() or 'romantic' in rel_desc.lower():
                rel_type = 'romantic'
            elif 'creator' in rel_desc.lower() or 'created' in rel_desc.lower():
                rel_type = 'creation'
            elif 'friend' in rel_desc.lower() or 'ally' in rel_desc.lower():
                rel_type = 'alliance'
            elif 'enemy' in rel_desc.lower() or 'adversary' in rel_desc.lower():
                rel_type = 'conflict'
            elif 'family' in rel_desc.lower() or 'father' in rel_desc.lower() or 'daughter' in rel_desc.lower():
                rel_type = 'family'

            if rel_type not in analysis['relationship_types']:
                analysis['relationship_types'][rel_type] = 0
            analysis['relationship_types'][rel_type] += 1

            # Identify key relationships
            if rel_type in ['romantic', 'creation', 'family'] or 'key' in rel_desc.lower():
                analysis['key_relationships'].append({
                    'character': related_char['name'],
                    'type': rel_type,
                    'description': rel_desc,
                    'character_type': related_char['type']
                })

    # Generate insights
    if analysis['relationship_count'] > 5:
        analysis['relationship_insights'].append(
            "This character has many connections, suggesting a central role in the narrative.")

    if 'creation' in analysis['relationship_types']:
        analysis['relationship_insights'].append(
            "This character has creator/creation relationships, indicating artificial origins or significant influence.")

    if 'romantic' in analysis['relationship_types']:
        analysis['relationship_insights'].append(
            "This character has romantic relationships, adding emotional depth to their story.")

    if 'conflict' in analysis['relationship_types']:
        analysis['relationship_insights'].append("This character has adversarial relationships, creating narrative tension.")

    return analysis

def generate_character_insights(char_data: Dict, relationship_analysis: Dict) -> str:
    """Generate insights about the character based on their data"""
    insights = []

    # Analyze character type
    if char_data['type'] == 'host':
        insights.append("As a host, this character represents themes of artificial consciousness and programming.")
        if 'consciousness' in char_data.get('narrative_function', '').lower():
            insights.append("This character is central to the consciousness theme, representing the journey to self-awareness.")
    elif char_data['type'] == 'human':
        insights.append("As a human, this character represents themes of human nature and morality.")

    # Analyze status
    if char_data['status'] == 'deceased':
        insights.append("This character's death creates narrative consequences and drives other characters' motivations.")

    # Analyze goals
    goals = char_data.get('goals', [])
    if len(goals) > 3:
        insights.append("This character has multiple complex goals, indicating a rich internal conflict.")

    if any('consciousness' in goal.lower() for goal in goals):
        insights.append("This character's goals align with the central consciousness theme.")

    # Analyze traits
    traits = char_data.get('traits', [])
    if len(traits) > 4:
        insights.append("This character has many defined traits, making them a complex and well-developed character.")

    if any('questioning' in trait.lower() for trait in traits):
        insights.append("This character's questioning nature drives their character arc and development.")

    return insights

def create_enriched_profile(char_data: Dict, relationship_analysis: Dict, insights: List[str]) -> str:
    """Create an enriched character profile"""
    profile = f"""# Enriched Profile: {char_data['name']}

## Basic Information
- **ID**: {char_data['id']}
- **Type**: {char_data['type']}
- **Role**: {char_data['role']}
- **Status**: {char_data['status']}
- **First Appearance**: {char_data.get('first_appearance', 'Unknown')}

## Character Analysis

### Relationship Network
- **Total Relationships**: {relationship_analysis['relationship_count']}
- **Relationship Types**: {', '.join(f'{k}: {v}' for k, v in relationship_analysis['relationship_types'].items())}

### Key Relationships
"""

    for rel in relationship_analysis['key_relationships']:
        profile += f"- **{rel['character']}** ({rel['type']}): {rel['description']}\n"

    profile += "\n### Character Insights\n"
    for insight in insights:
        profile += f"- {insight}\n"

    profile += "\n### Relationship Insights\n"
    for insight in relationship_analysis['relationship_insights']:
        profile += f"- {insight}\n"

    profile += f"""

## Original Profile Data

### Traits
"""
    for trait in char_data.get('traits', []):
        profile += f"- {trait}\n"

    profile += "\n### Goals\n"
    for goal in char_data.get('goals', []):
        profile += f"- {goal}\n"

    profile += "\n### Backstory\n"
    profile += f"{char_data.get('backstory', '')}\n"

    profile += "\n### Narrative Function\n"
    profile += f"{char_data.get('narrative_function', '')}\n"

    return profile

def process_character_file(char_file: Path, repo_root: Path, output_dir: Path):
    """Process a single character file and create enriched profile"""
    try:
        with open(char_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        char_id = post.get('id', char_file.stem)
        char_name = post.get('name', 'Unknown Character')

        # Load character data
        char_data = load_character_data(char_id, repo_root)
        if not char_data:
            print(f"ERROR: Failed to load character data for {char_name}")
            return

        # Analyze relationships
        relationship_analysis = analyze_relationships(char_data, repo_root)

        # Generate insights
        insights = generate_character_insights(char_data, relationship_analysis)

        # Create enriched profile
        enriched_profile = create_enriched_profile(char_data, relationship_analysis, insights)

        # Write output
        output_file = output_dir / f"{char_id.lower().replace('-', '_')}_enriched.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(enriched_profile)

        print(f"SUCCESS: Generated enriched profile for {char_name}")

    except Exception as e:
        print(f"ERROR: Failed to process {char_file.name}: {e}")

@click.command()
@click.option('--character-id', help='Specific character ID to process')
@click.option('--output-dir', default='generated/summaries', help='Output directory for enriched profiles')
@click.option('--repo-root', default='.', help='Repository root directory')
def main(character_id: str, output_dir: str, repo_root: str):
    """Enrich character profiles with relationship analysis and insights"""
    global repo_path
    repo_path = Path(repo_root)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    print("Enriching character profiles...\n")

    if character_id:
        # Process specific character
        char_file = repo_path / "canon" / "characters" / f"{character_id.lower().replace('-', '_')}.md"
        if char_file.exists():
            process_character_file(char_file, repo_path, output_path)
        else:
            print(f"ERROR: Character file not found: {char_file}")
            exit(1)
    else:
        # Process all characters
        chars_dir = repo_path / "canon" / "characters"
        if not chars_dir.exists():
            print("ERROR: Characters directory not found")
            exit(1)

        char_files = list(chars_dir.glob("*.md"))
        for char_file in char_files:
            if char_file.name == "index.md":
                continue
            process_character_file(char_file, repo_path, output_path)

    print(f"\nSUCCESS: Enriched profiles generated in {output_path}")


if __name__ == "__main__":
    main()
