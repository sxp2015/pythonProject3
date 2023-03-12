#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-03-12 16:13
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : get_project_path.py
# @IDE     : PyCharm
import os


# 获取项目根路径
def get_root_path():
    # 获取文件根目录
    CurPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径
    rootPath = CurPath[:CurPath.find("pythonProject3\\") + len("pythonProject3\\")]
    return rootPath
