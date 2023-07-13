from tkinter import *
from PIL import Image, ImageTk

# 创建窗口对象
window = Tk()
window.title('计算公式-eval')
# window.geometry('500x350')

input_label = Label(window, text="请输入数学表达式")
input_entry = Entry(window)
input_label.pack()
input_entry.pack()

out_label = Label(window)
out_label.pack(fill=BOTH, expand=True)


def cal():
    out_label.config(text="结果：" + str(eval(input_entry.get())))


cal_button = Button(window, text="计算", command=cal)
cal_button.pack(pady=5)

window.mainloop()
