import pyautogui, time, subprocess

time.sleep(2)
# 打开画图程序
ms_paint_path = r'C:\WINDOWS\system32\mspaint.exe'
subprocess.Popen(ms_paint_path)
time.sleep(2)
pyautogui.moveTo(318, 77)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(318, 377)
pyautogui.click()
# write(内容，等待时间)
time.sleep(1)
pyautogui.write('hello,world \n', 0.25)

pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])
time.sleep(1)
# 输出货币符号
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
pyautogui.keyDown('enter')
time.sleep(1)
# 快捷键

pyautogui.hotkey('ctrl', 's')
