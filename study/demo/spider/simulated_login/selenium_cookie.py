from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

from selenium.webdriver.common.by import By

BASE_URL = 'https://login2.scrape.center/'

LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(USERNAME)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(5)
# 从浏览器对象获取Cookies
cookies = driver.get_cookies()
print('cookies:', cookies)
driver.close()

# 把Cookie信息放入请求中
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response_index = session.get(INDEX_URL,verify='scrape.crt',allow_redirects=False)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
print('Session Cookies', session.cookies)
