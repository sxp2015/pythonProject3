from tkinter import *

window = Tk()
window.title('place方法')
window.geometry("640x480")

label_red = Label(window, bg='red', text='red', relief='raised', width=20, fg='white')
label_orange = Label(window, bg='orange', text='orange', relief='raised', width=20, fg='white')
label_yellow = Label(window, bg='yellow', text='yellow', relief='raised', width=20, fg='white')
label_green = Label(window, bg='green', text='green', relief='raised', width=20, fg='white')
label_blue = Label(window, bg='blue', text='blue', relief='raised', width=20, fg='white')
label_purple = Label(window, bg='purple', text='purple', relief='raised', width=20, fg='white')

label_purple.place(x=30, y=30)
label_blue.place(x=60, y=60)
label_green.place(x=90, y=90)

img = PhotoImage(file='images/north_gate.png')

label_image = Label(window, image=img, width=400, height=300)
label_image.place(x=30, y=120)

window.mainloop()
