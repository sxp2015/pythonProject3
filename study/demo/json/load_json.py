import json


# 请注意，JSON字符串总是用双引号 loads 是把字符串变成 Json, 也可以把Json数据，转成Python值
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)

print('json_data:', jsonDataAsPythonValue)

# 下面把Python 值 变成 Json
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
json_dumps_value = json.dumps(pythonValue)
print('json_dumps_value:', json_dumps_value)