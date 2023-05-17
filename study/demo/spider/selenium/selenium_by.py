from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置Chrome浏览器
driver = webdriver.Chrome()

# 打开目标网页
url = "https://www.example.com"
driver.get(url)

# 通过 ID 定位页面元素
elem = driver.find_element(By.ID, 'element-id')

# 通过 Class Name 定位页面元素
elem = driver.find_element(By.CLASS_NAME, 'element-class')

# 通过 Tag Name 定位页面元素
elem = driver.find_element(By.TAG_NAME, 'a')

# 通过 Name 定位页面元素
elem = driver.find_element(By.NAME, 'element-name')

# 通过 Link Text 定位页面元素
elem = driver.find_element(By.LINK_TEXT, 'link text')

# 通过 Partial Link Text 定位页面元素
elem = driver.find_element(By.PARTIAL_LINK_TEXT, 'partial link text')

# 通过 CSS Selector 定位页面元素
elem = driver.find_element(By.CSS_SELECTOR, '#element-id .element-class')

# 通过 XPath 定位页面元素
elem = driver.find_element(By.XPATH, "//ul[@id='element-id']/li[1]")


print('elem', elem)

# 关闭浏览器
driver.quit()
