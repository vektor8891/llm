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

# install dependencies and create virtual environment
poetry install

# activate the poetry shell
poetry shell

# run application
python qabot.py

# or run without entering the shell
poetry run python qabot.py

# add new dependencies
poetry add package-name

# remove dependencies
poetry remove package-name

# exit poetry shell
exit
```

## Poetry Benefits

- **Lock File**: `poetry.lock` ensures reproducible builds with exact dependency versions
- **Automatic Virtual Environment**: Poetry manages virtual environments automatically
- **Dependency Resolution**: Better conflict resolution compared to pip
- **Modern Configuration**: Uses `pyproject.toml` standard
- **Publishing**: Easy package building and publishing to PyPI
