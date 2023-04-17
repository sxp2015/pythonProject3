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


# 自定义函数：插入空白行或列
def insert_blank(ws, index, is_row=True):
    """
    在工作表中插入空白行或列

    参数：
    - ws：工作表对象
    - index：要插入的行号或列名
    - is_row：是否插入行（True表示插入行，False表示插入列）


    返回值：无
    """
    if is_row:
        ws.insert_rows(index)
    else:
        """
        column_index_from_string 字母转列号
        get_column_letter 列号转字母
        """
        col = column_index_from_string(index)  # 转成列号
        ws.insert_cols(col)


# 调用自定义函数插入空白行和列
insert_blank(ws, 3, is_row=True)
insert_blank(ws, 'C', is_row=False)

# 打印数据和插入的空白行/列
for row in range(1, 13):
    for col in range(1, 7):
        print(ws.cell(row=row, column=col).value, end='\t')
    print()

# 保存工作簿
wb.save("insert_blank.xlsx")
