@echo off

cd /d %~dp0
color a

python -m pip install -r requirements.txt
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
pyinstaller -v>NUL
if errorlevel 1 goto errorNoPyInstaller
cls
pyinstaller --clean --onefile --key dang123 main.py
rmdir /s /q build
del /f /q *.spec
pause
exit

:errorNoPython
echo Python is not installed on your system or not added to path!!!
pause
exit

:errorNoPip
echo Pip is not installed on your system or not added to path!!!
pause
exit

:errorNoPyInstaller
echo Pyinstaller is not installed on your system or not added to path!!!
pause
exit