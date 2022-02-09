import os
from os.path import exists
import shutil

print("\nB3 Installer\nV0.6")
print("\nIf you are stuck, view README.md file\n")

# GitHub Copilot is a great thing

input("\nRequired modules will now be installed. Press enter to continue. ")
os.system("pip install -r Required")
os.system("cls")

dir1 = "C:/Program Files/Google/Chrome/Application/chrome.exe"
dir2 = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

if exists(dir1 or dir2):
    pass
else:
    print("\nGoogle Chrome was not found automatically. Please make sure it's installed before continuing\n")
    input("Press enter to continue. ")

print("\nChromedriver will now be installed.")
input("Press Enter to continue. ")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path="NUL")
driver.close()

try:
    os.mkdir("C:/B3")
except FileExistsError:
    shutil.rmtree("C:/B3")
    os.mkdir("C:/B3")

cwd = os.getcwd()
shutil.move(cwd + r"/main.py", r"C:/b3/main.py")
shutil.move(cwd + r"/verify.py", r"C:/b3/verify.py")
shutil.move(cwd + r"/b3.py", r"C:/b3/b3.py")

os.system("cls")

print('You must now verify that the install went correct.')
print(r"To do this, go to C:\b3\verify.py and double click to run it.")
print("IF PROMPTED, ENTER BESTBUY CONFIRMATION EMAIL/TEXT")
input("Press Enter to close. ")
