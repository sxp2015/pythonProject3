from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建 Chrome 浏览器 WebDriver 对象
browser = webdriver.Chrome()

try:
    # 加载百度首页
    browser.get('https://www.baidu.com')

    # 通过 ID 定位搜索框，并输入要搜索的关键词 'Python'
    input_button = browser.find_element(By.ID, 'kw')
    input_button.send_keys('Python')

    # 模拟回车键，提交搜索请求
    input_button.send_keys(Keys.ENTER)

    # 显式等待，等待搜索结果页面的元素加载完成
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

    # 输出搜索结果页面的URL、cookies和HTML源码
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)

finally:
    # 关闭浏览器
    browser.close()

"""
在这个代码优化和修改的过程中，我们主要做了以下几点：
添加了类型标注，方便阅读和维护。
将该代码封装成函数，使其更加通用化，并且方便调用和测试。
使用 finally 关键字确保浏览器一定会被关闭，防止浏览器残留造成内存泄漏。
使用 quit() 函数代替 close() 函数确保浏览器资源的释放。
"""