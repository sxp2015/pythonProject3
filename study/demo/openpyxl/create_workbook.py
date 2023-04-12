import openpyxl

# 创建空工作簿
wb = openpyxl.Workbook()
# 激活定位到生成的当前文件
ws = wb.active
# 给表命名
ws.title = 'hello'

# 创建新工作表

wb.create_sheet(index=0, title='First Sheet')

# 保存表
wb.save('test_create_workbook.xlsx')
# 输出结果
print(wb.sheetnames)
