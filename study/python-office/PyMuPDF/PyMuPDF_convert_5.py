import os  # 处理文件和目录路径相关的功能
import pathlib
import re
import sys
from datetime import datetime
from pprint import pprint
import fitz  # 操作 PDF 文件的库 PyMuPDF

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

    # 检查部位的变量列表
    check_part_text_list = []

    # 遍历每一页PDF
    for page_num, page in enumerate(pdf_doc):
        # 获取当前页中所有的图形对象和文本块
        shape_list = page.get_drawings()
        block_list = page.get_text_blocks()

        # 遍历每个图形对象
        for shape in shape_list:
            # 如果当前图形对象包含矩形区域
            if 'rect' in shape:
                # 根据矩形区域判断是否为表格
                x0, y0, x1, y1 = shape['rect']

                # 获取表格的矩形区域
                table_rect = fitz.Rect(shape['rect'])
                table_word = page.get_textbox(table_rect)

                # 检查部位独占一行的情况,不要最后两页，以及第一页的描述内容
                if x1 - x0 >= 530 and y1 - y0 >= 40 and page_num + 1 not in [18, 19] \
                        and not str(table_word).strip().startswith('【'):
                    # 通过矩形的左上角和右下角的坐标判断检查部位的单元格，如果矩形是独占一行且没有1
                    if table_rect[0] == 29.75 and table_rect[2] == 565.25 and str(table_word) != '1':
                        # 提取矩形的文字给检查部位的变量
                        check_part = page.get_textbox(table_rect)
                        # 按检查部位分类创建目录
                        check_part_dir_name = check_part_images_dir + '/' + str(page_num + 1) + '-' + check_part
                        if not os.path.exists(check_part_dir_name) and check_part != '建议与说明':
                            os.mkdir(check_part_dir_name)
                        # 把检查部位的数据添加到列表
                        check_part_text_list.append(check_part)
                        # 遍历到最后断开循环
                        if '建议与说明' in check_part:
                            break
                        # print(f"检查部位: {check_part}")

                    # 不是检查部位的情况

                if x1 - x0 > 260 and y1 - y0 > 200:
                    # 从表格中提取文字内容
                    table_text_list = []

                    for block_index, block in enumerate(block_list):
                        """
                        我们可以使用fitz.Rect()方法创建一个矩形对象，并使用intersects()方法判断该矩形对象是否与当前文本块相交。
                        如果相交，则将该文本块的内容添加到table_text_list变量中。
                        """
                        if table_rect.intersects(fitz.Rect(block[:4])):
                            block_text = str(block[4]).strip()  # 获取文本块的内容，并去除首尾空格
                            # 定义特殊字符，排除空文本和数字
                            special_chart = ['空', '1', '', ' ', '\t', '\n']
                            if block_text and block_text not in special_chart and not block_text.isdigit():
                                # 添加到列表
                                table_text_list.append(block_text)

                            # 提取单元格中的文字
                            table_text = "\n".join(table_text_list)
                            # print('table_text', table_text)
                            print('table_text_list', table_text_list)

                        # 如果矩形与文本没有相交，说明是图片
                        else:
                            # 判断检查单元格中是否有图片
                            if len(table_text_list) != 0 and '\u3000' not in table_text_list[0] \
                                    and '【' not in table_text_list[0] and 'image' in table_text_list[0]:
                                # 从表格中提取图片
                                table_image = page.get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB,
                                                              clip=table_rect)
                                image_name = check_part_images_dir + '/' + '2-' + check_part_text_list[0] \
                                             + f'/page{page_num + 1}-image-{block_index + 1}-{dt}-table.png'
                                # 保存图片
                                table_image.save(image_name)
                                # print(f"table_text_list: {table_text_list}")

                                # print("*" * 20)
                                # print("table_image", table_image)

                        # 打印表格的宽度、高度、图片和文字
                        # print('table_rect-1', table_rect)
                        # print('table_text-1', table_text)
                        #  print("*" * 20)
                        # print(f"Table width-2: {table_rect.width}")
                        # print(f"Table height-3: {table_rect.height}")
                        # table_image.save(draw_pdf_dir + f'/image-{dt}-table.png')


if __name__ == "__main__":
    # print('get_images_in_pdf-1返回结果：', get_images_in_pdf_1(doc))
    # print('get_images_in_pdf-2返回结果：', get_images_in_pdf_2(doc))
    # print('get_texts_in_pdf_1-返回结果：', get_texts_in_pdf_1(doc))
    print('get_texts_in_pdf_2-返回结果：', get_texts_in_pdf_2(doc))
