import os  # 处理文件和目录路径相关的功能
import re
import struct
from collections import Counter
from pprint import pprint

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


# 获取PDF中所有页面的图片数量方法一
def get_images_in_pdf_1(pdf_doc):
    # 获取文档总页数
    total_pages = pdf_doc.page_count

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
    # 搜索 PDF 文件中是否存在 Image 子类型的对象 和 XObject 类型的对象
    checkXO = r'/Type(?= */XObject)'
    checkIM = r'/Subtype(?= */Image)'

    # 获取 PDF 文件的交叉引用表长度
    XrefLength = doc.xref_length()

    # 遍历 PDF 文件的交叉引用表
    for doc_xref in range(1, XrefLength):
        # 获取当前交叉引用表节点的文本
        xref_text = doc.xref_object(doc_xref)
        # 判断当前节点是否为 XObject 类型
        isXObject = re.search(checkXO, xref_text)
        # 判断当前节点是否为 Image 子类型
        isImage = re.search(checkIM, xref_text)
        #  如果不符合要求，则跳过
        if not isImage or not isXObject:
            continue
        # 计数器累加
        image_count += 1
        # 获取图片 pixmap 对象
        pix = fitz.Pixmap(doc, doc_xref)

        # 定义符合条件的图片文件存储名称
        pixmap_file_name = f'image-xref-{doc_xref}-time-{dt}.png'

        # 循环替换特殊字符
        for special_char in replace_symbol_list:
            pixmap_file_name = pixmap_file_name.replace(special_char, '_')

        # 判断图片是否符合规定大小和颜色空间
        if pix.n < 5 and pix.w >= 1500 and pix.h >= 1100:
            # 将满足要求的图片保存到本地
            # pix.save(pixmap_images_dir + '/' + pixmap_file_name)
            # print(pixmap_images_dir + '/' + pixmap_file_name)
            print('*' * 50)

        else:
            # 将图片转换为 RGB 颜色空间
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            if pix0.n < 5 and pix0.w >= 1500 and pix0.h >= 1100:
                # 将满足要求的图片保存到本地
                # pix0.save(pixmap_images_dir + '/' + pixmap_file_name)
                pix0 = None
        # 释放 Pixmap 对象及其资源
        pix = None

        # 打印当前提取的图片数量等信息
        # print(f'提取了{image_count}张图片')
        # print('isXObject:', isXObject, 'isImage:', isImage)
        # print('doc_xref:', doc_xref, 'doc pages:', doc.page_count, 'xref_text:', xref_text)


def get_images_in_pdf_2(pdf_doc):
    # 定义图片计数变量
    image_count = 0

    # 创建图片存放目录
    pixmap_images_dir = "pixmap_images"
    if not os.path.exists(pixmap_images_dir):
        os.mkdir(pixmap_images_dir)

    # 替换的特殊符号列表
    replace_symbol_list = ['、', ' ', '。', '，', '；', ':', '\\', 'u3000', '\t']

    # 搜索 PDF 文件中是否存在 Image 子类型的对象 和 XObject 类型的对象
    checkXO = r'/Type(?= */XObject)'
    checkIM = r'/Subtype(?= */Image)'

    # 获取 PDF 文件的交叉引用表长度
    XrefLength = pdf_doc.xref_length()

    # 遍历 PDF 文件的交叉引用表
    for doc_xref in range(1, XrefLength + 1):

        # 获取当前交叉引用表节点的文本
        xref_text = pdf_doc.xref_object(doc_xref)
        # 判断当前节点是否为 XObject 类型
        isXObject = re.search(checkXO, xref_text)
        # 判断当前节点是否为 Image 子类型
        isImage = re.search(checkIM, xref_text)
        #  如果不符合要求，则跳过
        if not isImage or not isXObject:
            continue
        # 计数器累加
        image_count += 1
        # 获取当前交叉引用表节点的文本
        img_dict = pdf_doc.extract_image(doc_xref)
        # 获取当前交叉引用表节点的图片
        img_data = img_dict['image']
        # 获取当前交叉引用表节点的图片尺寸
        img_size = img_dict["width"], img_dict["height"]
        # 判断色彩空间和模式
        img_colorspace = "RGB" if img_dict["colorspace"] == "/DeviceRGB" else "CMYK"
        # 定义符合条件的图片文件存储名称
        pixmap_file_name = pixmap_images_dir + '/' + f'image-{image_count}-{doc_xref}-time-{dt}-size-{img_size}-colorspace-{img_colorspace}.png'
        #
        # 循环替换特殊字符
        for special_char in replace_symbol_list:
            pixmap_file_name = pixmap_file_name.replace(special_char, '_')
        #
        # # 把img的二进制数据存储为图片
        with open(pixmap_file_name, 'wb') as f:
            f.write(img_data)


def get_texts_in_pdf(pdf_doc):
    for page_num, page in enumerate(pdf_doc):
        d = page.get_text("dict")
        blocks = d["blocks"]
        img_blocks = [b for b in blocks if b["type"] == 1]
        pprint(img_blocks[0])
        print({'bbox': img_blocks[0]['bbox'],
               'bpc': img_blocks[0]['bpc'],
               'colorspace': img_blocks[0]['colorspace'],
               'ext': img_blocks[0]['ext'],
               'height': img_blocks[0]['height'],
               # 'image': img_blocks[0]['image'],
               'size': img_blocks[0]['size'],
               'transform': img_blocks[0]['transform'],
               'type': img_blocks[0]['type'],
               'width': img_blocks[0]['width'],
               'xres': img_blocks[0]['xres'],
               'yres': img_blocks[0]['yres']})


if __name__ == "__main__":
    # print('get_images_in_pdf-1返回结果：', get_images_in_pdf_1(doc))
    print('get_images_in_pdf-2返回结果：', get_images_in_pdf_2(doc))
    # print('get_texts_in_pdf-返回结果：', get_texts_in_pdf(doc))
