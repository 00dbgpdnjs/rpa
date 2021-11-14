import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://shopping.naver.com/home/p/index.naver')

# Put in '무선마우스'
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')

time.sleep(1) # If error, adjust time

elem.send_keys(Keys.ENTER) # Press enter key

# < SCROLL > 
# Refer to 2_handle_scroll.py

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval) 

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

# 아래 있는 스크롤을 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(5)

browser.quit()