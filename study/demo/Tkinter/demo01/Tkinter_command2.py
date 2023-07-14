from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('Command 2标签')

window.geometry("480x320")

x, y = 0, 0
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x, y)
var.set(text)

var_text = StringVar()
var_text.set("Click Me")


# 鼠标移动事件
def mouse_motion(event):
    global x, y
    x, y = event.x, event.y
    var.set("Mouse location - x:{}, y:{}".format(x, y))


# 鼠标进入事件
def mouse_enter(event):
    var_text.set("Mouse entered")


# 鼠标移出事件
def mouse_leave(event):
    var_text.set("Mouse left")


# 键盘退出
def key_quit(event):
    is_quit = messagebox.askyesno("退出", "是否退出?")
    if is_quit:
        window.destroy()

    else:
        return


# 打印按下的键
def show_key(event):
    print(f"您按下了{repr(event.char)}键。。")


mouse_status_label = Label(window, textvariable=var_text, bg="yellow", fg="black", height=3, width=20, cursor="hand2",
                           font="Times 20 bold", relief=RAISED)
mouse_status_label.pack(anchor=W, padx=10, pady=10)
mouse_status_label.bind('<Leave>', mouse_leave)
mouse_status_label.bind('<Enter>', mouse_enter)

label = Label(window, textvariable=var)
label.pack(anchor=S, side=RIGHT, padx=10, pady=10)

window.bind("<Motion>", mouse_motion)
window.bind('<Escape>', key_quit)
window.bind('<Key>', show_key)

window.mainloop()
