from tkinter import *

window = Tk()

window.title("显示所选的项目-选择事件绑定")
window.geometry("400x300")

var = StringVar()


def item_selected(event):
    obj = event.widget
    index = obj.curselection()
    var.set(obj.get(index))


def item_selected2(event):
    obj = event.widget
    index = obj.curselection()
    for i in index:
        print(obj.get(i))
    print('______________')


fruits = ["Banana", "watermelon", "pineapple", "Orange", "Grapes", "Mango"]

lab = Label(window, text="所选的项目是", textvariable=var)
lab.pack(pady=5)

list_box = Listbox(window, selectmode=EXTENDED)
list_box2 = Listbox(window)

for fruit in fruits:
    list_box.insert(END, fruit)
    list_box2.insert(END, fruit)

list_box.bind("<<ListboxSelect>>", item_selected2)
list_box2.bind("<<ListboxSelect>>", item_selected)

list_box.pack(pady=5, side=LEFT)
list_box2.pack(pady=5, side=RIGHT)
window.mainloop()
