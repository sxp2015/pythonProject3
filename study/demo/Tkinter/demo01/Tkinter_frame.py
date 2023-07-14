from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('容器和框架')

frame_upper = Frame(window, bg="lightyellow", width=200, height=100, borderwidth=5, relief=RIDGE)
frame_upper.pack()

button_red = Button(frame_upper, text="Red", bg="red", fg="white", relief=RAISED)
button_red.pack(side=LEFT, padx=5, pady=5)

button_green = Button(frame_upper, text="Green", bg="green", fg="white", relief=RAISED)
button_green.pack(side=LEFT, padx=5, pady=5)

button_blue = Button(frame_upper, text="Blue", bg="blue", fg="white", relief=RAISED)
button_blue.pack(side=LEFT, padx=5, pady=5)

frame_lower = Frame(window, bg="lightblue")
frame_lower.pack()

button_orange = Button(frame_lower, text="Orange", bg="orange", fg="white", relief=RAISED)
button_orange.pack(side=LEFT, padx=5, pady=5)

sp = Separator(window, orient=HORIZONTAL)
sp.pack(fill=BOTH, padx=5, pady=5)

language_frame = Frame(width=400, height=200, relief=RAISED, borderwidth=5)
language_frame.pack(padx=5, pady=5)

label_title = Label(language_frame, text="语言选择")
label_title.pack(padx=5, pady=5)

python_option = Checkbutton(language_frame, text="Python")
python_option.pack(anchor=W, padx=5, pady=5)

java_option = Checkbutton(language_frame, text="Java")
java_option.pack(anchor=W, padx=5, pady=5)

html_option = Checkbutton(language_frame, text="HTML")
html_option.pack(anchor=W, padx=5, pady=5)

window.mainloop()
