# 导入 PyPDF2 库
import PyPDF2

# 定义第一个 PDF 文件的路径
pdf_2_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\2.pdf'
# 定义第二个 PDF 文件的路径
pdf_20_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\静夜思3.pdf'

# 以二进制模式打开第一个 PDF 文件
pdf_2_file = open(pdf_2_file_path, 'rb')
# 以二进制模式打开第二个 PDF 文件
pdf_20_file = open(pdf_20_file_path, 'rb')

# 创建一个 PdfReader 对象，用于读取第一个 PDF 文件
pdf_2_file_reader = PyPDF2.PdfReader(pdf_2_file)
# 创建一个 PdfReader 对象，用于读取第二个 PDF 文件
pdf_20_file_reader = PyPDF2.PdfReader(pdf_20_file)

# 创建一个 PdfWriter 对象，用于将两个 PDF 文件合并成一个
pdf_file_writer = PyPDF2.PdfWriter()

# 将第一个 PDF 文件中的所有页添加到 PdfWriter 对象中
for pageNum in range(len(pdf_2_file_reader.pages)):
    # 获取当前页对象
    pageObj = pdf_2_file_reader.pages[pageNum]
    # 旋转角度
    pageObj.rotate(90)
    # 将当前页对象添加到 PdfWriter 对象中
    pdf_file_writer.add_page(pageObj)

# 将第二个 PDF 文件中的所有页添加到 PdfWriter 对象中
for pageNum in range(len(pdf_20_file_reader.pages)):
    # 获取当前页对象
    pageObj = pdf_20_file_reader.pages[pageNum]
    # 将当前页对象添加到 PdfWriter 对象中
    pdf_file_writer.add_page(pageObj)

# 创建输出 PDF 文件，以二进制模式打开
pdfOutputFile = open('combined_minutes.pdf', 'wb')

# 将 PdfWriter 对象中的所有页写入输出 PDF 文件中
pdf_file_writer.write(pdfOutputFile)

# 关闭输出 PDF 文件和两个输入 PDF 文件
pdfOutputFile.close()
pdf_2_file.close()
pdf_20_file.close()

"""
这段代码使用 PyPDF2 库将两个 PDF 文件合并成一个。首先，导入 PyPDF2 库。然后，定义两个 PDF 文件的路径，并使用二进制模式打开这两个文件，  因为PDF 文件是二进制文件。接着，创建两个 PdfReader 
对象分别读取两个 PDF 文件的内容。然后，创建一个 PdfWriter 对象，用于将合并后的 PDF 文件写入到输出文件中。接下来，使用 for 循环遍历第一个 PDF  文件中的所有页，并将每一页添加到 PdfWriter 
对象中。使用 range() 函数和 len() 函数获取页数。获取当前页对象使用 PdfReader 对象的 pages 属性。然后，使用 add_page() 方法将当前页对象 添加到 PdfWriter 对象中。接着，使用 
for 循环遍历第二个 PDF 文件中的所有页，并将每一页添加到 PdfWriter 对象中。获取当前页对象的方式与第一个 PDF 文件相同。接着， 以二进制模式创建输出 PDF 文件，并将 PdfWriter 
对象中的所有页写入该文件中，使用 write() 方法。最后，关闭输出 PDF 文件和两个输入 PDF 文件，使用 close() 方法。
"""