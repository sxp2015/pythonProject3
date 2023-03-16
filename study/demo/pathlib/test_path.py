import os
from pathlib import Path

res1 = Path('spam') / 'bacon' / 'eggs'
res2 = Path('spam') / Path('bacon/eggs')
res3 = Path('spam') / Path('bacon', 'eggs')

print('res1=', res1)
print('res2=', res2)
print('res3=', res3)

# 使用\\的方式，虽然可以解决问题，但是有遇到不同的系统例如Linux就会报错
homeFolder = r'C:\Users\Al'
subFolder = 'spam'
res4 = homeFolder + '\\' + subFolder
res5 = '\\'.join([homeFolder, subFolder])

print('res4 = ', res4)
print('res5 = ', res5)

# res6
'''
无论你的代码运行在什么操作系统上，pathlib模块都可以重新使用/数学运算符正
确地连接路径，从而解决根据不同的系统使用不同的斜杠，正斜杠，还是倒斜杠
使用/运算符连接路径时，唯一需要记住的是，前两个值中有一个必须是Path对象。
'''
homeFolder2 = Path('C:/Users/Al')
subFolder2 = Path('spam')
res6 = homeFolder2 / subFolder2
res7 = str(homeFolder2 / subFolder2)
print('res6=', res6)
print('res7=', res7)

'''
利用Path.cwd()函数，可以取得当前工作路径的字符串，并可以利用os.chdir()改
变它。如果要更改的当前工作目录不存在，Python就会显示一个错误
'''
CurrentWorkDirectory = Path.cwd()

print('CurrentWorkDirectory=', CurrentWorkDirectory)

# 改变当前目录
# os.chdir('C:\\Windows\\System32')
# ChangedPath = Path.cwd()
# print('ChangedPath =', ChangedPath)

# 获取当前目录
cwd = os.getcwd()
print('cwd = ', cwd)

# 可以通过调用Path.home()获得主文件夹的Path对象
'''
主目录位于一个特定的位置，具体取决于你的操作系统。
在Windows操作系统上，主目录位于C:\\Users下。
在macOS上，主目录位于/Users下。
在Linux操作系统上，主目录通常位于/home下。
'''
home = Path.home()
print('home=', home)
