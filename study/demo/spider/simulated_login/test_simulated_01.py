import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'

LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
    # scrape.crt 保存的时候选证书链，且文件名，不要含特殊符号
}, verify='scrape.crt', allow_redirects=False)

cookies = response_login.cookies
print('cookies:', cookies)
response_index = requests.get(INDEX_URL, cookies=cookies, verify='scrape.crt',allow_redirects=False)

print(f'response_index.status_code: {response_index.status_code}')
print(f'Response URL: {response_index.url}')
