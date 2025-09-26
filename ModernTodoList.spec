# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Modern Todo List App
This file defines how to build the standalone executable.
"""

import os
import sys
from pathlib import Path

# Application name and version
APP_NAME = "ModernTodoList"
VERSION = "1.0.0"

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(SPEC))

# Define the main script
main_script = os.path.join(current_dir, "todo_gui.py")

# Data files to include (if any)
datas = [
    # Include any data files your app needs
    # (os.path.join(current_dir, "assets"), "assets"),
]

# Hidden imports (if needed)
hiddenimports = [
    "tkinter",
    "tkinter.ttk",
    "tkinter.messagebox",
    "tkinter.simpledialog",
]

# Files to exclude from the build
excludes = [
    "matplotlib",
    "numpy",
    "pandas",
    "scipy",
    "PIL",
    "pytest",
    "unittest",
]

# Analysis step
a = Analysis(
    [main_script],
    pathex=[current_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Remove duplicate entries
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Executable configuration
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to False for GUI app
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version=f"version_info.txt",
    icon=None,  # Add icon path here if you have one: "icon.ico"
)

# Optional: Create app bundle for macOS
if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name=f"{APP_NAME}.app",
        icon=None,  # Add icon path here if you have one
        bundle_identifier=f"com.todolist.{APP_NAME.lower()}",
        version=VERSION,
        info_plist={
            'NSHighResolutionCapable': 'True',
            'LSApplicationCategoryType': 'public.app-category.productivity',
            'CFBundleShortVersionString': VERSION,
            'CFBundleVersion': VERSION,
            'NSHumanReadableCopyright': 'Copyright © 2025 Todo List Developer',
        },
    )