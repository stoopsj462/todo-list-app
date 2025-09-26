@echo off
REM Modern Todo List App - Build Script for Windows
REM This script builds a standalone executable that users can run without Python

echo ========================================
echo   Modern Todo List App Builder
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo [1/5] Setting up build environment...
REM Create virtual environment if it doesn't exist
if not exist "build_env" (
    echo Creating virtual environment...
    python -m venv build_env
)

REM Activate virtual environment
call build_env\Scripts\activate.bat

echo [2/5] Installing dependencies...
REM Upgrade pip and install requirements
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo [3/5] Cleaning previous builds...
REM Remove old build directories
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"

echo [4/5] Building standalone executable...
REM Build using PyInstaller with our spec file
pyinstaller --clean --noconfirm ModernTodoList.spec

echo [5/5] Finalizing build...
REM Check if build was successful
if exist "dist\ModernTodoList.exe" (
    echo.
    echo ========================================
    echo   BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Your standalone application is ready:
    echo   Location: dist\ModernTodoList.exe
    echo   Size: 
    dir "dist\ModernTodoList.exe" | find "ModernTodoList.exe"
    echo.
    echo You can now distribute this .exe file to users.
    echo They can run it without installing Python!
    echo.
    
    REM Create a simple installer folder
    if not exist "installer" mkdir "installer"
    copy "dist\ModernTodoList.exe" "installer\"
    copy "README.md" "installer\" >nul 2>&1
    
    echo Created installer folder with the executable.
    echo.
) else (
    echo.
    echo ========================================
    echo   BUILD FAILED!
    echo ========================================
    echo.
    echo Check the output above for errors.
    echo Common issues:
    echo   - Missing dependencies
    echo   - Import errors in the code
    echo   - PyInstaller compatibility issues
    echo.
)

REM Deactivate virtual environment
deactivate

echo Press any key to exit...
pause >nul