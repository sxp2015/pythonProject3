import socks
import socket
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5, '142.54.239.1', 4145)
socket.socket = socks.socksocket
try:
    response = request.urlopen('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
