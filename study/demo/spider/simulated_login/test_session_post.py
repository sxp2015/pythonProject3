import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'

LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

session = requests.session()

response_login = session.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
    # scrape.crt 保存的时候选证书链，且文件名，不要含特殊符号
}, verify='scrape.crt', allow_redirects=False)

cookies = session.cookies
print('Cookies:', cookies)
response_index = session.get(INDEX_URL, verify='scrape.crt', allow_redirects=False)

print(f'Response Status : {response_index.status_code}')
print(f'Response URL: {response_index.url}')
