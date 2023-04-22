#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-04-22 21:10
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : open_chat_website.py
# @IDE     : PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# 设置Chrome浏览器驱动路径和启动选项
chrome_driver_path = "C:\\Program Files\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 最大化窗口

# 启动Chrome浏览器并访问指定页面
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get("https://random1.aichatos.com/#/chat/")

    # 等待页面加载完成
    time.sleep(2)
    question_textarea = '你现在是一名百科知识专家，请随机提供一个关于动物的百科知识提问，要求提问方式有吸引力，自行从专业知识角度详细回答，文体风格随机、写一篇长文章，要求2000' \
                        '字以上，在文章底部包含关于提问标题的冷知识及小贴士或温馨提醒和注意事项或真实案例 '
    input_text = driver.find_element(By.CLASS_NAME, 'n-input__textarea-el')
    button_submit = driver.find_element(By.CLASS_NAME, 'n-button__icon')

    input_text.send_keys(question_textarea)
    time.sleep(3)
    button_submit.click()
    time.sleep(120)

except Exception as e:
    print("程序运行出现错误：", e)
finally:
    # 关闭浏览器
    driver.quit()
