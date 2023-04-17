from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference, Series

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 填充一些数据
for i in range(1, 6):
    ws.cell(row=i, column=1, value=f"Product {i}")
    ws.cell(row=i, column=2, value=i * 10)

# 创建一个柱状图
chart = BarChart()
chart.title = "产品销售数据表"
chart.x_axis.title = "产品"
chart.y_axis.title = "销售"

"""
Reference是openpyxl.chart模块中的一个类，用于指定图表的数据范围和类别范围。
它可以用于创建柱状图、线图、饼图等各种类型的图表。
Reference方法可以指定一个或多个单元格范围，以便在图表中使用。它的参数包括：
ws：表示要引用的工作表对象。
min_col：表示数据范围或类别范围的左上角单元格的列号。
min_row：表示数据范围或类别范围的左上角单元格的行号。
max_col：表示数据范围或类别范围的右下角单元格的列号。
max_row：表示数据范围或类别范围的右下角单元格的行号。
"""
# 设置图表数据
data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=5)
categories = Reference(ws, min_col=1, min_row=1, max_row=5)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# 将图表插入到工作表中
ws.add_chart(chart, "A7")

# 保存工作簿
wb.save("chart.xlsx")