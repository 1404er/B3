import os
import shutil
from sys import argv

yn = input(r"Are you sure? This will delete all B3 related files in the C:\b3 directory [y\N] ")
yn = yn.lower()
if yn == "y":
    ync = input(r"Delete chromedriver.exe also? [Y\n] ")
    ync = ync.lower()
    os.remove(r"C:\b3\b3.py")
    os.remove(r"C:\b3\main.py")
    os.remove(r"C:\b3\verify.py")
    shutil.rmtree(r"C:\b3\ico")
    if ync == "y":
        os.remove(r"C:\b3\chromedriver.exe")
    else:
        pass
    try:
        os.rmdir(r"C:\b3")
    except OSError:
        pass
    input("B3 has been uninstalled. Press Enter to finish. ")
else:
    input("Deletion canceled. Press Enter to close. ")

if yn == "y":
    os.remove(argv[0])