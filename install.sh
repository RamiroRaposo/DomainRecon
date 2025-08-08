#!/usr/bin/env bash

set -e

if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "[!] Python not found. Install it before continuing"
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "[+] Creating virtual environment..."
    $PYTHON -m venv .venv
fi

if [ -f requirements.txt ]; then
    echo -e "\n[+] Installing dependencies...\n"
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r requirements.txt -q

else
    echo -e "\n[!] requirements.txt not found"
fi

echo -e "\n[$] Environment ready. To start the program, execute 'run.sh'"
