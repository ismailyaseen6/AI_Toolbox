@echo off
echo Fine-tuning the model...
python scripts\fineTune_HuggingFaceModel.py
if %errorlevel% neq 0 (
    echo Error: Fine-tuning failed!
    exit /b %errorlevel%
)
echo Model fine-tuning completed successfully

echo Merging LoRA weights with base model...
python scripts\modelToGGUF_part1.py
if %errorlevel% neq 0 (
    echo Error: Model merging failed!
    exit /b %errorlevel%
)
echo Model merging completed successfully

echo Converting to GGUF format...
call scripts\modelToGGUF_part2.bat
if %errorlevel% neq 0 (
    echo Error: GGUF conversion failed!
    exit /b %errorlevel%
)
echo GGUF conversion completed successfully

echo Importing GGUF model into Ollama...
call scripts\ollamaImportGGUF.bat
if %errorlevel% neq 0 (
    echo Error: Ollama import failed!
    exit /b %errorlevel%
)
echo Ollama import completed successfully

echo All steps completed! Check the Outputs folder for results.