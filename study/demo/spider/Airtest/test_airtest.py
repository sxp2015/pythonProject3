# 引入Android模块
from airtest.core.android import Android
# 引入API模块
from airtest.core.api import *
# 引入日志记录模块
import logging

# 设置airtest日志级别为WARNING
logging.getLogger('airtest').setLevel(logging.WARNING)
# 初始化Android设备
device: Android = init_device('Android')
# 判断设备是否已经锁屏
is_locked = device.is_locked()
print(f"is_locked:{is_locked}")
# 如果设备已经锁屏，解锁设备
if is_locked:
    device.unlock()
# 唤醒设备
device.wake()
# 获取设备应用列表
app_list = device.list_app()
print(f'app_list:{app_list}')
# 获取设备ID
uuid = device.uuid
print(f'uuid:{uuid}')
# 获取设备显示信息
display_info = device.get_display_info()
print(f'display_info:{display_info}')
# 获取设备渲染分辨率
resolution = device.get_render_resolution()
print(f'resolution:{resolution}')
# 获取设备IP地址
ip_address = device.get_ip_address()
print(f'ip_address:{ip_address}')
# 获取设备顶部Activity
top_activity = device.get_top_activity()
print(f'top_activity:{top_activity}')
# 判断设备是否显示软键盘
is_keyboard_shown = device.is_keyboard_shown()
print(f'is_keyboard_show:{is_keyboard_shown}')


# 定义一个返回设备信息的函数
def device():
    return G.DEVICE


# 打印设备信息
print('device-info:', device())

# 获取所有设备列表
device_list = G.DEVICE_LIST
print('device_list-1:', device_list)

# 获取容量存储信息
memory_info = shell('cat /proc/meminfo')
print('memory_info:', memory_info)


# uri = 'Android://127.0.0.1:7555/'
# device:Android = connect_device(uri)

# print('device_list-2:', device_list)
