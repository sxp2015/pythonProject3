import os.path
from docx import Document
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 文件必须是docx格式的！！！！！
word_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\docx\test\房屋买卖协议.docx'

# 打开word文件并读取内容
document = Document(word_file_path)

content = []
for paragraph in document.paragraphs:
    content.append(paragraph.text)

# 创建PDF文件并写入内容
pdf_file = os.path.basename(word_file_path).split('.')[0]+'.pdf'
pdf_buffer = BytesIO()

# 注册字体
pdfmetrics.registerFont(TTFont('mysimsun', 'simsun.ttc'))

pdf = canvas.Canvas(pdf_buffer)
y = 750
for line in content:
    pdf.setFont('mysimsun', 12)  # 设置字体和字号
    pdf.drawString(100, y, line.encode('utf-8').decode())
    y -= 20
pdf.save()

# 将PDF文件保存到磁盘
with open(pdf_file, 'wb') as f:
    f.write(pdf_buffer.getvalue())