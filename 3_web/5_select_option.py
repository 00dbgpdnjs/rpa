import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# way1. cars에 해당하는 elem을 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# option[1] : 첫번째 항목
# option[2] : 두번째 항목
# ...

# way2. 옵선 중에서 텍스트가 Audi 인 항목을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# way3. 텍스트 값이 부분 일치하는 항목 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')

elem.click()

time.sleep(5)

browser.quit()