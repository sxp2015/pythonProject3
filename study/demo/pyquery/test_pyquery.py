#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-06 20:28
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_pyquery.py
# @IDE     : PyCharm

from pyquery import PyQuery
import requests

BAIDU_URL = 'https://www.baidu.com/'
BAIDU_IMG_URL = 'https://image.baidu.com/'

text = """
<div class="header">
    <div class="wrap">
		<div class="header-left">
			<div class="logo">
				<a href="index.html"><img src="images/logo.jpg"/></a>
			</div>
		</div>
		<div class="header-right">
			<div class="top-nav">
				<ul>
						<li class="active"><a href="index.html">Home</a></li>
						<li><a href="about.html">About</a></li>
						<li><a href="blog.html">Blog</a></li>
					</ul>
				</div>

				<div class="sign-ligin-btns">
					<ul>

						<li id="loginContainer"><a class="login" id="loginButton" href="#"><span>LOGIN</span></a>
							 <div class="clear"> </div>
				                <div id="loginBox">                

				                </div>

						</li>
						<div class="clear"> </div>
					</ul>
				</div>
				<div class="clear"> </div>
				</div>
				<div class="clear"> </div>
			</div>
			</div>
			"""

doc = PyQuery(text)

baidu = PyQuery(url=BAIDU_URL)

print('a ==', doc('a'))
print('baidu ==', baidu('a'))
print('baidu index==', baidu('#head'))

with open('demo-01.html', 'r', encoding='utf-8') as file:
    html = file.read()
    demo01 = PyQuery(html)
    print('demo01 ==', demo01('button'))
print('#######################################')
# 把百度首面拿回来
baidu_img_index = requests.get(BAIDU_IMG_URL).text
baidu_img_parse = PyQuery(baidu_img_index)
print('baidu_img_parse == ', baidu_img_parse('.bd-home-content-album-item-title'))
print('#######################################')

# 解析并遍历所有项目，得到文本内容
for item in baidu_img_parse('.bd-home-content-album-item-title').items():
    print('item == ', item.text())

print('#######################################')


# 查找所有子孙节点
find01 = baidu_img_parse('.bd-home-content-album').find('div')
print('find01 ==', find01)
print('#######################################')

# 查找所有儿子节点
children_01 = baidu_img_parse('.bd-home-content-album').children()
print('children ==', children_01)
print('#######################################')

# 查找所有儿子节点
parents_01 = baidu_img_parse('.bd-home-content-album-item-pic').parents()
print('parents  ==', parents_01)