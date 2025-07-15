#!/usr/bin/env python3
"""
Simple script to identify which projects need .env files and create them selectively
"""

import os
import json
from pathlib import Path


def find_projects_needing_env():
    """Find projects that use environment variables or API keys"""

    base_dir = Path(__file__).parent.parent / "projects"
    projects_needing_env = []

    # List of patterns that indicate need for environment variables
    env_patterns = [
        'userdata.get', 'os.getenv', 'os.environ',
        'API_KEY', 'api_key', 'WATSONX', 'OPENAI', 'HUGGINGFACE',
        'WatsonxLLM', 'WatsonxEmbeddings'
    ]

    for project_dir in sorted(base_dir.glob('*/')):
        if not project_dir.is_dir():
            continue

        needs_env = False
        files_with_env = []

        # Check Python files
        for py_file in project_dir.glob('*.py'):
            try:
                content = py_file.read_text()
                for pattern in env_patterns:
                    if pattern in content:
                        needs_env = True
                        files_with_env.append(py_file.name)
                        break
            except:
                continue

        # Check Jupyter notebooks
        for nb_file in project_dir.glob('*.ipynb'):
            try:
                with open(nb_file, 'r') as f:
                    content = f.read()
                    for pattern in env_patterns:
                        if pattern in content:
                            needs_env = True
                            files_with_env.append(nb_file.name)
                            break
            except:
                continue

        if needs_env:
            projects_needing_env.append({
                'project': project_dir.name,
                'path': str(project_dir),
                'files': files_with_env
            })

    return projects_needing_env


def create_env_for_project(project_path):
    """Create .env file for a specific project"""

    env_content = """# IBM Watson X Configuration
WATSONX_URL=https://us-south.ml.cloud.ibm.com
IBM_CLOUD_API_KEY=your_ibm_cloud_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here

# Optional: Other API keys (uncomment and fill as needed)
# HUGGINGFACE_API_TOKEN=your_huggingface_token_here
# OPENAI_API_KEY=your_openai_api_key_here
# ANTHROPIC_API_KEY=your_anthropic_api_key_here
"""

    project_dir = Path(project_path)
    env_file = project_dir / ".env"
    env_template_file = project_dir / ".env.template"

    # Create .env.template (always)
    env_template_file.write_text(env_content)
    print(f"Created: {env_template_file}")

    # Create .env only if it doesn't exist
    if not env_file.exists():
        env_file.write_text(env_content)
        print(f"Created: {env_file}")
    else:
        print(f"Skipped (already exists): {env_file}")


if __name__ == "__main__":
    print("Scanning projects for environment variable usage...")
    print("=" * 60)

    projects = find_projects_needing_env()

    if not projects:
        print("No projects found that need environment variables.")
        exit(0)

    print(f"Found {len(projects)} projects that need environment variables:")
    print()

    for project in projects:
        print(f"📁 {project['project']}")
        print(f"   Files: {', '.join(project['files'])}")
        print()

    response = input("Create .env files for these projects? (y/n): ").lower()

    if response == 'y':
        print("\nCreating .env files...")
        print("=" * 40)

        for project in projects:
            print(f"\n📁 {project['project']}:")
            create_env_for_project(project['path'])

        print("\n" + "=" * 60)
        print("✅ Setup complete!")
        print("\nIMPORTANT: Remember to:")
        print("1. Fill in your actual API keys in the .env files")
        print("2. Never commit .env files to version control")
        print("3. Use .env.template as a reference for required variables")
    else:
        print("Setup cancelled.")
