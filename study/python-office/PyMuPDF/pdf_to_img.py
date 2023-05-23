import PyPDF2
from os.path import exists
from os import mkdir
from PIL import Image

pdf_file_path = 'pdf_files/查验报告.pdf'
output_folder_path = 'extract_images'

if not exists(output_folder_path):
    mkdir(output_folder_path)

import os
import PyPDF2
from PIL import Image


def extract_images_from_pdf(pdf_file_path, output_folder_path):
    # 检查输出文件夹是否存在，如果不存在则创建
    os.makedirs(output_folder_path, exist_ok=True)

    # 打开PDF文件
    with open(pdf_file_path, 'rb') as pdf_file:
        # 创建PDF阅读器对象
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # 遍历每一页
        for page_num in range(len(pdf_reader.pages)):
            # 获取页面对象
            page = pdf_reader.pages[page_num]
            # 获取页面中的所有XObject
            xobjects = page['/Resources']['/XObject'].get_object()

            # 遍历XObject
            for obj_name in xobjects:
                # 获取XObject
                obj = xobjects[obj_name]
                # 如果XObject是一个图像
                if obj['/Subtype'] == '/Image':
                    # 获取图像数据
                    img_data = obj.get_data()
                    # 使用Pillow库创建图像对象
                    img = Image.frombytes(obj['/ColorSpace'], (obj['/Width'], obj['/Height']), img_data)
                    # 保存图像到输出文件夹
                    img.save(f"{output_folder_path}/{obj_name[1:]}.png", "PNG")

    print(f"提取完成，已将所有图片保存在{output_folder_path}文件夹中。")


if __name__ == "__main__":
    extract_images_from_pdf(pdf_file_path, output_folder_path)
