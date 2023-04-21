import datetime
# 时间段
import time

timedelta = datetime.timedelta(days=3, hours=3, minutes=5, seconds=10, microseconds=22154)

# 计算1000天以后的日期
thousand_day = datetime.timedelta(days=1000)

today = datetime.datetime.now()

print('timedelta = ', timedelta)

print('total_seconds = ', timedelta.total_seconds())

print('1000天以后的日期', thousand_day + today)

# 指定时间触发程序

quitting_time = datetime.datetime(2023, 4, 21, 17, 00, 0)
while datetime.datetime.now() < quitting_time:
    time.sleep(1)

print('你的下班时间是:', quitting_time.strftime('%Y-%m-%d %H:%M:%S'), '现在时间是：',
      datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# ############ strptime函数示例 ##################

# 要转换的日期时间字符串
date_string = '2023-05-01 12:00:00'

# 字符串对应的日期时间格式化字符串
format_string = '%Y-%m-%d %H:%M:%S'

# 使用 strptime() 函数将字符串转换为日期时间对象
date_time = datetime.datetime.strptime(date_string, format_string)

# 打印转换后的日期时间对象
print(date_time)

"""
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)：创建一个包含日期和时间信息的日期时间对象。

year：年份（整数）
month：月份（整数，1-12）
day：日期（整数，1-31）
hour：小时数（整数，0-23）
minute：分钟数（整数，0-59）
second：秒数（整数，0-59）
microsecond：微秒数（整数，0-999999）
tzinfo：时区信息对象。默认情况下为None。
fold：代表了涉及到“时区调整”的逻辑。（Python 3.6 新增）
"""
