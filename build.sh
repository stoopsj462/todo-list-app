#!/bin/bash
# Modern Todo List App - Build Script for Unix/Linux/macOS
# This script builds a standalone executable that users can run without Python

echo "========================================"
echo "  Modern Todo List App Builder"
echo "========================================"
echo

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

echo "[1/5] Setting up build environment..."
# Create virtual environment if it doesn't exist
if [ ! -d "build_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv build_env
fi

# Activate virtual environment
source build_env/bin/activate

echo "[2/5] Installing dependencies..."
# Upgrade pip and install requirements
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "[3/5] Cleaning previous builds..."
# Remove old build directories
rm -rf build dist __pycache__ *.pyc

echo "[4/5] Building standalone executable..."
# Build using PyInstaller with our spec file
pyinstaller --clean --noconfirm ModernTodoList.spec

echo "[5/5] Finalizing build..."
# Check if build was successful
if [ -f "dist/ModernTodoList" ] || [ -f "dist/ModernTodoList.app/Contents/MacOS/ModernTodoList" ]; then
    echo
    echo "========================================"
    echo "  BUILD SUCCESSFUL!"
    echo "========================================"
    echo
    echo "Your standalone application is ready:"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "  Location: dist/ModernTodoList.app"
        echo "  Size: $(du -h dist/ModernTodoList.app | cut -f1)"
    else
        echo "  Location: dist/ModernTodoList"
        echo "  Size: $(du -h dist/ModernTodoList | cut -f1)"
    fi
    
    echo
    echo "You can now distribute this application to users."
    echo "They can run it without installing Python!"
    echo
    
    # Create a simple installer folder
    mkdir -p installer
    if [[ "$OSTYPE" == "darwin"* ]]; then
        cp -r dist/ModernTodoList.app installer/
    else
        cp dist/ModernTodoList installer/
    fi
    cp README.md installer/ 2>/dev/null || true
    
    echo "Created installer folder with the executable."
    echo
else
    echo
    echo "========================================"
    echo "  BUILD FAILED!"
    echo "========================================"
    echo
    echo "Check the output above for errors."
    echo "Common issues:"
    echo "  - Missing dependencies"
    echo "  - Import errors in the code"
    echo "  - PyInstaller compatibility issues"
    echo
fi

# Deactivate virtual environment
deactivate

echo "Press Enter to exit..."
read