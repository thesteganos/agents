#!/usr/bin/env python3
import argparse
import os
import re
import sys
import json
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "skills" / "SKILL_TEMPLATE.md"
SKILLS_DIR = BASE_DIR / "skills"

def validate_name(name):
    """Ensure name is strictly kebab-case."""
    pattern = r"^[a-z0-9]+(-[a-z0-9]+)*$"
    if not re.match(pattern, name):
        raise ValueError(f"Invalid skill name '{name}'. Must be kebab-case (e.g., 'git-commit-helper').")

def scaffold_skill(name, description):
    """Creates directory and populates SKILL.md from template."""
    try:
        # Validate
        validate_name(name)
        
        # Define paths
        target_dir = SKILLS_DIR / name
        target_file = target_dir / "SKILL.md"
        
        # Check existence
        if target_dir.exists():
            raise FileExistsError(f"Skill '{name}' already exists at {target_dir}")
        
        # Read template
        if not TEMPLATE_PATH.exists():
            raise FileNotFoundError(f"Template not found at {TEMPLATE_PATH}")
        
        with open(TEMPLATE_PATH, 'r') as f:
            content = f.read()
            
        # Replace placeholders
        # Note: We use simple string replacement to avoid external dependencies like Jinja2
        final_content = content.replace("{{name}}", name)
        final_content = final_content.replace("{{description}}", description)
        
        # Create structure
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "scripts").mkdir(exist_ok=True)
        
        # Write file
        with open(target_file, 'w') as f:
            f.write(final_content)
            
        return {
            "status": "success",
            "path": str(target_file.absolute()),
            "message": f"Skill '{name}' created successfully."
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new agent skill.")
    parser.add_argument("--name", required=True, help="Skill name in kebab-case")
    parser.add_argument("--description", default="TODO: Add description", help="Brief description of the skill")
    
    args = parser.parse_args()
    
    result = scaffold_skill(args.name, args.description)
    print(json.dumps(result, indent=2))
    
    if result["status"] == "error":
        sys.exit(1)
