_A=False
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
from sys import argv
FREE_ITEM='https://www.bestbuy.com/site/apple-free-apple-tv-for-3-months-new-or-returning-subscribers-only/6484512.p?skuId=6484512'
def verifyMode():
	match len(argv):
		case 2:return argv[1]=='--verify'
		case _:return _A
def main(p,link,email,password,verify):
	F='input[name="fld-e"]';E='button:has-text("Checkout")';B=p.firefox.launch(headless=_A);C=B.new_context();A=C.new_page();A.goto(link,timeout=10000)
	while True:
		try:A.locator('text=Add to Cart').click(timeout=5000)
		except TimeoutError:A.reload();continue
		sleep(3)
		with A.expect_navigation():A.goto('https://www.bestbuy.com/cart',timeout=10000)
		with A.expect_navigation():A.locator(E).click()
		A.locator(F).click();A.locator(F).fill(email);sleep(3);A.locator('[placeholder=" "]').click();A.locator('input[name="fld-p1"]').fill(password);sleep(3);A.locator('text=Email AddressShow passwordWarning: Pressing this button will display the passwor >> button').click();sleep(15)
		try:A.locator(E).click(timeout=10000)
		except:pass
		if not verify:D=A.locator('button:has-text("Place Your Order")');D.hover();sleep(1);D.click(timeout=120000);sleep(60)
		C.close();B.close();break
if __name__=='__main__':
	email=input('BestBuy Account Email: ');password=input('BestBuy Account Password: ')
	with sync_playwright()as p:
		if not verifyMode():link=input('BestBuy Item Link: ').lower();main(p,link,email,password,_A)
		else:main(p,FREE_ITEM,email,password,True);print('Test complete.')