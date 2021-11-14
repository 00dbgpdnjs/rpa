# < Download auto to the path[folder] I want (without pop-up) >
# Problem : 확장자가 tmp로 다운돼요. option 안주면 .jpg.crdownload로 다운돼요..

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\USER\Desktop\SW\project\PythonWorkspace'}) # ❗❗KEY CODE❗❗ prefs : preference

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()