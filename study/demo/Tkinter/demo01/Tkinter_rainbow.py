from tkinter import *

window = Tk()
window.title('彩虹')
Colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
r = 0

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

for color in Colors:
    Label(window, text=color, relief='groove', width=20).grid(row=r, column=0, sticky=W+N+S+E)
    Label(window, bg=color, relief='groove', width=20).grid(row=r, column=1, sticky=W+N+S+E)
    r += 1

window.mainloop()
