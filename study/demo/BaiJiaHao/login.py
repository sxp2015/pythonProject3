from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# 设置Chrome浏览器驱动路径和启动选项
chrome_driver_path = "C:\\Program Files\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 最大化窗口

# 启动Chrome浏览器并访问指定页面
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get("https://baijiahao.baidu.com/builder/theme/bjh/login")

    # 等待页面加载完成
    time.sleep(2)

    # 自动聚焦到输入框并输入文本
    input_userName = driver.find_element("id", "TANGRAM__PSP_4__userName")
    input_password = driver.find_element("id", "TANGRAM__PSP_4__password")
    button_submit = driver.find_element("id", "TANGRAM__PSP_4__submit")

    input_userName.send_keys("风车百科")
    input_password.send_keys("s*************0")
    time.sleep(2)
    button_submit.click()
    time.sleep(120)

except Exception as e:
    print("程序运行出现错误：", e)
# finally:
# 关闭浏览器
# driver.quit()
