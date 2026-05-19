#!/bin/bash
set -e

echo -e "\033[1;36m[+] Starting Shadow Sentry Automated Environment Setup...\033[0m"

# 1. Install system dependencies
echo -e "\033[1;33m[~] Installing system dependencies (Python3 & Venv)...\033[0m"
sudo apt update -y
sudo apt install -y python3 python3-pip python3-venv

# 2. Deploy Python Virtual Environment 
echo -e "\033[1;33m[~] Allocating isolated Python Virtual Environment (venv)...\033[0m"
python3 -m venv venv

# 3. Activate Virtual Environment and install packages
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo -e "\033[1;32m[+] Installing module dependencies via Pip inside venv...\033[0m"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo -e "\033[1;31m[-] Error: requirements.txt not found!\033[0m"
    exit 1
fi

echo -e "\033[1;32m[+] ENVIRONMENT SECURED. Run 'source venv/bin/activate && python run_sentry.py' to launch.\033[0m"
