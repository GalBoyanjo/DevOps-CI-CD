from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/GalBoyanjo/PycharmProjects/Automation/.binary/chromedriver"))

driver.implicitly_wait(1)

driver.get('https://translate.google.com')
print(driver.current_url)
print(driver.title)
# print(driver.page_source)
# driver.refresh()

str_to_trans = 'שלום'
txt_input_element = driver.find_element(By.CLASS_NAME, value='er8xn')
txt_input_element.click()
txt_input_element.send_keys(str_to_trans)

txt_output_element = driver.find_element(By.CLASS_NAME, value='jCAhz')
my_txt = txt_output_element.text
print("Translation of", str_to_trans, ": ", my_txt)

driver.quit()