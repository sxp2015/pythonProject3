#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-03-29 21:22
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : demo.py
# @IDE     : PyCharm
import shutil, os
from pathlib import Path

# 指定要查找文件的目录
# folder = f'C:\\Users\\Administrator\\Downloads\\rename'
folder = f'C:\\Users\\admin\\Desktop\\demo'


# 遍历指定目录下的所有文件,并重新命名
def rename_files(path):
    # 遍历指定路径下的所有文件
    for file_name in os.listdir(path):
        # 如果文件名不是以"."开头的隐藏文件
        if not file_name.startswith("."):
            # 构造新的文件名，格式为原文件名.jpg
            new_file_name = os.path.splitext(file_name)[0] + ".jpg"
            # 构造文件的完整路径
            file_path = os.path.join(path, file_name)
            new_file_path = os.path.join(path, new_file_name)
            # 重命名文件
            os.rename(file_path, new_file_path)


# 调用函数
rename_files(folder)
