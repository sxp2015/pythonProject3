from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('单选和复选框案例')

var = StringVar()
var.set("男生")

label = Label(window, text="请选择性别", bg="lightyellow", width=30, height=2)
label.pack()


def print_selection():
    label.config(text="你是" + var.get())


radio_man = Radiobutton(window, text="男生", variable=var, value="男生", command=print_selection)
radio_man.pack()

radio_woman = Radiobutton(window, text="女生", variable=var, value="女生", command=print_selection)
radio_woman.pack()

# orient 分隔符朝向 HORIZONTAL水平
sep = Separator(window, orient=HORIZONTAL)
sep.pack(fill=X, padx=5)

var_city = IntVar()
var_city.set(0)

cities = {0: "东京", 1: "纽约", 2: "巴黎", 3: "伦敦", 4: "香港"}


def print_cities():
    print('Cities:', cities[var_city.get()])


label_cities = Label(window, text="请选择城市", fg="black", bg="lightyellow", width=30, height=2)
label_cities.pack()

for val, city in cities.items():
    # indicatoron=False 可以让选项，变成盒子样式
    Radiobutton(window, text=city, indicatoron=False, variable=var_city, value=val, command=print_cities).pack()

# orient 分隔符朝向 HORIZONTAL水平
sep2 = Separator(window, orient=HORIZONTAL)
sep2.pack(fill=X, padx=5)

Label(window, text="请选择喜欢的运动", fg="blue", bg="lightyellow", width=30).pack()

sports = {0: "美式足球", 1: "棒球", 2: "篮球", 3: "网球"}
checkboxes = {}
for i in range(len(sports)):
    checkboxes[i] = BooleanVar()
    Checkbutton(window, text=sports[i], variable=checkboxes[i]).pack(fill=X, padx=5)


def print_sports_info():
    selection = ''
    for j in checkboxes:
        if checkboxes[j].get():
            selection = selection + sports[j] + '\t'
    print('selection', selection)


btn = Button(window, text="确定", width=10, command=print_sports_info)
btn.pack(fill=X, padx=5)

window.mainloop()
