# Setup using Poetry for Jupyter Notebooks in VS Code

```sh
# navigate to project directory
cd projects/38_react_agent

# regenerate lock file if pyproject.toml was modified
poetry lock

# install dependencies and create virtual environment
# Note: Uses package-mode = false for script-based projects
poetry install 

# install the kernel in Jupyter (important for VS Code notebook usage)
poetry run python -m ipykernel install --user --name=react-agent --display-name="React Agent (Poetry)"

# get the virtual environment path (you'll need this for VS Code)
poetry env info --path
```

## Working with Jupyter Notebooks in VS Code

### Initial Setup

1. **Install VS Code Extensions** (if not already installed):
   - Python extension (ms-python.python)
   - Jupyter extension (ms-toolsai.jupyter)

2. **Open the notebook**: Open `38_react_agent.ipynb` in VS Code

3. **Select the Poetry kernel**:
   - Click on the kernel selector in the top-right of the notebook
   - Choose "Select Another Kernel..."
   - Select "Python Environments..."
   - Look for "React Agent (Poetry)" OR manually select:
     `/Users/L015680/Library/Caches/pypoetry/virtualenvs/react-agent-474vt4AU-py3.12/bin/python`

4. **Verify the environment**: Run this in the first cell:

   ```python
   import sys
   print(f"Python executable: {sys.executable}")
   print(f"Python version: {sys.version}")
   ```

### Alternative Method - Auto-detect Poetry Environment

VS Code can often auto-detect Poetry environments:

1. **Open VS Code in the project directory**:

   ```sh
   cd projects/38_react_agent
   code .
   ```

2. **Select Python interpreter**:
   - Press `Cmd+Shift+P` (macOS)
   - Type "Python: Select Interpreter"
   - Choose the Poetry virtual environment:
     `/Users/L015680/Library/Caches/pypoetry/virtualenvs/react-agent-474vt4AU-py3.12/bin/python`

3. **Open the notebook**: VS Code should automatically use the selected interpreter

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

## Troubleshooting Poetry + Jupyter + VS Code Issues

If VS Code doesn't show the Poetry kernel:

```sh
# First, make sure the kernel is installed
poetry run python -m ipykernel install --user --name=react-agent --display-name="React Agent (Poetry)"

# Get the virtual environment path
poetry env info --path

# In VS Code: Cmd+Shift+P -> "Python: Select Interpreter" 
# Then manually browse to the path shown above + /bin/python
```

If VS Code shows "Kernel not found" or wrong Python version:

```sh
# Reload VS Code window
# Cmd+Shift+P -> "Developer: Reload Window"

# Or restart VS Code completely
# Make sure you're opening VS Code from the project directory
cd projects/38_react_agent
code .
```

If packages are not found in VS Code notebook:

```sh
# Install packages first
poetry add package-name

# Then in VS Code: restart the kernel
# Click the kernel name in top-right -> "Restart"

# Or reload the window
# Cmd+Shift+P -> "Developer: Reload Window"
```

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
