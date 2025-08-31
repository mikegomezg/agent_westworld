#!/usr/bin/env python3
"""
Validate markdown files with frontmatter for the Westworld framework.
This script checks that all markdown files have proper structure and required sections.
"""

import frontmatter
from pathlib import Path
from typing import Dict, List, Set
import click

class MarkdownValidator:
    def __init__(self, repo_root: Path = Path(".")):
        self.repo_root = repo_root
        self.errors = []
        self.warnings = []

    def validate_character_file(self, filepath: Path) -> bool:
        """Validate a character markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Check required frontmatter
            required_fields = ['id', 'name', 'type', 'role', 'status']
            missing_fields = [field for field in required_fields if field not in post]

            if missing_fields:
                self.errors.append(f"Character {filepath.name}: Missing required frontmatter fields: {missing_fields}")
                return False

            # Check required sections in content
            content = post.content
            required_sections = ['## Overview', '## Traits', '## Goals', '## Relationships', '## Backstory']
            missing_sections = [section for section in required_sections if section not in content]

            if missing_sections:
                self.errors.append(f"Character {filepath.name}: Missing required sections: {missing_sections}")
                return False

            return True

        except Exception as e:
            self.errors.append(f"Character {filepath.name}: Failed to parse: {e}")
            return False

    def validate_location_file(self, filepath: Path) -> bool:
        """Validate a location markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Check required frontmatter
            required_fields = ['id', 'name']
            missing_fields = [field for field in required_fields if field not in post]

            if missing_fields:
                self.errors.append(f"Location {filepath.name}: Missing required frontmatter fields: {missing_fields}")
                return False

            # Check required sections in content
            content = post.content
            required_sections = ['## Overview']
            missing_sections = [section for section in required_sections if section not in content]

            if missing_sections:
                self.errors.append(f"Location {filepath.name}: Missing required sections: {missing_sections}")
                return False

            return True

        except Exception as e:
            self.errors.append(f"Location {filepath.name}: Failed to parse: {e}")
            return False

    def validate_theme_file(self, filepath: Path) -> bool:
        """Validate a theme markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Check required frontmatter
            required_fields = ['id', 'name']
            missing_fields = [field for field in required_fields if field not in post]

            if missing_fields:
                self.errors.append(f"Theme {filepath.name}: Missing required frontmatter fields: {missing_fields}")
                return False

            # Check required sections in content
            content = post.content
            required_sections = ['## Description', '## Examples', '## Significance']
            missing_sections = [section for section in required_sections if section not in content]

            if missing_sections:
                self.errors.append(f"Theme {filepath.name}: Missing required sections: {missing_sections}")
                return False

            return True

        except Exception as e:
            self.errors.append(f"Theme {filepath.name}: Failed to parse: {e}")
            return False

    def validate_timeline_file(self, filepath: Path) -> bool:
        """Validate a timeline event markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Check required frontmatter
            required_fields = ['id', 'title']
            missing_fields = [field for field in required_fields if field not in post]

            if missing_fields:
                self.errors.append(f"Timeline {filepath.name}: Missing required frontmatter fields: {missing_fields}")
                return False

            # Check required sections in content
            content = post.content
            required_sections = ['## Overview', '## Significance']
            missing_sections = [section for section in required_sections if section not in content]

            if missing_sections:
                self.errors.append(f"Timeline {filepath.name}: Missing required sections: {missing_sections}")
                return False

            return True

        except Exception as e:
            self.errors.append(f"Timeline {filepath.name}: Failed to parse: {e}")
            return False

    def validate_scene_file(self, filepath: Path) -> bool:
        """Validate a scene markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Check required frontmatter
            required_fields = ['id', 'episode', 'title']
            missing_fields = [field for field in required_fields if field not in post]

            if missing_fields:
                self.errors.append(f"Scene {filepath.name}: Missing required frontmatter fields: {missing_fields}")
                return False

            # Check required sections in content
            content = post.content
            required_sections = ['## Synopsis', '## Characters']
            missing_sections = [section for section in required_sections if section not in content]

            if missing_sections:
                self.errors.append(f"Scene {filepath.name}: Missing required sections: {missing_sections}")
                return False

            return True

        except Exception as e:
            self.errors.append(f"Scene {filepath.name}: Failed to parse: {e}")
            return False

    def validate_characters(self) -> bool:
        """Validate all character markdown files"""
        chars_dir = self.repo_root / "canon" / "characters"
        if not chars_dir.exists():
            self.errors.append("Missing characters directory")
            return False

        valid = True
        char_files = list(chars_dir.glob("*.md"))

        for char_file in char_files:
            if char_file.name == "index.md":
                continue
            if not self.validate_character_file(char_file):
                valid = False
            else:
                print(f"SUCCESS: Character {char_file.name} valid")

        return valid

    def validate_locations(self) -> bool:
        """Validate all location markdown files"""
        locs_dir = self.repo_root / "canon" / "locations"
        if not locs_dir.exists():
            self.errors.append("Missing locations directory")
            return False

        valid = True
        loc_files = list(locs_dir.glob("*.md"))

        for loc_file in loc_files:
            if loc_file.name == "index.md":
                continue
            if not self.validate_location_file(loc_file):
                valid = False
            else:
                print(f"SUCCESS: Location {loc_file.name} valid")

        return valid

    def validate_themes(self) -> bool:
        """Validate all theme markdown files"""
        themes_dir = self.repo_root / "canon" / "themes"
        if not themes_dir.exists():
            self.errors.append("Missing themes directory")
            return False

        valid = True
        theme_files = list(themes_dir.glob("*.md"))

        for theme_file in theme_files:
            if theme_file.name == "index.md":
                continue
            if not self.validate_theme_file(theme_file):
                valid = False
            else:
                print(f"SUCCESS: Theme {theme_file.name} valid")

        return valid

    def validate_timeline(self) -> bool:
        """Validate all timeline markdown files"""
        timeline_dir = self.repo_root / "canon" / "timeline"
        if not timeline_dir.exists():
            self.errors.append("Missing timeline directory")
            return False

        valid = True
        timeline_files = list(timeline_dir.glob("*.md"))

        for timeline_file in timeline_files:
            if timeline_file.name == "index.md":
                continue
            if not self.validate_timeline_file(timeline_file):
                valid = False
            else:
                print(f"SUCCESS: Timeline {timeline_file.name} valid")

        return valid

    def validate_scenes(self) -> bool:
        """Validate all scene markdown files"""
        scenes_dir = self.repo_root / "story" / "scenes" / "s01e01"
        if not scenes_dir.exists():
            self.warnings.append("No scenes directory found")
            return True

        valid = True
        scene_files = list(scenes_dir.glob("*.md"))

        for scene_file in scene_files:
            if scene_file.name == "index.md":
                continue
            if not self.validate_scene_file(scene_file):
                valid = False
            else:
                print(f"SUCCESS: Scene {scene_file.name} valid")

        return valid

    def check_continuity(self) -> bool:
        """Check for continuity issues between files"""
        print("INFO: Continuity checks not yet implemented")
        return True

    def run_all_checks(self) -> bool:
        """Run all validation checks"""
        print("\nRunning Markdown Validation\n")

        checks = [
            ("Characters", self.validate_characters),
            ("Locations", self.validate_locations),
            ("Themes", self.validate_themes),
            ("Timeline", self.validate_timeline),
            ("Scenes", self.validate_scenes),
            ("Continuity", self.check_continuity),
        ]

        all_valid = True
        for name, check_func in checks:
            print(f"Checking {name}...")
            if not check_func():
                all_valid = False

        # Print summary
        if self.errors:
            print("\nERRORS:")
            for error in self.errors:
                print(f"  ERROR: {error}")

        if self.warnings:
            print("\nWARNINGS:")
            for warning in self.warnings:
                print(f"  WARNING: {warning}")

        if all_valid:
            print("\nSUCCESS: All checks passed!")
        else:
            print("\nERROR: Validation failed")

        return all_valid

@click.command()
@click.option('--strict', is_flag=True, help='Treat warnings as errors')
def main(strict):
    """Validate Westworld markdown framework files"""
    validator = MarkdownValidator()
    valid = validator.run_all_checks()

    if not valid or (strict and validator.warnings):
        exit(1)


if __name__ == "__main__":
    main()
