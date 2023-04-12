import openpyxl

# 打开文件（如果文件不存在则创建）
try:
    wb = openpyxl.load_workbook('test_create_workbook.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()

# 获取所有工作表数量
sheet_num = wb.sheetnames.__len__()

# 激活定位到生成的当前文件
ws = wb.active

# 给表命名（每次运行自动递增）
new_name = f'Sheet-{sheet_num + 1}'

# 创建新工作表
wb.create_sheet(index=0, title=new_name)

# 保存工作表
wb.save('test_create_workbook.xlsx')

# 输出结果
print(f'New sheet name: {new_name}')
print(f"All sheet names: {wb.sheetnames}")
