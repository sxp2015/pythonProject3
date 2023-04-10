# 导入selenium和webdriver模块
from selenium import webdriver

# 创建Chrome浏览器驱动对象
driver = webdriver.Chrome('C:\\Program Files\\chromedriver')

# 打开网页
url = "https://www.baidu.com"
driver.get(url)

try:
    elem = driver.find_element_by_class_name('cos-pc')
    print('Found <%s> element with that class name!' % elem.tag_name)
except FileNotFoundError:
    print('Was not able to find an element with that name.')


# 获取页面标题
title = driver.title
print("页面标题为：", title)

# 关闭浏览器
driver.quit()