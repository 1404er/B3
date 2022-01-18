import os
import shutil
from sys import argv

yn = input(r"Are you sure? This will delete all B3 related files in the C:\b3 directory [y\N] ")
yn = yn.lower()
if yn == "y":
    shutil.rmtree("C:/b3")
elif yn == "n":
    input("Deletion canceled. Press Enter to close. ")
else:
    input("Invalid input. Press Enter to close. ")

if yn == "y":
    os.remove(argv[0])