import re, requests

# 目标URL
TARGET_URL = 'https://antispider4.scrape.center/css/app.654ba59e.css'

# 发送HTTP请求，获取响应内容
response = requests.get(TARGET_URL, verify='./scrape.crt')

# 定义正则表达式
pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')

# 使用正则表达式搜索匹配项
results = re.findall(pattern, response.text)

# 将搜索结果转换为字典
icon_map = {item[0]: item[1] for item in results}
# print('icon_map:', icon_map)
print('icon_map[789]:', icon_map['789'])
print('icon_map[437]:', icon_map['437'])