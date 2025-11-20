@echo off
REM Get configuration values
for /f "delims=" %%i in ('python get_config_value.py tokenizer_model_src') do set TOKENIZER_SRC=%%i
for /f "delims=" %%i in ('python get_config_value.py tokenizer_model_dst') do set TOKENIZER_DST=%%i
for /f "delims=" %%i in ('python get_config_value.py gguf_path') do set GGUF_PATH=%%i

echo Creating merged-model directory...
if not exist "Outputs\merged-model" mkdir "Outputs\merged-model"

echo Copying tokenizer model...
if exist "%TOKENIZER_SRC%" (
    copy /Y "%TOKENIZER_SRC%" "%TOKENIZER_DST%"
) else (
    echo Warning: Tokenizer model not found at %TOKENIZER_SRC%, skipping copy
)

echo Converting to GGUF format...
cd llama.cpp
python convert_hf_to_gguf.py ..\Outputs\merged-model --outfile ..\%GGUF_PATH% --outtype f16
cd ..