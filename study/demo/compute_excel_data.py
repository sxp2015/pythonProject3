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
# 定义所有省份浏览量的变量
province_set = set()
# 遍历表的所有行
for row_i in range(1, sheet.nrows):
    num = sheet.cell_value(row_i, 0)
    name = sheet.cell_value(row_i, 1)
    province = sheet.cell_value(row_i, 2)
    job = sheet.cell_value(row_i, 3)
    views = sheet.cell_value(row_i, 4)

    single = {
        'num': num,
        'name': name,
        'province': province,
        'views': views
    }
    all_data.append(single)
    province_set.add(province)
    # print('all-data:',all_data)
    # print('单元格数据', len(all_data))
    # print('行数据', len(province_set))

# 按省计算总浏览量
sum_list = []
for province_item in province_set:
    province_name = ''
    views_sum = 0
    for item in all_data:
        # print('views:', item['views'])
        if province_item == item['province']:
            views_sum += item['views']
            province_name = item['province']
    sum_item = {
        'province_name': province_name,
        'views_count': views_sum
    }
    sum_list.append(sum_item)

print('sum_list=', sum_list)

# 创建新工作簿和工作表
new_workbook = xlwt.Workbook()
new_sheet = new_workbook.add_sheet('统计结果')

# 写入内容（标题表头部分）
new_sheet.write(0, 0, '省份')
new_sheet.write(0, 1, '合计')

# 循环写入
for row in range(0, len(sum_list)):
    new_sheet.write(row + 1, 0, sum_list[row]['province_name'])
    new_sheet.write(row + 1, 1, sum_list[row]['views_count'])

# 保存
new_workbook.save('统计结果.xls')
