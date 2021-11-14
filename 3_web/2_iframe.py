# < 아이프레임 태그 밑에 있는 elem의 xpath를 해당 아이프레임으로 전환 >

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # ❗❗Key Code❗❗ frame 전환 / Put frame's id

elem = browser.find_element_by_xpath('//*[@id="html"]') # 성공 / iframe 내에 있는 path

elem.click()

browser.switch_to.default_content() # 상위로[iframe태그 밖으로] 빠져 나옴

elem = browser.find_element_by_xpath('//*[@id="html"]') # 실패

elem.click()

time.sleep(5)

browser.quit()