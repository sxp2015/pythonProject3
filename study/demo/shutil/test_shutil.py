import shutil, os
from pathlib import Path

p = Path().cwd()
# shutil.copy(source, destination)， destination 是文件新名字 或新路径
res = shutil.copy(p / 'test.txt', p / 'test2')
# some_folder 这个文件夹必须先存在，才能复制过去
res2 = shutil.copy(p / 'test.txt', p / 'some_folder/test3.txt')
shutil.copy(p / 'test.txt', p / 'some_folder/test4.txt')

# shutil.copytree()将复制整个文件夹以及它包含的文件夹和文件
# shutil.copytree(p / 'some_folder', p / 'some_folder7/sub_folder')


# 调用shutil.move(source, destination)，将路径source处的文件夹移动到路径
# destination，并返回新位置的绝对路径的字符串（各层级目录必须已经存在）
# shutil.move('some_folder', 'test_move/')
# shutil.move('test_move/some_folder', 'some_folder')

print('res = ', res)
print('res2 = ', res2)
print('p = ', p)
