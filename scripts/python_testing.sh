#!/bin/sh
echo "Testing python"

export TESTING=1
pytest --cov


# Check the exit status of pytest
pytest_exit_status=$?

# Exit the script with a non-zero status code if pytest failed
if [ $pytest_exit_status -ne 0 ]; then
  echo "Pytest failed. Exiting the script."
  exit 1
fi

# Continue with the rest of the script
echo "Pytest succeeded. Continuing with the script."
export TESTING=0