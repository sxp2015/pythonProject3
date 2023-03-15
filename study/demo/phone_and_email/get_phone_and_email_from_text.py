import numbers
import re, pyperclip

# 传入一个字符串值，表示正则表达式，它将返回一个Regex模式对象（或者就简称为“Regex对象”）。
phoneRegex = re.compile(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$')
# 座机带区号正则表达式 电话号码分隔字符可以是空格（\s）、短横线（-）或句点（.）
landlineRegex = re.compile(r'(\d{3,4}|\(\d{3,4}\))?(\s|-|\.)?(\d{7,8})')
# ?匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
# 当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。
# 非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，
# 对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。
# ?:pattern  匹配 pattern 但不获取匹配结果，
# \D 匹配一个非数字字符。等价于 [^0-9]。
phoneRegex2 = re.compile(r'(?:^|\D)(1\d{10})(?:$|\D)')
# 匹配手机呈的正则表达式
phoneRegex3 = re.compile(r'(?:^|\D)(1[3-9]\d{9})(?:$|\D)')
# 邮箱正则表达式
emailRegex = re.compile(r'[a-zA-Z\d._%+-]+ @[a-zA-Z\d.-]+ (\.[a-zA-Z]{2,4})')

# 获取剪切板的内容并强制文本化
text = str(pyperclip.paste())
# 定义空数组存放符合条件的内容
matches = []
# 搜索出来符合条件的数据
for groups in phoneRegex3.findall(text):
    phoneNum = ''.join(groups)
    if len(groups) == 11:
        matches.append(phoneNum)
        # 判断数组是否为空
        if len(matches) > 0:
            pyperclip.copy('\n'.join(matches))
            print('复制一行新数据到剪切板:')
            print('\n'.join(matches))
        else:
            print('No phone numbers or email addresses found.')



