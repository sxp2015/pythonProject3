import pyautogui

# for i in range(2):
#     print(pyautogui.position())
#     pyautogui.move(100, 0, duration=0.25)  # right
#     print(pyautogui.position())
#     pyautogui.move(0, 100, duration=0.25)  # down
#     print(pyautogui.position())
#     pyautogui.move(-100, 0, duration=0.25)  # left
#     print(pyautogui.position())
#     pyautogui.move(0, -100, duration=0.25)  # up
#     print(pyautogui.position())


# 移动鼠标到指定位置

# 移动鼠标到指定位置
pyautogui.moveTo(222, 748)

print('当前位置是', pyautogui.position())
# 默认是鼠标左键点击，click()，如果不传参数，默认是当前鼠标位置，如果有参数click(x,y)则是指定位置
pyautogui.click()
pyautogui.moveTo(718, 197)
pyautogui.click()