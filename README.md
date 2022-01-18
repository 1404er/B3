# B3
Best-Buy-Bot. Written in Python

**NOTICE:**

**Don't use this for any scalping/reselling purposes.**

## About
B3 is a bot thats a newer and updated version of a now deprecated bot called BBB. It's now improved to be faster, more accurate, and easier to use then before. 
B3 automatically purchases an item from BestBuy when it's available using the given link.


## Supported Operating Systems
### Windows - Supported
### Mac OS - Not Supported
### Linux - Not Supported
Although Mac OS and Linux aren't supported (Yet) __they still might work but are untested at the moment.__ Til then, Feel free to download and try to run it or even
tweak the source code if you want to try and port it.


# Install
Install guide

### Links you'll need:
#### [Python 3](https://www.python.org/downloads/)
__Keep this page. Don't download anything from it just yet.__
#### [Google Chrome](https://www.google.com/chrome/)
As of now, only Google Chrome is supported.
#### [ChromeDriver](https://chromedriver.chromium.org/downloads)
__Keep this page. Don't download anything from it just yet.__
#### [B3](https://github.com/Dogey11/B3/releases)
The latest release of B3.

### Installation Guide:

### Step 1: Installing Python
__If you already have python installed, skip this step.__

#### 1.1. Go to the 1st link and click the download button shown below:
![Screenshot 2021-11-30 094425](https://user-images.githubusercontent.com/69096657/144100197-6a2118eb-14dd-441f-8dae-6bc0a4d30ea9.png)
#### 1.2. Open the installer.
![unknown](https://user-images.githubusercontent.com/69096657/144100640-49284c03-c5a3-40ff-bb8e-fb68b0d3225e.png)
#### Select the Add Python 3.10 to PATH option. Note: this may require administrator privileges.
#### Select Install Now.
#### 1.3. When the install is finished, Select disable path length limit if prompted.
![unknown2](https://user-images.githubusercontent.com/69096657/144101345-6d57414a-089b-4351-a3ba-22aa7d2c27eb.png)
#### Restart your pc and go to the next step.

### Step 2: Installing Google Chrome

#### 2.1 Go to the 2nd link if you don't already have chrome.
#### 2.2 Whether you already had Chrome or you just installed it, open Chrome
#### 2.3 In the address bar near the top (Not to be confused with the search bar), type chrome://settings/help
#### This will open a "About Chrome" page.
![Screenshot 2021-11-30 100328](https://user-images.githubusercontent.com/69096657/144102967-57177b05-0e37-4b4c-9443-afda00aa5ce2.png)
#### 2.4 In the highlighted area shown above, remember Chrome's current version, you will need this later

### Step 3: Downloading ChromeDriver

#### Go to the 3rd link.
![Screenshot 2021-11-30 100724](https://user-images.githubusercontent.com/69096657/144103533-1e8a44bc-a575-4e7b-a325-a110f8e44266.png)
#### 3.1 Click the link corresponding to your Chrome version.
![Screenshot 2021-11-30 101017](https://user-images.githubusercontent.com/69096657/144104253-96282165-d487-4069-9bdb-80b281da96d4.png)
#### 3.2 Since this guide is for Windows, select chromedriver_win32.zip.
#### 3.3 When the download is finished, Right click or click the arrow next to the zip file and choose "Show in Folder"
![Screenshot 2021-11-30 101456](https://user-images.githubusercontent.com/69096657/144104692-b7902048-aede-4633-8cd1-edfb74262306.png)
#### 3.4 Right click the zip folder and click Extract All
![Screenshot 2021-11-30 101841](https://user-images.githubusercontent.com/69096657/144105069-19cef50d-323c-4e04-bace-47e595102365.png)
#### 3.5 Choose where to extract the zip
#### 3.6 Go to the extracted folder. It should look something like this:
![Animation](https://user-images.githubusercontent.com/69096657/144106021-5ba0984b-3c0e-4593-8ff9-450ffa75faba.gif)
#### 3.7 Click the Address bar, then right click and choose copy.
#### You will need this later.

### Step 4: Create and Configure A BestBuy Account
### These are the most crucial steps and if not done right, B3 won't be able to complete the purchase.
#### 4.1 Create A BestBuy account if you don't have one. If you do, make a new one for the bot or use your own.
#### 4.20 Make sure the address you want the product to be shipped to is the ONLY address saved to your BestBuy account.
#### 4.3 Make sure only the payment method you plan to use is saved.
#### 4.4 Make sure 2FA (Two factor authentication) is DISABLED on your account.

### Step 5: Running B3
#### Now that everything is configured, It's time to actually install B3.
#### 5.1 Go to the 4th link. At the newest release, scroll down to files and download b3v0.2win.zip
#### 5.2 extract it.
#### 5.3 In the extracted folder, run setup.py
#### 5.4 Press Ctrl + V to paste the directory copied earlier.
#### 5.5 Follow the rest of the prompts.
#### 5.6 After the inital setup, go to C:\b3 in File Explorer. run verify.py by double clicking. read carefully and start the check.
#### 5.7 During the check you might see a prompt from BestBuy asking for email and or phone confirmation. B3 cannot do this itself yet. You must click and allow the sign in.
#### 5.8 When the verification check is done, Close the window.
#### 5.9 Go to the C:\b3 folder again.
#### 5.10 Right click "b3.py" and choose Send to -> Desktop (create shortcut)
#### 5.11 Double click the shortcut and enter in the item & login info when prompted.
#### 5.12 Let it run until your item is bought!

# Modules used

### Internal:

Datetime

os

shutil

sys

time


### Third-Party:

Selenium
