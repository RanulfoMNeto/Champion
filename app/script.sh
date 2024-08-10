#!/bin/bash

# Use curl to download the HTML page with the specified user agent
curl -o "index.html" https://u.gg/lol/champions/mordekaiser/build

# Run the parser script using the virtual environment's Python
/opt/venv/bin/python parser.py
