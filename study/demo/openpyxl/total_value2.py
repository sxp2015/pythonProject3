import openpyxl
from openpyxl.styles import Font

try:
    # 使用 with 语句管理文件的打开和关闭
    wb = openpyxl.load_workbook('test_create_workbook.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()
    # 创建新工作表
    ws = wb.create_sheet(index=0, title='hello')

    # 定义字体
    italic24font = Font(size=24, italic=True, bold=True)
    # 赋值并改变字体
    ws['A1'].value = 'hello world'
    ws['A1'].font = italic24font

    # 设置行高和列宽
    for i in range(1, 5):
        ws.row_dimensions[i].height = 70
    for i in range(1, 7):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = 20

    sumResult = 0  # 汇总数据
    lastRow = 0  # 用于记录最后一行的空白栏
    for cell in ws.iter_rows(min_row=2, max_row=4, min_col=1, max_col=6):
        list_cell = list(cell)
        for index, item in enumerate(list_cell):
            item.value = index + 1
            sumResult += item.value
            # 用于记录最后一行的空白栏
            lastRow = cell[0].row

    # 公式求和赋值
    ws['A' + str(lastRow + 1)].value = '合计'
    for col in ['B', 'C', 'D', 'E', 'F']:
        ws[col + str(lastRow + 1)].value = '=SUM(' + col + '2:' + col + '4)'

    # 保存表
    wb.save('test_create_workbook.xlsx')
    # 输出结果
    print(wb.sheetnames)

except Exception as e:
    print('出现异常:', e)