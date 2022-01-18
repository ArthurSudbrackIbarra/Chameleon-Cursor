@echo off

python %~dp0main.py

set exit_code=%errorlevel%

if %exit_code%==1 (
    echo:
    echo You're missing required modules, they'll be installed now:
    echo:
    pip install -r requirements.txt && python %~dp0main.py
)
