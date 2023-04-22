# 导入 subprocess 和 time 模块
import subprocess
import time

# 设置倒计时时间
time_left = 6

# 循环执行倒计时，每秒输出当前剩余时间
while time_left > 0:
    print(time_left, end=' ')
    time.sleep(1)
    time_left -= 1

# 倒计时结束，播放音乐文件
# subprocess.Popen 函数用于执行系统命令，['start', 'Alarm.mp3'] 表示启动默认程序打开 Alarm.mp3 音乐文件
# shell=True 表示在命令行中执行命令
subprocess.Popen(['start', 'Alarm.mp3'], shell=True)
