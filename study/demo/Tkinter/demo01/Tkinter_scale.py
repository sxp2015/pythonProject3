from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('Scale 刻度尺')

window.geometry('300x150')
"""
from =0  #起点值
to=10,  # 终点值
troughcolor="yellow" #槽的颜色
width="30"  槽的高度
tickinterval=2  刻度
label="My Scale"  标签
length=300   控件像素的长度
orient=HORIZONTAL 布局方向：水平

"""

slider = Scale(window, from_=0, to=10, orient=HORIZONTAL, troughcolor='yellow', width=20, length=300, tickinterval=2,
               label="阀值滑块")

# 设置默认初始值
slider.set(3)

slider.pack()

window.mainloop()
