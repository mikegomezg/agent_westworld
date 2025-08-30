#!/usr/bin/env python3
import click
import yaml
import json
from pathlib import Path
from typing import Dict, List, Set
from rich.console import Console
from rich.table import Table
from pydantic import ValidationError

from schemas import Character, Location, Scene, Episode, Theme, TimelineEvent

console = Console()

class StoryValidator:
    def __init__(self, repo_root: Path = Path(".")):
        self.repo_root = repo_root
        self.errors = []
        self.warnings = []
        
    def load_yaml(self, filepath: Path) -> Dict:
        """Load and parse YAML file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"Failed to load {filepath}: {e}")
            return {}
    
    def validate_characters(self) -> bool:
        """Validate all character definitions"""
        char_file = self.repo_root / "canon" / "characters.yml"
        if not char_file.exists():
            self.errors.append(f"Missing characters.yml")
            return False
            
        data = self.load_yaml(char_file)
        valid = True
        
        for char_data in data.get("characters", []):
            try:
                Character(**char_data)
                console.print(f"SUCCESS: Character {char_data['id']} valid", style="green")
            except ValidationError as e:
                self.errors.append(f"Character {char_data.get('id', 'unknown')}: {e}")
                valid = False
                
        return valid
    
    def validate_world(self) -> bool:
        """Validate world and location definitions"""
        world_file = self.repo_root / "canon" / "world.yml"
        if not world_file.exists():
            self.errors.append(f"Missing world.yml")
            return False
            
        data = self.load_yaml(world_file)
        valid = True
        
        for location_data in data.get("locations", []):
            try:
                Location(**location_data)
                console.print(f"SUCCESS: Location {location_data['id']} valid", style="green")
            except ValidationError as e:
                self.errors.append(f"Location {location_data.get('id', 'unknown')}: {e}")
                valid = False
                
        return valid
    
    def validate_episodes(self) -> bool:
        """Validate episode definitions"""
        episodes_dir = self.repo_root / "story" / "episodes"
        if not episodes_dir.exists():
            self.warnings.append("No episodes directory found")
            return True
            
        valid = True
        for episode_file in episodes_dir.glob("*.yml"):
            try:
                data = self.load_yaml(episode_file)
                Episode(**data)
                console.print(f"SUCCESS: Episode {episode_file.stem} valid", style="green")
            except ValidationError as e:
                self.errors.append(f"Episode {episode_file.stem}: {e}")
                valid = False
                
        return valid
    
    def check_continuity(self) -> bool:
        """Check for continuity issues"""
        # Check character references in scenes
        # Check timeline consistency
        # Check location connections
        console.print("INFO: Continuity checks not yet implemented", style="blue")
        return True
    
    def run_all_checks(self) -> bool:
        """Run all validation checks"""
        console.print("\n[bold]Running Story Validation[/bold]\n")
        
        checks = [
            ("Characters", self.validate_characters),
            ("World & Locations", self.validate_world),
            ("Episodes", self.validate_episodes),
            ("Continuity", self.check_continuity),
        ]
        
        all_valid = True
        for name, check_func in checks:
            console.print(f"Checking {name}...")
            if not check_func():
                all_valid = False
                
        # Print summary
        if self.errors:
            console.print("\n[red]ERRORS:[/red]")
            for error in self.errors:
                console.print(f"  ERROR: {error}")
                
        if self.warnings:
            console.print("\n[yellow]WARNINGS:[/yellow]")
            for warning in self.warnings:
                console.print(f"  WARNING: {warning}")
                
        if all_valid:
            console.print("\n[green]SUCCESS: All checks passed![/green]")
        else:
            console.print("\n[red]ERROR: Validation failed[/red]")
            
        return all_valid

@click.command()
@click.option('--strict', is_flag=True, help='Treat warnings as errors')
def main(strict):
    """Validate Westworld story framework files"""
    validator = StoryValidator()
    valid = validator.run_all_checks()
    
    if not valid or (strict and validator.warnings):
        exit(1)
        
if __name__ == "__main__":
    main()

