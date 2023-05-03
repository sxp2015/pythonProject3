#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-04-29 20:57
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_request.py
# @IDE     : PyCharm
import requests

r = requests.get('https://www.baidu.cn')

exit() if not r.status_code == requests.codes.ok else print('请求成功')
print('code1', r.status_code)
print('code2', requests.codes.ok)


