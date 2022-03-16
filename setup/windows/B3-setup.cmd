@ECHO OFF

SET B3_PRE_PATH = %CD%

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
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/B3.py > B3.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/main.py > main.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/uninstall.py > uninstall.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/verify.py > verify.py
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
IF %B3_EXE% == 2 (
    ECHO: 
    ECHO Skipping... 
    ECHO:
)
IF %B3_EXE% == 3 ( EXIT /B )

REM Make shortcuts

CD %B3_TEMP%
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/setup/windows/B3-shortcut.vbs > B3-shortcut.vbs

CHOICE /c ync /n /m "Make Desktop shortcut? [Y/N]: "

SET B3_CHOICE=%ERRORLEVEL%

IF %B3_EXE% == 1 ( SET B3_TYPE = .exe )
IF %B3_EXE% == 2 ( SET B3_TYPE = .py )

IF %B3_CHOICE% == 1 ( B3-shortcut.vbs %B3_TYPE% 1 )

B3-shortcut.vbs %B3_TYPE% 2

ECHO:
ECHO Install complete. Running verification test...
TIMEOUT /T 5
CLS
ECHO:

verify.py

CD %B3_PRE_PATH%
PAUSE
EXIT /B