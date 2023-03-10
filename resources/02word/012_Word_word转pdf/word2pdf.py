# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


from win32com.client import Dispatch,constants,gencache

doc_path = 'test.docx'
pdf_path = 'test.pdf'

gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}',0,8,4)
wd = Dispatch("Word.Application")
doc = wd.Documents.Open(doc_path,ReadOnly=1)
doc.ExportAsFixedFormat(pdf_path,constants.wdExportFormatPDF,Item=constants.wdExportDocumentWithMarkup,CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
wd.Quit(constants.wdDoNotSaveChanges)