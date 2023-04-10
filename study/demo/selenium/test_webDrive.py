# 导入selenium和webdriver模块
from selenium import webdriver
# 导入键盘的按键
from selenium.webdriver.common.keys import Keys
# 导入时间用于等待
import time

# 创建Chrome浏览器驱动对象,要把当前目录drive下的exe文件，复制到下面指定的路径中，再把下面的目录添加到环境变量中
browser = webdriver.Chrome('C:\\Program Files\\chromedriver')

# 打开网页
url = "https://www.baidu.com"
browser.get(url)

try:
    # 获取到百度的input标签的类名
    # elem = driver.find_element_by_class_name('s_ipt')
    # 通过ID的方式获取input
    elem = browser.find_element_by_id('kw')
    print('Found <%s> element with that class name!' % elem.tag_name)
    # 往input标签中添加内容，然后提交
    elem.send_keys('百家号')
    elem.submit()

    # 模拟页面滚动顶部和底部
    htmlElem = browser.find_element_by_tag_name('html')
    """
    Keys.END 用于模拟输入结束
    Keys.HOME来用于模拟移动到行首的操作。
    Keys.PAGE_DOWN和Keys.PAGE_UP，Keys.PAGE_DOWN表示下一页，Keys.PAGE_UP表示上一页
    """
    htmlElem.send_keys(Keys.END)
    time.sleep(2)
    htmlElem.send_keys(Keys.HOME)

    # 模拟点击百度首页-新闻菜单的行为
    # linkElem = browser.find_element_by_link_text('新闻')
    # linkElem.click()
except FileNotFoundError:
    print('Was not able to find an element with that name.')

# 获取页面标题
title = browser.title
print("页面标题为：", title)




# 关闭浏览器
# browser.quit()
