from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('列表项操作')

window.geometry("480x320")

fruits = ["Banana", "watermelon", "pineapple", "Orange", "Grapes", "Mango"]

balls = ['football', 'basketball', 'tennis ball', 'volleyball']

# selectmode=MULTIPLE 多选模式  selectmode=EXTENDED 框选模式
lb = Listbox(window, selectmode=EXTENDED)

for fruit in fruits:
    # END 索引，从后面插入
    lb.insert(END, fruit)

for ball in balls:
    # ACTIVE 索引， 从前面插入
    lb.insert(ACTIVE, ball)

lb.pack(padx=5, pady=10)

# 输出列表数量长度
print("size:", lb.size())

# 选择指定项 前4个（0-3的索引）
# lb.delete(0,3) 删除前四个
# lb.get(1) 获取指定索引的值
# lb.curselection() 传回当前选中的索引，用回调函数，先选中，触发按钮事件，调用函数，
# 在函数中，调用lb.curselection，返回列表，遍历列表后输出
# 返回指定项是否被选中，lb.selection_includes(3) 布尔值 ，True 或 False, 在按钮中触发回调函数检查
lb.selection_set(0, 3)

window.mainloop()
