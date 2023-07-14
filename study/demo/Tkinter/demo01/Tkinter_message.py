from tkinter import *

window = Tk()

window.title('Message 标签')

window.geometry("480x320")

text_val = StringVar()
msg = Message(window, textvariable=text_val, bg="yellow", relief=RIDGE, width=150)
msg2 = Message(window, text="另外一种配置内容的方式", bg="lightblue", relief=RAISED)

text_val.set("这是一条短信息的内容，通过Message函数创建的")

msg.pack(padx=5, pady=5)
msg2.pack(padx=5, pady=5)

window.mainloop()
