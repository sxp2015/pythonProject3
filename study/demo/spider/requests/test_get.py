import requests
import re
from faker import Faker
# 生成随机请求头
from fake_user_agent import user_agent

# 创建实例
ua = Faker()

# 定义请求头
headers = {
    'User-Agent': ua.user_agent()
}

headers2 = {
    'User-Agent': user_agent()
}

# 定义数据
data = {
    'name': 'germey',
    'age': 15
}

# 定义网站
r = requests.get('https://www.baidu.com/')
r2 = requests.get('https://www.httpbin.org/get', params=data)
r3 = requests.get('https://dog.ceo/')
r4 = requests.get('https://p5.lw05.cn/favicon.ico')
r5 = requests.get('https://p5.lw05.cn/', headers=headers)

print('r5 headers', r5.text)


# 写入图片
with open('favicon.ico', 'wb') as f:
    f.write(r4.content)

pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r3.text)

print('titles =', titles)
print('type:', type(r))
print('status_code:', r.status_code)
print('r.text:', type(r.text))
print('r.text[:100]:', r.text[:100])
print('r.cookies:', r.cookies)

print('r2:', r2.text)
print('r2.url:', r2.url)

# 把返回的Json类型转为字典
print('r2.json:', r2.json())

print('type(r2):', type(r2.json()))
