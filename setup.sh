#!/bin/bash

# Define a cleanup function to exit the virtual environment
cleanup() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo -e "\n\033[1;32m[+] Deactivating virtual environment layers cleanly. Returning to Ubuntu.\033[0m"
        deactivate
    fi
}

# Register the cleanup function to trigger on script exit or user interrupt (Ctrl+C)
trap cleanup EXIT INT TERM

# 1. Verify or install system dependencies silently
if ! command -v python3 &> /dev/null || ! dpkg -s python3-venv &> /dev/null; then
    echo -e "\033[1;33m[~] Provisioning infrastructure dependencies...\033[0m"
    sudo apt update -y && sudo apt install -y python3 python3-pip python3-venv
fi

# 2. Build or activate the isolated virtual environment
if [ ! -d "venv" ]; then
    echo -e "\033[1;36m[+] Allocating isolated Python Virtual Environment (venv)...\033[0m"
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# 3. Launch the game engine directly (Interactive mode restored!)
python3 run_sentry.py
