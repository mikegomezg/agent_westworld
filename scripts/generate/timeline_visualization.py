#!/usr/bin/env python3
"""
Generate timeline visualizations from timeline event markdown files.
This script creates chronological summaries and visual representations of the Westworld timeline.
"""

import frontmatter
from pathlib import Path
from typing import Dict, List
import click
from datetime import datetime

def load_timeline_event(event_file: Path) -> Dict:
    """Load timeline event data from markdown file"""
    try:
        with open(event_file, 'r', encoding='utf-8') as f:
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
            'title': post.get('title', ''),
            'date': post.get('date', ''),
            'period': post.get('period', ''),
            'episode_reference': post.get('episode_reference', ''),
            'overview': sections.get('Overview', ''),
            'characters': sections.get('Characters Involved', ''),
            'significance': sections.get('Significance', ''),
            'content': content
        }
    except Exception as e:
        print(f"ERROR: Failed to load {event_file.name}: {e}")
        return {}

def parse_date(date_str: str) -> int:
    """Parse date string to year for sorting"""
    try:
        if isinstance(date_str, int):
            return date_str
        if isinstance(date_str, str):
            # Handle various date formats
            if date_str.isdigit():
                return int(date_str)
            # Add more date parsing logic as needed
        return 0
    except:
        return 0

def generate_timeline_summary(events: List[Dict]) -> str:
    """Generate a chronological timeline summary"""
    # Sort events by date
    sorted_events = sorted(events, key=lambda x: parse_date(x.get('date', 0)))

    timeline = "# Westworld Timeline\n\n"
    timeline += "## Chronological Summary\n\n"

    current_period = None
    for event in sorted_events:
        if not event:
            continue

        period = event.get('period', 'Unknown Period')
        if period != current_period:
            current_period = period
            timeline += f"### {period}\n\n"

        date = event.get('date', 'Unknown Date')
        title = event.get('title', 'Untitled Event')
        overview = event.get('overview', '')

        timeline += f"**{date}** - {title}\n"
        if overview:
            timeline += f"{overview}\n"
        timeline += "\n"

    return timeline

def generate_period_breakdown(events: List[Dict]) -> str:
    """Generate breakdown by narrative periods"""
    periods = {}

    for event in events:
        if not event:
            continue

        period = event.get('period', 'Unknown Period')
        if period not in periods:
            periods[period] = []
        periods[period].append(event)

    breakdown = "## Narrative Periods\n\n"

    for period, period_events in periods.items():
        breakdown += f"### {period}\n\n"

        # Sort events in this period by date
        sorted_events = sorted(period_events, key=lambda x: parse_date(x.get('date', 0)))

        for event in sorted_events:
            date = event.get('date', 'Unknown Date')
            title = event.get('title', 'Untitled Event')
            breakdown += f"- **{date}**: {title}\n"

        breakdown += "\n"

    return breakdown

def generate_character_timeline(events: List[Dict]) -> str:
    """Generate character-focused timeline"""
    character_events = {}

    for event in events:
        if not event:
            continue

        characters = event.get('characters', '')
        if characters:
            # Parse character list
            char_lines = characters.split('\n')
            for line in char_lines:
                if line.strip().startswith('- '):
                    char_id = line.strip()[2:]
                    if char_id not in character_events:
                        character_events[char_id] = []
                    character_events[char_id].append(event)

    timeline = "## Character Timelines\n\n"

    for char_id, char_events in character_events.items():
        timeline += f"### {char_id}\n\n"

        # Sort events by date
        sorted_events = sorted(char_events, key=lambda x: parse_date(x.get('date', 0)))

        for event in sorted_events:
            date = event.get('date', 'Unknown Date')
            title = event.get('title', 'Untitled Event')
            timeline += f"- **{date}**: {title}\n"

        timeline += "\n"

    return timeline

def process_timeline_events(repo_root: Path, output_dir: Path):
    """Process all timeline events and generate visualizations"""
    timeline_dir = repo_root / "canon" / "timeline"

    if not timeline_dir.exists():
        print("ERROR: Timeline directory not found")
        return

    # Load all timeline events
    event_files = list(timeline_dir.glob("*.md"))
    events = []

    for event_file in event_files:
        if event_file.name == "index.md":
            continue
        event_data = load_timeline_event(event_file)
        if event_data:
            events.append(event_data)

    print(f"SUCCESS: Loaded {len(events)} timeline events")

    # Generate different timeline views
    timeline_summary = generate_timeline_summary(events)
    period_breakdown = generate_period_breakdown(events)
    character_timeline = generate_character_timeline(events)

    # Combine into full timeline
    full_timeline = timeline_summary + "\n" + period_breakdown + "\n" + character_timeline

    # Write output
    output_file = output_dir / "westworld_timeline.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_timeline)

    print(f"SUCCESS: Generated timeline visualization in {output_file}")

@click.command()
@click.option('--output-dir', default='generated/summaries', help='Output directory for timeline')
@click.option('--repo-root', default='.', help='Repository root directory')
def main(output_dir: str, repo_root: str):
    """Generate timeline visualizations from timeline event files"""
    repo_path = Path(repo_root)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    print("Generating timeline visualizations...\n")

    process_timeline_events(repo_path, output_path)

    print(f"\nSUCCESS: Timeline visualizations generated in {output_path}")


if __name__ == "__main__":
    main()
