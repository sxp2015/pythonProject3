#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-04-29 21:18
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : get_session.py
# @IDE     : PyCharm
import requests
from requests.auth import HTTPBasicAuth

# get and set cookies
# s = requests.sessions.session()
# s.get('https://www.httpbin.org/cookies/set/number/123456789')
# res = s.get('https://www.httpbin.org/cookies/')
# print('cookies: ', res.text)

# 发送 GET 请求，获取 session ID
url = 'https://www.baidu.com'
url2 = 'https://ssr2.scrape.center'
url3 = 'https://ssr3.scrape.center'

response2 = requests.get(url2, verify=False, cert=False)
response3 = requests.get(url3, auth=HTTPBasicAuth('admin', 'admin'), verify=False, cert=False)

# 影响状态
print('response2', response2.text)
print('response3', response3.text)
