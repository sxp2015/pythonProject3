from tkinter import *

window = Tk()

window.title('Button按钮嵌入图片')

window.geometry("200x100")

message_label = Label(window)


def show_message():
    message_label.config(text=" I love Python and Tkinter", bg="red", fg="white",
                         font="Helvetic 26 bold")


print_logo_img = PhotoImage(file="images/print.png")
#  compound=LEFT , 图标的图片文件在左边（LEFT , RIGHT, TOP, BOTTOM）
print_logo_btn = Button(window, image=print_logo_img, command=show_message, text="打印消息", compound=LEFT, cursor="hand2")

message_label.pack()
print_logo_btn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

window.mainloop()
