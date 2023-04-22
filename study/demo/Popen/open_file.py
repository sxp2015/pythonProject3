import subprocess

"""
每个操作系统都有一个程序，其行为等价于双击文档文件来打开它。在Windows操作
系统上，这是start程序。在macOS上，这是open程序。在Ubuntu Linux操作系统上，这
是see程序
"""
fileObj = open('hello.txt', 'w')
fileObj.write('Hello, world!')

fileObj.close()
# 传入了shell=True关键字参数，这只在Windows操作系统上需要。操作系统知道所有的文件关联
subprocess.Popen(['start', 'hello.txt'], shell=True)
