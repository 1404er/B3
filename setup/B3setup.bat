@ECHO OFF

ECHO:
ECHO B3 Installer
ECHO:
ECHO Required modules will now be installed.

@PAUSE

CD C:\Windows\Temp
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/B3req.txt > B3req.txt

pip install -r B3req.txt

IF EXIST C:\B3\ (
    @RD /S /Q C:\B3\
)
MKDIR C:\B3
CD C:\B3

curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/B3.py > B3.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/main.py > main.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/uninstall.py > uninstall.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/verify.py > verify.py

curl -s https://raw.githubusercontent.com/Dogey11/B3/main/LICENSE > LICENSE.txt

CLS

CHOICE /c ync /n /m "Make executable? (8MB needed) (Y/N): "
IF %ERRORLEVEL% == 1 (
    pip uninstall enum34 -y
    pyinstaller --onefile B3.py
    DEL B3.py
    @RD /S /Q C:\B3\__pycache__
    @RD /S /Q C:\B3\build
    MOVE C:\B3\dist\B3.exe C:\B3\B3.exe
    @RD /S /Q C:\B3\dist
    CLS
)
IF %ERRORLEVEL% == 2 (
    ECHO: 
    ECHO Skipping... 
    ECHO:
)
IF %ERRORLEVEL% == 3 ( EXIT /B )

ECHO:

ECHO Install complete. Running verification test...
ECHO:

verify.py

ECHO:
@PAUSE
EXIT /B