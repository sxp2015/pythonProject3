import random
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 随机生成一些数据
for row in range(1, 11):
    for col in range(1, 6):
        ws.cell(row=row, column=col, value=random.randint(1, 100))

# 打印原始数据
print("原始数据：")
for row in ws.iter_rows(min_row=1, max_row=10, min_col=1, max_col=5, values_only=True):
    print('\t'.join(str(cell) for cell in row))

# 翻转行和列
new_ws = Workbook().active
for row in range(1, 6):
    for col in range(1, 11):
        new_ws.cell(row=row, column=col, value=ws.cell(row=col, column=row).value)

# 打印翻转后的数据
print("翻转后的数据：")
for row in new_ws.iter_rows(min_row=1, max_row=5, min_col=1, max_col=10, values_only=True):
    print('\t'.join(str(cell) for cell in row))

# 保存工作簿
wb.save("random_data.xlsx")