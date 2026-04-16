@echo on
setlocal

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не найден. Начинам загрузку и установку...
    
    set "py_url=https://python.org"
    set "py_exe=%TEMP%\python_installer.exe"

    curl -L %py_url% -o %py_exe%

    echo Установка Python, это займет время...
    start /wait %py_exe% /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
    
    del %py_exe%
    
    echo Python успешно установлен! Пожалуйста, перезапустите этот файл.
    pause
    exit
)

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
