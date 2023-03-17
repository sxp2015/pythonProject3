from pathlib import Path

p1 = Path('test.txt')
# 读文件
p2 = open(Path('test.txt'))
p3 = open(Path('test.txt'), 'r')
# 读单行文件内容 readline 或 readline（s）
p4 = p3.readline()
# 读所有文件内容 返回一个列表
p5 = p3.readlines()

# 写文件将'w'作为第 二个参数传递给open()，以写模式将覆写原有的文件,
p6 = open(Path('test2.txt'), 'w')
p6.write('hello, world!\n')
p6.close()

# 写文件将'a'作为第 二个参数传递给open()，添加模式将在已有文件的末尾添加文本
p7 = open(Path('test.txt'), 'a')
p7.write('hello, world!\n')
p7.close()

print('p1读取出来的数据：\n', p1.read_text())
print('p2 open读取出来的数据：\n', p2.read())
print('p3 open读取出来的数据：\n', p3.read())
print('p4 open读取出来的数据', p4)


