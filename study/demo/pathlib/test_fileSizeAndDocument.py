import os
from pathlib import Path

file_path = os.path.abspath('test_directory.py')
doc_path = Path.cwd()
# 获取文件大小
file_size = os.path.getsize(file_path)
print('file_size=', file_size)

# 获取指定目录下 文件 / 文件夹列表
file_list = os.listdir(doc_path)
print('file_list = ', file_list)

# 计算指定目录的总容量
totalSize = 0

for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
    documents = os.path.join('', filename)
    # print('document', documents)

print('totalSize', totalSize)

# 获取指定目录中所有文件
home_all_path = Path.home().glob('*')
# 放到一个列表里
home_path_list = list(home_all_path)
print('home_path_list', home_path_list)
