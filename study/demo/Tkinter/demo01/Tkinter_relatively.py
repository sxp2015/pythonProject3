from tkinter import *

window = Tk()
window.title('相对位置')
window.geometry("1600x900")

img = PhotoImage(file='images/north_gate.png')

label_image = Label(window, image=img)
# relx/rely 可以设置相对于父容器(可想成父窗口)的位置，
# relwidth/relheight 设置相对大小。这个相对位置与相对大小是相对于父窗口而言，其值为 0.0~1.0。
label_image.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

window.mainloop()

"""
我们使用 tkinter 模块设计 GUI程序时，虽然可以使用 place()方法很精确地设置控件的位置，
不过笔者建议尽量使用 pack()和 grid()方法定位组件，因为当窗口中组件较多时，
使用 place()计算组件位置较不方便，同时若有新增或减少组件时又须重新计算设置组件位置，这样会比较不方便。
"""