


# Notebook for local LLMs

The goal of the project is to let people easily load their local LLMs in a notebook for testing with langchain or other agents. This notebook is a companion to [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) and uses all the same code for loading models. If you are using cpp only you do not need the text-generation-webui code.

## Agent instructed to give the answer as a pirate and search google
![image](https://i.imgur.com/pt4XYcL.png)
Model: llama-30b-sft-oa-alpaca-epoch-2

## Getting Started
These instructions assume you have successfully set up the one-click installer `text-generation-webui` on Windows with CUDA or installed `llama-cpp` and its dependencies.

If you are using `llama-cpp` models only, you do not need to follow the instructions for `text-generation-webui`.

### Jupyter Notebook Usage:
1. Activate your Python or Conda environment.
2. Install Jupyter Notebook by running `pip install jupyter` in your preferred command prompt or terminal.
3. Restart your command prompt or terminal to ensure that the installation is properly configured.
4. Activate your Python or Conda environment again and run `jupyter notebook` in the command prompt or terminal to launch the Jupyter interface.
5. Navigate to the directory where `LLM-Loader.ipynb` is located (ooba users: `./text-generation-webui`) and open the notebook in the Jupyter interface.



## Contributions
Feel free to open issues, submit pull
