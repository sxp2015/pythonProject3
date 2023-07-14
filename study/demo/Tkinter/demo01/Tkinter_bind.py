from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('按钮事件绑定和解绑')

window.geometry("480x320")


def bind_me(event):
    print("You bind event!, 绑定了事件")


# def unbind_me(event):
#     print("取消了事件")


def toggle(on_or_off):
    if var_check.get():
        #  on_or_off.bind('<Button-1>', bind_me,add='+')，可以绑定多个事件
        on_or_off.bind('<Button-1>', bind_me, )
    else:
        print("取消了事件绑定")
        on_or_off.unbind('<Button-1>')


btn = Button(window, text="切换绑定状态")
btn.pack(anchor=W, padx=5, pady=5)

var_check = BooleanVar()
check_button = Checkbutton(window, text="bind / unbind", variable=var_check, command=lambda: toggle(btn))
check_button.pack(anchor=W, padx=5, pady=5)

window.mainloop()
