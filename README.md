


# Notebook for local LLMs

The goal of the project is to let people easily load their local LLMs in a notebook for testing with langchain. We have one notebook  that leverages the [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) venv and modules for loading models and a Kobold API version. There is a small section for llama.cpp users to load thier models in the Oobabooga notebook.

## Agent instructed to give the answer as a pirate and search google
![image](https://i.imgur.com/pt4XYcL.png)

Model: llama-30b-sft-oa-alpaca-epoch-2

## Getting Started
These instructions assume you have successfully loaded up local models before in text-gen-webui, llama.cpp or KoboldAI.


### Oooba Jupyter Notebook Usage:
1. Activate your Python or Conda environment.
2. Install Jupyter Notebook by running `pip install jupyter` in your preferred command prompt or terminal.
3. Restart your command prompt or terminal to ensure that the installation is properly configured.
4. Activate your Python or Conda environment again and run `jupyter notebook` in the command prompt or terminal to launch the Jupyter interface.
5. Navigate to the directory where `Alpaca-wikipedia-search.ipynb` is located (ooba users put it in `./text-generation-webui/` and open the notebook in the Jupyter interface.

Koboold users just need to put an api key in a cell and run it. You can even do it on collab.

## Disclaimer
This might not work the same for every model and search query. Prompts may need to be tweaked to get the Agent to follow the instructions correctly. If you know of any instruct prompts that work well with certain models let me know.


## Contributions
Feel free to open issues, submit pull requests etc if you want to join in on this research


