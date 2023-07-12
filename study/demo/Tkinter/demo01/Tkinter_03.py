# 导入 tkinter 模块
from tkinter import *
from tkinter.ttk import Separator

container = Tk()
container.title('demo-03')

myTitle = """一个人的极境施行"""
myContent = """2016年12月,我一个人订了机票和船票开始我的南板旅行，飞机经迪拜再往阿根廷的乌斯怀亚，在此我登上邮轮开始我的南板之旅"""

lab1 = Label(container, text=myTitle, font="Helvetic 20 bold")
lab1.pack(padx=10, pady=10)

# orient 分隔符朝向 HORIZONTAL水平
sep_1 = Separator(container, orient=HORIZONTAL)
sep_1.pack(fill=X, padx=5)

lab2 = Label(container, text=myContent)
lab2.pack(padx=10, pady=10)

# orient 分隔符朝向 HORIZONTAL水平
sep_2 = Separator(container, orient=HORIZONTAL)
sep_2.pack(fill=X, padx=5)

lab3 = Label(container, text="Python Tkinter Pack方法", bg='lightyellow', width=25)
lab4 = Label(container, text="Python Tkinter Label方法", bg='lightgreen', width=25)
lab5 = Label(container, text="Python Tkinter Tk方法", bg='lightblue', width=25)

lab3.pack(side=LEFT)
lab4.pack(side=LEFT)
lab5.pack(side=LEFT)

# orient 分隔符朝向 HORIZONTAL水平
# sep_3 = Separator(container, orient=HORIZONTAL)
# sep_3.pack(fill=X, padx=5)

# lab6 = Label(container, text="Python Tkinter Pack方法", bg='lightyellow', width=25)
# lab7 = Label(container, text="Python Tkinter Label方法", bg='lightgreen', width=25)
# lab8 = Label(container, text="Python Tkinter Tk方法", bg='lightblue', width=25)
#
# lab6.pack()
# lab7.pack(side=LEFT)
# lab8.pack(side=RIGHT)


# orient 分隔符朝向 HORIZONTAL水平
# sep_4 = Separator(container, orient=HORIZONTAL)
# sep_4.pack(fill=X, padx=5)

Reliefs = ("flat", "groove", "raised", "ridge", "solid", "sunken")

for Relief in Reliefs:
    Label(container, text=Relief, relief=Relief, fg="blue", font="Times 20 bold").pack(side=LEFT, padx=5)

# orient 分隔符朝向 HORIZONTAL水平
# sep_4 = Separator(container, orient=HORIZONTAL)
# sep_4.pack(fill=X, padx=5)

container.mainloop()
