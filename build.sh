#!/bin/bash
set -e

isort .
black .
mypy .
docker build -t app app/.
docker compose up