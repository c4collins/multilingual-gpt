#!/bin/sh

run_script_py(){
    script_name="$1.py"
    echo "Running $script_name"
    activate_venv
    if python ./scripts/"$script_name"; then
        echo "$script_name succeeded"
        echo ""
    else
        echo "$script_name failed. Exiting the script."
        exit 1
    fi
}

run_script() {
    script_name="$1.${2:-sh}"
    echo "Running $script_name"
    if ./scripts/"$script_name"; then
        echo "$script_name succeeded"
        echo ""
    else
        echo "$script_name failed. Exiting the script."
        exit 1
    fi
}

echo "Process: START"
. ./scripts/fn_activate_venv.sh

echo "Running config scripts"
SUPPORTED_LANGUAGES="en $1" # es jp de ru po
export SUPPORTED_LANGUAGES=$SUPPORTED_LANGUAGES
echo $SUPPORTED_LANGUAGES

run_script verify_env
run_script generate_env_template
run_script upsert_venv
run_script create_translation_files
run_script_py get_script_translations
run_script convert_translations_to_machine_code
run_script python_formatting
run_script python_testing

echo "Process: OK/DONE"
