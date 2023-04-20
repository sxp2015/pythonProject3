import json, requests

weather_api = 'https://restapi.amap.com/v3/weather/weatherInfo?city=431025&key=f92689f7114be34ac30fcb3e90a183d9'

resp = requests.get(weather_api).text

# # 请注意，JSON字符串总是用双引号 loads 是把字符串变成 Json, 也可以把Json数据，转成Python值
data = json.loads(resp)
"""
indent：指定缩进级别，默认为 None。如果指定了该参数，则会在输出结果中使用指定数量的空格进行缩进，
让结果更加易读。例如 indent=4 表示使用 4 个空格进行缩进。
ensure_ascii：指定是否只使用 ASCII 字符编码，默认为 True。
如果指定了 ensure_ascii=False，则表示输出结果可以包含非 ASCII 字符，例如中文字符等。
"""
# json.dumps 把Python 值 变成 Json
print('Json: ', json.dumps(data, indent=4, ensure_ascii=False))
