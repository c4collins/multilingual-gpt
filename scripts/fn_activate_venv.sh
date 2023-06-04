#!/bin/sh

echo "activate_env function loaded"

activate_venv(){
    if [ -z "$VIRTUAL_ENV" ]; then
        if [ "$OSTYPE" == "msys" ] || [ "$OSTYPE" == "win32" ]; then
            source "$VENV_DIR/Scripts/activate"
        else
            source "$VENV_DIR/bin/activate"
        fi
    fi
}