from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('Scale 刻度尺滑块，改变背景颜色案例')

window.geometry('360x240')


def bg_update(source):
    """更改窗口背景颜色"""
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()
    print("R = %d, G=%d, B=%d" % (red, green, blue))
    # 颜色转成十六进制的字符串
    # % ：是格式化字符串的起始符号。
    # 0 ：表示使用零填充，即如果生成的十六进制字符串不够两位数，会在前面填充零。
    # 2 ：表示生成的十六进制字符串的宽度为两个字符，不足两个字符时会进行填充。
    # x ：表示小写字母形式的十六进制数字。
    my_color = "#%02x%02x%02x" % (red, green, blue)
    window.config(bg=my_color)


frame = Frame(window)
frame.pack(pady=10)

red_slider = Scale(frame, from_=0, to=255, command=bg_update)
green_slider = Scale(frame, from_=0, to=255, command=bg_update)
blue_slider = Scale(frame, from_=0, to=255, command=bg_update)
green_slider.set(125)
red_slider.grid(row=0, column=0)
blue_slider.grid(row=0, column=1)
green_slider.grid(row=0, column=2)

window.mainloop()
