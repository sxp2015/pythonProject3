from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('简单程序')

entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W)

var = BooleanVar()
var.set(False)


def select_all():
    # 全选字符串
    entry.select_range(0, END)


def cancel_select():
    entry.select_clear()


def delete_input():
    entry.delete(0, END)


def read_only():
    entry.config(state=DISABLED) if var.get() else entry.config(state=NORMAL)


# ROW1 - Button
btn_select_all = Button(window, text='全选', command=select_all)
btn_select_all.grid(row=1, column=0, padx=5, pady=5, sticky=W)

btn_cancel_select = Button(window, text='取消全选', command=cancel_select)
btn_cancel_select.grid(row=1, column=1, padx=5, pady=5, sticky=W)

btn_delete_input = Button(window, text='删除', command=delete_input)
btn_delete_input.grid(row=1, column=2, padx=5, pady=5, sticky=W)

btn_quit = Button(window, text='退出', command=window.destroy)
btn_quit.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# ROW2 - Separator
sep = Separator(window, orient=HORIZONTAL)
sep.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=W)

check_read_only = Checkbutton(window, text='只读', variable=var, command=read_only)
check_read_only.grid(row=3, column=0, padx=5, pady=5, sticky=W)

window.mainloop()
