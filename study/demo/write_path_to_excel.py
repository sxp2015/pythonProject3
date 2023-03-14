import xlwt
import os

# 定义路径
file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\demo'

# 列出路径
list_path = os.listdir(file_path)

# 创建工作簿\工作表
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('打印路径到表.xls')

# 定义一个行变量
row = 0

# 遍历路径
for item in list_path:
    sheet.write(row, 0, item)
    row += 1
workbook.save('打印路径到表.xls')
