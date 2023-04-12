# langchain-ooba-4bit-128g
I was able to do a simple test with langchain that uses all the same modules and shares from the text-generation-webui. Uploading my code for documentation and in case anybody else finds it useful. I plan on learning langchain and wanted to have it running locally.

I am using the one click installer version of text-generation-webui on windows with cuda. I used a slightly modified bat file to put me in the conda environment and then ran python main.py --auto-devices --wbits 4 --groupsize 128 --listen --no-stream
