@echo off
REM Quick configuration script for AI_Toolbox
REM This makes it easy to switch between different HuggingFace models

echo ============================================
echo AI_TOOLBOX MODEL CONFIGURATION
echo ============================================
echo.

REM Show current configuration
echo Current Configuration:
python configure.py show
echo.

echo ============================================
echo Would you like to change the model?
echo ============================================
echo.
echo Popular models:
echo   1. google/gemma-3-1b-it
echo   2. microsoft/phi-2
echo   3. mistralai/Mistral-7B-v0.1
echo   4. meta-llama/Llama-2-7b-chat-hf
echo   5. TinyLlama/TinyLlama-1.1B-Chat-v1.0
echo   6. Custom model ID
echo   7. Keep current configuration
echo.

set /p CHOICE="Enter your choice (1-7): "

if "%CHOICE%"=="1" (
    python configure.py set google/gemma-3-1b-it
) else if "%CHOICE%"=="2" (
    python configure.py set microsoft/phi-2
) else if "%CHOICE%"=="3" (
    python configure.py set mistralai/Mistral-7B-v0.1
) else if "%CHOICE%"=="4" (
    python configure.py set meta-llama/Llama-2-7b-chat-hf
) else if "%CHOICE%"=="5" (
    python configure.py set TinyLlama/TinyLlama-1.1B-Chat-v1.0
) else if "%CHOICE%"=="6" (
    echo.
    set /p MODEL_ID="Enter HuggingFace model ID: "
    python configure.py set %MODEL_ID%
) else (
    echo.
    echo Keeping current configuration.
)

echo.
echo ============================================
echo Configuration complete!
echo ============================================
echo.
echo Next steps:
echo   1. Run setup.bat (if not done already)
echo   2. Run Run.bat to start the pipeline
echo.
pause
