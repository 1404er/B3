import os
import shutil

print("\nB3 Installer\nV0.4")
print("\nIf you are stuck, view README.md file\n")

# GitHub Copilot is a great thing

input("\nRequired modules will now be installed. Press enter to continue. ")
os.system("pip install selenium")
os.system("pip install webdriver-manager")

print("Chromedriver will now be installed.")
input("Press Enter to continue...")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path="NUL")
driver.close()

try:
    os.mkdir("C:/B3")
except FileExistsError:
    pass

mkdirico = "C:/B3/ico"

try:
    os.mkdir(mkdirico)
except FileExistsError:
    pass

cwd = os.getcwd()
shutil.move(cwd + r"\main.py", r"C:\b3\main.py")
shutil.move(cwd + r"\verify.py", r"C:\b3\verify.py")
shutil.move(cwd + r"\b3.py", r"C:\b3\b3.py")
shutil.move(cwd + r"\ico\pyinstallerdefault.ico", r"C:\b3\ico\pyinstallerdefault.ico")

os.system("cls")

print('You must now verify that the install went correct.')
print(r"To do this, go to C:\b3\verify.py and double click to run it.")
print("IF PROMPTED, ENTER BESTBUY CONFIRMATION EMAIL/TEXT")
input("Press Enter to close. ")
