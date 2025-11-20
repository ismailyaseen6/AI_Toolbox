@echo off
echo ========================================
echo Ollama Cleanup - Stop and Delete All Models
echo ========================================
echo.

echo Stopping Ollama service...
taskkill /F /IM ollama.exe 2>nul
if %errorlevel% equ 0 (
    echo Ollama stopped successfully.
) else (
    echo Ollama was not running or already stopped.
)
echo.

echo Waiting for Ollama to fully stop...
timeout /t 3 /nobreak >nul
echo.

echo Starting Ollama service...
start /B ollama serve >nul 2>&1
timeout /t 5 /nobreak >nul
echo Ollama service started.
echo.

echo Listing all models...
ollama list
echo.

echo Deleting all models...
for /f "skip=1 tokens=1" %%i in ('ollama list') do (
    if not "%%i"=="NAME" (
        echo Deleting model: %%i
        ollama rm %%i
    )
)
echo.

echo Verifying deletion...
ollama list
echo.

echo ========================================
echo Cleanup complete!
echo ========================================
pause
