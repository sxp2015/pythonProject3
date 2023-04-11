from selenium import webdriver
import time

# 创建WebDriver对象，选择浏览器类型和对应的驱动程序
browser = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')

# 打开指定的页面
browser.get('https://dict.youdao.com/')

# 滚动页面到底部
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# 滚动页面到顶部
browser.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
# 关闭浏览器
browser.quit()