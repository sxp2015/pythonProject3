import time

from selenium import webdriver

# 创建 Chrome 浏览器 WebDriver 对象
browser = webdriver.Chrome()

browser.get('https://antispider1.scrape.center/')

time.sleep(5)