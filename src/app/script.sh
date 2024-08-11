#!/bin/bash

# Define variables
URL="https://u.gg/lol/champions"
OUTPUT_FILE="champions.html"
PYTHON_PATH="/opt/venv/bin/python"
SCRIPT="main.py"

# Use curl to download the HTML page
curl -o "$OUTPUT_FILE" "$URL"

# Run the parser script using the virtual environment's Python
"$PYTHON_PATH" "$SCRIPT"
