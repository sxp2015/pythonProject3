# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


import zipfile

word_book = zipfile.ZipFile('word_table.docx')
xml = word_book.read("word/document.xml").decode('utf-8')
# print(xml)
xml_list = xml.split('<w:t>')
print(xml_list)
text_list = []
for i in xml_list:
    if i.find('</w:t>') + 1:
        text_list.append(i[:i.find('</w:t>')])
    else:
        pass
text = "".join(text_list)
print(text)
