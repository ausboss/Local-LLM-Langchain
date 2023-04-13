# Langchain-ooba: Developer Edition

This repository is a companion to [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) and provides a command line and Jupyter Notebook interface for developers to run the text generation code without using Gradio.

## Prerequisites

- Basic knowledge of Python and command line usage
- Familiarity with Python environments

## Dependencies

`main.py` uses the same modules as `text-generation-webui`. Make sure to fulfill all dependencies mentioned in the `text-generation-webui` repository. If any modules are missing just pip install them while the environment is activated.

## Getting Started

These instructions assume you have successfully set up the one-click installer version of `text-generation-webui` on Windows with CUDA.

### Command Line Usage

1. Place `langchain.bat` and `requirements.txt` in your `obabooga-windows` folder.
2. Move `main.py` to the `obabooga-windows/text-generation-webui` folder.
3. Run `langchain.bat`.

### Jupyter Notebook Usage

1. Activate your Mamba Miniconda environment and run `pip install jupyter`.
2. Restart your command prompt or terminal, activate the environment again, and run `jupyter notebook`.
3. Place `Main.ipynb` in the `obabooga-windows/text-generation-webui` folder.
4. Open the notebook in the Jupyter interface. You can provide your arguments as a string in one of the cells.

![Jupyter Notebook Example](https://i.imgur.com/bxo09OAl.png)

## Compatibility with other Ooba versions

This setup should work with regular Ooba versions as well. Just make sure to activate your Python environment and use `main.py` similarly to `server.py` in the original setup.

## Contributions

Feel free to open issues, submit pull requests, or provide feedback to improve this repository and its documentation. Your contributions are appreciated!
