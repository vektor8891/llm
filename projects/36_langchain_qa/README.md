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

# deactivate environment
conda deactivate
```
