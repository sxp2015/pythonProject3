from tkinter import *

window = Tk()

window.title('变量赋值与取值')

msg_on = False

x = StringVar()


def btn_hit():
    global msg_on
    if not msg_on:
        msg_on = True
        x.set('I like Tkinter')
    else:
        msg_on = False
        x.set("")


def btn_hit2():
    if x.get() == "":
        x.set("I like Tkinter")
    else:
        x.set("")


label = Label(window, textvariable=x, fg="blue", bg="lightyellow", font="Verdana 16 bold", width=25, height=2)
label.pack()

btn = Button(window, text="点击显示", command=btn_hit2)
btn.pack()

window.mainloop()
