#!/usr/bin/env python3
"""
Script to set up .env files across all LLM projects
"""

import os
import shutil
from pathlib import Path


def create_env_files():
    """Create .env files for all project directories"""

    # Base directory containing all projects
    base_dir = Path(__file__).parent / "projects"

    # Template .env content
    env_template = """# IBM Watson X Configuration
WATSONX_URL=https://us-south.ml.cloud.ibm.com
IBM_CLOUD_API_KEY=your_ibm_cloud_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here

# Optional: Other API keys (uncomment and fill as needed)
# HUGGINGFACE_API_TOKEN=your_huggingface_token_here
# OPENAI_API_KEY=your_openai_api_key_here
# ANTHROPIC_API_KEY=your_anthropic_api_key_here
"""

    # Get all project directories
    project_dirs = [d for d in base_dir.iterdir()
                    if d.is_dir() and d.name.startswith(('0', '1', '2', '3'))]

    print(f"Found {len(project_dirs)} project directories")

    for project_dir in sorted(project_dirs):
        env_file = project_dir / ".env"
        env_template_file = project_dir / ".env.template"

        # Create .env.template file
        if not env_template_file.exists():
            with open(env_template_file, 'w') as f:
                f.write(env_template)
            print(f"Created: {env_template_file}")

        # Create .env file only if it doesn't exist
        if not env_file.exists():
            with open(env_file, 'w') as f:
                f.write(env_template)
            print(f"Created: {env_file}")
        else:
            print(f"Skipped (already exists): {env_file}")


def update_requirements():
    """Add python-dotenv to requirements.txt files that don't have it"""

    base_dir = Path(__file__).parent / "projects"
    project_dirs = [d for d in base_dir.iterdir()
                    if d.is_dir() and d.name.startswith(('0', '1', '2', '3'))]

    for project_dir in sorted(project_dirs):
        req_file = project_dir / "requirements.txt"

        if req_file.exists():
            # Read current requirements
            with open(req_file, 'r') as f:
                content = f.read()

            # Check if python-dotenv is already in requirements
            if 'python-dotenv' not in content:
                # Add python-dotenv to the beginning
                if content.strip():
                    new_content = f"python-dotenv\n{content}"
                else:
                    new_content = "python-dotenv\n"

                with open(req_file, 'w') as f:
                    f.write(new_content)
                print(f"Added python-dotenv to: {req_file}")
            else:
                print(f"python-dotenv already in: {req_file}")


if __name__ == "__main__":
    print("Setting up .env files for LLM projects...")
    print("=" * 50)

    create_env_files()
    print("\n" + "=" * 50)
    print("Updating requirements.txt files...")
    update_requirements()

    print("\n" + "=" * 50)
    print("Setup complete!")
    print("\nIMPORTANT: Remember to:")
    print("1. Fill in your actual API keys in the .env files")
    print("2. Never commit .env files to version control")
    print("3. Use .env.template as a reference for required variables")
