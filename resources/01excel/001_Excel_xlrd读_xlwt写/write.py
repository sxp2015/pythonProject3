# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


import xlwt
# 新建工作簿
new_workbook = xlwt.Workbook()
# 新建sheet
worksheet = new_workbook.add_sheet('new_test')
# 新建单元格，并写入内容
worksheet.write(0, 0, 'test')
# 保存
new_workbook.save('test.xls')