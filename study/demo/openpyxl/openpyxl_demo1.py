"""
需求：从指定表格中，统计指定列的值

active属性则是直接返回当前活动的工作表对象，即当前被打开并查看的工作表。
通过.active属性可以避免手动指定工作表名的麻烦，使得代码更加简洁和易读
"""
# 导入库
import numbers

import openpyxl

# 定义工作簿的路径
file = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\test.xlsx'

# 导入工作簿
wb = openpyxl.load_workbook(file)

# 指定工作表 也可以 wb.active
# sheet = wb.active
ws = wb['new_test']

# 指定工作表的列
cell_values = tuple(ws['$C':'$C'])

# 遍历数据
sum_value = 0
for cell in cell_values:
    if cell.value is None:
        continue

        # isinstance是Python内置函数，用于判断一个对象是否是指定类或其子类的实例。这个函数有两个参数：第一个是要判断的对象，
        # 第二个是类名或其元组。如果第一个参数是第二个参数指定的类或其子类的实例则返回True，否则返回False

    elif isinstance(cell.value, (float, str)):
        sum_value += int(cell.value)
    else:
        print(f"Warning! The value in cell {cell.coordinate} is not a number: {cell.value}")

    # 打印求和结果
    print(f"The sum of column C is {sum_value}")

