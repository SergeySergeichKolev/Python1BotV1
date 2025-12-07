#!/usr/bin/env bash
# build.sh

# Устанавливаем Python 3.12 если не установлен
if ! command -v python3.12 &> /dev/null; then
    apt-get update && apt-get install -y python3.12 python3.12-venv
fi

# Устанавливаем зависимости
pip install -r requirements.txt