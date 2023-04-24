#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-04-24 20:18
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : operation.py
# @IDE     : PyCharm

import time

import pyautogui

# 先把浏览器打开，移动到任务栏点击
pyautogui.click(280, 750)
time.sleep(0.5)
# 点击内容管理
pyautogui.click(94, 540)
time.sleep(0.5)
# 点击更多
pyautogui.click(1235, 442)
time.sleep(0.5)
