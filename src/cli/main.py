import selenium
import selenium.common.exceptions as ec
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


link = None
email = None
pwd = None
cvv = None


def askForLink():
    global link
    link = input("BestBuy Item Link: ")
    link = link.lower()


def askForInfo():
    global email
    global pwd
    global cvv

    email = input("BestBuy Account Email: ")
    pwd = input("BestBuy Account Password: ")

    print("\nThis is required by BestBuy to use the default payment.")
    cvv = input("BestBuy Default Payment Method CVV/CVC: ")


def time():
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S")


def run():
    askForLink()
    askForInfo()

    bought = False

    service = Service(executable_path=GeckoDriverManager().install())

    with webdriver.Firefox(service=service) as driver:
        driver.get(link)
        while not bought:
            try:
                addToCartBtn = WebDriverWait(driver, 3).until(
                    presence_of_element_located((By.CLASS_NAME, 
                "c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"))
                )
            except ec.NoSuchElementException:
                try:
                    surveyNo = driver.find_element(By.ID, "survey_invite_no")
                    surveyNo.click()
                except ec.NoSuchElementException:
                    pass

                addToCartBtn = WebDriverWait(driver, 10).until(
                    presence_of_element_located((By.CLASS_NAME, 
                "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"))
                )

                print(f"Available as of {time()}")
                addToCartBtn.click()
                driver.get("https://www.bestbuy.com/cart")

                toBuyScreen = WebDriverWait(driver, 60).until(
                    presence_of_element_located((By.XPATH, "//*[text()='Checkout']"))
                )
                toBuyScreen.click()

                enterEmail = WebDriverWait(driver, 60).until(
                    presence_of_element_located((By.ID, "fld-e"))
                )

                enterEmail.send_keys(email)
                sleep(0.1)
                enterPassword = driver.find_element(By.ID, "fld-p1")
                enterPassword.send_keys(pwd)
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
                print(f"Purchased at {time()}")
                bought = True
            except selenium.common.exceptions.TimeoutException:
                print(f"Out of Stock as of {time()}")
                driver.refresh()

        sleep(60)
        driver.quit()
    input(f"Finished at {time()}")


if __name__ == "__main__":
    run()