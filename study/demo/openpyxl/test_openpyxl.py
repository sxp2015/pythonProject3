import openpyxl

# 定义文件路径
file = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\job.xlsx'
# 读取文件
wb = openpyxl.open(file)
# 获取工作簿的表名列表
print('表名列表：', wb.sheetnames)
# print('wb', type(wb))
# 从工作簿中获取一张表
sheet = wb['Sheet1']
# 获取表的表名
print('title = ', sheet.title)
# 获取当前活动的表
anotherSheet = wb.active
print('anotherSheet', anotherSheet)

# 获取单元格的内容
A1 = sheet['A1']
B2 = sheet['B2'].value
C3 = sheet['C3']
print('A1的内容是: ', A1)
print('B2的内容是: ', B2)

print('查询结果：', '第%s行, 第%s列 内容是: %s' % (A1.row, A1.column, A1.value))

# 获取单元格的内容(传位置参数)
print('第一行，第二列是值是：', sheet.cell(row=1, column=2).value)


# 通过 for 循环遍历 1 到 7 的整数序列（步长为 2）。
# 使用 sheet.cell(row=i, column=2) 方法获取当前表格的第 i 行、第 2 列单元格对象，并返回该单元格的值并打印输出。
for i in range(1, 8, 1):
    print('数据', i, sheet.cell(row=i, column=2).value)
