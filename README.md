# langchain-ooba
I was able to do a simple test with langchain that uses all the same modules and shares from the text-generation-webui. Uploading my code for documentation and in case anybody else finds it useful. I plan on learning langchain and wanted to have it running locally.

I am using the one click installer version of text-generation-webui on windows with cuda. I used a slightly modified bat file to put me in the conda environment and then ran python main.py --auto-devices --wbits 4 --groupsize 128 --listen --no-stream (i added this bat to the repo)

I have not tested this with regular versions of ooba but in theory it should work the same

# Instructions for one click installer ooba users: 
>1. put langchain.bat and requirements.txt in your obabooga-windows folder

>2. put main.py in the obabooga-windows/text-generation-webui

>3. Run langchain.bat

>4. ????

>5. PROFIT!!!


# jupyter notebook
I just added a jupyter notebook method for easily testing out langchain in one cell to make things easier
>1. activate your mamba miniconda env and pip install jupyter

>2. restart your cmd/terminal and activate the env again and run: jupyter notebook

>3. put Main.ipynb in the obabooga-windows/text-generation-webui folder

>4. Load the notebook. You can input your args as a string in one of the cells
