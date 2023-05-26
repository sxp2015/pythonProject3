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
import fitz  # 操作 PDF 文件的库 PyMuPDF
import io  # 读取二进制数据的库
from PIL import Image  # 处理图片的库
import tabula  # 读取表格数据的库
import pandas as pd  # 处理表格数据的库

# PDF 文件路径
pdf_file_path = os.path.join('pdf_files/查验报告.pdf')
doc = fitz.open(pdf_file_path)


def get_pdf_info():
    images = []
    # 获取文档中所有表格数据
    tables = []

    pages = []

    result = []

    # 遍历所有页面
    for page in doc.pages():
        pages.append(page)

        # 遍历页面的表格
        for block in page.get_text("blocks"):
            # 如果文本块是一张图片
            if block[0] == 1:
                # 读取图片数据并保存为 JPEG 文件
                img_data = block[4].get_raw_data('png')
                image = Image.open(io.BytesIO(img_data))
                image.save('image{}.jpg'.format(page + 1))

        for table in page.get_text('tables'):
            tables.append(table)

    table_texts = ''.join(tables)
    return {'pages': pages, 'images': images, 'tables': table_texts}


if __name__ == "__main__":
    res = get_pdf_info()
    print('*' * 80)
    print('res:', res)
