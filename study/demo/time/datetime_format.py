import datetime

# 中国人的习惯，当前时间
import time

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 获得当前时间的，时间戳
current_form_timestamp = time.time()

# fromtimestamp 方法将 Unix 时间戳（从 1970 年 1 月 1 日开始的秒数）转换为对应的本地时间。
# 在这个例子中，时间戳 1000000 对应的时间是 1970 年 1 月 12 日 9 点 46 分 40 秒。
print('time:',datetime.datetime.fromtimestamp(1000000))

print('当前时间', current_time)
print('当前时间戳', current_form_timestamp)
