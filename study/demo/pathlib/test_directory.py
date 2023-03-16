import os
from pathlib import Path

# 用os.makedirs()创建新文件夹
cwd = Path.cwd()
# os.mkdir(cwd / 'hello')
# os.makedirs('C:\\Users\\admin\\PycharmProjects\\pythonProject3\\study\\demo\\pathlib\\hello2\\1\\2\\')
# os.makedirs(cwd / 'hello3/hello4/hello5')

# 传入一个目录，返回这个目录的绝对路径
absolute_path = os.path.abspath('hello')
print('absolute_path = ', absolute_path)

'''
调用os.path.relpath(path, start)将返回从开始路径到path的相对路径的字符
串。如果没有提供开始路径，就将当前工作目录作为开始路径
'''
related_path = os.path.relpath(cwd, Path.home())
# 相对于程序的当前工作目录。
print('related_path = ', related_path)

# 获得主文件夹的Path对象
print('path_home = ', Path.home())

# 获得当前目录的绝对路径
print('absolute path 2= ', os.path.abspath('.'))

# os.path.abspath('test_directory.py') 这行与下面的写法不同，意思一样的
p = Path.cwd() / 'test_directory.py'

print('p = ', p)
print('anchor', p.anchor)
print('p.parent =', p.parent)
print('p.name =', p.name)
print('p.stem =', p.stem)
print('p.suffix =', p.suffix)
print('p.drive =', p.drive)

# 上级目录
print('parents-1', Path.cwd().parents[0])
print('parents-2', Path.cwd().parents[1])
print('parents-3', Path.cwd().parents[2])
print('parents-4', Path.cwd().parents[3])
print('parents-5', Path.cwd().parents[4])

# 用os.path.dirname(path)将返回一个字符串，它包含path参数中最后一个斜杠
# 之前的所有内容。
before_dir = os.path.dirname(Path.cwd())
print('最后一个目录之前所有的目录', before_dir)

# os.path.basename(path)将返回一个字符串，它包含path参数
# 中最后一个斜杠之后的所有内容
last_dir = os.path.basename(Path.cwd() / 'hello3/1')
print('指定一个目录返回其最后目录', last_dir)

# 需要一个路径的目录名称和基本名称，就可以调用os.path. split()，获
# 得这两个字符串的元组
calcFilePath = os.path.abspath('test_directory.py')
calcPath = os.path.split(calcFilePath)
print('calcPath==', calcPath)
print('calcPath[0]==', calcPath[0])
print('calcPath[1]==', calcPath[1])

# os.sep正确的用斜杠分隔目录 ，并返回一系列单个文件夹的列表
sep_path = calcFilePath.split(os.sep)
print('sep_path', sep_path)
