import re, requests

# 目标URL
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_URL_1 = 'https://antispider4.scrape.center/css/app.654ba59e.css'
TARGET_URL_2 = 'https://antispider4.scrape.center/'

# 发送HTTP请求，获取响应内容 ，这里从网站获取SSL的CA证书的时候要注意，保存的文件格式是 证书链文件，而不是单一证书文件
response = requests.get(TARGET_URL_1, verify='./scrape.crt')

# 定义正则表达式
pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')

# 使用正则表达式搜索匹配项
results = re.findall(pattern, response.text)

# 将搜索结果转换为字典
icon_map = {item[0]: item[1] for item in results}

# print('icon_map:', icon_map)


def parse_score(item):
    elements = item('.icon')
    icon_values = []
    for element in elements.items():
        class_name = (element.attr('class'))
        icon_key = re.search('.icon-(\d+)', class_name).group(1)
        icon_value = icon_map.get(icon_key)
        icon_values.append(icon_value)

    return ''.join(icon_values)


# 配置 ChromeOptions，将 Chrome 设置为无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# 启动浏览器
browser = webdriver.Chrome(options=chrome_options)
browser.get(TARGET_URL_2)

# 等待页面加载完成
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.item')))

# 获取页面HTML代码，并解析
html: str = browser.page_source
doc: pq = pq(html)

items = doc('.item')

for item in items.items():
    name = item('.name').text()
    categories = [o.text() for o in item('.categories button').items()]
    score = parse_score(item)
    print(f'name: {name}, categories: {categories}, score: {score}')

browser.close()
