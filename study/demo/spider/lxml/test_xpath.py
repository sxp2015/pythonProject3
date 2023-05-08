from lxml import etree

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
        <li class="li li-first" name="item"><a href="container.html">contains</a></li>
        <li class="item-0"><a href="link1.html">sixth item</a></li>
        <li class="item-1"><a href="link2.html">seventh item</a></li>
    </ul>
</div>
"""

html_text = etree.HTML(text)
html_parse = etree.parse('./test.html', etree.HTMLParser())

result = etree.tostring(html_parse)
result2 = html_parse.xpath('//*')
result3 = html_parse.xpath('//li')
result4 = html_parse.xpath('//li/a')
result5 = html_parse.xpath('//a[@href="link3.html"]/../@class')
result6 = html_parse.xpath('//a[@href="link3.html"]/parent::*/@class')
result7 = html_parse.xpath('//li[@class="item-0"]')
result8 = html_parse.xpath('//li[@class="item-0"]//text()')
result9 = html_parse.xpath('//li[@class="item-0"]/a/text()')
result10 = html_parse.xpath('//li[@class="item-0"]/a/@href')

"""
# contains()是XPath的一个函数，用于检查一个字符串是否包含另一个字符串。
/tag[contains(@attribute, 'substring')]
其中，tag表示要匹配的标签名，@attribute表示要匹配的属性名，而'substring'则是要查找的子字符串。
例如，如果我们要查找一个HTML文档中所有class属性包含'test'字符串的div标签，可以使用如下的XPath表达式：
//div[contains(@class, 'test')]
"""
result11 = html_parse.xpath('//li[contains(@class,"li")]/a/text()')
result12 = html_parse.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# 按序选择
result13 = html_parse.xpath('//li[1]/a/text()')
result14 = html_parse.xpath('//li[last()]/a/text()')
result15 = html_parse.xpath('//li[last()-2]/a/text()')
result16 = html_parse.xpath('//li[position()<3]/a/text()')

# 节点轴选择
# ancestor轴，可以获取所有祖先节点
result17 = html_parse.xpath('//li[1]/ancestor::*')
# 冒号后面加了div，于是得到的结果就只有 div 这个祖先节点了。
result18 = html_parse.xpath('//li[1]/ancestor::div')
# attribute轴，可以获取所有属性值
result19 = html_parse.xpath('//li[1]/attribute::*')
# child轴，可以获取所有直接子节点
result20 = html_parse.xpath('//li[1]/child::a[@href="link1.html"]')
# descendant轴，可以获取所有子孙节点
result21 = html_parse.xpath('//li[1]/descendant::span')
# following轴，可以获取当前节点之后的所有节点,加了索引选择，所以只获取了第二个后续节点
result22 = html_parse.xpath('//li[1]/following::*[2]')
# following-sibling 轴可以获取当前节点之后的所有同级节点
result23 = html_parse.xpath('//li[1]/following-sibling::*')

print(result.decode('utf-8'))
print('result2 : ', result2)
print('result3 : ', result3)
print('result4 : ', result4)
print('result5 : ', result5)
print('result6 : ', result6)
print('result7 : ', result7)
print('result8 : ', result8)
print('result9 : ', result9)
print('result10 : ', result10)
print('result11 : ', result11)
print('result12 : ', result12)
print('result13 : ', result13)
print('result14 : ', result14)
print('result15 : ', result15)
print('result16 : ', result16)
print('result17 : ', result17)
print('result18 : ', result18)
print('result19 : ', result19)
print('result20 : ', result20)
print('result21 : ', result21)
print('result22 : ', result22)
print('result23 : ', result23)
