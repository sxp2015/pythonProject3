import requests

url = 'https://api-hmugo-web.itheima.net/api/public/v1/home/catitems'
res = requests.get(url)
# 调用raise_for_status()，确保下载成功,下载中断会抛异常
res.raise_for_status()

dataFile = open('download.txt', 'wb')

# iter_content()方法在循环的每次迭代中返回一段内容,每一段都是bytes数据类型，你需要指定一段包含多少字节
for chunk in res.iter_lines():
    dataFile.write(chunk)

dataFile.close()
