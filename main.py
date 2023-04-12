import os
import re
import sys
import time
from pathlib import Path
import modules.extensions as extensions_module
from modules import api, chat, shared, training, ui
from modules.html_generator import chat_html_wrapper
from modules.LoRA import add_lora_to_model
from modules.models import load_model, load_soft_prompt
from modules.text_generation import generate_reply, stop_everything_event
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig, pipeline
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

import torch
torch.cuda.set_device(0)
# Loading custom settings
settings_file = None
if shared.args.settings is not None and Path(shared.args.settings).exists():
    settings_file = Path(shared.args.settings)
elif Path('settings.json').exists():
    settings_file = Path('settings.json')
if settings_file is not None:
    print(f"Loading settings from {settings_file}...")
    new_settings = json.loads(open(settings_file, 'r').read())
    for item in new_settings:
        shared.settings[item] = new_settings[item]

shared.settings['seed'] = -1


def get_available_models():
    if shared.args.flexgen:
        return sorted([re.sub('-np$', '', item.name) for item in list(Path(f'{shared.args.model_dir}/').glob('*')) if item.name.endswith('-np')], key=str.lower)
    else:
        return sorted([re.sub('.pth$', '', item.name) for item in list(Path(f'{shared.args.model_dir}/').glob('*')) if not item.name.endswith(('.txt', '-np', '.pt', '.json'))], key=str.lower)

available_models = get_available_models()

if shared.args.model is not None:
    shared.model_name = shared.args.model
else:
    if len(available_models) == 0:
        print('No models are available! Please download at least one.')
        sys.exit(0)
    elif len(available_models) == 1:
        i = 0
    else:
        print('The following models are available:\n')
        for i, model in enumerate(available_models):
            print(f'{i+1}. {model}')
        print(f'\nWhich one do you want to load? 1-{len(available_models)}\n')
        i = int(input()) - 1
        print()
    shared.model_name = available_models[i]
shared.model, shared.tokenizer = load_model(shared.model_name)
if shared.args.lora:
    add_lora_to_model(shared.args.lora)





tokenizer = shared.tokenizer

base_model = shared.model

pipe = pipeline(
    "text-generation",
    model=base_model, 
    tokenizer=tokenizer,
    device=0,  # Set the device to use CUDA
    max_length=256,
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.2
)

local_llm = HuggingFacePipeline(pipeline=pipe)

template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction: 
{instruction}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["instruction"])
llm_chain = LLMChain(prompt=prompt,
                     llm=local_llm
                     )

question = "What is the capital of England?"

print(llm_chain.run(question))


template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction: 
{instruction}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["instruction"])
