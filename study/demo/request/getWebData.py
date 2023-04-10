from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 定义需要提取的页面URL和文本内容保存的文件名
url = "https://chat.binjie.site:7777/?ref=www.deepdh.com#/chat/1680759442328"
filename = "output.txt"

# 打开浏览器，并访问指定的页面 # 注意替换成适合自己系统的chromedriver路径
driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

driver.get(url)

# 在页面中定位到需要获取的元素位置
element = driver.find_element(By.XPATH, "//div[@class='markdown-body']")

# 获取元素的HTML代码，并用BeautifulSoup解析
html = element.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")

# 提取文本内容并保存到本地文件
text = soup.get_text()
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

# 关闭浏览器
driver.quit()