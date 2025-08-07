#!/usr/bin/env bash

set -e

if [ ! -d ".env" ]; then
    echo -e "\n[+] Creating virtual enviroment..."
    python -m venv .venv
fi

echo -e "\n[+] Activating virtual environment..."
source .venv/bin/activate

if [ -f requirements.txt ]; then
    echo -e "\n[+] Installing dependencies...\n"
    python pip install --upgrade pip
    python pip install -r requirements.txt -q
else
    echo -e "\n[!] requirements.txt not found"
fi

echo -e "\n[$] Environment ready. To start the program, execute 'run.sh'"