import json
import os  # 处理文件和目录路径相关的功能
import pathlib
import random
import re
import sys
from datetime import datetime
from pprint import pprint
import fitz  # 操作 PDF 文件的库 PyMuPDF
import itertools

# PDF 文件路径
from PIL import Image

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


def get_images_in_pdf_3(pdf_doc):
    for page_num, page in enumerate(pdf_doc):
        d = page.get_text("dict")
        blocks = d["blocks"]
        # 图片块
        img_blocks = [b for b in blocks if b["type"] == 1]
        # 文本块
        text_blocks = [b for b in blocks if b["type"] == 2]
        # 路径块
        rect_blocks = [b for b in blocks if b["type"] == 3]

        pprint(img_blocks[0])
        # pprint(text_blocks[0])
        # pprint(rect_blocks[0])
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


def get_texts_in_pdf_1(pdf_doc):
    # 创建文字存放目录
    extract_texts_dir = "extract_texts"
    if not os.path.exists(extract_texts_dir):
        os.mkdir(extract_texts_dir)
        """
        chr(12) 表示ASCII码值为12的字符，也称为换页符（Form Feed，简写为 FF）。在打印机时代，换页符通常用于在打印机上分隔纸张。在这里，
        换页符被用作页面文本内容的分隔符，以便在将文本内容写入新的文本文件时，可以轻松地分隔每个页面的文本内容
        """

    with fitz.open(pdf_doc) as document:  # open document
        text = chr(12).join([page.get_text() for page in document])
        # write as a binary file to support non-ASCII characters
        pathlib.Path(extract_texts_dir + f'/text-{dt} + .txt').write_bytes(text.encode())


