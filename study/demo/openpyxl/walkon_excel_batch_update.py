# 导入库
import openpyxl

# 定义工作簿的路径
file = r'C:\Users\admin\PycharmProjects\pythonProject3\study\excel\test.xlsx'

# 导入工作簿
wb = openpyxl.load_workbook(file)

# 指定工作表 也可以 wb.active
ws = wb['new_test']

# 定义包含需要更新电子邮件的字典
EMAIL_UPDATES = {'马海燕': 'mhy123@qq.com'}

# 遍历工作表中所有行（从第1行到最大行），rowNum表示行号
for rowNum in range(1, ws.max_row):
    # 获取当前行第一列的内容
    userName = ws.cell(row=rowNum, column=1).value

    # 如果userName出现在EMAIL_UPDATES字典中
    if userName in EMAIL_UPDATES:
        # 在第六列单元格上更新电子邮件为EMAIL_UPDATES[userName]字典中对应的值
        ws.cell(row=rowNum, column=6).value = EMAIL_UPDATES[userName]

    # 保存更新后的工作表到updated.xlsx
    wb.save('updated.xlsx')