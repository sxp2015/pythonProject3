from tkinter import *

window = Tk()
window.title('匿名函数Lambda')
window.geometry('480x320')


def change_background(background):
    window.config(bg=background)


exit_btn = Button(window, text='退出', command=window.destroy)
blue_btn = Button(window, text='Blue', command=lambda: change_background('blue'))
red_btn = Button(window, text='Red', command=lambda: change_background('red'))

exit_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
blue_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
red_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()
