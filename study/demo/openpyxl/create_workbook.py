import openpyxl
from openpyxl.styles import Font

try:
    wb = openpyxl.load_workbook('test_create2.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()
    # 创建新工作表
    wb.create_sheet(index=0, title='First Sheet')

    # 激活定位到生成的当前文件
    ws = wb.active
    # 给表命名
    ws.title = 'hello2'

    # 定义字体
    italic24font = Font(size=24, italic=True, bold=True)
    # 赋值并改变字体
    ws['A1'].value = 'hello world'
    ws['A1'].font = italic24font

    # 保存表
    wb.save('test_create2.xlsx')
    # 输出结果
    print(wb.sheetnames)

except Exception as e:
    print('出现异常:', e)
