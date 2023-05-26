import os
import fitz
import io
from PIL import Image
import tabula
import pandas as pd

# PDF文件路径
PDF_FILE_PATH = os.path.join('pdf_files/查验报告.pdf')

# 打开PDF文件
pdf_file = PDF_FILE_PATH
pdf_document = fitz.open(pdf_file)

# 创建一个空的DataFrame，用于存储所有表格数据
pdf_all = pd.DataFrame()

# 遍历PDF中的每一页
for page_num in range(pdf_document.page_count):
    # 获取当前页
    page = pdf_document[page_num]

    # 获取当前页中的所有文本块
    page_blocks = page.get_text("blocks")

    # 遍历当前页中的所有文本块
    for block in page_blocks:
        print(block)
        # 如果文本块是一张图片
        if block[0] == 1:
            # 读取图片数据并保存为JPEG文件
            img_data = block[4].get_raw_data('png')
            image = Image.open(io.BytesIO(img_data))
            image.save('image{}.jpeg'.format(page_num+1))

        # 如果文本块是一个表格
        elif block[0] == 0 and block[4]:
            # 获取表格位置信息
            bbox = block[4]
            x1, y1, x2, y2 = bbox

            # 使用tabula-py库读取表格数据
            df: pd.DataFrame = tabula.read_pdf(pdf_file, pages=str(page_num+1), area=[y1, x1, y2, x2], output_format='dataframe', lattice=True)

            # 将读取的表格数据添加到新的DataFrame中
            pdf_all = pd.concat([pdf_all, df], axis=0)

# 将所有读取的表格数据保存到新的CSV文件中
pdf_all.to_csv('all_tables.csv', index=False)
