# Only refer to 5_select_option.py and from 3_login_auto.py among 6_selenium

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
# If error about no such a elem ("how to" btn), add a code to maximaize window

# 4번 구현 (4 ways)
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click() # 주의 : 위에 a태그가 추가되면 118번째로 밀려남
# browser.find_element_by_link_text('Contact Form').click() # N.B.: The main page may have the same text.
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # Best Code
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()