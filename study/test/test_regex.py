import re

# 手机号正则表达式
phone = str(input('请输入手机号:'))

# 传入一个字符串值，表示正则表达式，它将返回一个Regex模式对象（或者就简称为“Regex对象”）。
text = re.compile(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$')

# 调用search()，向它传入想查找的 字符串。查找的结果保存在变量mo （match object）中
mo = re.search(text, phone)
if mo:
    # group()方法，它返回被查找字符串中实际匹配的文本
    print(mo.group(), '是正常手机号')
else:
    print('手机号格式不正确')
