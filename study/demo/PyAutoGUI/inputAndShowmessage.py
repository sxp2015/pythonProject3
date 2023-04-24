import time

import pyautogui

pyautogui.alert(text='hello')
time.sleep(0.5)
pyautogui.confirm('你要登陆吗？')
time.sleep(0.5)
pyautogui.prompt(title='用户登陆', text='用户名/邮箱/手机号')
time.sleep(0.5)
pyautogui.password(title='用户登陆', text='用户密码最少6位')
