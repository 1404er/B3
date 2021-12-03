import os
import shutil

print("\nB3 Installer\nV0.2")
print("\nIf you are stuck, view README.md file\n")
cdd = input("Chromedriver Directory: ")
cdd.lower()
#print(r"Driveletter for install location")
#driveletter = input(r"( Default: C:\ ): ")
installlocation = r"C:\b3\chromedriver.exe"
if "chromedriver.exe" in cdd:
    pass
else:
    cdd = cdd + r"\chromedriver.exe"

mkdir = r"C:\b3"
mkdirico = mkdir + r"\ico"
try:
    os.mkdir(mkdir)
except FileExistsError:
    pass

try:
    os.mkdir(mkdirico)
except FileExistsError:
    pass

try:
    shutil.move(cdd, installlocation)
except OSError as e:
    print('Error trying to move chromedriver.exe. Setup will now cancel')
    raise

cwd = os.getcwd()
shutil.move(cwd + r"\b3\main.py", r"C:\b3\main.py")
shutil.move(cwd + r"\b3\verify.py", r"C:\b3\verify.py")
shutil.move(cwd + r"\b3\b3.py", r"C:\b3\b3.py")
shutil.move(cwd + r"\b3\ico\pyinstallerdefault.ico", r"C:\b3\ico\pyinstallerdefault.ico")

input("\nRequired modules will now be installed. Press enter to continue.")

os.system("pip install winshell")
os.system("pip install pywin32")
os.system("pip install selenium")
os.system("pip install pyinstaller")

os.system("cls")

# Exe temporarily not available due to windows defender thinking it's a trojan.
# Will try to find fix for this

#shortcut = input("\nAn exe will now be created.\nWould you like to make a shortcut? [Y/n]")
#shortcut = shortcut.lower()
#answeredshortcut = False
#while not answeredshortcut:
#    if shortcut == "y":
#        makeShortcut = True
#        answeredshortcut = True
#    elif shortcut == "n":
#        makeShortcut = False
#        answeredshortcut = True
#    else:
#       answeredshortcut = False

#os.system("pyinstaller " + driveletter + r"b3\b3.py -F")
#

#if makeShortcut:
#    import winshell
#    from win32com.client import Dispatch
#
#    desktop = winshell.desktop()
#    path = os.path.join(desktop, "B3.lnk")
#    exedir = driveletter + r"b3\b3.exe"
#    folderdir = driveletter + r"b3"
#    target = exedir
#    wDir = folderdir
#    icon = folderdir + r"\ico\pyinstallerdefault.ico"
#
#    shell = Dispatch("WScript.Shell")
#    mkshortcut = shell.CreateShortCut(path)
#    mkshortcut.Targetpath = target
#    mkshortcut.WorkingDirectory = wDir
#    mkshortcut.IconLocation = icon
#    mkshortcut.save()
#else:
#    pass
#

print('You must now verify that the install went correct.')
print(r"To do this, go to C:\b3\verify.py and double click to run it.")
print("IF PROMPTED, ENTER BESTBUY CONFIRMATION EMAIL/TEXT")
input("Press Enter to close")

#verify = r"C:\b3\verify.py"
#b3dir = r"C:\b3"
#os.system("cd " + b3dir)
#os.system("verify.py")