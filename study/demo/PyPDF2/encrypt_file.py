import PyPDF2

# 定义文件路径
pdf_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\2.pdf'

# 打开PDF文件
pdf_file = open(pdf_file_path, "rb")

# 创建PdfFileReader对象
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 创建PdfFileWriter对象
pdf_writer = PyPDF2.PdfWriter()

# 循环遍历每一页
for page_num in range(len(pdf_reader.pages)):
    # 获取当前页
    page = pdf_reader.pages[page_num]
    # 将页添加到PdfFileWriter对象
    pdf_writer.add_page(page)

# 设置密码
pdf_writer.encrypt("mypassword")

# 创建输出PDF文件
output_pdf = open("output.pdf", "wb")

# 将加密后的PDF文件写入输出文件中
pdf_writer.write(output_pdf)

# 关闭文件
output_pdf.close()
pdf_file.close()

"""
这个示例代码使用PyPDF2库打开一个PDF文件，然后创建一个PdfFileReader对象和一个PdfFileWriter对象。
它遍历输入PDF文件的每一页，并将每一页添加到PdfFileWriter对象中。然后，
它使用encrypt()方法将输出PDF文件加密，并将加密后的PDF文件写入输出文件中。最后，它关闭所有文件。

请注意，这个示例代码使用的是基于用户密码的加密，也称为打开密码。如果您需要使用基于所有者密码的加密，
也称为权限密码，请在encrypt()方法中传递第二个参数，如下所示：

pdf_writer.encrypt("mypassword", "ownerpassword")
这个示例代码将使用"mypassword"作为用户密码，并使用"ownerpassword"作为所有者密码。
"""