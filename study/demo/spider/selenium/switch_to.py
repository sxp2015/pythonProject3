import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element(By.CLASS_NAME, 'logo')
except NoSuchElementException:
    print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element(By.CLASS_NAME, 'logo')
    print(logo)
    print(logo.text)
