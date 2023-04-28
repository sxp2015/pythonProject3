#!/usr/bin/env python3

"""
Copyright (C) 2023 - 2023 Sunny, Inc. All Rights Reserved
"""

import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'name': 'germey'}).encode('utf-8')

response = urllib.request.urlopen('https://www.baidu.com', data=data)

print('python', response.read())
print('python status', response.status)
print('python getHeaders', response.getheaders())
