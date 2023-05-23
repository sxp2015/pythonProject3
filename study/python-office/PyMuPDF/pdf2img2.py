import os
import fitz


def extract_images(pdf_file, output_dir):
    # 创建一个PdfFileReader对象
    with fitz.open(pdf_file) as doc:
        for page_num, page in enumerate(doc):
            # 遍历当前页面中所有图片
            for img_index, img in enumerate(page.get_images()):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:  # 只处理非CMYK格式图片
                    img_filename = f"page{page_num + 1}_img{img_index + 1}.png"
                    img_path = os.path.join(output_dir, img_filename)
                    pix.save(img_path)
                # pix.close()


if __name__ == '__main__':
    pdf_file = 'pdf_files/查验报告.pdf'
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    extract_images(pdf_file, output_dir)
