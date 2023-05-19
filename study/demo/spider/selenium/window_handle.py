import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 创建 Chrome 浏览器对象
browser = webdriver.Chrome()
try:

    # 打开百度网站
    browser.get('https://www.baidu.com')

    # 等待页面加载完成
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'kw')))

    # 在当前窗口中执行 JavaScript 语句，新开一个窗口
    browser.execute_script('window.open()')

    # 输出浏览器的所有窗口句柄
    print('browser.window_handles:', browser.window_handles)

    # 切换到新打开的窗口
    browser.switch_to.window(browser.window_handles[1])

    # 打开淘宝网站，并等待页面加载完成
    browser.get('https://www.taobao.com')

    # 等待页面加载完成
    input_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'q')))
    input_button.send_keys('Python')

    # 等待页面加载完成
    browser.implicitly_wait(2)

    # 清除输入的内容
    input_button.clear()

    # 切换回原来的窗口，打开必应网站
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://cn.bing.com')

    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 等待 2 秒
    WebDriverWait(browser,2)
finally:
    # 关闭浏览器
    browser.quit()
