import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="html"]')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")