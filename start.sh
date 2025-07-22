#!/bin/bash
set -e

# activate virtual environment
source venv/bin/activate

# run the fastapi server

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload