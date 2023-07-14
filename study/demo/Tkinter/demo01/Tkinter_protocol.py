from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('单通信协议, Protocol')

window.geometry("480x320")


def on_closing():
    res = messagebox.askokcancel("退出", "是否退出?")
    if res:
        window.destroy()
    else:
        return


window.protocol('WM_DELETE_WINDOW', on_closing)

window.mainloop()
