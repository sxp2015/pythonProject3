import json

"""
注意这里使用的是 
一、load方法，参数是一个文件操作对象，是将整个文件中的内容转化为JSON对象
二、loads方法，参数是一个JSON字符串,可以更灵活地控制要转化哪些内容
三、dumps方法 是将JSON对象转化为字符串
这两种写法的运行结果是完全一样的，可以在适当的场景下选择使用。

如果想保存JSON对象的缩进格式，可以再往dumps方法中添加一个参数indent，代表缩进字符的个数
要想输出中文，还需要指定参数ensure asci为False，以及规定文件输出的编码:

"""

json_str = """
[{"name":"Bob","gender":"male","birthday":"1992-10-18"},
{"name":"Selina","gender":"female","birthday":"1995-10-18"},
{"姓名":"张三","性别":"男","出生日期":"1990年12月11日"}]
"""
json_data = json.loads(json_str)

with open('data.json', 'a+', encoding='utf-8') as file:
    file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    file.close()

print('type ==', type(json_str))
print('json_data ==', json_data)
print('json_data type==', type(json_data))
print('json_data data 0==', json_data[0]['name'])
print('json_data data 1==', json_data[1].get('name'))
print('json_data data get==', json_data[1].get('age', 33))
print('json_data data get==', json_data[1])
