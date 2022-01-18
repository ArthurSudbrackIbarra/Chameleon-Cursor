@echo off

python %~dp0.program-files/main.py

set exit_code=%errorlevel%

if %exit_code%==1 (
    echo:
    echo You're missing required modules, they'll be installed now:
    echo:
    pip install -r %~dp0.program-files/requirements.txt && %~dp0.program-files/main.py
)
