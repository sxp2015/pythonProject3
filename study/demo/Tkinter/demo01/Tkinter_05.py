# 导入 tkinter 模块
from tkinter import *
from tkinter.ttk import Separator

window = Tk()
window.title('demo-05')
window.geometry("300x200")

Mississippi_Label = Label(window, text="Mississippi", font="Times 24 bold", fg="white", bg="red")
Mississippi_Label.pack(fill=X)

Kentucky_Label = Label(window, text="Kentucky", font="Times 24 bold italic", fg="white", bg="green")
Kentucky_Label.pack(fill=BOTH, expand=True)

Purdue_Label = Label(window, text="Purdue", font="Times 24 bold", fg="white", bg="blue")
Purdue_Label.pack(fill=X)

# orient 分隔符朝向 HORIZONTAL水平
sep_1 = Separator(window, orient=HORIZONTAL)
sep_1.pack(fill=X, padx=5)

Label(window,text='=========================').pack(fill=X)

Mississippi_Label2 = Label(window, text="Mississippi", font="Times 24 bold", fg="white", bg="red")
Mississippi_Label2.pack(side=LEFT, fill=Y)

Kentucky_Label2 = Label(window, text="Kentucky", font="Times 24 bold italic", fg="white", bg="green")
Kentucky_Label2.pack(side=LEFT, fill=BOTH, expand=True)

Purdue_Label2 = Label(window, text="Purdue", font="Times 24 bold", fg="white", bg="blue")
Purdue_Label2.pack(side=LEFT, fill=Y)

# slaves()传回所有 Widget 控件对象
print('pack方法',window.pack_slaves())
# info()传回 pack 选项的对应值
# 隐藏 Widget 控件，可以用 pack(option..··) 复原显示
# 传回此点是否在单元格，如果是传回坐标，如果不是传回(-1.-1)
# 传回 Widget 控件大小
# 参数是 True 表示父窗口大小由子控件决定，默认为 True

window.mainloop()
