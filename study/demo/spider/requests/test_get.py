import requests

data = {
    'name': 'germey',
    'age': 15
}

r = requests.get('https://www.baidu.com')
r2 = requests.get('https://www.httpbin.org/get', params=data)


print('type:', type(r))
print('status_code:', r.status_code)
print('r.text:', type(r.text))
print('r.text[:100]:', r.text[:100])
print('r.cookies:', r.cookies)
print('===================================')

print('r2:', r2.text)
print('r2.url:', r2.url)

# 把返回的Json类型转为字典
print('r2.json:', r2.json())

print('type(r2):', type(r2.json()))
