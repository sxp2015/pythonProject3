from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.ttk import Separator

window = Tk()
window.title('通过按钮选择，改变背景颜色案例')

window.geometry('360x240')


def bg_update():
    """更改窗口背景颜色"""
    my_color = askcolor()
    print(type(my_color), my_color)
    # 使用 my_color 元组中的第二个元素（即十六进制表示的颜色）更新窗口的背景色
    window.config(bg=str(my_color[1]))


btn = Button(text="选择背景颜色", command=bg_update)
btn.pack(pady=10)

window.mainloop()
