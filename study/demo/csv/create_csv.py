import csv

# CSV文件头部
header = ['姓名', '年龄', '性别']

# 要写入CSV文件的数据
data = [
    ['张三', 25, '男'],
    ['李四', 30, '女'],
    ['王五', 28, '男']
]

# 创建CSV文件并写入数据
with open('example.csv', 'w', newline='', encoding='ansi') as file:
    # delimiter分隔单元格的符号
    # lineterminator='\n\n' 行距
    writer = csv.writer(file, delimiter=',', lineterminator='\n\n')

    # 写入文件头部
    writer.writerow(header)

    # 写入数据行
    for row in data:
        writer.writerow(row)
