@echo off
echo Installing main requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 exit /b %errorlevel%
echo Main requirements installed successfully

echo Checking llama.cpp repository...
if exist llama.cpp (
    echo llama.cpp directory already exists, skipping clone
) else (
    echo Cloning llama.cpp repository...
    git clone https://github.com/ggerganov/llama.cpp
    if %errorlevel% neq 0 exit /b %errorlevel%
    echo llama.cpp cloned successfully
)

echo Installing llama.cpp requirements...
cd llama.cpp
pip install -r requirements.txt
if %errorlevel% neq 0 exit /b %errorlevel%
cd ..
echo llama.cpp requirements installed successfully

echo Downloading base model from HuggingFace...
python scripts\download_HuggingFaceBaseModel.py
if %errorlevel% neq 0 exit /b %errorlevel%
echo Base model downloaded successfully