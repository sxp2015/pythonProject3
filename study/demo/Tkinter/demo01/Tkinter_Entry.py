from tkinter import *

window = Tk()
window.title('文本框')

label_name = Label(window, text="姓名")
label_address = Label(window, text="地址")
label_password = Label(window, text="密码")

entry_name = Entry(window)
entry_address = Entry(window)
entry_password = Entry(window, show='*')

label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)

label_address.grid(row=1, column=0)
entry_address.grid(row=1, column=1)

label_password.grid(row=2, column=0)
entry_password.grid(row=2, column=1)

window.mainloop()
