from tkinter import *

window = Tk()
window.title('简易计算器')

equ = StringVar()
equ.set('0')


# 执行计算显示结果
def calculate():
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))


# 更新显示区的计算公式
def show(button_string):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + button_string)


# 删除前一个字符
def backspace():
    equ.set(str(equ.get()[:-1]))


# 清除显示区，放置0
def clear():
    equ.set("0")


# 设计显示区
label = Label(window, width=25, height=2, relief="raised", anchor=SE, textvariable=equ)
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W + E + N + S)

# 清除显示区的按钮
clearButton = Button(window, text="C", fg="blue", width=5, command=clear)
clearButton.grid(row=1, column=0)
# row1的其他按钮
Button(window, text="DEL", width=5, command=backspace).grid(row=1, column=1)
Button(window, text="%", width=5, command=lambda: show("%")).grid(row=1, column=2)
Button(window, text="/", width=5, command=lambda: show("/")).grid(row=1, column=3)
# 以下是row2的其他按钮
Button(window, text="7", width=5, command=lambda: show("7")).grid(row=2, column=0)
Button(window, text="8", width=5, command=lambda: show("8")).grid(row=2, column=1)
Button(window, text="9", width=5, command=lambda: show("9")).grid(row=2, column=2)
Button(window, text="*", width=5, command=lambda: show("*")).grid(row=2, column=3)
# 以下是row3的其他按钮
Button(window, text="4", width=5, command=lambda: show("4")).grid(row=3, column=0)
Button(window, text="5", width=5, command=lambda: show("5")).grid(row=3, column=1)
Button(window, text="6", width=5, command=lambda: show("6")).grid(row=3, column=2)
Button(window, text="-", width=5, command=lambda: show("-")).grid(row=3, column=3)
# 以下是row4的其他按钮
Button(window, text="1", width=5, command=lambda: show("1")).grid(row=4, column=0)
Button(window, text="2", width=5, command=lambda: show("2")).grid(row=4, column=1)
Button(window, text="3", width=5, command=lambda: show("3")).grid(row=4, column=2)
Button(window, text="+", width=5, command=lambda: show("+")).grid(row=4, column=3)
# 以下是其他Row5的按钮
Button(window, text="0", width=12, command=lambda: show("0")).grid(row=5, column=0, columnspan=2)
Button(window, text=".", width=5, command=lambda: show(".")).grid(row=5, column=2)
Button(window, text="=", width=5, bg="yellow", command=lambda: calculate()).grid(row=5, column=3)

window.mainloop()
