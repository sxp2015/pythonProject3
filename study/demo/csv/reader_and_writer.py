import csv

# 打开 'example.csv' 文件，并将其转化为一个读取器对象
csv_reader = csv.reader(open('example.csv'))
csv_DictReader = csv.DictReader(open('example.csv'), ['姓名', '年龄', '性别'])

# 写入
outputFile = open('output.csv', 'w', newline='')
csv_DictWriter = csv.DictWriter(outputFile, fieldnames=['Name', 'Pet', 'Phone'])
csv_DictWriter.writeheader()

csv_DictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555- 1234'})
csv_DictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
csv_DictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

outputFile.close()

# 打印当前行的编号
# for row in csv_reader:
#     print(f'当前行的编号是：{csv_reader.line_num}, 内容是：{row}')

# 将读取器对象转化为列表形式，保存到变量 csv_list 中
csv_list = list(csv_reader)

# 输出 csv_list 变量的值，以检查文件是否被正确读入
# print('reader_list', csv_list)

# 遍历 csv_list 列表，并输出每个元素的值和对应的序号
for i, csvItem in enumerate(csv_list):
    print(f'第{i + 1}个值是：{csvItem}')


# 另一种获取CSV文件内容的方法
for row in csv_DictReader:
    print(f'姓名:{row["姓名"]} 年龄：{row["年龄"]} 性别：{row["性别"]}')
