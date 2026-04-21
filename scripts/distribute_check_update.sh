#!/bin/bash

# Path to the source file (relative to the project root)
SOURCE_FILE="scripts/check_update.py"

# Check if the source file exists
if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "Error: File $SOURCE_FILE not found."
    exit 1
fi

# Find all skill directories in .agents/skills/
# and copy the file into their respective scripts/ subdirectories
for skill_dir in .agents/skills/*/; do
    if [[ -d "$skill_dir" ]]; then
        target_scripts_dir="${skill_dir}scripts"

        # Create the scripts directory if it doesn't exist
        mkdir -p "$target_scripts_dir"

        # Copy the file
        cp "$SOURCE_FILE" "$target_scripts_dir/"

        echo "Copied to: $target_scripts_dir"
    fi
done

echo "Distribution complete."
