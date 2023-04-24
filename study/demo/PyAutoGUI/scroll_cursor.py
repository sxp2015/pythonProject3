# 导入需要的库
import subprocess # 可以启动外部程序
import time # 可以进行时间相关操作
import pyautogui # 可以模拟鼠标和键盘操作

# 定义Chrome浏览器路径
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# 启动Chrome浏览器
subprocess.Popen(chrome_path)

# 休眠4秒钟（等待Chrome浏览器完全打开）
time.sleep(4)

# 使用pyautogui模拟鼠标滚轮向下滚动550个单位距离
pyautogui.scroll(-550)
