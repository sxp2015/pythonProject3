import time  # 导入time模块

# 让用户按下回车键，然后开始计时
print('按【回车键Enter】开始启动秒表，按【 Ctrl + C 】退出秒表')
input()

print('开始计时...')  # 提示开始计时

start_time = time.time()  # 记录开始计时时的时间戳
last_time = start_time  # 上次按下回车键的时间戳
lap_num = 1  # 初始化lap_num变量，记录当前为第几圈

try:
    while True:  # 进入循环，等待用户按下回车键
        input()  # 等待用户按下回车键

        lap_time = round(time.time() - last_time, 2)  # 计算自上次按下回车键以来的时间差，并保留两位小数
        total_time = round(time.time() - start_time, 2)  # 计算总共经过的时间，并保留两位小数

        # 输出当前圈数、总用时、本圈用时
        print('当前圈数 # %s: 总用时:%s (本圈用时:%s)' % (lap_num, total_time, lap_time), end='')

        lap_num += 1  # 圈数加1
        last_time = time.time()  # 更新上一次按下回车键的时间

        # 计数10次，程序退出
        if lap_num == 10:
            break

except KeyboardInterrupt:  # 如果捕获到Ctrl+C异常，则退出程序并输出"结束"
    print('\n 结束')
