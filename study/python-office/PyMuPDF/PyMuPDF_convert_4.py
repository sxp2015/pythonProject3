#!/usr/bin/python3
# coding:utf-8
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved
#
# @Time    : 2023-05-26 21:12
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : conver_tesst.py
# @IDE     : PyCharm
# 导入必要的库
import os  # 处理文件和目录路径相关的功能
import re

import fitz  # 操作 PDF 文件的库 PyMuPDF
import io  # 读取二进制数据的库
from PIL import Image  # 处理图片的库
import tabula  # 读取表格数据的库
import pandas as pd  # 处理表格数据的库
from datetime import datetime
from openpyxl import Workbook

# PDF 文件路径
pdf_file_path = os.path.join('pdf_files/查验报告.pdf')
doc = fitz.open(pdf_file_path)


# 获取PDF中所有页面的图片数量
def get_table_cells_color():
    # 打开PDF文档
    doc = fitz.open(pdf_file_path)
    # 获取文档总页数
    page_count = doc.page_count
    # 定义颜色信息列表
    color_info_list = []

    # 遍历所有页面，统计满足条件的单元格数量
    condition_one = 0

    # 遍历每一页PDF页面
    for page_num, page in enumerate(doc):
        # 页面的所有行
        rows = page.get_text("table").split("\n")

        # 遍历每一行
        for i, row in enumerate(rows):

            # 得到每一行的所有单元格
            cells = row.strip().split("\t")

            # 遍历每一行的每一个单元格
            for j, cell in enumerate(cells):
                # 如果单元格中包含1,且只有一个单元格，并且不是第一页
                # print('cell', cell)
                if cell == '1' and len(cells) == 1 and page_num != 0:
                    # 累加汇总一共有多少个包含1的单元格
                    condition_one += 1
                    # 得到上一个单元格检查部位的单元格
                    # print('cell,', cell)
                    if j > 0:
                        pre_cell = cell[j - 1]
                        print('pre_cell', pre_cell)

                # print(f'在第{page_num + 1}页,第{i + 1}行 存在满足条件的单元格,总共有:{condition_one}个单元格')

            # # 如果不是第一行
            # if i > 0:
            #     # 获取上一行的所有单元格
            #     pre_row = rows[i - 1].strip().split("\t")
            #     # 遍历上一行的每个单元格
            #     for k in range(len(pre_row)):
            #         pre_cell = pre_row[k]
            #         print('pre_cell', pre_cell)


if __name__ == "__main__":
    print('*' * 80)

    print('返回结果：', get_table_cells_color())
