import xlrd

xlsx = xlrd.open_workbook('test.xlsx')
table = xlsx.sheet_by_index(0)
print(table.cell_value(0, 0))
