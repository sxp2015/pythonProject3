import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('树状结构视图案例')
window.geometry('600x400')

# 定义一个文本变量，用于在Label中显示当前选中的是哪一项
checked_item = StringVar()


# 定义一个方法，用于获得当前选中控件中的内容
def tree_selected(event):
    # 获得当前选中的控件对象
    widget_object = event.widget
    # 获得选中项
    item_selected = widget_object.selection()[0]
    # 获得图标栏内容
    col_1 = widget_object.item(item_selected, 'text')
    # 获得索引栏为0的位置的内容
    col_2 = widget_object.item(item_selected, 'values')[0]
    # 组合内容
    checked_item.set(col_1 + ' ：' + col_2)


# show='headings' 不显示图标栏 也就是 text="湖南省"
tree = Treeview(window, columns=('cities', 'peoples'))

stateCity = {"伊利诺": "芝加哥", "加州": "洛杉矶", "德州": "休斯敦", "华盛顿州": "西雅图", "江苏": "南京", "山东": "青岛", "广东": "广州", "福建": "厦门"}

# 建立栏标题
tree.heading('#0', text='省份')
tree.heading('#1', text='市区')
tree.heading('#2', text='人口')

# 建立内容
# 当所建的栏是最顶层时，可以用空字符串处理
# index=END 代表将资料插入 Treeview 末端
# 第三个参数 text 是设置图标栏的内容。第 4 个参数的 values 是设置City 栏的内容。
tree.insert('', index=END, text='湖南省', values=('长沙', 1000000))
tree.insert('', index=END, text='湖北省', values=('武汉', 2120500))
tree.insert('', index=END, text='广东省', values=('广州', 3125000))

# 设置标签 双行彩色
tree.tag_configure('even_color', background='yellow')
# 定义行号
row_count = 1
for key in stateCity.keys():
    if row_count % 2 == 1:
        tree.insert('', index=row_count, text=key, values=stateCity[key])
    else:
        tree.insert('', index=row_count, text=key, values=stateCity[key], tags=('even_color',))
    row_count += 1

# 格式化栏位,设置宽度和对齐方式
tree.column('#0', width=100, anchor=CENTER)
tree.column('#1', width=150, anchor=CENTER)
tree.column('#2', width=150, anchor=CENTER)
# 给树状结构图绑定和添加一个选择事件
tree.bind('<<TreeviewSelect>>', tree_selected)
tree.pack()

# 建立状态栏
label = Label(window, textvariable=checked_item, relief=GROOVE)
label.pack(fill=X, side=BOTTOM)

window.mainloop()
