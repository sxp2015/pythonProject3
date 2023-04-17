# 导入 PyPDF2 库
import PyPDF2

# 定义第一个 PDF 文件的路径
pdf_1_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\1.pdf'
# 定义水印 PDF 文件的路径
logo_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\logo.pdf'

pdf_1_file = open(pdf_1_file_path, 'rb')
logo_file = open(logo_file_path, 'rb')

# 创建 PdfReader 对象，用于读取第一个 PDF 文件和水印 PDF 文件
pdf_1_reader = PyPDF2.PdfReader(pdf_1_file)
water_mark = PyPDF2.PdfReader(logo_file)

# 获取第一个 PDF 文件的第一页和水印 PDF 文件的第一页
pdf_1_page = pdf_1_reader.pages[0]
logo_page = water_mark.pages[0]

# 缩小水印 PDF 文件的大小
logo_page.scale(0.5, 0.5)

# 将水印 PDF 文件合并到第一个 PDF 文件的第一页
pdf_1_page.merge_page(logo_page)

# 创建 PdfWriter 对象，用于将结果写入到新的 PDF 文件
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(pdf_1_page)

# 将第一个 PDF 文件的剩余页面添加到 PdfWriter 对象中
for pageNum in range(1, len(pdf_1_reader.pages)):
    pageObj = pdf_1_reader.pages[pageNum]
    pdf_writer.add_page(pageObj)

# 将结果写入到新的 PDF 文件
resultPdfFile = open('walter_mark.pdf', 'wb')
pdf_writer.write(resultPdfFile)

# 关闭打开的文件对象
pdf_1_file.close()
resultPdfFile.close()
logo_file.close()
"""
这段代码主要使用 PyPDF2 库对 PDF 文件进行操作，具体实现了将一个水印 PDF 文件添加到第一个 PDF 文件的第一页，并将合并后的结果保存到一个新的 PDF 文件中。下面是每个部分的详细说明：

导入 PyPDF2 库：使用 import 语句导入 PyPDF2 库，以便在代码中使用该库提供的功能。

定义 PDF 文件的路径：使用变量 pdf_1_file_path 和 logo_file_path 存储第一个 PDF 文件和水印 PDF 文件的路径。

打开 PDF 文件：使用 open() 函数以二进制模式打开第一个 PDF 文件和水印 PDF 文件，并将文件对象分别存储在 pdf_1_file 和 logo_file 变量中。

创建 PdfReader 对象：使用 PyPDF2.PdfReader() 函数创建 PdfReader 对象，用于读取第一个 PDF 文件和水印 PDF 文件的内容，分别存储在 pdf_1_reader 和 water_mark 变量中。

获取 PDF 文件的页面：使用 pdf_1_reader.pages[0] 和 water_mark.pages[0] 获取第一个 PDF 文件和水印 PDF 文件的第一页。

缩小水印 PDF 文件的大小：使用 logo_page.scale(0.5, 0.5) 缩小水印 PDF 文件的大小，以便将其添加到第一个 PDF 文件的第一页上。

合并 PDF 文件页面：使用 pdf_1_page.merge_page(logo_page) 将水印 PDF 文件的第一页合并到第一个 PDF 文件的第一页上。

创建 PdfWriter 对象：使用 PyPDF2.PdfWriter() 函数创建 PdfWriter 对象，用于将结果写入到新的 PDF 文件中。

将 PDF 文件页面添加到 PdfWriter 对象中：使用 pdf_writer.add_page() 将第一个 PDF 文件的第一页添加到 PdfWriter 对象中，并使用 for 循环将第一个 PDF 文件的剩余页面添加到 PdfWriter 对象中。

将结果写入到新的 PDF 文件：使用 pdf_writer.write() 将 PdfWriter 对象中合并后的 PDF 文件页面写入到新的 PDF 文件中，并将结果保存在 resultPdfFile 文件对象中。

关闭打开的文件对象：使用 close() 方法关闭打开的文件对象，释放资源。
"""

