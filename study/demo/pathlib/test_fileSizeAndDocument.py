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
home_all_path = Path.cwd().glob('*')
py_all_path = Path.cwd().glob('*.py')
# 问号（?）代表任意单个字符：
index_hello_path = Path.cwd().glob('hello?')
# 放到一个列表里
home_path_list = list(home_all_path)
# 遍历列表
for home_path in home_path_list:
    # print('home_path = ', home_path)
    print('home_path_base_name = ', os.path.basename(home_path))

py_all_path_list = list(py_all_path)
for py_path in py_all_path_list:
    # print('list_py_path', os.listdir(Path.cwd()))
    print('py_path_base_name = ', os.path.basename(py_path))

index_hello_path_list = list(index_hello_path)
for hello_path in index_hello_path_list:
    # print('hello_path', hello_path)
    print('hello_path =', os.path.basename(hello_path))

# list(Path.cwd().glob('*.?x?') 返回具有任意名称和任意3个字符的扩展名的文件
# print('home_path_list', home_path_list)
# print('py_all_path_list', py_all_path_list)
# print('index_hello_path_list', index_hello_path_list)
