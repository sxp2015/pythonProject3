import openpyxl

# 定义文件路径
file = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\job.xlsx'
# 读取文件
wb = openpyxl.open(file)
# 获取表名列表
print('表名列表：', wb.sheetnames)
print('wb', type(wb))
