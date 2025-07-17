# Setup

## Option 1: Traditional Conda + pip

```sh
# create conda environment
cd projects/37_langchain_rag
conda create -n langchain_rag python=3.10 -y
conda info --envs

# activate environment
conda activate langchain_rag
pip install -r requirements.txt

# check installed packages
pip list
pip list | grep -E "(langchain|gradio|ibm-watsonx|chromadb)"
pip freeze > requirements.txt

# upgrade langchain imports (optional)
pip install langchain-cli
langchain-cli migrate --diff .  # preview changes
langchain-cli migrate .         # apply changes

# run application
python qabot.py

# deactivate environment
conda deactivate
```

## Option 2: Poetry (Modern Python Dependency Management)

```sh
# navigate to project directory
cd projects/37_langchain_rag

# regenerate lock file if pyproject.toml was modified
poetry lock

# install dependencies and create virtual environment
# Note: Uses package-mode = false for script-based projects
poetry install 

# activate the poetry environment (Poetry 2.0+)
poetry env activate

# or run without activating the environment (recommended)
poetry run python qabot.py

# add new dependencies
poetry add package-name

# remove dependencies
poetry remove package-name

# deactivate environment (if using env activate)
deactivate

# OR exit poetry shell (if using legacy shell command)
# exit
```

### Troubleshooting Poetry Issues

If you get "USER_AGENT environment variable not set" warning:

```sh
# Optional: Set USER_AGENT to identify your requests
export USER_AGENT="my-app/1.0"
# Or add to your shell profile (.bashrc, .zshrc, etc.)
echo 'export USER_AGENT="my-app/1.0"' >> ~/.bashrc
```

If you get "cannot import name 'TextFileLoader'" error:

```sh
# This is fixed by using TextLoader instead of TextFileLoader
# The code has been updated to use the correct import
```

If you get "pymupdf package not found" error:

```sh
# This dependency has been added to pyproject.toml
# Run poetry lock and poetry install to install it
poetry lock
poetry install
```

If you get "ModuleNotFoundError" when running `python qabot.py`:

```sh
# Make sure you're using Poetry's environment, not the base environment
# Option 1: Use poetry run (recommended)
poetry run python qabot.py

# Option 2: Activate the environment first
poetry env activate
which python  # should show Poetry's virtual environment path
python qabot.py
```

If you encounter "shell command is not available" error (Poetry 2.0+):

```sh
# Use the new env activate command instead
poetry env activate

# Or install the shell plugin for backward compatibility
poetry self add poetry-plugin-shell
poetry shell
```

If you encounter errors about the current project not being installable:

```sh
# Install dependencies without installing the current project as a package
poetry install --no-root
```

If you get "pyproject.toml changed significantly" error:

```sh
# Regenerate the lock file to match current dependencies
poetry lock
# Then install
poetry install
```

## Poetry Benefits

- **Lock File**: `poetry.lock` ensures reproducible builds with exact dependency versions
- **Automatic Virtual Environment**: Poetry manages virtual environments automatically
- **Dependency Resolution**: Better conflict resolution compared to pip
- **Modern Configuration**: Uses `pyproject.toml` standard
- **Publishing**: Easy package building and publishing to PyPI
