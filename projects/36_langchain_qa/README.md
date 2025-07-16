# Setup

```sh
# create conda environment
cd projects/36_langchain_qa
conda create -n langchain_qa python=3.10 -y
conda info --envs

# activate environment
conda activate langchain_qa
pip install -r requirements.txt

# check installed packagess
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
