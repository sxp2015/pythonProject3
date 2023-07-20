import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('树状结构视图案例')
window.geometry('600x400')

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

# 格式化栏位
tree.column('#0', width=100, anchor=CENTER)
tree.column('#1', width=150, anchor=CENTER)
tree.column('#2', width=150, anchor=CENTER)

tree.pack()
window.mainloop()
