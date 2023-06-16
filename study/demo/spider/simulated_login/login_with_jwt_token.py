from urllib.parse import urljoin

import requests

# 基础 URL
BASE_URL = 'https://login3.scrape.center/'

# 登录 URL
LOGIN_URL = urljoin(BASE_URL, '/api/login')

# 首页 URL
INDEX_URL = urljoin(BASE_URL, '/api/book')

# 用户名和密码
USERNAME = 'admin'
PASSWORD = 'admin'

# 发送登录请求，并获取响应数据
response_login = requests.post(LOGIN_URL, json={'username': USERNAME, 'password': PASSWORD}, verify='login3.crt')
data = response_login.json()  # 解析响应数据为 JSON 格式
print('Response Json', data)

# 从响应数据中获取 JWT token
token = data.get('token')
print('token', token)

# 构建请求头，添加 JWT token
headers = {'Authorization': f'jwt {token}'}

# 发送请求，获取响应数据
response_index = requests.get(INDEX_URL, params={'limit': 18, 'offset': 0}, headers=headers, verify='login3.crt')

# 打印响应数据的一些信息
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
print('Response Headers', response_index.headers)
print('Response Cookies', response_index.cookies)
print('Response Text', response_index.text)
# 解析响应数据为 JSON 格式
print('Response Json', response_index.json())