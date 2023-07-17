from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('列表项添加和删除操作')

window.geometry("380x320")

fruits = ["Banana", "watermelon", "pineapple", "Orange", "Grapes", "Mango"]


def item_add():
    var_add = entry.get()
    if len(var_add.strip()) == 0:
        return
    lb.insert(END, var_add)
    entry.delete(0, END)


def item_deleted():
    index = lb.curselection()
    if len(index) == 0:
        return
    lb.delete(index[0])


entry = Entry(window)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_add = Button(window, text="添加", width=10, command=item_add)
btn_add.grid(row=0, column=1, padx=5, sticky=W)

btn_delete = Button(window, text="删除", width=10, command=item_deleted)
btn_delete.grid(row=0, column=2, padx=5, pady=5, sticky=W)


lb = Listbox(window)
lb.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=W+E)


window.mainloop()
