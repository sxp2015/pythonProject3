from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('Message Box 标签')

window.geometry("480x320")


def show_msg():
    # messagebox.showinfo()
    messagebox.showinfo("邮件通知", "邮件已被删除")


def retry_cancel():
    retry = messagebox.askretrycancel("重试", "是否重试?")
    print('retry', retry)


def yes_no_cancel():
    yes_no = messagebox.askyesnocancel("安装", "是否取消?")
    print('yes_no', yes_no)


btn_msg = Button(window, text="显示弹窗", command=show_msg)

btn_msg.pack()

btn_retry = Button(window, text="重试", command=retry_cancel)
btn_retry.pack()

Button(window, text='安装失败', command=retry_cancel).pack()

Button(window, text='结束完成', command=yes_no_cancel).pack()

window.mainloop()
