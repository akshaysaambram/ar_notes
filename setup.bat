@echo off

REM Check if pip is installed, and install it if not
where pip >nul 2>nul || (
    echo Installing pip...
    python -m ensurepip --default-pip
)

REM Create virtual environment
python -m venv env

REM Activate virtual environment
call env\Scripts\activate.bat

REM Clone GitHub repository
git clone https://github.com/akshaysaambram/ar_notes

REM Navigate to project directory and install dependencies
cd ar_notes
pip install -r requirements.txt

REM Run Django migrations
python manage.py makemigrations
python manage.py migrate

REM Start the development server
python manage.py runserver
