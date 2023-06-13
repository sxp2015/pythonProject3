from typing import List, Dict
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re

TARGET_URL_1: str = 'https://antispider3.scrape.center/'


# 有CSS位置偏移的反爬数据，如何获取数据的处理方法
def parse_name(name_html: pq) -> str:
    # 判断类名是否存在whole的情况
    has_whole = name_html('.whole')
    if has_whole:
        return name_html.text()
    else:
        # 从HTML中解析出姓名 使用PyQuery 对象的调用方式
        chars = name_html('.char')  # 找到所有字符,也可以写成这样 chars = name_html.find('.char')
        items = []
        for char in chars.items():
            items.append({
                'text': char.text().strip(),  # 文本内容
                'left': int(re.search('(\d+)px', char.attr('style')).group(1))  # 字符在页面上的水平位置
            })
        items = sorted(items, key=lambda x: x['left'], reverse=False)  # 根据水平位置排序
        return ''.join(item['text'] for item in items)  # 拼接字符，得到姓名


# 配置 ChromeOptions，将 Chrome 设置为无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# 启动浏览器
browser = webdriver.Chrome(options=chrome_options)
browser.get(TARGET_URL_1)

# 等待页面加载完成
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.item')))

# 获取页面HTML代码，并解析
html: str = browser.page_source
doc: pq = pq(html)

# 找到所有姓名元素，并逐个解析姓名
names = doc('.item .name')
for html_item in names.items():
    name = parse_name(html_item)
    print('name:', name)

# 关闭浏览器
browser.close()
