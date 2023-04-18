#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-03-12 18:34
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_xlutils.py
# @IDE     : PyCharm

# xlrd读取Excel时传入 formatting_info=True 报错
# 将.xlsx文件另存为.xls，然后再进行后续操作，亲测有效，能正常保存Excel原有格式，不用修改代码。
from xlutils.copy import copy
import xlwt
import xlrd
from study.utils.get_project_path import get_root_path

PROJECT_PATH = get_root_path()

temp_excel = xlrd.open_workbook(PROJECT_PATH + r'/study/test/xlutils/test.xls', formatting_info=True)
temp_sheet = temp_excel.sheet_by_index(0)

new_book = copy(temp_excel)
new_sheet = new_book.get_sheet(0)
style = xlwt.XFStyle()

# 字体
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360  # 对应18号字体大小 18*20=360
style.font = font

# 边框
borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

# 对齐
align = xlwt.Alignment()
align.horz = xlwt.Alignment.HORZ_CENTER
align.vert = xlwt.Alignment.VERT_CENTER
style.alignment = align

# 写入
new_sheet.write(0, 1, '测试1')
new_sheet.write(2, 3, '数据2')
new_sheet.write(2, 5, '有样式1', style)
new_sheet.write(2, 7, '无样式2', style)

# 保存
new_book.save('测试创建表并设置样式.xlsx')
