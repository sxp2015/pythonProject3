import xlrd
import xlwt
from study.utils.get_project_path import get_root_path

PROJECT_PATH = get_root_path()
# 读取Excel
workbook = xlrd.open_workbook(PROJECT_PATH + r'\study\excel\job.xlsx')
# 读取Sheet
sheet = workbook.sheet_by_index(0)
# 定义所有单元格数据的变量
all_data = []
# 定义所有学生数量的变量
num_set = set()
# 遍历表的所有行
for row_i in range(1, sheet.nrows):
    num = sheet.cell_value(row_i, 0)
    name = sheet.cell_value(row_i, 1)
    province = sheet.cell_value(row_i, 2)
    job = sheet.cell_value(row_i, 3)
    views = sheet.cell_value(row_i, 4)

    employee = {

        'name': name,
        'province': province,
        'views': views
    }
    all_data.append(employee)
    num_set.add(num)
    print('all-data:',all_data)
