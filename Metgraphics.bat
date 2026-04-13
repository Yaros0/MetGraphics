@echo on
set venv_dir=venv
chcp 65001 >nul

if not exist %venv_dir% (
    python -m venv %venv_dir%
)

echo Скачиваем необходимые файлы...
call %venv_dir%\Scripts\activate.bat
python -m pip install --upgrade pip
pip install matplotlib numpy tkinter

echo Запускаем MetGraphics...
python MetGraphics.py

pause
