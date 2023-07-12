from tkinter import *

window = Tk()
window.title('彩虹')
Colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
r = 0

for color in Colors:
    Label(window, text=color, relief='groove', width=20).grid(row=r, column=0)
    Label(window, bg=color, relief='groove', width=20).grid(row=r, column=1)
    r += 1

window.mainloop()
