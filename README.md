## Notebook for Local LLMs
The goal of this project is to allow users to easily load their locally hosted language models in a notebook for testing with Langchain. 
There are currently three notebooks available. Two of them use an API to create a custom Langchain LLM wrapper—one for oobabooga's text generation web UI and the other for KoboldAI. The third notebook loads the models without an API by leveraging the oobabooga's text-generation-webui virtual environment and modules for model loading.

You will end up with an instance of the Custom LLM Wrapper that can be used to generate text: 

```llm("prompt goes here")```

You can use this instead of the OpenAI LLM class that you see used in most of the guides and documentation.

## Getting Started
Please follow the setup instructions for the APIs provided in their respective repositories. Just update the url variable with your api url then run the cells to create an instance of the Custom LLM Wrapper. 

### Roadmap
Using the API is now my preferred method for loading the models. I plan on improving the API classes/notebooks, but for now, they work quite well. I'm leaving the non-api stuff up for now, but I won't be actively maintaining them in the future, so things might break.

### Non-API Notebook Instructions:
1. Activate your Python or Conda environment.
2. Install Jupyter Notebook by running `pip install jupyter` in your preferred command prompt or terminal.
3. Restart your command prompt or terminal to ensure that the installation is properly configured.
4. Activate your Python or Conda environment again and run `jupyter notebook` in the command prompt or terminal to launch the Jupyter interface.
5. Navigate to the directory where `Non-API-Notebook.ipynb` is located (ooba users put it in `./text-generation-webui/` and open the notebook in the Jupyter interface.
