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
				<ul id="nav-ul">
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

# 查找所有父节点
parents_01 = baidu_img_parse('.bd-home-content-album-item-pic').parents()
print('parents  ==', parents_01)
print('#######################################')
# 查找所有兄弟节点
siblings_01 = baidu_img_parse('.bd-home-content-album-item-pic').siblings()
print('siblings_01  ==', siblings_01)
print('#######################################')
album_html = baidu_img_parse('.bd-home-content-album').html()
album_text = baidu_img_parse('.bd-home-content-album').text()
print('album_html  ==', album_html)
print('album_html  text ==', album_text)

# 添加或删除节点
print('未删除之前 ==', doc('ul li'))
# 删除样式
remove_li = doc('ul li.active')
print('删除active ==', remove_li.remove_class('active'))
print('添加active ==', remove_li.add_class('active'))

"""
如果 attr 方法只传人第一个参数，即属性名，则表示获取这个属性值:如果传人第二个参数，则可以用来修改属性值。
text 和 html 方法如果不传参数，表示的是获取节点内的纯文本和HTML文本;如果传人参数，则表示进行赋值。
"""
# 选择器
attr_li = doc('.active')
print('attr_li  == ', attr_li)

# 伪类选择pseudo selector
attr_pseudo1 = doc('ul li:last-child')
attr_pseudo2 = doc('ul li:first-child')
attr_pseudo3 = doc('ul li:nth-child(2)')
print('attr_pseudo1 ==', attr_pseudo1)
print('attr_pseudo2 ==', attr_pseudo2)
print('attr_pseudo3 ==', attr_pseudo3)

# 修改
attr_li_changed = doc('.active').attr('class', 'disable')
print('attr_li_changed  == ', attr_li_changed)

# 提取内容
attr_li_text = doc('ul li').text('hello world')
print('attr_li_changed text == ', attr_li_text)

# 新增
attr_li_html = doc('ul li').html('<span>新增内容</span>')
print('attr_li_changed html  == ', attr_li_html)


# 删除内容
attr_remove = doc('ul li').remove('span')
print('attr_remove   == ', attr_remove)
