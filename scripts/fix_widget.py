import json

# Path to your notebook
notebook_path = 'projects/11_bert_pretraining/11_bert_pretraining.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Fix or remove 'metadata.widgets'
if 'widgets' in notebook.get('metadata', {}):
    notebook['metadata']['widgets']['state'] = notebook['metadata']['widgets'].get(
        'state', {})
else:
    notebook['metadata']['widgets'] = {'state': {}}

# Save the fixed notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=4)

print("Notebook fixed successfully!")
