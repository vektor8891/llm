"""
This script processes all Jupyter Notebook files (.ipynb) within the specified directory 
and its subdirectories, removing the 'widgets' entry from the 'metadata' section if it exists.

Steps performed by the script:
1. Searches for all .ipynb files in the 'projects/11_bert_pretraining/' directory and its subdirectories.
2. Opens each notebook file and loads its content as JSON.
3. Checks if the 'metadata.widgets' key exists in the notebook.
4. If the key exists, it is removed from the notebook's metadata.
5. Saves the modified notebook back to its original file path with proper formatting.
6. Prints a success message for each processed notebook.

Dependencies:
- json: For parsing and manipulating JSON data.
- glob: For finding files matching a specified pattern.

Usage:
Run the script to clean up 'metadata.widgets' from all notebooks in the specified directory.

Example:
    python3 scripts/fix_widget.py
"""
import json
import glob

# Get all .ipynb files in the directory and subdirectories
notebook_paths = glob.glob(
    'projects/11_bert_pretraining/**/*.ipynb', recursive=True)

for notebook_path in notebook_paths:
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Fix or remove 'metadata.widgets'
    if 'widgets' in notebook.get('metadata', {}):
        del notebook['metadata']['widgets']

    # Save the fixed notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=4)

    print(f"Notebook {notebook_path} fixed successfully!")
