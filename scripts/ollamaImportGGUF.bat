@echo off
REM Batch file to import GGUF model into Ollama

echo ============================================
echo Ollama GGUF Model Import Script
echo ============================================
echo.

REM Set the GGUF file path
set "GGUF_FILE=Outputs\gemma-3-1b-it-yaseen.gguf"

REM Set the model name in Ollama
set "MODEL_NAME=gemma-3-1b-it-yaseen"

REM Check if GGUF file exists
if not exist "%GGUF_FILE%" (
    echo ERROR: GGUF file not found at %GGUF_FILE%
    echo Please ensure the file exists before running this script.
    pause
    exit /b 1
)

echo GGUF File: %GGUF_FILE%
echo Model Name: %MODEL_NAME%
echo.

REM Check if Ollama is installed
where ollama >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Ollama is not installed or not in PATH
    echo Please install Ollama from https://ollama.ai
    pause
    exit /b 1
)

echo Creating Modelfile...
echo.

REM Create a temporary Modelfile
(
echo FROM %GGUF_FILE%
) > Modelfile.temp

REM Import the model into Ollama
echo Importing model into Ollama...
echo Running: ollama create %MODEL_NAME% -f Modelfile.temp
echo.

ollama create %MODEL_NAME% -f Modelfile.temp

if %errorlevel% equ 0 (
    echo.
    echo ============================================
    echo SUCCESS: Model imported successfully!
    echo ============================================
    echo.
    echo Model name: %MODEL_NAME%
    echo.
    echo You can now run the model with:
    echo   ollama run %MODEL_NAME%
    echo.
    echo To list all models:
    echo   ollama list
    echo.
) else (
    echo.
    echo ============================================
    echo ERROR: Failed to import model
    echo ============================================
    echo.
)

REM Clean up temporary Modelfile
if exist Modelfile.temp del Modelfile.temp

pause
