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
import struct
from collections import Counter

import fitz  # 操作 PDF 文件的库 PyMuPDF
import io  # 读取二进制数据的库

import numpy as np
from PIL import Image  # 处理图片的库
import tabula  # 读取表格数据的库
import pandas as pd  # 处理表格数据的库
from datetime import datetime
from openpyxl import Workbook

# PDF 文件路径
pdf_file_path = os.path.join('pdf_files/查验报告.pdf')
doc = fitz.open(pdf_file_path)

# 获取当前时间并格式化，用于保存图片命名
dt = datetime.now().strftime("%Y%m%d_%H%M%S")


# 获取像素图出现次数最多的颜色
def get_most_common_color(pixmap):
    # 定义列表用于整合颜色数据
    most_color_list = []

    # 提取像素图的宽和高
    width, height = pixmap.width, pixmap.height

    # 遍历宽和高，获得每个像素点的RGB值
    for y in range(height):
        for x in range(width):
            r, g, b = pixmap.pixel(x, y)
            # print(f"Pixel ({x}, {y}): R={r}, G={g}, B={b}")

    # 将 pixmap 转换为 Numpy 数组
    arr = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape((pixmap.height, pixmap.width, pixmap.n))

    # 获取颜色出现次数
    color_counts = Counter(map(tuple, arr.reshape(-1, arr.shape[-1])))

    # 选取出现次数最多的颜色
    most_common_color = color_counts.most_common(1)[0][0]

    # print( f"Most common color-占比最大的颜色RGB值: " f"R={most_common_color[0]}, G={most_common_color[1]},
    # B={most_common_color[2]},出现次数：{max(color_counts.values())}")

    most_color_list.append(
        {'RGB_Color': (most_common_color[0], most_common_color[1], most_common_color[2]),
         'count': max(color_counts.values())})

    return most_color_list


# 获取图像详细信息,得到出现最多的颜色的RGB值,并保存为图片
def get_image_info(cell, pixmap):
    # 创建图片存放目录
    if not os.path.exists("pixmap_image"):
        os.mkdir("pixmap_image")
    # 像素图的色彩空间
    color_space = pixmap.colorspace
    # 确定使用的颜色
    color_count = pixmap.color_count()
    # 确定最常用颜色的份额占比
    top_colors = pixmap.color_topusage()
    # 调用方法获取出现最多的颜色
    most_color_list = get_most_common_color(pixmap)
    # print('most_color_list:', most_color_list)

    # most_color_count = most_color_list[0]['count']
    # 出现最多的次数
    # most_color_value = max(most_color_count.values())
    # 定义出现最多的颜色

    # for color in most_color_count:
    #     most_color = most_color_count[color]
    #     if max(most_color_count.values()) == most_color:
    #         most_rgb_colors.append(color)
    #         print(f"颜色：{color},出现次数：{most_color}次")

    # print('most_rgb_color:', most_rgb_color)
    # 获取像素图的RGB值，返回是一个 bytes 对象
    # color_rgb = pixmap.samples
    # print('color_space-色彩空间:', color_space)
    # print('color_space-色彩空间:', color_space)
    # print('most_color-最多的颜色:', most_color[0])
    # print('top_colors-占比是:', round(top_colors[0] * 100, 2), '%')
    # print('color_rgb:', color_rgb)
    # print('=' * 30)
    # 保存像素图为图片

    pixmap.save(f'pixmap_image/{cell}-{dt}.png')
    if isinstance(color_space, type(fitz.csRGB)):
        min_val = 0
        max_val = 255
    elif color_space == "DeviceGray":
        min_val = max_val = pixmap.n - 1
    else:
        raise ValueError(f"Unexpected color space: {color_space}")
    # print(f"颜色空间：{color_space}, 范围值：{min_val}～{max_val}")

    # 获取图片中的像素点数
    n_pixels = pixmap.width * pixmap.height
    # 颜色图片中的列表
    colors = [pixmap.pixel(x, y) for x in range(pixmap.width) for y in range(pixmap.height)]
    # print(f"像素点数量：{n_pixels}")
    # print(f"颜色列表：{colors}")

    return most_color_list


# 获取PDF中所有页面的图片数量
def get_table_cells_color():
    # 打开PDF文档
    doc = fitz.open(pdf_file_path)
    # 获取文档总页数
    page_count = doc.page_count
    # 定义颜色信息列表
    color_info_list = []

    # 遍历每一页PDF页面
    for page_num, page in enumerate(doc):
        # 获取所有页面的文本内容
        rows = page.get_text().split("\n")

        # 遍历每一行
        for i, row in enumerate(rows):

            # 获取每行的所有单元格
            cells = row.strip().split("\t")

            # 遍历每一行的每一个单元格
            for j, cell in enumerate(cells):

                # 如果单元格中包含1,且只有一个单元格，并且不是第一页
                if cell == '入户门' and len(cells) == 1 and page_num != 0:
                    # 使用 search_for() 方法查找包含"入户门"文本的单元格位置信息，并取第一个结果。
                    cell_position = page.search_for(cell)[0]
                    # print('得到单元格的位置信息：', cell_position)

                    # 将找到的单元格位置信息转换为 fitz.Rect 对象，以便后续获取该单元格的颜色信息。
                    rect = fitz.Rect(cell_position.x0, cell_position.y0, cell_position.x1, cell_position.y1)
                    # 使用 get_pixmap() 方法获取指定范围内的图像数据，并返回 fitz.Pixmap 对象。
                    pixmap = page.get_pixmap(matrix=fitz.Identity, colorspace=fitz.csRGB, clip=rect)
                    # print('pixmap:', pixmap)

                    # 对图片进行处理，获取图片信息
                    cell_image_info = get_image_info(cell, pixmap)

                    # 将图片信息加入到列表中
                    color_info_list.append({'page_num': page_num,
                                            'cell_position': cell_position,
                                            'cell_image_info': cell_image_info,
                                            'pixmap_width': pixmap.width,
                                            'pixmap_height': pixmap.height})

            # print(f'在第{page_num + 1}页,第{i + 1}行 存在满足条件的单元格,总共有:{condition_one}个单元格')

    # 打印颜色信息列表
    return color_info_list


if __name__ == "__main__":
    print('*' * 80)

    print('返回结果：', get_table_cells_color())
