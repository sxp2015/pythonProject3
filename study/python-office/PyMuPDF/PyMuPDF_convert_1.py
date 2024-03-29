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
dt = datetime.now().strftime("%Y%m%d-%H%M%S%f")


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
    total_pages = doc.page_count

    # 定义颜色信息列表
    color_info_list = []

    # 创建图片存放目录
    pixmap_images_dir = "pixmap_images"
    if not os.path.exists(pixmap_images_dir):
        os.mkdir(pixmap_images_dir)

    # 创建文本存放目录
    pixmap_text_dir = "text_images"
    if not os.path.exists(pixmap_text_dir):
        os.mkdir(pixmap_text_dir)

    # 定义符合要求的图片存放目录
    cell_image_dir = "cell_images"
    if not os.path.exists(cell_image_dir):
        os.makedirs(cell_image_dir)

    # 定义目标像素RGB值
    target_rgb = (255, 199, 0)

    # 定义列表变量用于存储单元格提取后整合的数据
    cell_data_list = []

    # 定义循环文档的起始页和结束页
    start_page = None

    start_index = 0  # 开始处理的行索引

    # 定义循环文档的结束页
    end_page = total_pages - 1

    # 定义检查部位
    check_part_name = None

    # 定义检查部位列表
    check_part_name_list = []

    # 宽1500，高1100 像素图片列表
    pix_image_list = []

    # 替换的特殊符号列表
    replace_symbol_list = ['/', '、', ' ', '。', '，', '；', ':', '\\', 'u3000', '\t']

    # 定义变量记录符合要求的图片数量计数
    image_count = 0

    # 定义图片索引号
    image_index = 0

    # 检查XObject对象的正则表达式
    checkXO = r'/Type(?=*/XObject)'
    # 检查Image对象的正则表达式
    checkIM = r'/Subtype(?=*/Image)'

    # 获取对象长度
    lenXREF = doc.xref_length()

    print(f'lenXREF:{lenXREF},页面数: {len(doc)}')

    # 将 start_page 和 end_page 按需进行处理
    if start_page is None:
        start_page = 0
    elif start_page >= total_pages:
        raise ValueError("起始页码超出文档总页数！")
    else:
        start_page -= 1

    if end_page is None:
        end_page = total_pages
    elif end_page > total_pages:
        raise ValueError("终止页码超出文档总页数！")
    else:
        end_page -= 1

    # 遍历每一页PDF页面

    # for page_num, page in enumerate(doc, start=start_page):
    for page in range(1, lenXREF+1):

        # 获取所有页面的文本内容
        #  rows = page.get_text().split("\n")

        text = doc.extract_image(page)

        isXObject = re.search(checkXO, text)

        isImage = re.search(checkIM, text)

        print('text:', text)

    #     # 得到当前页面的所有图片列表
    #     page_image_list = page.get_images()
    #
    #     # print('cell_images_list:', doc_images_list)
    #     # print('【rows:】', rows)
    #
    #     # 遍历每一页的每一行文本
    #     for i, row in enumerate(rows[start_index:]):
    #
    #         # 获取每行的所有单元格列表
    #         cells = row.strip().split("\t")
    #
    #         # 输出测试
    #         # print('rows:', rows[i], 'index:', i)
    #
    #         # print('【cells:】', cells)
    #         # 如果是检查部位的单元格位置
    #
    #         # 遍历每一行的每一个单元格
    #         for j, cell in enumerate(cells):
    #
    #             # 定义符合条件的图片文件存储名称
    #             pixmap_file_name = f'page-{page_num + 1}_{rows[i]}_{cells[j]}_{dt}.png'
    #
    #             # 循环替换特殊字符
    #             for special_char in replace_symbol_list:
    #                 pixmap_file_name = pixmap_file_name.replace(special_char, '_')
    #
    #             # 查找每个单元格的位置信息
    #             cell_position_list = page.search_for(cell)
    #             # print('cell_position_list:', cell_position_list)
    #
    #             # 如果单元格有值说明单元格是文本
    #             if cell_position_list:
    #                 # print(f'单元格内容：{cell},行索引号{i}，列索引号{j}')
    #
    #                 # 遍历单元格位置坐标
    #                 for cell_index, cell_position in enumerate(cell_position_list[start_index:]):
    #
    #                     # 确定检查部位在页面的位置
    #                     # 将找到的单元格位置信息转换为 fitz.Rect 对象，以便后续获取该单元格的颜色信息。
    #                     cell_rect = fitz.Rect(cell_position.x0, cell_position.y0, cell_position.x1,
    #                                           cell_position.y1)
    #                     # print('cell_rect:', cell_rect)
    #
    #                     # 加上矩形的尺寸判断条件
    #                     # print('文字:', cell_text, '矩形宽度:', cell_rect.width,
    #                     #      '矩形宽度:', cell_rect.height, '坐标:', cell_position)
    #
    #                     # 使用 get_pixmap() 方法获取指定范围内的图像数据，并返回 fitz.Pixmap 对象。
    #                     # 得到像素图对象
    #                     pixmap = page.get_pixmap(matrix=fitz.Identity, colorspace=fitz.csRGB, clip=cell_rect)
    #
    #                     # 调用获取单元格图片信息的方法，对像素图进行处理，返回图片的RGB值和其他信息
    #                     cell_image_info = get_image_info(cell, pixmap)
    #
    #                     # 根据RGB颜色值判断是否为目标像素RGB值
    #                     if cell_image_info and cell_image_info[0]['RGB_Color'] == target_rgb:
    #                         # print('cell_image_info:', cell_image_info)
    #                         # 给查检部位赋值
    #                         check_part_name = rows[i]
    #                         check_part_name_list.append(check_part_name)
    #                         start_page = page_num
    #                         start_index = i + 1 if check_part_name in rows[i + 1:] else 0
    #                         image_index = 0
    #                         break
    #                         # print('page_rgb_in_rows:', i + 1, 'page_num:', page_num + 1, 'check_part_name',
    #                         #       check_part_name)
    #
    #                         # 得到当前的索引下标
    #                         # cell_index = cell_position_list[cell_index]
    #
    #                         # print('cell_index:', cell_index)
    #
    #                         # print('rows[i]:', i, 'cells[j]:', j)
    #
    #                         # 把检查的部位添加到单元格数据列表
    #                         # cell_data_list.append(
    #                         #     {'check_part': check_part_name, 'cell_text_list': cell_text_list})
    #                         # print(f'部位名称:{rows[i]}')
    #                         # print(f'部位名称:{cells[j]}')
    #                         # 定义图片保存路径
    #                         pixmap_image_path = os.path.join(pixmap_images_dir, pixmap_file_name)
    #                         # 保存目标像素RGB值为图片
    #                         # pixmap.save(pixmap_image_path)
    #
    #                     # 定义文本转图片的保存路径
    #                     pixmap_text_path = os.path.join(pixmap_text_dir, pixmap_file_name)
    #                     # 保存检查部位的像素RGB值为图片
    #                     # pixmap.save(pixmap_text_path)
    #                     print('pixmap_text_path:', pixmap_text_path)
    #
    #                     # 如果是检查部位点并且有值
    #                     if check_part_name:
    #                         # 得到坐标的文字列表
    #                         cell_text = page.get_textbox(rows[i + 1])
    #                         # print('cell_text[rows[i+1]]:', cell_text)
    #                         #
    #                         print('cell_text:', cell_text)
    #                         # print('cell_image_list:', page_image_list)
    #
    #                         if rows[i] != check_part_name:
    #                             continue
    #                         else:
    #                             image_index = 0
    #
    #     # 如果是检查部位，则开始遍历当前页面的所有图片，保存符合条件的图片
    #     for image_index, cell_images in enumerate(page_image_list):
    #         if check_part_name:
    #             # 遍历每一页PDF的图片列表
    #             # 定义问题点图片文件的存储名称
    #             cell_file_name = f'page-{page_num + 1}-{check_part_name}-count-{image_index + 1}-{dt}.png'
    #             # 循环替换特殊字符
    #             for special_char in replace_symbol_list:
    #                 cell_file_name = cell_file_name.replace(special_char, '_')
    #
    #             # 一个图片对象中获取了图片在文档中的位置信息，即 xref。
    #             xref = cell_images[0]
    #
    #             # 从指定的 PDF 文档中获取一个图片对象的像素图。 doc: 文档对象 ，xref:图片在文档中的位置信息/编号
    #             pix = fitz.Pixmap(doc, xref)
    #
    #             # 如果图片符合条件并且是检查部位有值
    #             if pix.w >= 1500 and pix.h >= 1100:
    #                 # 图片计数
    #                 image_index += 1
    #                 # 组合图片的保存路径
    #                 image_path = os.path.join(cell_image_dir, cell_file_name)
    #                 # 保存符合条件的图片
    #                 # pix.save(image_path)
    #                 print('image_path:', image_path)
    #             pix = None
    #             continue
    #         else:
    #             pix_image_list.append(cell_images)
    #             cell_data_list.append({'pix_image_list': pix_image_list})
    #             print('pix_image_list length:', len(pix_image_list))
    #     # 如果结束处理页码等于当前页面的页码，则结束循环
    #     if end_page == page_num and start_index == 0:
    #         break
    #     elif rows[i] == check_part_name:
    #         break
    # # 返回整合后的数据
    # return cell_data_list


if __name__ == "__main__":
    print('返回结果：', get_table_cells_color())
