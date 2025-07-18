# Setup using Poetry for Jupyter Notebooks

```sh
# navigate to project directory
cd projects/38_react_agent

# regenerate lock file if pyproject.toml was modified
poetry lock

# install dependencies and create virtual environment
# Note: Uses package-mode = false for script-based projects
poetry install 

# activate the poetry environment (Poetry 2.0+)
poetry env activate

# install the kernel in Jupyter (important for notebook usage)
poetry run python -m ipykernel install --user --name=react-agent --display-name="React Agent (Poetry)"

# start Jupyter Lab (recommended) or Jupyter Notebook
poetry run jupyter lab
# OR
poetry run jupyter notebook

# alternatively, run without activating environment
poetry run jupyter lab
```

## Working with Jupyter Notebooks

Once Jupyter is running:

1. **Select the correct kernel**: When opening `38_react_agent.ipynb`, make sure to select the "React Agent (Poetry)" kernel
2. **Verify environment**: Run a cell with `!which python` to ensure you're using Poetry's virtual environment
3. **Install additional packages**: Use `poetry add package-name` in terminal, then restart the kernel

## Package Management

```sh
# add new dependencies
poetry add package-name

# remove dependencies
poetry remove package-name

# update all dependencies
poetry update

# show installed packages
poetry show
```

## Environment Management

```sh
# deactivate environment (if using env activate)
deactivate

# remove the Jupyter kernel (if needed)
jupyter kernelspec uninstall react-agent
```

## Troubleshooting Poetry + Jupyter Issues

If you get "Kernel not found" error in Jupyter:

```sh
# Make sure the kernel is properly installed
poetry run python -m ipykernel install --user --name=react-agent --display-name="React Agent (Poetry)"

# List available kernels
jupyter kernelspec list

# If needed, remove and reinstall kernel
jupyter kernelspec uninstall react-agent
poetry run python -m ipykernel install --user --name=react-agent --display-name="React Agent (Poetry)"
```

If packages are not found in Jupyter notebook:

```sh
# Restart the kernel after installing new packages
# In Jupyter: Kernel -> Restart Kernel

# Or verify the Python path in a notebook cell:
import sys
print(sys.executable)
```

If you get "USER_AGENT environment variable not set" warning:

```sh
# Optional: Set USER_AGENT to identify your requests
export USER_AGENT="react-agent/1.0"
```

If you get "ModuleNotFoundError" when running `python react_agent.py`:

```sh
# Make sure you're using Poetry's environment, not the base environment
# Option 1: Use poetry run (recommended)
poetry run python react_agent.py

# Option 2: Activate the environment first
poetry env activate
which python  # should show Poetry's virtual environment path
python react_agent.py
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
