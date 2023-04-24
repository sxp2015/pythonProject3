import pyautogui

""""
pyautogui.mouseInfo() 是PyAutoGUI库中的一个函数，用于获取当前鼠标的位置及RGB颜色值等信息。
它返回的是一个字符串，其中包括了当前鼠标所在位置以及该位置的RGB颜色值。

这个函数可以帮助我们快速定位鼠标的位置，并查看该位置的颜色值，
方便进行后续的图像处理或界面识别等操作。在使用过程中，我们可以将鼠标移动到特定的位置，然后调用 pyautogui.mouseInfo() 函数来获取该位置的信息。

需要注意的是，该函数只能在Windows和macOS系统中正常工作，
且显示的RGB颜色值是基于屏幕的实际像素颜色值而非浏览器的颜色值。
另外，在调用该函数之前，需要确保安装了PyAutoGUI库，并激活了对应的Python虚拟环境。
"""
info = pyautogui.mouseInfo()

im = pyautogui.screenshot()

width, height = im.size
print('width', width, 'height', height)
im.save('screenshot.png')

# pixel(x,y)函数获得屏幕上某一像素点的RGB颜色值
print('RGB 颜色值 ： ', pyautogui.pixel(220, 750))
