#!/bin/sh

run_processing() {
    echo "Running _processing.sh"
    if ./scripts/_processing.sh $1; then
        echo "_processing.sh succeeded"
        echo ""
    else
        echo "_processing.sh failed. Exiting the script."
        exit 1
    fi
}

check_git_status(){
    output=$(git diff-index --quiet HEAD --)
    exit_status=$?

    # Check if there are uncommitted changes or files
    if [ $exit_status -ne 0 ]; then
        echo "Warning: There are uncommitted changes or files."
        if [ $PRODUCTION ]; then
            exit 1
        fi
    fi
}

export_from_env(){
    var_value=$(grep "^$1=" .env | cut -d '=' -f2-)
    echo "Exporting \$$1=$var_value"
    export $1="$var_value"
}

echo "Run: PREPARING"
export_from_env VENV_DIR

echo "Run: START"
cat README.md

echo "Run: PROCESSING"
lang=${1:-en}
run_processing "$lang"
check_git_status

echo "Run: APPLICATION"
. ./scripts/fn_activate_venv.sh
activate_venv
python -m src.run $1

echo "Run: END/DONE"
