import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/GalBoyanjo/PycharmProjects/Automation/.binary/chromedriver"))
driver.implicitly_wait(5)
#### 1.
# driver.get('https://www.walla.co.il')

#### 2.
# web_title = driver.title
# driver.refresh()
# if driver.title == web_title:
#     print('OK')

#### 4.
# driver.get('https://translate.google.com')
#
# str_to_trans = 'שלום'
# txt_input_element = driver.find_element(By.CLASS_NAME, value='er8xn')
# txt_input_element.click()
# txt_input_element.send_keys(str_to_trans)
#
# txt_output_element = driver.find_element(By.CLASS_NAME, value='jCAhz')
# my_txt = txt_output_element.text
# print("Translation of", str_to_trans, ": ", my_txt)
#
# driver.quit()

#### 5.
driver.maximize_window()
driver.get('https://www.youtube.com/')
search_element = driver.find_element(By.XPATH, '//input[@id="search"]')
search_btn_element = driver.find_element(By.ID, 'search-icon-legacy')
search_element.send_keys('ed sheeran')
search_btn_element.click()
time.sleep(5)

#### 8.
# driver.get('https://www.ynet.co.il')
# print(driver.get_cookies())
# driver.delete_all_cookies()
# print(driver.get_cookies())

#### 9.
# driver.get('https://github.com/')
# search_elm = driver.find_element(By.CLASS_NAME, 'header-search-input')
# search_elm.send_keys('Selenium')
# search_elm.send_keys(Keys.ENTER)
# time.sleep(5)
















