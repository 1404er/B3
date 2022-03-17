import os
import selenium.common.exceptions as ec
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

print("This will start a verification test to check B3 is functioning properly.")
print("This is required before running B3.")
print("B3 will launch FireFox and PRETEND to purchase a FREE item.")
print("Nothing will be bought and this is purely to test stability.")
print("If test fails for any reason, please relaunch verify.py")
input("Press Enter to continue. ")

link = "https://www.bestbuy.com/site/free-youtube-premium-for-3-months-new-subscribers-only/6453905.p?skuId=6453905"

email = input("BestBuy Account Email: ")
password = input("BestBuy Account Password: ")

bought = False

service = Service(executable_path=GeckoDriverManager().install())

with webdriver.Firefox(service=service) as driver:
    driver.get(link)
    while not bought:
        try:
            addToCartBtn = driver.find_element(By.CLASS_NAME, "c-button-disabled")
            sleep(1)
            driver.refresh()
        except ec.NoSuchElementException:
            try:
                surveyNo = driver.find_element(By.ID, "survey_invite_no")
                surveyNo.click()
            except ec.NoSuchElementException:
                pass

            addToCartBtn = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.CLASS_NAME, "c-button-primary"))
            )

            addToCartBtn.click()
            driver.get("https://www.bestbuy.com/cart")

            toBuyScreen = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "//*[text()='Checkout']"))
            )
            toBuyScreen.click()

            enterEmail = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.ID, "fld-e"))
            )

            enterEmail.send_keys(email)
            sleep(0.1)
            enterPassword = driver.find_element(By.ID, "fld-p1")
            enterPassword.send_keys(password)
            sleep(0.1)
            signInBtn = driver.find_element(By.XPATH, "//*[text()='Sign In']")
            signInBtn.click()

            placeOrderBtn = WebDriverWait(driver, 1000).until(
                presence_of_element_located((By.CLASS_NAME, "btn-lg.btn-block.btn-primary.button__fast-track"))
            )

            driver.close()

            bought = True

os.system("cls")
print("Test complete. You may now close.")
print("\nIt is recommended to remove the free item from your cart before continuing.\n")
