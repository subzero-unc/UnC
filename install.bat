@echo off
echo Do you have Python installed? [Y/N]
set /p response=

if /i "%response%"=="N" (
    echo Python is not installed.
    echo Redirecting to the Python download page...
    start https://www.python.org/downloads/
    echo Please install Python, add it to PATH, and rerun this script.
    pause
    exit
)

if /i "%response%"=="Y" (
    echo Checking Python installation...
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Python is not properly installed or not added to PATH.
        echo Redirecting to the Python download page...
        start https://www.python.org/downloads/
        echo Please install Python, add it to PATH, and rerun this script.
        pause
        exit
    ) else (
        echo Python is installed.
    )
)

echo Installing dependencies...
python -m ensurepip --default-pip
python -m pip install --upgrade pip
pip install nuitka
echo Dependencies installed successfully.
pause
