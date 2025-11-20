@echo off
if not exist "Outputs\merged-model" mkdir "Outputs\merged-model"
copy /Y "Outputs\gemma-3-1b-it\tokenizer.model" "Outputs\merged-model\tokenizer.model"
cd llama.cpp
python convert_hf_to_gguf.py ..\Outputs\merged-model --outfile ..\Outputs\gemma-3-1b-it-yaseen.gguf --outtype f16
cd ..