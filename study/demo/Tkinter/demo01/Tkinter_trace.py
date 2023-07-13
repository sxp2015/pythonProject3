from tkinter import *
from tkinter import *

window = Tk()

window.title('变量改变追踪')


def input_callback(name, index, mode):
    # out_label.config(text=x.get())
    out_variable.set("同步显示：" + x.get())
    print("data changed:", x.get())
    print("name = %r, index = %r, mode=%r" % (name, index, mode))


x = StringVar()

x_label = Label(window, text="请输入任意数值")
x_entry = Entry(window, textvariable=x)

out_variable = StringVar()
out_variable.set("同步显示")
out_label = Label(window, textvariable=out_variable)

x_label.pack(side=LEFT, pady=5, padx=5)
x_entry.pack(padx=5, pady=5)
out_label.pack(padx=5, pady=5, side=LEFT)

x.trace('w', callback=input_callback)
window.mainloop()
