from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time

from loguru import logger

COUNT = 1000

for i in range(1, COUNT + 1):
    browser = webdriver.Chrome()
    try:
        wait = WebDriverWait(browser, 10)
        browser.get("https://captcha1.scrape.center/")
        # # 输入用户名和密码
        browser.find_element(By.CSS_SELECTOR, '.el-input input[type="text"]').send_keys('admin')
        browser.find_element(By.CSS_SELECTOR, '.el-input input[type="password"]').send_keys('admin')
        time.sleep(1)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button")))
        time.sleep(2)
        button.click()
        captcha = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slicebg .geetest_absolute')))
        time.sleep(1)
        captcha.screenshot(f"captcha/images/captcha_{i}.png")
    except WebDriverException as e:
        logger.error(f'webdriver error: {e.msg}')
    finally:
        browser.close()
