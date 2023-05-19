import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver_path = 'C:\\Program Files\\chromedriver.exe'


# 检查 webdriver 是否已经安装
def check_webdriver():
    return os.path.isfile(chromedriver_path)


if not check_webdriver():
    print('Error: Webdriver not found.')
    exit(1)

# 创建一个 ChromeOptions 对象
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')

# 创建一个浏览器对象，传入 ChromeOptions 对象
browser = webdriver.Chrome(options=option)

try:
    # 设置窗口尺寸
    browser.set_window_size(1366, 768)
    # 打开待爬取的网站
    browser.get('https://www.baidu.com')
    # 确保页面加载完成
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'su')))
    # 截屏保存图片
    browser.save_screenshot('preview3.png')

except TimeoutException as e:
    print(f'Error: {e}, 页面加载超时')
except WebDriverException as e:
    print(f'Error: {e}, WebDriver异常')
finally:
    browser.close()
    browser.quit()
