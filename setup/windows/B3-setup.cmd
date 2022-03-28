@ECHO OFF


ECHO:
ECHO B3 Installer
ECHO:
ECHO Required modules will now be installed.

PAUSE

REM Paths
SET B3_PATH=%LOCALAPPDATA%\Dogey11\B3
SET B3_PATH_ALT=%LOCALAPPDATA%\Dogey11
SET B3_TEMP=C:\Windows\Temp

IF EXIST %B3_PATH% (
    RD /S /Q %B3_PATH%
    CD %B3_PATH_ALT%
    MKDIR B3
) ELSE IF EXIST %B3_PATH_ALT% (
    CD %B3_PATH_ALT%
    MKDIR B3
) ELSE (
    CD %LOCALAPPDATA%
    MKDIR Dogey11
    CD Dogey11
    MKDIR B3
)
CD B3

REM Output license
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/LICENSE > LICENSE.txt
CLS
type LICENSE.txt

ECHO:

CHOICE /c ync /n /m "Do you agree to the terms of the license? [Y/N]: "
IF %ERRORLEVEL% == 1 (
    CLS 
)
IF %ERRORLEVEL% == 2 (
    DEL LICENSE.txt
    ECHO: 
    ECHO Exiting . . .
    EXIT /B
)
IF %ERRORLEVEL% == 3 ( EXIT /B )

REM Install modules
CD %B3_TEMP%
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/setup/windows/B3-Req-win32 > B3req.txt
pip install -r B3req.txt

REM Get files
CD %B3_PATH%
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/B3.py > B3.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/main.py > main.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/uninstall.py > uninstall.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/verify.py > verify.py
CLS

REM Make executable
CHOICE /c ync /n /m "Make executable? (8MB needed) [Y/N]: "
SET B3_EXE=%ERRORLEVEL%
IF %B3_EXE% == 1 (
    pip uninstall enum34 -y
    pip install pyinstaller==4.10
    pyinstaller --onefile main.py
    DEL main.py
    RD /S /Q __pycache__
    RD /S /Q build
    MOVE dist\main.exe B3.exe
    RD /S /Q dist
    MOVE main.spec B3.spec
    MOVE B3.py B3.dg11
    CLS
)
IF %B3_EXE% == 2 ( ECHO: )
IF %B3_EXE% == 3 ( EXIT /B )

REM Make shortcuts

CD %B3_TEMP%
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/setup/windows/B3-shortcut.vbs > B3-shortcut.vbs

IF %B3_EXE% == 1 (
    B3-shortcut.vbs .exe 1
    B3-shortcut.vbs .exe 2
) ELSE (
    B3-shortcut.vbs .py 1
    B3-shortcut.vbs .py 2
)

CD %B3_PATH%

ECHO Install complete. Running verification test...
TIMEOUT 5
CLS
ECHO:

verify.py

PAUSE
EXIT /B