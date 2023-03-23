import shutil, os
from pathlib import Path
import send2trash

# 利用os模块中的函数，可以删除一个文件或一个空文件夹。利用shutil模块，可以删除一个文件夹及其所有的内容。
# 返回显示会被删除的文件
# 调用os.unlink(path)将删除path处的文件。
# os.unlink('test1/hello.txt')

# 调用os.rmdir(path)将删除path处的文件夹。该文件夹必须为空，其中不能有任何文件和文件夹。
# os.rmdir('a')

# # 调用shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都会被删除。
# shutil.rmtree('b')


# for filename in Path.cwd().glob('*'):
# os.unlink(filename) //删除文件
# print('file', filename)

# 用send2trash模块安全地删除
# 它会将文件夹和文件发送到计算机的回收站，而不是永久删除它们

# baconFile = open('bacon.txt', 'a')  # creates the file
# baconFile.write('Bacon is not a vegetable.')
#
# baconFile.close()
# send2trash.send2trash('bacon.txt')


# range()，os.walk()在循环的每次迭代中返回以下3个值。
# 当前文件夹名称的字符串。
# 当前文件夹中子文件夹的字符串的列表。
# 当前文件夹中文件的字符串的列表。
for folderName, sub_folders, filenames in os.walk(Path().cwd()):
    print('The current folder is ' + folderName)
    for sub_folder in sub_folders:
        print('SUB FOLDER OF ' + folderName + ': ' + sub_folder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        print('')
