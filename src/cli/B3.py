import os
from sys import platform as p

if p == "linux" or p == "linux2":
    B3_Path = os.path.expanduser("~") + "/Dogey11/B3"
    os.chdir(B3_Path)
    os.system("python3 main.py")
elif p == "win32":
    B3_Path = os.getenv("LOCALAPPDATA") + r"Dogey11\B3"
    os.chdir(B3_Path)
    os.system("main.py")