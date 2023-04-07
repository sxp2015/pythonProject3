"""
这段代码是一个简单的Python程序，可以从必应搜索引擎爬取一组图片，并将其保存到本地。
具体来说，它首先使用requests库发起网络请求，获取必应搜索引擎中查询关键字为“春分临近农事忙”的图片搜索结果页面。
然后，使用BeautifulSoup库解析HTML响应，获取网页中所有图片的img标签。
接下来，程序会在本地创建一个名为bing_images的文件夹。循环遍历每张图片的img标签，
并使用requests库发起网络请求，获取图片二进制数据。最后，将图片数据写入以image_i.jpg格式命名的文件中，保
存到bing_images文件夹下。注意，在对图片进行网络请求时，需要先判断该图片链接是否为空，防止出现错误。

"""

import requests
from bs4 import BeautifulSoup
import os

url = "https://cn.bing.com/images/search?q=%e6%98%a5%e5%88%86%e4%b8%b4%e8%bf%91%e5%86%9c%e4%ba%8b%e5%bf%99&form=ISTRTH&id=A397739CCC77DA385C40AFE115BA19DD1D2EC4E0&cat=%E4%BB%8A%E6%97%A5%E7%83%AD%E5%9B%BE&disoverlay=1&first=1"


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img", class_="mimg")

if not os.path.exists("bing_images"):
    os.makedirs("bing_images")

for i, img in enumerate(img_tags):
    img_url = img.get("src")
    if not img_url:
        continue
    filename = f"bing_images/image_{i}.jpg"
    image_content = requests.get(img_url).content
    with open(filename, "wb") as f:
        f.write(image_content)