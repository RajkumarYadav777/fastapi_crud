#!/bin/bash
set -e

# update system
sudo apt update
# install virtaul env
sudo apt install python3-venv -y
# create virtual env
python3 -m venv venv
# activate
source venv/bin/activate
# upgrade pip
pip install --upgrade pip
# install fastapi and other dependencies
pip install fastapi uvicorn[standard] psycopg2-binary alembic \
pydantic[email] passlib[bcrypt] python-dotenv