def get_texts_in_pdf_2(pdf_doc):
    # 创建检查部位图片的存放目录
    check_part_images_dir = "check_part_images"
    if not os.path.exists(check_part_images_dir):
        os.mkdir(check_part_images_dir)

    # 检查部位的名称变量列表
    check_part_text_list = []

    # 检查部位图片存放目录
    check_part_dir_name = None

    # 从表格中提取文字内容列表
    table_text_list = []
    table_text = None
    # 定义当前单元格的内容
    table_word = None
    # 当前的文本块内容
    current_block_text = None

    # 定义特殊字符，排除空文本和数字
    special_chart = ['空', '1', '', ' ', '\t', '\n', '\r']

    # 获取文档的所有xref对象数量
    doc_xref_length = pdf_doc.xref_length()

    # 定义当前遍历到的矩形
    table_rect = None

    # 定义矩形坐标
    x0, y0, x1, y1 = 0, 0, 0, 0
    # 定义通用判断条件
    common_condition = None
    # 定义图片文件保存路及图片文件名称

    image_file_dir = None
    image_file_name_list = []

    # 遍历每一页PDF
    for page_num, page in enumerate(pdf_doc):
        # 获取当前页中所有的图形对象和文本块
        shape_list = page.get_drawings()
        block_list = page.get_text_blocks()
        image_list = page.get_images()
        cell_text = None
        name_index = 0
        file_name = None

        # 遍历每个图形对象
        for shape_index, shape in enumerate(shape_list):
            # 如果当前图形对象包含矩形区域
            if 'rect' in shape:
                # 根据矩形区域判断是否为表格
                x0, y0, x1, y1 = shape['rect']
                # 获取表格的矩形区域
                table_rect = fitz.Rect(shape['rect'])

                # 获取表格单元格的文字
                table_word = page.get_textbox(table_rect)

                # 定义检查部位的文字
                check_part = None

                # 通用判断条件:独占一行不含1并且不含建议说明，不要最后两页，以及第一页的描述内容
                common_condition = page_num + 1 not in [18, 19] \
                                   and not str(table_word).strip().startswith('【') \
                                   and str(table_word) not in ['1', '建议与说明']

                # 检查部位独占一行的情况
                if x1 - x0 >= 530 and y1 - y0 >= 40 and common_condition:
                    # 提取矩形的文字给检查部位的变量
                    check_part = page.get_textbox(table_rect)
                    # 按检查部位分类创建目录
                    check_part_dir_name = check_part_images_dir + '/' + str(page_num + 1) + '-' + check_part + '/'
                    if not os.path.exists(check_part_dir_name):
                        os.mkdir(check_part_dir_name)

                    # 定义图片保存路径
                    image_file_dir = check_part_dir_name
                    # 把检查部位的数据添加到列表
                    check_part_text_list.append(check_part)

                    # print(f"检查部位1: {check_part}")

                    # 如果是一行两列的情况

                if x1 - x0 > 260 and y1 - y0 > 25 and common_condition:

                    # 判断保存的名称：
                    if table_word and str(table_word).strip() != '空' and table_word != check_part:
                        image_file_name = str(image_file_dir + table_word) + f'-{dt}.png'
                        table_text = table_word
                        table_text_list.append(table_text)
                        image_file_name_list.append(image_file_name)

                    # print('len(image_file_name_list)', len(image_file_name_list))
                    print('---' * 10)

                    # print('table_word', table_word)
                    # print('file_name', image_file_name)
                    # print('image_file_name_list', image_file_name_list)
                    # print('_list_length', len(image_file_name_list))

                    # 保存图片

        # 遍历每一页的图片列表
        if image_list and image_file_name_list:

            # 遍历每页的图片对象列表
            for image_index, image in enumerate(image_list):
                # 一个图片对象中获取了图片在文档中的位置信息，即 xref。
                xref = image[0]

                for image_file_index, image_file_name in enumerate(image_file_name_list):
                    image_index = image_file_index
                    file_name = image_file_name
                    # print(f'image_file_index:{name_index},image_file_name:{image_file_name}')
                    continue

                # 遍历文件名列表
                if image_index < len(image_file_name_list):
                    pix = fitz.Pixmap(pdf_doc, xref)
                    # 如果pix对象有值且宽和高符合要求，并且不是当前项，则保存图片
                    if pix and pix.n < 5 and pix.w >= 1500 and pix.h >= 1100:
                        # print('image_file_name:', file_name)
                        print('--' * 20)
                        # pix.save(file_name)
                        # 把文件名置空
                    # 释放 Pixmap 对象及其资源
                    pix = None
                else:
                    file_name = None
                    continue

        # 遍历文本块列表
        for block_index, block in enumerate(block_list):
            # 定义检查部位的文字
            check_part = None

            block_image = block[4]
            block_x0, block_y0, block_x1, block_y1 = block[:4]
            block_rect = fitz.Rect(block_x0, block_y0, block_x1, block_y1)

            cell_text_list = str(block_image).strip().split('\n')

            # 通用判断条件:独占一行不含1并且不含建议说明，不要最后两页，以及第一页的描述内容
            block_common_condition = page_num + 1 not in [18, 19] \
                                     and not str(block_image).strip().startswith('【') \
                                     and str(block_image) not in ['1', '建议与说明']

            # 检查部位独占一行的情况
            # if block_x1 - block_x0 >= 530 and block_y1 - block_y0 >= 40:
            #     # 提取矩形的文字给检查部位的变量
            #     check_part = page.get_textbox(block_rect)

            # 定义图片保存名称

            for cell_text_index, cell_text in enumerate(cell_text_list):
                # print(f'index-{cell_text_index}-value-{cell_text}')
                # print('block_image', block_image)

                if str(cell_text).strip() != '空' and (page_num + 1) not in [1, 18, 19] \
                        and not str(cell_text).strip().startswith('【') \
                        and str(cell_text) not in ['1', '建议与说明']:
                    # print('cell_text', cell_text)
                    # print('table_text', table_text)
                    print('-' * 40)

                if 'image' in cell_text:
                    # 生成随机的 4 位正整数
                    random_num = random.randint(1000, 9999)
                    # rect = page.search_for(block_rect)
                    pix = page.get_pixmap(matrix=fitz.Identity, colorspace=fitz.csRGB, clip=block_rect, alpha=False,
                                          dpi=200)
                    # print('Width:', pix.width)
                    # print('Height:', pix.height)

                    if pix and pix.n < 5 and pix.width >= 730 and pix.height >= 550:
                        # print('Width:', pix.width)
                        # print('Height:', pix.height)
                        # 输出像素图
                        # 定义图片保存路径
                        image_file_dir = f'{check_part_dir_name}-{table_text}-{page_num + 1}-{block_index}-{random_num}-{dt}.png'
                        # 保存图片
                        print('image_file_dir', image_file_dir)
                        # pix.save(image_file_dir)

                    # print('文字:', block[4], '矩形宽度:', block_rect.width,
                    #       '矩形高度:', block_rect.height, '坐标:', block_rect)
                    # print('block_image', block_image)
                    # print('block_rect', block_rect)

    return table_text_list, check_part_text_list


if __name__ == "__main__":
    # print('get_images_in_pdf-1返回结果：', get_images_in_pdf_1(doc))
    # print('get_images_in_pdf-2返回结果：', get_images_in_pdf_2(doc))
    # print('get_texts_in_pdf_1-返回结果：', get_texts_in_pdf_1(doc))
    print('get_texts_in_pdf_2-返回结果：', get_texts_in_pdf_2(doc))
