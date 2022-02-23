@ECHO OFF

ECHO:
ECHO B3 v0.7 Installer
ECHO (Installer v0.1)
ECHO:
ECHO Required modules will now be installed.

@PAUSE

if exist C:\B3\ (
    @RD /S /Q C:\B3\
)
mkdir C:\B3
cd C:\B3

curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/B3.py > B3.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/main.py > main.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/uninstall.py > uninstall.py
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/src/verify.py > verify.py

cd C:\Windows\Temp
curl -s https://raw.githubusercontent.com/Dogey11/B3/main/Required > B3req.txt

pip install -r B3req.txt

cls
ECHO Install complete. You may now close this window.
@PAUSE
