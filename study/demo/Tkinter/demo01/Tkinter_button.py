from tkinter import *

window = Tk()
window.title('按钮布局及事件触发')


# window.geometry("1600x900")


def show_message():
    message_label["text"] = "I love Python"
    message_label["bg"] = "lightyellow"
    message_label["fg"] = "black"
    message_label["font"] = "Helvetic 24 bold"


def show_message2():
    message_label2.config(text="I love Tkinter", bg="lightgreen", fg="white", font="Rome 24 bold")


message_label = Label(window)

message_label2 = Label(window)

btn = Button(window, text="打印消息", command=show_message)
btn2 = Button(window, text="打印消息2", command=show_message2)
close_btn = Button(window, text="关闭打印", command=window.destroy)

message_label.pack()
message_label2.pack()

btn.pack(side=LEFT)
btn2.pack(side=LEFT)
close_btn.pack(side=LEFT)

window.mainloop()
