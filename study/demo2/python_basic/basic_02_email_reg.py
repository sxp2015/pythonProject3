import time, sys, keyword, os, re

local_time = time.localtime()
print('本地时间：', local_time)
print(f'{local_time.tm_year}年,{local_time.tm_mon}月,{local_time.tm_mday}日', end='\n')
print(f'{local_time.tm_hour}时,{local_time.tm_min}分,{local_time.tm_sec}秒', end='\n')

# print('请输入字符串，按Enter:', end=' ')
# msg = sys.stdin.readline()
# sys.stdout.write("HHH")
# print('您输入的字符串为:', msg)

print('Python 中的关键字:', keyword.kwlist)

print('当前路径:', os.curdir)
print('打印文件的绝对路径:', os.path.abspath(os.getcwd()))

print('打印文件的相对路径:', os.path.relpath("C:\\", "basic_02.py"))

msg = 'txt@deepstone.com.tw kkk@gmail.com'
pattern = r'''(
[a-zA-Z0-9_.]+  #使用者账号
@  # @符号
[a-zA-Z0-9_.]+   # 主机域名domain
[\.]   #.符号
[a-zA-Z]{2,4}  #可能是com或edu或其他
([\.])?  # .符号，也可能是国别
([a-zA-Z]{2,4})?   # 国别
)'''
eMail = re.findall(pattern, msg, re.VERBOSE)
print(eMail)
