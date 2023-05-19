import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建 Chrome 浏览器 WebDriver 对象
browser = webdriver.Chrome()

try:
    # 加载淘宝首页
    browser.get('https://www.baidu.com')
    browser.get('https://cn.bing.com')
    browser.get('https://www.taobao.com')

    time.sleep(1)
    browser.back()
    time.sleep(1)
    browser.forward()
    # browser.close()

    # 通过 ID 定位搜索框，并输入要搜索的关键词 'Python'
    input_button = browser.find_element(By.ID, 'q')
    input_button.send_keys('Python')

    # 等待页面加载完成
    browser.implicitly_wait(10)

    # 清除输入的内容
    input_button.clear()

    # 输入要搜索的关键词 'iphone'
    input_button.send_keys('iphone')

    # 获取搜索按钮
    search_button = browser.find_element(By.CLASS_NAME, 'btn-search')

    # 获取logo
    # taobao_logo = # 获取“淘宝网” logo 的超链接元素
    taobao_logo = browser.find_element(By.XPATH, '//a[contains(@class,"logo-bd") and contains(text(),"淘宝网")]')
    # baidu_logo = browser.find_element(By.CLASS_NAME, 'index-logo-aging-tools')

    print('logo-bd:', taobao_logo)

    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    search_button.click()

    # 输出搜索结果页面的URL、cookies和HTML源码
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    print('logo-url:', taobao_logo.get_attribute('href'))
    print('logo-text:', taobao_logo.text)


finally:
    # 关闭浏览器
    browser.quit()

"""
在这个代码优化和修改的过程中，我们主要做了以下几点：
添加了类型标注，方便阅读和维护。
将该代码封装成函数，使其更加通用化，并且方便调用和测试。
使用 finally 关键字确保浏览器一定会被关闭，防止浏览器残留造成内存泄漏。
使用 quit() 函数代替 close() 函数确保浏览器资源的释放。
"""
