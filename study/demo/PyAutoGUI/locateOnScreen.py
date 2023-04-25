import time, pathlib
import webbrowser
import pyautogui, pygetwindow

# 打开网页
# url = 'https://baijiahao.baidu.com/builder/rc/home'
# webbrowser.open(url)

# 等待3秒切换界面
time.sleep(3)

# 先获取屏幕快照截图
# im = pyautogui.screenshot()

# 获取当前屏幕的尺寸
screen_size = pyautogui.size()
print('屏幕尺寸:', screen_size)

# 根据坐标取色
# pyautogui.pixel(74, 384)

# 在定义图片的位置
image_file = 'submit.png'
image_path = str(pathlib.Path.cwd() / image_file)

# 在截图中查找指定的图片
image_location = pyautogui.locateOnScreen(image_path)

# 如果找到了图片，则输出图片的位置
if image_location:
    print('Image found at:', image_location)

    # 点击识别成功的坐标
    pyautogui.click(image_location)

    # 输出识别到的参数
    # print('left:', image_location[0])
    # print('left:', image_location.left)
    # print('top:', image_location.top)
    # print('width', image_location.width)
    # print('height:', image_location.height)


else:
    print('Image not found on the screen.')

# 当前活动窗口
fw = pyautogui.getActiveWindow()
print('活动窗口', str(fw))
print('活动窗口标题', str(fw.title))
print('活动窗口尺寸', str(fw.size))
print('活动窗口区域', str(fw.area))
print('活动窗口左上角', str(fw.topleft))
print('活动窗口右下角', str(fw.bottomright))
print('是否最大化', str(fw.isMaximized))

if not fw.isMaximized:
    # 获取窗口对象 返回一个窗口对象列表
    window = pygetwindow.getWindowsWithTitle(str(fw.title))[0]

    # 最大化窗口
    window.maximize()

    print("window = ", window)

# 保存屏幕快照
# im.save('图像识别.png')
