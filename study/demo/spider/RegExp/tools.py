#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-03 17:20
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : tools.py
# @IDE     : PyCharm
#

# 在线正则表达式测试
# https://tool.oschina.net/regex

#
"""
Hello,my phone number is +86 15575694746 and email is 240746804@qq.com
https://www.lw05.cn
and my website is


那么，为什么加了一个换行符，就匹配不到了呢?这是因为匹配的内容是除换行符之外的任意字符，
当遇到换行符时，.?就不能匹配了，
所以导致匹配失败。这里只需加一个修饰符 re.S，即可修正这个错误:
result = re.match('He.*?(\d+).*?Demo$"，content,re.S)
这个修饰符的作用是使匹配内容包括换行符在内的所有字符。


re.I  使匹配对大小写不敏感
re.L  实现本地化识别(locale-aware)匹配
re.M  多行匹配，影响^和$
re.S  使匹配内容包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符。这个标志会影响 \w、\W、\b和\B
re.X  该标志能够给予你更灵活的格式，以便将正则表达式书写得更易于理解


例如 \.就可以用来匹配..运行结果如下
当在目标字符串中遇到用作正则匹配模式的特殊字符时，在此字符前面加反斜线\转义一下即可。

match 方法 是从字符串的开头开始匹配的，意味着一旦开头不匹配，整个匹配就失败了。

search 方法,它在匹配时会扫描整个字符串，然后返回第一个匹配成功的结果

findall 方法 获取与正则表达式相匹配的 所有字符串，返回一个列表

compile 方法 将正则表达式编译成一个正则表达式对象，以便复用 pattern = re.compile('d(2):\d(2)')

sub  方法 修改匹配成功的内容， 第一个参数是匹配规则，第二个参数是修改或替换内容 (如果去掉该参数，可以赋值为空)，第三个参数是原字符串。
例如：
 content='54aK54yr5oiR54ix5L2g
content = re.sub('\d+', '', content)

由于绝大部分HTML文本包含换行符，所以需要尽量加上re.S修饰符，以免出现匹配不到的问题

"""
