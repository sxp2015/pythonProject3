"""
利用BeautiflSoup可以省去很多烦琐的提取工作，提高解析网页的效率
"""
import re

from bs4 import BeautifulSoup

text = """

<html>
    <head>
        <title name="name-for-title">The Documents story</title>
    </head>
    <body>
        <div>
            <ul>
                <span id="hello">top span</span>
                <li class="item-0"><a href="link1.html"><span id="span1">first item</span></a></li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-inactive"><a href="link3.html">third item</a></li>
                <li class="item-1"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
                <li class="li li-first" name="item"><a href="container.html">contains</a></li>
                <li class="item-0"><a href="link1.html">sixth item</a></li>
                <li class="item-1"><a href="link2.html" blank=True >seventh item</a></li>
                <li class="item-3"><button type="submit" class="btn-submit" action="form.html" data-id="userID">点击提交</button></li>
                <li class="item-1"><a href="link2.html"><span id="span2">这是一段测试文本</span></a></li>
                <span>bottom span</span>
            </ul>
        </div>
    </body>
</html>
"""

text2 = """
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

soup1 = BeautifulSoup(text, 'lxml')
soup2 = BeautifulSoup(text2, 'lxml')
# prettify方法。这个方法可以把要解析的字符串以标准的缩进格式输出
print('soup1', soup1.prettify())
# 输出HTML中title节点的文本内容
print('soup1 title', soup1.title.string)
print('soup1 title 2', soup1.title)
print('soup1 title 2 type', type(soup1.title))
print('========================')
# print('soup1 head = ', soup1.head)
print('========================')
# print('soup1 body =', soup1.body)
print('========================')
# 获取标签名称
print('soup1  name=', soup1.title.name)
print('========================')
# 获取属性名称
print('soup1  attribute=', soup1.span.attrs['id'])
print('soup1  attribute2=', soup1.button['type'])
print('soup1  attribute3=', soup1.button['action'])
print('soup1  attribute4=', soup1.button['data-id'])
print('========================')
# 获取直接子节点
print('soup1  contents=', soup1.ul.contents)
for index, child in enumerate(soup1.ul.children):
    print(f'第 {index} 个内容是 {child}')
print('========================')
# 获取父或祖先节点
print('soup1  parent =', soup1.a.parents)
print('soup1  parent type=', type(soup1.a.parents))
print('soup1  parent list=', list(enumerate(soup1.a.parents)))
print('========================')
# 获取上一个兄弟和下一个兄弟节点
print('soup1  previous_sibling =', soup1.findAll('li')[5].find_previous_sibling())
print('soup1  next_sibling =', soup1.findAll('li')[5].find_next_sibling())
print('========================')
# 提取信息
print('soup1  提取信息 ID=', soup1.select_one('#span2').text)
print('soup1  提取信息 CLASS=', soup1.select_one('.li').text)
print('========================')

# findall方法
print('soup1  findall 标签名name方法 =', soup1.findAll(name='span'))
print('soup1  提取信息 标签 =', soup1.findAll('li')[5].text)
print('soup1  提取信息 attrs=', soup1.findAll(attrs={'blank': 'True'}))
print('soup1  提取信息 text正则表达式=', soup1.findAll(string=re.compile('^f.*?')))
# find方法也可以询符合条件的素，只不过find方法返回的是单个元素
print('soup1  find方法 =', soup1.find(name='a'))
"""
在find al1方法中传人text 参数，该参数为正则表达式对象，
返回结果是由所有与正则表达式相匹配的节点文本组成的列表。
"""

print('===========soup2=============')

# select方法
print('soup2 select方法 CLSS=', soup2.select('.header-left'))
print('soup2 select方法 UL =', soup2.select('ul')[0])

for ul in soup2.select('ul'):
    print("li == ", ul.select('li'))
    for li in ul.select('li'):
        print('li get_text ==', li.get_text())
        print('li string ==', li.string)
