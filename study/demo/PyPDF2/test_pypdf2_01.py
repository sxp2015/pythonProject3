import PyPDF2

pdf_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf\1.pdf'

# 'rb' 读取方式
pdf_file_boj = PyPDF2.PdfReader(pdf_file_path)

# 获取页码对象
pageObj = pdf_file_boj.pages[0]


t2 = pageObj.extract_text()

print('PDF页码数量：', len(pdf_file_boj.pages))

print('PDF页码的内容：', t2)
