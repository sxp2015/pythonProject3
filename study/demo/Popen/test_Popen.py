# 的Popen()函数，Python程序可以启动计算机中的其他程序

import subprocess

# 定义程序的路径
program_path = r'C:\Windows\System32\calc.exe'
PDF_program_path = r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'
PDF_file_path = r'D:\PS+CDR\注塑三车间调整\注塑三车间调整.pdf'

paint_Proc = subprocess.Popen(program_path)

# poll()方法是反复问你的司机“我们还没到吗？
if paint_Proc.poll() is None:
    print('程序还没启动')

# 使用程序打开指定的文件Popen(程序路径，程序文件)

subprocess.Popen([PDF_program_path, PDF_file_path])

# 可以在Python中启动另一个Python脚本
# subprocess.Popen(['C:\\Users\\<YOUR USERNAME>\\AppData\\Local\\Programs\\ Python\\Python38\\python.exe', 'hello.py'])
