from playwright.sync_api import sync_playwright, TimeoutError
from time import sleep
from sys import argv


FREE_ITEM = "https://www.bestbuy.com/site/apple-free-apple-tv-for-3-months-new-or-returning-subscribers-only/6484512.p?skuId=6484512"


def verifyMode():
    match len(argv):
        case 2:
            return argv[1] == "--verify"
        case _:
            return False


def main(p, link, email, password, verify):
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto(link, timeout=10000)

    while True:
        try:
            page.locator("text=Add to Cart").click(timeout=5000)
        except TimeoutError:
            page.reload()
            continue

        sleep(3)

        with page.expect_navigation():
            page.goto("https://www.bestbuy.com/cart", timeout=10000)

        with page.expect_navigation():
            page.locator("button:has-text(\"Checkout\")").click()

        page.locator("input[name=\"fld-e\"]").click()

        page.locator("input[name=\"fld-e\"]").fill(email)

        sleep(3)

        page.locator("[placeholder=\" \"]").click()

        page.locator("input[name=\"fld-p1\"]").fill(password)

        sleep(3)

        page.locator("text=Email AddressShow passwordWarning: Pressing this button will display the passwor >> button").click()

        sleep(15)

        try:
            page.locator("button:has-text(\"Checkout\")").click(timeout=10000)
        except:
            pass

        if not verify:
            place = page.locator("button:has-text(\"Place Your Order\")")
            place.hover()
            sleep(1)
            place.click(timeout=120000)
            sleep(60)

        context.close()
        browser.close()
        break


if __name__ == "__main__":
    email = input("BestBuy Account Email: ")
    password = input("BestBuy Account Password: ")

    with sync_playwright() as p:
        if not verifyMode():
            link = input("BestBuy Item Link: ").lower()
            main(p, link, email, password, False)
        else:
            main(p, FREE_ITEM, email, password, True)
            print("Test complete.")