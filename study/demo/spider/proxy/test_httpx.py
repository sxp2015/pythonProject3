
# proxy = 'username:password@142.54.239.1:4145'
# socks5proxy = '142.54.239.1:4145'
# proxy = '111.43.105.50:9091'
# proxy = '134.209.222.252:8080'
# proxy = '83.40.144.222:80'
# proxy = '61.175.214.2:9091'
# proxy = '140.206.62.198:9002'
import httpx

proxy = '64.139.79.35:8080'
# proxies = {'http': 'socks5://' + proxy, 'socks5': 'https://' + proxy}
proxies = {'http://': 'http://' + proxy, 'https://': 'https://' + proxy}

with httpx.Client(proxies=proxies) as client:
    response = client.get('https://httpbin.org/get')
    print(response.text)
