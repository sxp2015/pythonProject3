import os
from pathlib import Path

# 函数用于路径拼接文件路径，可以传入多个路径
# 如果不存在以‘’ / ’开始的参数，则函数会自动加上
print(os.path.join('path', 'abc', 'yyy'))
# >>> path\abc\yyy

# 存在以‘’ / ’’开始的参数，从最后一个以” / ”开头的参数开始拼接，之前的参数全部丢弃。
print('1', os.path.join('aaa', '/bbb', 'ccc.txt'))
# >>> 1 /bbb\ccc.txt【这里aaa丢失了】


print('1', os.path.join('/aaa', '/bbb', 'ccc.txt'))
# >>> 1 /bbb\ccc.txt【这里/aaa丢失了】

print('1', os.path.join('/aaa', '/bbb', '/ccc.txt'))
# >>> 1 /ccc.txt【这里'/aaa', '/bbb', 丢失了】


print('1', os.path.join('/aaa', 'bbb', 'ccc.txt'))
# >>> 1 /aaa\bbb\ccc.txt 【这里没有丢失但斜杠方向不对】

print('1', os.path.join('/aaa', 'bbb', '/ccc.txt'))
# >>> 1 /ccc.txt  【 /aaa', 'bbb', 丢失，以最后一个/ 为准】


# 同时存在以‘’./ ’与‘’ / ’’开始的参数，【以‘’ / ’为主】
# 从最后一个以” / ”开头的参数开始拼接，之前的参数全部丢弃。

print('2', os.path.join('/aaa', './bbb', 'ccc.txt'))
# >>> 2 /aaa\./bbb\ccc.txt


print('2', os.path.join('aaa', './bbb', '/ccc.txt'))
# >>> 2 /ccc.txt 【'aaa', './bbb', 丢失】

# 只存在以‘’./ ’开始的参数, 会从”./ ”开头的参数的上一个参数开始拼接。
print('2', os.path.join('aaa', './bbb', 'ccc.txt'))
# >>> 2 aaa\./bbb\ccc.txt


p1 = Path('C:/yyy/yyy_data/')
p2 = Path.cwd()
print(os.path.join(p1, '/abc'))
# >>> C:/abc

print(os.path.join(p1, 'abc'))
# >>> C:/yyy/yyy_data/abc

is_exist = p1.exists()
is_file = p1.is_file()
is_dir = p1.is_dir()

is_exist2 = p2.exists()
is_file2 = p2.is_file()
is_dir2 = p2.is_dir()

print('is_exist = ', is_exist)
print('is_file = ', is_file)
print('is_dir = ', is_dir)

print('is_exist2 = ', is_exist2)
print('is_file2 = ', is_file2)
print('is_dir2 = ', is_dir2)
