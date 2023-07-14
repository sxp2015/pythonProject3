from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('Command 标签')

window.geometry("480x320")


def button_clicked():
    label.config(text="You clicked me!")


def click_me_right(event):
    label.config(text="你点击了鼠标右键")
    print(f'event:{event}, event_x:{event.x}, event_y:{event.y}')


def button_python_clicked():
    if var_python.get():
        label.config(text="You selected Python!")
    else:
        label.config(text="You unselected Python!")


def button_java_clicked():
    if var_Java.get():
        label.config(text="You selected Java!")
    else:
        label.config(text="You unselected Java!")


btn = Button(window, text="Click me", command=button_clicked)
btn.pack(anchor=W)

btn2 = Button(window, text="单击鼠标右键")
btn2.bind("<Button-3>", click_me_right)
btn2.pack(anchor=W)

var_python = BooleanVar()
check_button_python = Checkbutton(window, text="Python", variable=var_python, command=button_python_clicked)
check_button_python.pack(anchor=W)

var_Java = BooleanVar()
check_button_Java = Checkbutton(window, text="Java", variable=var_Java, command=button_java_clicked)
check_button_Java.pack(anchor=W)

label = Label(window, bg="yellow", fg="black", height=3, width=20, font="Times 20 bold")
label.pack()

window.mainloop()
