#!/bin/sh

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    python -m venv $VENV_DIR
    echo "Virtual environment created at $VENV_DIR"

    activate_venv

    echo "Updating pip"
    python.exe -m pip install --upgrade pip

    echo "Installing from requirements.txt"
    python -m pip install -r requirements.txt
else
    echo "Activiating existing Python virtual environment at $VENV_DIR"
    activate_venv
    echo "Freezing requirements"
    pip freeze > requirements.txt
fi
