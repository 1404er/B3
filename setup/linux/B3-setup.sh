#!/bin/bash

B3_PRE_PATH=$PWD

function makeDir {
    B3_PATH=$HOME/.Dogey11/B3
    [ -d "$B3_PATH" ] && rm -rf $B3_PATH
    mkdir .Dogey11
    cd .Dogey11
    mkdir B3
    cd B3
}

function license {
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/LICENSE
    clear
    cat LICENSE
    echo
    read -r -p "Do you agree to the terms of the license? [Y/N] " YN
    if [ "$YN" != "y" ] && [ "$YN" != "Y" ]
    then
        echo
        echo "Exiting . . ."
        exit
    fi
}

function installModules {
    cd /var/tmp
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/setup/linux/requirements.txt

    pip3 install -r requirements.txt
}

function getFiles {
    cd $B3_PATH

    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/B3.py
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/main.py
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/uninstall.py
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/src/cli/verify.py
}

echo
echo "B3 Installer"
echo
echo "Required modules will now be installed."

read -p "Press Enter to continue . . . "

makeDir
license
installModules
getFiles

echo
echo "Install complete. Verification test will now run."
read -p "Press Enter to continue . . . "
clear
echo

python3 verify.py

cd $B3_PRE_PATH
read -p "Press Enter to close . . . "
exit