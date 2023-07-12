# 导入 tkinter 模块
from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('demo-04')
window.geometry("300x180")

OK_Label = Label(window, text="OK", font="Times 20 bold", fg="white", bg="blue")
OK_Label.pack(anchor=S, side=RIGHT, padx=10, pady=10)

NO_Label = Label(window, text="NO", font="Times 20 bold", fg="white", bg="red")
NO_Label.pack(anchor=S, side=RIGHT, pady=10)

window.mainloop()
