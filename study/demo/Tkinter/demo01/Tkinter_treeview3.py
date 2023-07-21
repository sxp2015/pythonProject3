import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('树状结构视图案例3')
# window.geometry('600x400')
# 窗口缩放配置
# row1 会随窗口缩放1:1变化
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(3, weight=1)


# 删除选择项的方法
def remove_item():
    # 获得所选项目
    ids = tree.selection()
    for item_id in ids:
        tree.delete(item_id)


# 插入内容的方法
def insert_item():
    state = state_entry.get()
    city = city_entry.get()
    if len(state.strip()) == 0 or len(city.strip()) == 0:
        messagebox.showinfo(title='提示', message='输入不能为空')
        return
    # 插入内容
    tree.insert('', index=END, text=state, values=(city,))
    state_entry.delete(0, END)
    city_entry.delete(0, END)


# 鼠标双击弹出选择项的内容
def double_click(event):
    # 获得事件控件
    double_widget = event.widget
    # 获得项目ID
    item_id = double_widget.identify('item', event.x, event.y)
    # 获得州省
    state = double_widget.item(item_id, 'text')
    # 获得城市
    city = double_widget.item(item_id, 'values')[0]
    # 组合获得的值
    format_state_city = "州省：{0} | 城市：{1}".format(state, city)
    # 弹出消息框
    messagebox.showinfo(title='提示', message=format_state_city)


# 列排序方法
def treeview_sort_column(tv, col, reverse):
    """
        列排序方法treeview_sort_column用于对Treeview控件的列进行排序。

    函数接受三个参数：tv表示Treeview控件对象，col表示要排序的列名，reverse表示是否降序排序。

    首先，函数使用列表推导式将Treeview控件中的所有项目的列数据和项目ID组成的元组放入一个列表中。这里使用了tv.get_children('')来获取所有项目的ID。

    然后，通过调用列表的sort()方法对列表进行排序。传入的关键字参数是以要排序的列数据作为排序依据。

    根据reverse参数判断是否需要进行降序排序。如果reverse为True，则进行降序排序，否则进行升序排序。

    最后，根据排序后的列表重新设置项目的顺序。通过调用Treeview控件的move()方法将项目按照排序后的顺序移动到指定位置。

    最后，通过调用Treeview控件的heading()方法更新列标题的点击事件，使得点击列标题可以再次调用treeview_sort_column函数进行排序。

    这样，每次点击列标题时，都会触发一次排序操作，并更新Treeview控件中的项目顺序和列标题的点击事件处理方法，实现了对Treeview控件列的排序功能。
    :param tv:
    :param col:
    :param reverse:
    :return:
    """
    # tv.set() 方法用于获取一个项目在指定列上的值。第一个参数 k 是项目的ID，第二个参数 col 是要获取值的列名。
    # 将获取到的项目列数据和项目ID组成的元组 (tv.set(k, col), k) 添加到列表中。(值value,ID)
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    # 排序
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


stateCity = {"伊利诺": "芝加哥", "加州": "洛杉矶", "德州": "休斯敦", "华盛顿州": "西雅图", "江苏": "南京", "山东": "青岛", "广东": "广州", "福建": "厦门"}

# 建立Treeview
tree = Treeview(window, columns=('cities',), selectmode=EXTENDED)
# 绑定鼠标双击事件
tree.bind('<Double-1>', double_click)
# 栏标题(并且有排序方法)
tree.heading('#0', text='州/省', command=lambda: treeview_sort_column(tree, 'cities', False))
tree.heading('cities', text='城市')
# 格式化栏位
tree.column('#0', width=200, anchor='center')
tree.column('cities', width=200, anchor='center')

# 配置滚动条(和Treeview互相关联绑定)
yscrollbar = Scrollbar(window, command=tree.yview, orient=VERTICAL)
yscrollbar.grid(row=1, column=5, sticky=N + S, padx=2)
tree.configure(yscrollcommand=yscrollbar.set)

# 建立内容
for i in range(1, 4):
    for key in stateCity.keys():
        tree.insert('', index=END, text=key, values=stateCity[key])
    tree.grid(row=1, column=0, columnspan=5, padx=5, sticky=N + S + E + W)

# 删除按钮
remove_button = Button(window, text='删除', command=remove_item)
remove_button.grid(row=2, column=2, padx=5, pady=3, sticky=W)
# 州省标签和输入
state_lab = Label(window, text='州省:')
state_lab.grid(row=0, column=0, padx=5, pady=3, sticky=W)
state_entry = Entry(window)
state_entry.focus()
state_entry.grid(row=0, column=1, padx=5, pady=3, sticky=W)
# 城市标签和输入
city_lab = Label(window, text='城市:')
city_lab.grid(row=0, column=2, padx=5, pady=3, sticky=E)
city_entry = Entry(window)
city_entry.grid(row=0, column=3, padx=5, pady=3, sticky=E)
# 插入按钮
insert_button = Button(window, text='插入', command=insert_item)
insert_button.grid(row=0, column=4, padx=5, pady=3)

window.mainloop()
