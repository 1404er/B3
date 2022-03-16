import os
from shutil import rmtree as rm
from sys import platform as p
from time import sleep

path = None

if p == "linux" or p == "linux2":
    path = os.path.expanduser("~") + "/.Dogey11/B3"
elif p == "win32":
    path = os.getenv("LOCALAPPDATA") + r"\Dogey11\B3"
else:
    print("\nError: Unsupported platform.\n")
    exit(1)

yn = input(fr"Are you sure? This will delete all files in the {path} directory [y\N] ")
yn = yn.lower()

if yn == "y":
    try:
        rm(path)
    except Exception as e:
        print(f"\nError: Could not delete {path}:\n{e}\n")
        print("\nClosing . . .\n")
        sleep(10)
        exit(1)
elif yn == "n":
    input("Deletion canceled. Press Enter to close. ")
else:
    input("Invalid input. Press Enter to close. ")
