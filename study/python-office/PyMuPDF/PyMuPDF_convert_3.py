#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-30 5:16
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : PyMuPDF_convert_3.py
# @IDE     : PyCharm
import os

import fitz

pdf_file_path = os.path.join('pdf_files/查验报告.pdf')


# 获取指定 PDF 文件中指定单元格范围内所有页面的符合要求的图片数量
def get_images_count(file_path, start_cell_value='1', end_cell_value='1', width_threshold=1500, height_threshold=1100):
    # 打开 PDF 文件
    doc = fitz.open(file_path)

    # 定义图片计数器
    images_count = 0

    # 定义循环起始和结束标志
    start_flag = False
    end_flag = False

    # 遍历 PDF 文件的所有页面
    for page_num, page in enumerate(doc):
        if start_flag and end_flag:  # 如果已经找到了终点，直接退出
            break

        # 检查所有的文本块，以确定是否应该开始或结束循环
        blocks = page.get_text_blocks('table')

        for b in blocks:
            if b[4] == start_cell_value:
                start_flag = True
                end_flag = False
                break
            elif b[4] == end_cell_value:
                end_flag = True
                break
        if not start_flag or end_flag:  # 如果未找到起点或已经找到终点，继续下一页
            continue

        # 获取当前页面中的所有图像对象
        image_list = page.get_images()
        print('image_list:', image_list)
        # 遍历图像列表，统计符合要求的图像数量
        for img in image_list:
            # 获取图像对象对应的 Pixmap 对象
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)

            # 判断是否符合要求
            if pix.w >= width_threshold and pix.h >= height_threshold:
                images_count += 1

    # 关闭 PDF 文件
    doc.close()

    # 返回结果
    return images_count


if __name__ == "__main__":
    print('*' * 80)
    image_count = get_images_count(pdf_file_path)
    print('返回结果：', image_count)
