#!/bin/bash

python excelplay-circuimstance/excelplay_circuimstance/manage.py makemigrations && \
	python excelplay-circuimstance/excelplay_circuimstance/manage.py makemigrations api && \
	python excelplay-circuimstance/excelplay_circuimstance/manage.py migrate
cd excelplay-circuimstance/excelplay_circuimstance
gunicorn excelplay_circuimstance.wsgi --bind 0.0.0.0:8004

