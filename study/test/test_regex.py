import re

# 手机号正则表达式
phone = str(input('请输入手机号:'))

text = re.compile(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$')
s = re.search(text, phone)
if s:
    print(s.group(), '是正常手机号')
else:
    print('手机号格式不正确')
