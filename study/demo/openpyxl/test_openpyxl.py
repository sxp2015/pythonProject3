import openpyxl
from openpyxl.utils import column_index_from_string, get_column_letter

"""
1．导入openpyxl模块。
2．调用openpyxl.load_workbook()函数。
3．取得Workbook对象。
4．使用active或sheetnames属性。
5．取得Worksheet对象。
6．使用索引或工作表的cell()方法，带上row和column关键字参数。
7．取得Cell对象。
8．读取Cell对象的value属性。
"""

# 定义文件路径
file = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\job.xlsx'
file2 = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\test.xlsx'
file3 = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\StaffHistoricalJob.xlsx'
# 读取文件
wb = openpyxl.open(file)
wb2 = openpyxl.load_workbook(file2)
wb3 = openpyxl.load_workbook(file3)
# 获取工作簿的表名列表
# print('表名列表：', wb.sheetnames)
# print('wb', type(wb))
# 从工作簿中获取一张表
sheet = wb['Sheet1']
sheet2 = wb2['new_test']
# 获取活动的表格
wb2_active = wb2.active
wb3_active = wb3.active

# 获取表的表名
# print('title = ', sheet.title)
# 获取当前活动的表
anotherSheet = wb.active
# print('anotherSheet', anotherSheet)

# 打印活动的表格
print('wb3_active', wb3_active)
print('wb3 sheets', wb3.sheetnames)

# 获取单元格的内容
A1 = sheet['A1']
B2 = sheet['B2'].value
C3 = sheet['C3']
# print('A1的内容是: ', A1)
# print('B2的内容是: ', B2)
#
# print('查询结果：', '第%s行, 第%s列 内容是: %s' % (A1.row, A1.column, A1.value))
#
# # 获取单元格的内容(传位置参数)
# print('第一行，第二列是值是：', sheet.cell(row=1, column=2).value)

# 获取指定列的位置字母或列位置数字
letter = get_column_letter(300)
num_letter = column_index_from_string('ABC')
# print('letter === ', letter)
# print('num_letter=== ', num_letter)

# 有数值的列中，最大列数
max_column = get_column_letter(sheet2.max_column)
# print('max_column', max_column)

# 获取指定区别的值
values = tuple(sheet2['A1':'L2'])
# print('values', values)

"""
要输出这个区域中所有单元格的值，我们使用两个for循环。外层for循环遍历这个
切片中的每一行❶。然后针对每一行，内层for循环遍历该行中的每个单元格❷。
"""

# for rowOfCellObjects in sheet2['A1':'L2']:
#     for cellObject in rowOfCellObjects:
#         print('行数:', cellObject.row, '单元格内容', cellObject.value)
#         print('列名:', cellObject.column_letter, '单元格内容', cellObject.value)
#         print('行列名:', cellObject.coordinate, '单元格内容', cellObject.value)
#     print('----END----')

# 遍历一张表的某一列数据
# for cell_obj in list(wb2_active.columns)[1]:
#     print('cell_obj_value ==', cell_obj.value)

# 通过 for 循环遍历 1 到 7 的整数序列（步长为 2）。
# 使用 sheet.cell(row=i, column=2) 方法获取当前表格的第 i 行、第 2 列单元格对象，并返回该单元格的值并打印输出。
# for i in range(1, 8, 1):
#     print('数据', i, sheet.cell(row=i, column=2).value)

# 遍历一张表的某一列数据
# for cell in list(wb3_active.columns):
#     print('cell_value ==', cell.value)
