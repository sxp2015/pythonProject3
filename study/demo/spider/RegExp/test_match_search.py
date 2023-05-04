import re

content1 = 'Hello 1234567 World This is a Regex Demo'
content2 = """Hello 1234567 World This 
is a Regex Demo"""
content3 = """ Extra stings Hello 1234567 World This is a Regex Demo Extra stings"""

result1 = re.match("^He.*?(\d+).*?Demo", content1)
print('没有加re.S ', result1.group(1))

result2 = re.match("^He.*?(\d+).*?Demo", content2, re.S)
print('加re.S ', result2.group(1))

# match 方法 是从字符串的开头开始匹配的，意味着一旦开头不匹配，整个匹配就失败了。所以换成Search方法
# result3 = re.match("^He.*?(\d+).*?Demo", content3, re.S)
# print('加re.S ', result3.group(1))

result3 = re.search(r'\d+', content3)
print('search方法 ', result3.group())
