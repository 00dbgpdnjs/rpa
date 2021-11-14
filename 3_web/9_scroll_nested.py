# < 특정 영역 스크롤 >

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')

time.sleep(5)

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# way0 : Just click without scrolling

# way1 : AcionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# way2 : Get coordinates of "elem" 
# 좌표정보를 얻기위해 동작하다 보니까 자동으로 스크롤을 해줌 ; 특정 elem으로 스크롤 하는 효과
xy = elem.location_once_scrolled_into_view
print("type : ", type(xy)) # dict
print("value : ", xy)

elem.click()

time.sleep(5)
browser.quit()