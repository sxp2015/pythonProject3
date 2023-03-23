import zipfile, os
from pathlib import Path

p = Path.cwd()

# 调用zipfile.ZipFile()函数，向它传入一个字符串，表示ZIP文件的文件名
exampleZip = zipfile.ZipFile(p / 'example.zip')
# ZipFile对象有一个namelist()方法，它返回ZIP文件中包含的所有文件和文件夹的字符串的列表
name_list = exampleZip.namelist()
print('name_list', name_list)
