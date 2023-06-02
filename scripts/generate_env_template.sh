#!/bin/sh

# Source file
source_file=".env"

# Destination file
destination_file=".env.template"

# Delete existing contents of destination file
> "$destination_file"

# Read the source file line by line
while IFS= read -r line || [ -n "$line" ]; do
  # Check if the line is empty or starts with a #
  if [ -z "$line" ] || echo "$line" | grep -q "^[[:space:]]*#"; then
    # Write a blank line to the destination file
    echo >> "$destination_file"
  else
    # Remove the value by extracting the variable name
    variable=$(echo "$line" | awk -F '=' '{print $1}')
    # Write the variable name to the destination file
    echo "$variable=" >> "$destination_file"
  fi
done < "$source_file"

cat $destination_file | sed 's/^/    /'
echo "Copied $source_file to $destination_file with values removed."