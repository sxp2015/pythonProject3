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
def get_images_count():
    # 从开始点统计到结束点row==‘1’为止，累加所有的图片数量

    images_list = []
    for page_num, page in enumerate(doc):
        rows = page.get_text("table").split("\n")

        # 遍历每一行
        for i, row in enumerate(rows):
            # 如果单元格图片
            cells = row.strip().split("\t")

            for j, cell in enumerate(cells):
                if '1' in cell:
                    # print(f'数字1出现在: 第{page_num + 1}页，第{i + 1}行，第{j + 1}列')
                    # 找到起始页
                    start_page = page_num

                    # 找到结束点row==‘1’为止
                    end_page = start_page + 1
                    for k in range(i + 1, len(rows)):
                        if '1' in rows[k].strip().split('\t'):
                            end_page = page_num + k - i
                            break

                    # 遍历每个单元格，统计其中符合要求的图片数量
                    for m in range(start_page, end_page):
                        cells_on_page = rows[i:end_page]
                        images_count = 0
                        for n, cell_on_page in enumerate(cells_on_page):
                            cell_info = cell_on_page.strip().split('\t')[j].strip()
                            if '1' in cell_info:
                                image_results = doc.load_page(m).get_images(cell_info)
                                for img in image_results:
                                    xref = img[0]
                                    pix = fitz.Pixmap(doc, xref)
                                    if pix.w >= 1500 and pix.h >= 1100:
                                        images_count += 1
                                images_dict = {'page_num页码:': m+1, 'cell_info': cell_info, 'images_count': images_count}
                                images_list.append(images_dict)

                    break

        # 如果当前页数超过总页数，则跳出循环
        if page_num >= len(doc):
            break

    return images_list


if __name__ == "__main__":
    print('*' * 80)

    print('返回结果：', get_images_count())
