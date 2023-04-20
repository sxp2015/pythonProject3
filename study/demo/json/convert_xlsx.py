import openpyxl
import csv


# 定义CSV文件路径
csv_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\demo\csv\output.csv'
# 先用正确的方法，打开文件，再读取csv文件，把数据变成列表
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile))

# 创建工作簿
workbook = openpyxl.Workbook()

# 获取第一个工作表
sheet = workbook.active

# 写入数据到工作表中
for row in data:
    sheet.append(row)

# 保存工作簿
workbook.save('new_xlsx_file.xlsx')


