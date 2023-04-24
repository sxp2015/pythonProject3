import pyautogui, time, subprocess

time.sleep(2)
# 打开画图程序
ms_paint_path = r'C:\WINDOWS\system32\mspaint.exe'

subprocess.Popen(ms_paint_path)

pyautogui.moveTo(23, 22)

pyautogui.click()

distance = 300

change = 10

pyautogui.moveTo(300, 300)

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)  # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)  # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    stance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.


# while change < distance:
#     pyautogui.drag(change, 0, duration=0.2)  # Move right.
#     pyautogui.drag(0, change, duration=0.2)  # Move down.
#     pyautogui.drag(-change, 0, duration=0.2)  # Move left.
#     pyautogui.drag(0, -change, duration=0.2)  # Move up.
#
#     change += change
