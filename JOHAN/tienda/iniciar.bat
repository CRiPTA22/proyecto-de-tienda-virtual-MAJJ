@echo off
cd /d "%~dp0"
pip install django
start http://localhost:8000/login/
python manage.py runserver
pause
