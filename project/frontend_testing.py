from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from db_connector import get_config
from project.web_app import USERNAME, PASSWORD

"""
Frontend testing using selenium
1. Start a Selenium Webdriver session.
2. Navigate to web interface URL using an existing user id.
3. Check that the user name element is showing (web element exists).
4. Print user name (using locator)
"""
# Get browser type from DB
config = get_config(USERNAME, PASSWORD)
browser_type = config[1]
if browser_type == 'Chrome':
    driver = webdriver.Chrome(service=Service("C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/.binary/chromedriver"))
elif browser_type == 'Firefox':
    driver = webdriver.Firefox(service=Service("C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/.binary/geckodriver"))
else:
    raise Exception("Wrong browser configuration from config table")

driver.implicitly_wait(1)

try:
    driver.get('http://' + config[0] + '/get_user_name/1')
    user_id_element = driver.find_element(By.ID, value='user')
    print(user_id_element.text)
except NoSuchElementException as elm_exception:
    print(elm_exception)
finally:
    driver.quit()
