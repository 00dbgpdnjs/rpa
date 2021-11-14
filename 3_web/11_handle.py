# handle : Key value for the OS to identify[distinguish] something. 
# key value which os 
# 운영체제가 관리하기 위해 각 브라우저[창]에 다른 헨들 번호를 부여함

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # All (of two) window handle info
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # Move on to the window
    print(browser.title)
    print()

# code... (some work)

print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title) # >> HTML input type="radio"

time.sleep(5)
browser.get("http://daum.net")

time.sleep(5)
browser.quit()