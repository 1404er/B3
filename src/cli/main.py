from time import sleep
from datetime import datetime
from sys import argv
import selenium
import selenium.webdriver
import selenium.common.exceptions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


FREE_ITEM = "https://www.bestbuy.com/site/free-youtube-premium-for-3-months-new-subscribers-only/6453905.p?skuId=6453905"


def tryParse(i):
    try:
        int(i)
        return True
    except:
        pass
    return False


def verifyMode():
    match len(argv):
        case 2:
            return argv[1] == "--verify"
        case _:
            return False


def getLink():
    return input("BestBuy Item Link: ").lower()


def getEmail():
    return input("BestBuy Account Email: ")


def getPassword():
    return input("BestBuy Account Password: ")


def getCVV():
    print("\nThis is required by BestBuy to use the default payment.")

    cvv = input("BestBuy Default Payment Method CVV/CVC: ")
    if len(cvv) <= 4 and tryParse(cvv):
        return cvv
    else:
        raise Exception("Invalid.")


def getTime():
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S")


def main():
    link = getLink()
    email = getEmail()
    pwd = getPassword()
    cvv = getCVV()

    service = Service(executable_path=GeckoDriverManager().install())

    with selenium.webdriver.Firefox(service=service) as driver:
        driver.get(link)
        while True:
            try:
                addToCartBtn = WebDriverWait(driver, 3).until
                (
                    presence_of_element_located((By.CLASS_NAME, 
                    "c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"))
                )
            except ec.NoSuchElementException:
                try:
                    surveyNo = driver.find_element(By.ID, "survey_invite_no")
                    surveyNo.click()
                except ec.NoSuchElementException:
                    pass

                addToCartBtn = WebDriverWait(driver, 10).until
                (
                    presence_of_element_located((By.CLASS_NAME, 
                    "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"))
                )

                print(f"Available as of {getTime()}")
                addToCartBtn.click()
                driver.get("https://www.bestbuy.com/cart")

                toBuyScreen = WebDriverWait(driver, 60).until
                (
                    presence_of_element_located((By.XPATH, "//*[text()='Checkout']"))
                )
                toBuyScreen.click()

                enterEmail = WebDriverWait(driver, 60).until
                (
                    presence_of_element_located((By.ID, "fld-e"))
                )

                enterEmail.send_keys(email)
                sleep(0.1)
                enterPassword = driver.find_element(By.ID, "fld-p1")
                enterPassword.send_keys(pwd)
                sleep(0.1)
                signInBtn = driver.find_element(By.XPATH, "//*[text()='Sign In']")
                signInBtn.click()

                enterCVV = WebDriverWait(driver, 600).until
                (
                    presence_of_element_located((By.ID, "cvv"))
                )

                enterCVV.send_keys(cvv)
                sleep(0.5)
                confirmBuy = driver.find_element(By.CLASS_NAME, "btn-lg.btn-block.btn-primary.button__fast-track")
                confirmBuy.click()
                sleep(5)
                print(f"Purchased at {getTime()}")
                break
            except selenium.common.exceptions.TimeoutException:
                print(f"Out of Stock as of {getTime()}")
                driver.refresh()

    sleep(60)
    print(f"Finished at {getTime()}")
    driver.quit()


if __name__ == "__main__":
    main()