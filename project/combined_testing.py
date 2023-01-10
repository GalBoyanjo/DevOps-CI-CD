import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from db_connector import get_user, get_config, get_all_ids

"""
Combined Testing - for Web interface, REST API and Database testing
1. Post any new user data to the REST API using POST method.
2. Submit a GET request to make sure data equals to the posted data.
3. Using pymysql, check posted data was stored inside DB (users table).
4. Start a Selenium Webdriver session.
5. Navigate to web interface URL using the new user id.
6. Check that the user name is correct

Any failure will throw an exception using the following code: raise Exception("test failed")
"""

# User data variables
config = get_config()
user_id = 1
user_name = config[2]

# check validation of user_id to insert
ids = get_all_ids()
while True:
    if user_id not in ids:
        break
    else:
        user_id += 1

try:
    # Post user data to the REST API
    post_res = requests.post('http://127.0.0.1:5000/users/' + str(user_id), json={"user_name": user_name})
    if not post_res.ok:
        raise Exception("test failed")
    # Get user data from REST API and verify its match to the post data
    get_res = requests.get('http://127.0.0.1:5000/users/' + str(user_id))
    if not get_res.ok or get_res.json()['user_name'] != user_name:
        raise Exception("test failed")
    # Get user data from DB(using pymysql)
    if get_user(user_id) != user_name:
        raise Exception("test failed")
except:
    raise Exception("test failed")

browser_type = config[1]
if browser_type == 'Chrome':
    driver = webdriver.Chrome(
        service=Service("C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/.binary/chromedriver"))
elif browser_type == 'Firefox':
    driver = webdriver.Firefox(
        service=Service("C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/.binary/geckodriver"))
else:
    raise Exception("test failed")
driver.implicitly_wait(1)
try:
    # Navigate to web interface
    driver.get('http://' + config[0] + '/get_user_name/' + str(user_id))
    # Find user name element and verify its march to user_name
    user_id_element = driver.find_element(By.ID, value='user')
    if user_id_element.text != user_name:
        raise Exception("test failed")
except:
    raise Exception("test failed")
finally:
    driver.quit()
