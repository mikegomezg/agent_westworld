#!/usr/bin/env python3
import yaml
import json
from pathlib import Path
from typing import Dict, List

class NarrativeGenerator:
    def __init__(self):
        self.root = Path.cwd().parent
        self.characters = self.load_characters()
        self.world = self.load_world()
        self.themes = self.load_themes()

    def load_yaml(self, filepath: Path) -> Dict:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def load_characters(self) -> Dict:
        data = self.load_yaml(self.root / 'canon' / 'characters.yml')
        return {c['id']: c for c in data.get('characters', [])}

    def load_world(self) -> Dict:
        return self.load_yaml(self.root / 'canon' / 'world.yml')

    def load_themes(self) -> Dict:
        data = self.load_yaml(self.root / 'canon' / 'themes.yml')
        return {t['id']: t for t in data.get('themes', [])}

    def generate_scene_narrative(self, scene: Dict) -> str:
        """Generate prose narrative from scene data"""
        location = next((l for l in self.world['locations']
                        if l['id'] == scene.get('location')), None)

        narrative = []

        # Opening description
        if location:
            narrative.append(f"The scene opens in {location['name']}. {location['description']}.")

        # Character introductions
        for char_id in scene.get('characters', []):
            if char_id in self.characters:
                char = self.characters[char_id]
                narrative.append(f"{char['name']}, {char['role']}, is present.")

        # Main action
        narrative.append(scene.get('synopsis', ''))

        # Dialogue
        if 'dialogue' in scene:
            for line in scene['dialogue']:
                narrative.append(f'Someone says, "{line}"')

        # Actions
        if 'actions' in scene:
            narrative.extend(scene['actions'])

        return '\n\n'.join(narrative)

    def generate_all_narratives(self):
        """Generate narratives for all scenes"""
        scenes_dir = self.root / 'story' / 'scenes'
        output_dir = self.root / 'site' / 'src' / 'content' / 'narratives'
        output_dir.mkdir(parents=True, exist_ok=True)

        for scene_file in scenes_dir.glob('*.yml'):
            if scene_file.name == 'TEMPLATE.yml':
                continue

            scene = self.load_yaml(scene_file)
            narrative = self.generate_scene_narrative(scene)

            output_file = output_dir / f"{scene['id']}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# {scene['title']}\n\n")
                f.write(narrative)


if __name__ == "__main__":
    generator = NarrativeGenerator()
    generator.generate_all_narratives()
    print("Narratives generated successfully!")
