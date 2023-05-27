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


# 提取表格单元格中的信息
def extract_table_cells(page):
    # 调用 get_text("table") 方法获取表格数据
    table_data = page.get_text("table")

    # print('*' * 80)
    # print('table_data:', table_data)

    # 如果表格数据为空，则返回空列表
    if not table_data:
        return []

    # 将表格数据按行分割
    rows = table_data.split("\n")

    # 用于存储单元格数据和位置信息的列表
    table_cells = []

    # 遍历表格数据的每一行
    for i, row in enumerate(rows):
        # 将每一行按制表符（\t）分割成各个单元格
        cells = row.strip().split("\t")

        # 如果该行不为空，则遍历该行中的所有单元格
        if cells:
            for j, cell in enumerate(cells):
                # 使用 search_for 方法查找 PDF 中的单元格
                search_result = page.search_for(cell)
                print(f'从第{j + 1}页中获取到的单元格的值是： {cell}')
                print(f'search_result： {search_result}')
                if search_result:
                    # 遍历 search_for 方法返回的所有对象
                    for obj in search_result:
                        # 将对象转换为 Rect 类型，并获取其位置信息
                        # search_for 方法返回的结果是一个列表，其中每个元素都是一个包含四个元素的元组，
                        # 分别表示匹配项的左、上、右、下四个角的坐标。这四个坐标可以用来创建一个 fitz.Rect 对象，
                        # 从而表示该匹配项在 PDF 页面上的位置和大小。因此，代码中的 bbox = fitz.Rect(obj[:4])
                        # 表示将第一个匹配项的四个坐标传递给 fitz.Rect 构造函数，创建一个 Rect 对象并将其赋值给 bbox 变量。
                        # 结果就是 bbox 变量包含了这个匹配项在页面上的位置和大小信息，可以用于后续的处理。
                        bbox = fitz.Rect(obj[:4])
                        # print('bbox', bbox)
                        # 将单元格的数据和位置信息添加到列表中
                        table_cells.append({
                            "value": cell,
                            "page_num": page.number+1,
                            "left": bbox.x0,
                            "top": bbox.y0,
                            "right": bbox.x1,
                            "bottom": bbox.y1
                        })
        # print('table_cells',table_cells)
        return table_cells


# 获取pdf文档每页的文字信息
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
        # 获取当前页的所有图片
        pixmaps = page.get_pixmap()
        if isinstance(pixmaps, fitz.Pixmap):
            # 如果只有一张图片，则将其转换为列表形式
            pixmaps = [pixmaps]

        # for index, pixmap in enumerate(pixmaps):
        #     # 获取像素数据
        #     samples = pixmap.samples
        #     width = pixmap.width  # 图像宽度
        #     height = pixmap.height  # 图像高度
        #     colorspace = pixmap.colorspace  # 图像颜色空间
        #     # 将图片数据存储为 JPEG 格式文件
        #     # print(index, pixmap, width, height, colorspace)
        #     if colorspace == 'DeviceGray':
        #         mode = 'L'
        #     else:
        #         mode = 'RGB'
        #     image = Image.frombuffer(mode, (width, height), samples)
        #     image.save('image{}_{}.jpg'.format(page.number, index))

        for table in page.get_text('tables'):
            tables.append(table)

    table_texts = ''.join(tables)
    return {'pages': pages, 'images': images, 'tables': table_texts}


# # 遍历所有页面
# for page in doc:
#     # 提取当前页的表格单元格数据，并将其添加到总列表中
#     table_cells_list += extract_table_cells(page)
#
#
#
# # 打印所有表格单元格数据
# for cell_data in table_cells_list:
#     print(cell_data)


# 判断PDF中是否有图片

def find_images_in_pdf(pdf_path):
    # 用于存储所有表格单元格数据的列表
    table_cells_list = []

    if not os.path.exists("pdf_image"):
        os.mkdir("pdf_image")
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):

        # 获取图片列表
        image_list = page.get_images()
        if image_list:
            print(f"Page {page_num + 1} contains {len(image_list)} image(s):")
            for image_index, image in enumerate(image_list):
                xref = image[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.w >= 1500 and pix.h >= 1100:
                    image_dir = "pdf_image"
                    if not os.path.exists(image_dir):
                        os.makedirs(image_dir)
                    image_path = os.path.join(
                        image_dir, f"查验报告_page{page_num + 1}_image{image_index + 1}.png"
                    )
                    # pix.save(image_path)
                    print(f"\t{image_path}")
                pix = None
        else:
            print(f"Page {page_num + 1} does not contain any images.")

        # 对当前页执行表格提取
        table_cells_list += extract_table_cells(page)

        # 如果存在表格，则打印表格数据
        if table_cells_list:
            print('table_cells_list',table_cells_list)
            # for table in table_cells_list:
            #     # print("=" * 20)
            #     for row in table:
            #         print("=" * 20)
        else:
            print(f"No table found on page {page.number}.")

    doc.close()


if __name__ == "__main__":
    print('*' * 80)
    find_images_in_pdf(pdf_file_path)
