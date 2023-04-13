import openpyxl
from openpyxl.styles import Font

try:

    # 使用 with 语句管理文件的打开和关闭
    wb = openpyxl.load_workbook('test_create_workbook.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()
    # 创建新工作表
    wb.create_sheet(index=0, title='First Sheet')

    # 激活定位到生成的当前文件
    ws = wb.active
    # 给表命名
    ws.title = 'hello'

    # 定义字体
    italic24font = Font(size=24, italic=True, bold=True)
    # 赋值并改变字体
    ws['A1'].value = 'hello world'
    ws['A1'].font = italic24font

    # 设置宽高
    ws.row_dimensions = 30
    ws.column_dimensions = 10

    sumResult = 0  # 汇总数据
    lastRow = 0  # 用于记录最后一行的空白栏
    for cell in ws.iter_rows(min_row=2, max_row=4, min_col=1, max_col=6):
        list_cell = list(cell)
        for index, item in enumerate(list_cell):
            item.value = index + 1
            sumResult += item.value
            # 用于记录最后一行的空白栏
            lastRow = index
            # print('item', item.value)
            # print('sum2', sumResult)

    print('最后一行是', lastRow)
    # 公式求和赋值
    ws['A' + str(lastRow)].value = '合计'
    ws['B' + str(lastRow)].value = sumResult
    ws['C' + str(lastRow)].value = '=sum(A2:F4)'

    # 保存表
    wb.save('test_create_workbook.xlsx')
    # 输出结果
    print(wb.sheetnames)

except Exception as e:
    print('出现异常:', e)
