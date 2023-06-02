#!/bin/sh

VENV_DIR=".venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    
    # Create a virtual environment using the desired Python version
    python3 -m venv $VENV_DIR
    
    echo "Virtual environment created at $VENV_DIR"
    source .venv/bin/activate
    echo "Installing from requirements.txt"
    python -m pip install -r requirements.txt
else
    echo "Python virtual environment already exists at $VENV_DIR"
    echo "Freezing requirements"
    pip freeze > requirements.txt
fi
