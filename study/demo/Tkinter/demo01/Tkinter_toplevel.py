import random
from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('Toplevel 子窗口')
# window.geometry('200x200')

msg_yes, msg_no, msg_exit = 1, 2, 3


def message_box():
    msg_type = random.randint(1, 3)
    label_text = None

    if msg_type == msg_yes:
        label_text = 'Yes'
    elif msg_type == msg_no:
        label_text = 'No'
    elif msg_type == msg_exit:
        label_text = 'Exit'

    top_level = Toplevel()
    top_level.title("message box")
    top_level.geometry('200x100')
    Label(top_level, text=label_text).pack(fill=BOTH, expand=True)


btn = Button(window, text="Click Me", command=message_box)
btn.pack()

window.mainloop()
