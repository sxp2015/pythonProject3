import time
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('进度条案例')
window.geometry('600x400')

download_bytes = 0
max_bytes = 10000

var_progress3 = DoubleVar()
var_progress4 = DoubleVar()

# 是否停止运行
is_stop = True


# 模拟加载数据
def load_data_1():
    pb1['value'] = 0
    pb1['maximum'] = max_bytes
    running_1()


# 定义函数让进度条运行起来
def running_1():
    global download_bytes
    download_bytes += 500
    pb1['value'] = download_bytes
    if download_bytes < max_bytes:
        # 0.05 秒运行一次
        pb1.after(50, running_1)


def running_2():
    for i in range(100):
        pb2['value'] = i + 1
        window.update()
        time.sleep(0.05)


def running_3():
    while pb3.cget('value') < pb3['maximum']:
        pb3.step(2)
        window.update()
        var_progress3.set(pb3.cget('value'))
        time.sleep(0.05)


# 开始运行函数
def start_running():
    pb4.start()
    while pb4.cget('value') < pb4['maximum']:
        pb4.step(1)
        window.update()
        var_progress4.set(pb4.cget('value'))
        time.sleep(0.05)


# 停止运行函数
def stop_running():
    pb4.stop()


# 创建进度条1
pb1 = Progressbar(window, maximum=100, mode='determinate', value=0, orient=HORIZONTAL, length=200)
pb1.pack(padx=10, pady=10)
# 创建启动按钮1
button_start_1 = Button(window, text='启动1', command=load_data_1)
button_start_1.pack(padx=10, pady=10)

# 创建进度条2
pb2 = Progressbar(window, maximum=100, mode='determinate', value=0, orient=HORIZONTAL, length=200)
pb2.pack(padx=10, pady=10)
# 创建启动按钮2
button_start_2 = Button(window, text='启动2', command=running_2)
button_start_2.pack(padx=10, pady=10)

# 创建进度条3
frame1 = Frame(window)
frame1.pack(padx=10, pady=10, fill=X)

pb3 = Progressbar(frame1, maximum=100, mode='determinate', value=0, orient=HORIZONTAL, length=200)
pb3.pack(padx=10, pady=10, side=LEFT)

lab1 = Label(frame1, text='进度值3', textvariable=var_progress3)
lab1.pack(padx=10, pady=10, side=LEFT)

# 创建启动按钮3
button_start_3 = Button(frame1, text='启动3', command=running_3)
button_start_3.pack(padx=10, pady=10, side=RIGHT)

# 创建进度条4
frame2 = Frame(window)
frame2.pack(padx=10, pady=10, fill=X)

pb4 = Progressbar(frame2, maximum=100, mode='indeterminate', value=0, orient=HORIZONTAL, length=200)
pb4.pack(padx=10, pady=10, side=LEFT)

lab2 = Label(frame2, text='进度值4', textvariable=var_progress4)
lab2.pack(padx=10, pady=10, side=LEFT)

# 创建启动按钮4
button_start_4 = Button(frame2, text='启动4', command=start_running)
button_start_4.pack(padx=10, pady=10, side=RIGHT)

# 创建停止按钮4
stop_style = Style()
stop_style.configure('Custom.TButton', background='red')

# 这里设置调用一个函数，比如 stop_running
button_stop = Button(frame2, text='停止4', command=stop_running, style='Custom.TButton')
button_stop.pack(padx=10, pady=10, side=RIGHT)

# 运行程序
window.mainloop()
