#!/bin/bash

function isRoot {
    if [ "$EUID" != 0 ]
    then
        echo "Error: Please run as root."
        exit
    fi
}

function makeDir {
    B3_PATH=$HOME/Dogey11/B3
    [ -d "$B3_PATH" ] && sudo rm -rf $B3_PATH
    sudo mkdir Dogey11
    cd Dogey11
    sudo mkdir B3
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
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/B3req.txt

    pip3 install -r B3req.txt
}

function getFiles {
    wget -q https://raw.githubusercontent.com/Dogey11/B3/main/src/cli
}

echo
echo "B3 Installer"
echo
echo "Required modules will now be installed."

read -p "Press Enter to continue . . . "

isRoot
makeDir
license
installModules
