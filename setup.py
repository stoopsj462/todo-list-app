#!/usr/bin/env python3
"""
Setup script for Modern Todo List App
"""
from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A modern, stylish todo list application with dark/light themes and intuitive interface."

setup(
    name="modern-todo-list",
    version="1.0.0",
    author="Todo List Developer",
    author_email="developer@todolist.com",
    description="A modern, stylish todo list application with dark/light themes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/modern-todo-list",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Scheduling",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
    ],
    python_requires=">=3.8",
    install_requires=[
        # tkinter is included with Python standard library
    ],
    extras_require={
        "build": [
            "pyinstaller>=5.0",
            "setuptools>=65.0",
            "wheel>=0.37.0",
        ],
        "dev": [
            "pip-tools>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "todo-cli=main:main",
            "todo-gui=todo_gui:main",
        ],
        "gui_scripts": [
            "modern-todo=todo_gui:main",
        ],
    },
    py_modules=[
        "main",
        "todo_gui",
        "todo_app", 
        "todo_list",
        "todo_item",
    ],
    include_package_data=True,
    zip_safe=False,
    keywords="todo, task, manager, gui, tkinter, productivity, organizer",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/modern-todo-list/issues",
        "Source": "https://github.com/yourusername/modern-todo-list",
        "Documentation": "https://github.com/yourusername/modern-todo-list/wiki",
    },
)