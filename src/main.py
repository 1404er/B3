import selenium.common.exceptions as ec
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager

link = input("BestBuy Item Link: ")
link = link.lower()

link_www_check = link[0:4]
if link_www_check == "www.":
    pass
else:
    link_www_check = link[0:12]
    if link_www_check == "https://www.":
        pass
    else:
        link = "www." + link

link_https_check = link[0:8]
if link_https_check == "https://":
    pass
else:
    link = "https://" + link

email = input("BestBuy Account Email: ")
password = input("BestBuy Account Password: ")

print("\nThis is required by BestBuy to use the default payment.")
cvv = input("BestBuy Default Payment Method CVV/CVC: ")

bought = False

with webdriver.Chrome(ChromeDriverManager().install(), service_log_path="NUL") as driver:
    driver.get(link)
    while not bought:
        try:
            addToCartBtn = driver.find_element(By.CLASS_NAME, "c-button-disabled")
            time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print("Out of Stock as of " + time)
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

            time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print("Available as of " + time)
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

            enterCVV = WebDriverWait(driver, 600).until(
                presence_of_element_located((By.ID, "cvv"))
            )

            enterCVV.send_keys(cvv)
            sleep(0.5)
            confirmBuy = driver.find_element(By.CLASS_NAME, "btn-lg.btn-block.btn-primary.button__fast-track")
            confirmBuy.click()
            sleep(5)
            time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print("Purchased " + time)
            bought = True

    sleep(60)
    driver.quit()
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    input("Finished " + time)
