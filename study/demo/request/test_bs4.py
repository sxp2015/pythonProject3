import requests, bs4

url = 'https://www.baidu.com'

# 从网络上获取HTML文件
res = requests.get(url)

res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

print('noStarchSoup', type(noStarchSoup))

# 方法二读取本地HTML文件
exampleFile = open('test.html', 'r', encoding='utf8')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
# 返回的是一个集合
root_el = exampleSoup.select('#root')
# 获取集合中的一个节点 str(spanElem)
spanElem = root_el[0]
print('spanElem', str(spanElem))

# 获取节点中指定的内容 get('id')
id_content = spanElem.get('id')
print('id_content', id_content)

print('exampleSoup', type(exampleSoup))
print('root_el', type(root_el))
print('root_el_len', len(root_el), str(root_el[0]))
