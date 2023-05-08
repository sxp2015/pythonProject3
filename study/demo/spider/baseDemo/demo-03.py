"""
项目需求，请求一个网站，把网站上的信息保存到本地一个txt文件
网站：BASE_URL = 'https://ssr1.scrape.center'
"""
import re

import requests
from pyquery import PyQuery as pq

# 定义请求的网站
BASE_URL = 'https://ssr1.scrape.center'
# 请求网站的内容
try:
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        html_content = response.text
        # 实例化一个PyQuery
        doc = pq(html_content)
        # 获取节点上需要的内容
        items = doc('.el-card').items()
        # 定义打开保存的文件
        with open('movie.txt', 'w', encoding='utf-8') as file:
            # 遍历文件
            for item in items:
                # 电影名称
                name = item.find('a > h2').text()
                file.write(f'名称：{name}\n')
                # 类别
                categories = [i.text() for i in item.find('.categories button span').items()]
                file.write(f'类名：{categories}\n')
                # 获取发表时间
                published_at = item.find('.info:contains(上映)').text()
                published_at_format = None
                match = re.search('\d{4}-\d{2}-\d{2}', published_at)
                if match:
                    published_at_format = match.group(0)
                file.write(f'发表时间：{published_at_format}\n')

                # 评分
                score = item.find('p.score').text()
                file.write(f'评分：{score}\n')
                file.write(f'{"*" * 50}\n')

        # 关闭文件流
        file.close()
except requests.RequestException as e:
    print('请求 %s 时发生了错误: %s', BASE_URL, str(e))
