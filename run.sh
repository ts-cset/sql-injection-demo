#!/bin/sh

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=injectiondemo
export FLASK_ENV=development
psql postgres -c "CREATE DATABASE injectiondemo"
flask init-db
flask run

