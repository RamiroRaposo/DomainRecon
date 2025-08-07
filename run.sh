#!/usr/bin/env bash
set -e

if [ ! -d ".venv" ]; then
    echo "[!] Virtual environment not found. Run ./setup.sh first."
    exit 1
fi

.venv/bin/python main.py
