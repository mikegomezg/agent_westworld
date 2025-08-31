#!/usr/bin/env python3
"""
Master script to run all generation tasks.
This script orchestrates the entire content generation pipeline.
"""

import subprocess
import sys
from pathlib import Path
import click

def run_generation_script(script_name: str, args: list = None) -> bool:
    """Run a generation script and return success status"""
    script_path = Path(__file__).parent / "generate" / script_name

    if not script_path.exists():
        print(f"ERROR: Script not found: {script_path}")
        return False

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    try:
        print(f"Running {script_name}...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())

        if result.returncode == 0:
            print(f"SUCCESS: {script_name} completed successfully")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"ERROR: {script_name} failed with return code {result.returncode}")
            if result.stderr:
                print(f"Error output: {result.stderr}")
            return False

    except Exception as e:
        print(f"ERROR: Failed to run {script_name}: {e}")
        return False

def generate_all_content(repo_root: str = "."):
    """Generate all content using the generation pipeline"""
    print("Starting Westworld content generation pipeline...\n")

    # Ensure we're in the right directory
    repo_path = Path(repo_root).resolve()
    if not repo_path.exists():
        print(f"ERROR: Repository root not found: {repo_path}")
        return False

    print(f"Repository root: {repo_path}\n")

    # Run all generation scripts
    scripts_to_run = [
        ("narrative_from_scene.py", []),
        ("enrich_character_profile.py", []),
        ("timeline_visualization.py", []),
        ("theme_analysis.py", [])
    ]

    success_count = 0
    total_scripts = len(scripts_to_run)

    for script_name, args in scripts_to_run:
        if run_generation_script(script_name, args):
            success_count += 1
        print()

    # Summary
    print("=" * 50)
    print(f"Generation Pipeline Complete")
    print(f"SUCCESS: {success_count}/{total_scripts} scripts completed successfully")

    if success_count == total_scripts:
        print("\nAll content has been generated successfully!")
        print("Check the 'generated/' directory for output files:")
        print("- generated/narratives/ - Scene narratives")
        print("- generated/summaries/ - Character profiles, timeline, themes")
        return True
    else:
        print(f"\nWARNING: {total_scripts - success_count} scripts failed")
        print("Check the error messages above for details")
        return False

@click.command()
@click.option('--repo-root', default='.', help='Repository root directory')
def main(repo_root: str):
    """Run the complete Westworld content generation pipeline"""
    success = generate_all_content(repo_root)

    if success:
        print("\nSUCCESS: Content generation pipeline completed successfully!")
        sys.exit(0)
    else:
        print("\nERROR: Some generation tasks failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
