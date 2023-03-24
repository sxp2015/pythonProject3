import zipfile, os
from pathlib import Path

p = Path.cwd()

# 调用zipfile.ZipFile()函数，向它传入一个字符串，表示ZIP文件的文件名
exampleZip = zipfile.ZipFile(p / 'example.zip')
# ZipFile对象有一个namelist()方法，它返回ZIP文件中包含的所有文件和文件夹的字符串的列表
name_list = exampleZip.namelist()
print('name_list', name_list)
# getinfo()方法，返回一个关于特定文件的ZipInfo对象
fileInfo = exampleZip.getinfo('example/bacon.txt')
file_size = fileInfo.file_size
file_name = fileInfo.filename
compress_size = fileInfo.compress_size
print('file_size', file_size, '\nfile_name', file_name, '\ncompress_size', compress_size)

# 计算压缩后的文件大小效率
computed_size = round(file_size / compress_size, 2)

print('computed_size', computed_size)

# 解压到当前文件 extractall(destination?) 参数可选，若不填默认解压到当前位置
# 解压到指定路径 extractall('C:\\ delicious')

# 解压当个单个文件 返回值是被压缩后文件的绝对路径。
# exampleZip.extract('spam.txt')
# 解压单个文件到指定目录
# exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.extractall()
exampleZip.close()