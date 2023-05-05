"""
利用BeautiflSoup可以省去很多烦琐的提取工作，提高解析网页的效率
"""

from bs4 import BeautifulSoup

text = """

<html>
    <head>
        <title name="name-for-title">The Documents story</title>
    </head>
    <body>
        <div>
            <ul>
                <li class="item-0"><a href="link1.html"><span id="span1">first item</span></a></li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-inactive"><a href="link3.html">third item</a></li>
                <li class="item-1"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
                <li class="li li-first" name="item"><a href="container.html">contains</a></li>
                <li class="item-0"><a href="link1.html">sixth item</a></li>
                <li class="item-1"><a href="link2.html">seventh item</a></li>
                <li class="item-3"><button type="submit" class="btn-submit" action="form.html" data-id="userID">点击提交</button></li>
                <li class="item-1"><a href="link2.html"><span id="span2">这是一段测试文本</span></a></li>
            </ul>
        </div>
    </body>
</html>
"""

soup1 = BeautifulSoup(text, 'lxml')
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

# 获取属性名称
print('soup1  attribute=', soup1.span.attrs['id'])
print('soup1  attribute2=', soup1.button['type'])
print('soup1  attribute3=', soup1.button['action'])
print('soup1  attribute4=', soup1.button['data-id'])

# 获取直接子节点
print('soup1  contents=', soup1.ul.contents)
for index, child in enumerate(soup1.ul.children):
    print(f'第 {index} 个内容是 {child}')

# 获取父或祖先节点
print('soup1  parent =', soup1.a.parents)
print('soup1  parent type=', type(soup1.a.parents))
print('soup1  parent list=', list(enumerate(soup1.a.parents)))
