import openpyxl
from openpyxl.styles import Font

try:
    wb = openpyxl.load_workbook('test_create_workbook.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()
    # 创建新工作表
    wb.create_sheet(title='First Sheet', index=0)

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
    ws.row_dimensions[1].height = 30
    ws.column_dimensions['A'].width = 10

    sumResult = 0  # 汇总数据
    lastRow = 0  # 用于记录最后一行的空白栏
    for row in ws.iter_rows(min_row=1, max_row=4, min_col=1, max_col=6):
        for index, cell in enumerate(row):
            cell.value = index + 1
            sumResult += cell.value
            # 用于记录最后一行的空白栏
            lastRow = cell.row

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