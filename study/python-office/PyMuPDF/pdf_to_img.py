import fitz  # PyMuPDF 第三方库
import os
import pandas as pd

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from openpyxl import load_workbook

PDF_FILE_PATH = 'pdf_files/查验报告.pdf'
IMAGES_OUTPUT_FOLDER_PATH = 'extract_images'

INPUT_PDF_FILE_PATH = PDF_FILE_PATH
# 定义Excel输出
EXCEL_OUTPUT_FOLDER_PATH = 'extract_excel'
EXCEL_FILE_PATH = os.path.join(EXCEL_OUTPUT_FOLDER_PATH, 'extract_excel.xlsx')
# 定义World输出
WORD_OUTPUT_FOLDER_PATH = 'extract_word'
# 定义提取的图片尺寸大小
image_size = 600

if not os.path.exists(IMAGES_OUTPUT_FOLDER_PATH):  # 如果输出文件夹不存在，则创建该文件夹
    os.mkdir(IMAGES_OUTPUT_FOLDER_PATH)

if not os.path.exists(EXCEL_OUTPUT_FOLDER_PATH):  # 如果输出文件夹不存在，则创建该文件夹
    os.mkdir(EXCEL_OUTPUT_FOLDER_PATH)


# 提取PDF图片的方法
def extract_images_from_pdf(pdf_file_path, output_folder_path):
    # 打开指定的 PDF 文件
    with fitz.open(pdf_file_path) as pdf:
        # 遍历每一页
        for page_num in range(pdf.page_count):
            # 获取页面对象
            page = pdf[page_num]
            # 获取页面中所有的图像对象
            image_list = page.get_images()

            # 遍历每个图像对象
            for image_index, img in enumerate(image_list):
                # 获取图像像素信息
                xref = img[0]  # 图像引用编号
                pix = fitz.Pixmap(pdf, xref)  # 将引用编号转换为图片像素数据
                if not pix.n:  # 如果图片没有颜色通道，则跳过该图片
                    continue
                if pix.size > (image_size * 1024) and pix.h >= 1100 and pix.w >= 1500:
                    print('图片大小:', pix.size, '宽:', pix.w, '高:', pix.height)
                    # 将图像保存到文件夹中
                    img_path = os.path.join(output_folder_path, f'image{page_num + 1}-{image_index + 1}.png')
                    pix.save(img_path)
                    pix = None  # 释放图片像素数据

    print(f"提取完成，已将所有图片保存在 {output_folder_path} 文件夹中。")


# 把PDF转成excel的方法
def pdf_to_excel(input_file_path, output_file_name):
    """
    将PDF文件转换为Excel文件并保存到当前文件夹。

    :param input_file_path: str，输入PDF文件的路径。
    :param output_file_name: str，输出Excel文件的文件名（不包括文件扩展名，自动添加.xlsx扩展名）。
    """
    # 构造输出文件名
    output_file_path = os.path.join(EXCEL_OUTPUT_FOLDER_PATH, output_file_name + '.xlsx')

    # 读取PDF文件并转换为DataFrame
    data = []
    with open(input_file_path, 'rb') as fp:
        parser = PDFParser(fp)
        doc = PDFDocument(parser)
        pdf_resource_manager = PDFResourceManager()
        device = PDFPageAggregator(pdf_resource_manager, laparams=None)
        interpreter = PDFPageInterpreter(pdf_resource_manager, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if hasattr(element, 'get_text'):
                    data.append(element.get_text())
    df = pd.DataFrame(data)

    # 将DataFrame写入Excel文件
    df.to_excel(output_file_path, index=False)

    # 输出成功信息
    print(f'PDF文件已成功转换为Excel文件：{output_file_path}')


def read_excel_file(file_path):
    """
    读取指定路径下的Excel文件，遍历第一列所有单元格的值并返回

    Args:
        file_path: str, 文件路径

    Returns:
        list[str], 第一列所有单元格的值
    """
    # 加载 Excel 文件
    wb = load_workbook(filename=file_path)

    # 获取当前活动的 sheet
    sheet = wb.active

    # 遍历第一列单元格并返回其值

    return ''.join([str(cell.value) for cell in sheet['A']
                    if cell.value is not None and cell.value != ''
                    and isinstance(cell.value, str)]).replace(" ", "")



if __name__ == "__main__":
    # extract_images_from_pdf(PDF_FILE_PATH, IMAGES_OUTPUT_FOLDER_PATH)
    # pdf_to_excel(INPUT_PDF_FILE_PATH, EXCEL_OUTPUT_FOLDER_PATH)

    values = read_excel_file(file_path=EXCEL_FILE_PATH)
    print('values:', values)
    # print('读总的字数是:', len(values))
