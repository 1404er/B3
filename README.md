# B3
Best-Buy-Bot. Written in Python

**NOTICE:**

**Don't use this for any scalping/reselling purposes.**

**This is documentation for versions 0.4 and up. If you need documentation for an older version you can find it [here.](https://github.com/Dogey11/B3/blob/00c4ff6993c74df2608e0b1d9381c93b5901e491/README.md)**

## About
B3 is a bot thats a newer and updated version of a now deprecated bot called "BBB". It's now improved to be faster, more accurate, and easier to use then before. 
B3 automatically purchases an item from BestBuy when it's available using the given link.

<sub><sup>Real original name right?</sup></sub>

## Currently Supported Operating Systems
### Windows - Supported
### Mac OS - Not Supported
### Linux - Not Supported
Although Mac OS and Linux aren't supported (Yet) __they still might work but are untested at the moment.__ Til then, Feel free to download and try to run it or even
tweak the source code if you want to try and port it.


## Install
Install guide

### Links you'll need:
#### [Python 3](https://www.python.org/downloads/)
You'll need Python 3.10 or later.
#### [Google Chrome](https://www.google.com/chrome/)
As of now, only Google Chrome is supported.
#### [B3](https://github.com/Dogey11/B3/releases/latest)
The latest version of B3.

### Installation Guide:

### Step 1: Installing Python
__If you already have python installed, skip this step.__

#### 1.1. Go to the 1st link and click the download button shown below:
![Screenshot 2021-11-30 094425](https://user-images.githubusercontent.com/69096657/144100197-6a2118eb-14dd-441f-8dae-6bc0a4d30ea9.png)
<sub><sup>My microsoft paint circle lol</sup></sub>

#### 1.2. Open the installer.
![unknown](https://user-images.githubusercontent.com/69096657/144100640-49284c03-c5a3-40ff-bb8e-fb68b0d3225e.png)

<sub><sup>I'm good at making circles</sup></sub>
#### Select the Add Python 3.10 to PATH option. Note: this may require administrator privileges.
#### Select Install Now.

#### 1.3. When the install is finished, Select disable path length limit if prompted.
![unknown2](https://user-images.githubusercontent.com/69096657/144101345-6d57414a-089b-4351-a3ba-22aa7d2c27eb.png)
#### Restart your pc and go to the next step.



### Step 2: Create and Configure A BestBuy Account
### These are the most crucial steps and if not done right, B3 won't be able to complete the purchase.
#### 2.1 Create A BestBuy account if you don't have one. If you do, make a new one for the bot or use your own.
#### 2.2 Make sure the address you want the product to be shipped to is the ONLY address saved to your BestBuy account.
#### 2.3 Make sure only the payment method you plan to use is saved.
#### 2.4 Make sure 2FA (Two factor authentication) is DISABLED on your account.



### Step 3: Running B3
#### Now that everything is configured, It's time to actually install B3.
#### 3.1 Go to the 4th link. At the newest release, scroll down to files and download b3v0.2win.zip
#### 3.2 extract it.
#### 3.3 In the extracted folder, run setup.py
#### 3.4 Press Ctrl + V to paste the directory copied earlier.
#### 3.5 Follow the rest of the prompts.
#### 3.6 After the inital setup, go to C:\b3 in File Explorer. run verify.py by double clicking. read carefully and start the check.
#### 3.7 During the check you might see a prompt from BestBuy asking for email and or phone confirmation. B3 cannot do this itself yet. You must click and allow the sign in.
#### 3.8 When the verification check is done, Close the window.
#### 3.9 Go to the C:\b3 folder again.
#### 3.10 Right click "b3.py" and choose Send to -> Desktop (create shortcut)
#### 3.11 Double click the shortcut and enter in the item & login info when prompted.
#### 3.12 Let it run until your item is bought!



## Modules used

#### Internal:

Datetime

os

shutil

sys

time


#### Third-Party:

[Selenium](https://pypi.org/project/selenium/)

[webdriver-manager](https://pypi.org/project/webdriver-manager/)

## Installing from source
``` 
git clone https://github.com/Dogey11/B3
```
