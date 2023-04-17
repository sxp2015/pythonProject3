import pathlib

import PyPDF2, os

pdfFiles = []
pdf_files_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\pdf'

for filename in os.listdir(pdf_files_path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfWriter()
print('pdf files', pdfFiles)

# 遍历所有PDF文件
for filename in pdfFiles:
    pdf_file_Obj = open(pdf_files_path + '\\' + f'{filename}', 'rb')
    pdf_file_reader = PyPDF2.PdfReader(pdf_file_Obj)
    # 遍历所有页面，除了第一页,如果要包含第一页，则把range(1, len(pdf_file_reader.pages)), 中的1，换成0即可
    for pageNum in range(1, len(pdf_file_reader.pages)):
        pageObj = pdf_file_reader.pages[pageNum]
        pdfWriter.add_page(pageObj)

# 保存结果页到文件
pdfOutput = open('all_merge_page.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
