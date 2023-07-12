from tkinter import *

window = Tk()
window.title('合并单元格测试')

label_1 = Label(window, text='标签1', relief='raised')
label_2 = Label(window, text='标签2', relief='raised')
label_3 = Label(window, text='标签3', relief='raised')
label_4 = Label(window, text='标签4', relief='raised')
label_5 = Label(window, text='标签5', relief='raised')
label_6 = Label(window, text='标签6', relief='raised')
label_7 = Label(window, text='标签7', relief='raised')
label_8 = Label(window, text='标签8', relief='raised')

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1, rowspan=2)
label_3.grid(row=0, column=2)
label_4.grid(row=0, column=3)
label_5.grid(row=1, column=0)
label_7.grid(row=1, column=2)
label_8.grid(row=1, column=3)

window.mainloop()
