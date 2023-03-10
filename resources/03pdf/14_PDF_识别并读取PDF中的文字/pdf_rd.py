# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH



# pip install pdfminer3k
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# 打开pdf文件
pdf_file = open('静夜思.pdf', 'rb')

########默认操作#######
rsrcmgr = PDFResourceManager()
retstr = StringIO()
laparams = LAParams()
device = TextConverter(rsrcmgr=rsrcmgr,outfp=retstr,laparams=laparams)
process_pdf(rsrcmgr=rsrcmgr,device=device,fp=pdf_file)
device.close()
content = retstr.getvalue()
retstr.close()
pdf_file.close()
########默认操作#######

print(content)
