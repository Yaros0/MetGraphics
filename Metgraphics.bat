@echo off
chcp 65001 >nul	
setlocal

python --version >nul 2>nul
if %errorlevel% neq 0 (
	echo Python не обнаружен, скачайте Python
	pause
)

set venv_dir=venv
if not exist %venv_dir% (
    python -m venv %venv_dir%
)



echo проверяем и скачиваем необходимые файлы...
call %venv_dir%\Scripts\activate.bat
python -m pip install --upgrade pip
pip install matplotlib numpy re

echo Запускаем MetGraphics...
python MetGraphics.py

pause
