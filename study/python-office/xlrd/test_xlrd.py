#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-03-12 16:11
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_xlrd.py
# @IDE     : PyCharm
import xlrd

from study.utils.get_project_path import get_root_path

PROJECT_PATH = get_root_path()
# 打开工作表
# xlsx = xlrd.open_workbook(PROJECT_PATH + '/study/excel/test.xls')
xlsx = xlrd.open_workbook('test.xlsx')

# 三种读取表内容的方式
sheet = xlsx.sheet_by_index(0)
sheet_1 = sheet.cell_value(0, 0)
sheet_2 = sheet.cell(0, 1).value
sheet_3 = sheet.row(0)[2].value

print('sheet_1= ', sheet_1)
print('sheet_2= ', sheet_2)
print('sheet_3= ', sheet_3)

# 读取表名(方法一)
for i in range(0, xlsx.nsheets):
    sheet = xlsx.sheet_by_index(i)
    print('i=', i)
    print('sheet=', sheet.name)

# 读取表名(方法二)
for j in xlsx.sheet_names():
    print('sheetName= ', j)
