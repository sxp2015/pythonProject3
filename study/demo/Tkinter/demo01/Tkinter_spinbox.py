from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('spinbox 输入框')

window.geometry('300x350')


def print_info():
    print("spin", spin.get())


def print_info2():
    print("spin", spin2.get())


def print_info3():
    print("spin", spin3.get())


spin = Spinbox(window, from_=10, to=30, width=20, increment=2, command=print_info)
spin2 = Spinbox(window, width=20, values=["1", "5", "9", "33"], command=print_info2)
spin3 = Spinbox(window, width=20, values=("北京", "上海", "广州", "深圳"), command=print_info3)
spin.pack(pady=20)
spin2.pack(pady=20)
spin3.pack(pady=20)

window.mainloop()
