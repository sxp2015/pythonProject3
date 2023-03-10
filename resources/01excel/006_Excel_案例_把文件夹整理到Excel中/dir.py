# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


import os
import xlwt

# 目标文件夹
file_path = 'd:/'
# 取出目标文件夹下的文件名
os.listdir(file_path)

new_workbook = xlwt.Workbook()
sheet = new_workbook.add_sheet('new_dir')

n = 0
for i in os.listdir(file_path):
    sheet.write(n,0,i)
    n+=1
new_workbook.save('dir.xls')