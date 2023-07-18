from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

window.title('下拉列表选项案例')

window.geometry("480x320")

var = StringVar()

combo_var = StringVar()

option_menu = ("Banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango", "Apple", "Pear", "Peach", "Cherry")


def get_option_value():
    print("value = ", var.get())


def combo_selected(event):
    combo_var.set(var.get())


# 设立默认选项  也可以，# var.set(option_menu[0])
var.set("Banana")

option = OptionMenu(window, var, *option_menu)

combobox = Combobox(window, textvariable=var, values=option_menu)


combobox.bind("<<ComboboxSelected>>",  combo_selected)

# 默认选项
# combobox.current(2)

lab = Label(window, text="选项是：", textvariable=var)

combo_label = Label(window, text="当前的选项是：", textvariable=combo_var)

btn = Button(window, text="打印选项", command=get_option_value)

lab.pack(anchor=CENTER, pady=10)

combo_label.pack(anchor=CENTER, pady=10)

combobox.pack(anchor=CENTER, pady=10)

btn.pack(anchor=S, side=BOTTOM, pady=10)
option.pack()

window.mainloop()
