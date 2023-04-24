import time, pathlib
import webbrowser
import pyautogui

url = 'https://baijiahao.baidu.com/builder/rc/home'
webbrowser.open(url)
# 等待3秒切换界面
time.sleep(10)
# 先获取屏幕快照截图
im = pyautogui.screenshot()
# 取色
# pyautogui.pixel(74, 384)

# 在截图中查找指定的图片
image_file = 'baijiahao.png'
image_path = str(pathlib.Path.cwd() / image_file)

image_location = pyautogui.locateOnScreen(image_path)

# 如果找到了图片，则输出图片的位置
if image_location:
    print('Image found at:', image_location)
else:
    print('Image not found on the screen.')

# 当前活动窗口
# fw = pyautogui.getActiveWindow
#
# print('fw', str(fw))
# print('image_location', image_location)

im.save('图像识别.png')

# 输出图像的位置
# print("submit position", submit)
# print("submit position2", submit2)
