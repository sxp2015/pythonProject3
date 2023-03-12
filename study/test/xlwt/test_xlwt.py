# !/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-03-12 16:59
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_xlwt.py
# @IDE     : PyCharm
import xlwt

from study.utils.get_project_path import get_root_path

PROJECT_PATH = get_root_path()

# 创建工作簿
new_book = xlwt.Workbook()
# 创建新的工作表
new_sheet = new_book.add_sheet('测试的新表')
# 写入内容
new_sheet.write(0, 0, '序号')
new_sheet.write(0, 1, '标题')

# 保存工作簿
new_book.save('test_write.xlsx')
