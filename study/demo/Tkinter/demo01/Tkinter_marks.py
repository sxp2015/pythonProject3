import time  # 导入时间模块
from tkinter import *  # 导入 tkinter 库的所有模块
from tkinter import messagebox  # 导入 tkinter 的 messagebox 模块
from tkinter.font import *
from tkinter.ttk import *

window = Tk()  # 创建一个窗口实例
window.title('书签和标签案例')  # 设置窗口标题
window.geometry('400x300')  # 设置窗口大小

text = Text(window)  # 创建一个文本实例

for i in range(1, 20):
    text.insert(END, str(i) + 'I like Python Tkinter\n')

# 设置书签
text.mark_set("mark1", "4.0")
text.mark_set("mark2", "9.0")

# 得到书签的值
mark = text.get("mark1", "mark2")

# 定义标签给书签添加颜色
text.tag_add("tag1", "mark1", "mark2")
text.tag_configure("tag1", foreground="red", background="yellow")

# 定义Label显示书签的值
mark_label = Label(window, text=f'mark = {mark}', background="yellow")
mark_label.pack(side=BOTTOM, fill=X)

text.pack(fill=X, expand=1)

window.mainloop()
