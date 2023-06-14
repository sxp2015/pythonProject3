import requests
import socket
import socks
socks_proxy = '142.54.239.1:4145'
proxy = '142.54.239.1:4145'
# proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
proxies = {'http': 'socks5://' + proxy, 'socks5': 'https://' + proxy}
# socks.set_default_proxy(socks.SOCKS5, '142.54.239.1', 4145)
# socket.socket = socks.socksocket
try:
    response = requests.get('https://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Proxy Error')

