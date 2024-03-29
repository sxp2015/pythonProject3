from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('列表项添加和删除操作')

window.geometry("480x320")

fruits = ["Banana", "watermelon", "pineapple", "Orange", "Grapes", "Mango"]

is_checked_var = BooleanVar()


def item_add():
    var_add = entry.get()
    if len(var_add.strip()) == 0:
        return
    lb.insert(END, var_add)
    entry.delete(0, END)


def item_deleted():
    selected_items = lb.curselection()
    if len(selected_items) == 0:
        return
    for index in reversed(selected_items):
        lb.delete(index)


def item_sort():
    if is_checked_var.get():
        # 从大到小排序 True
        reverse_bool = True
    else:
        # 从大到小排序 False
        reverse_bool = False
    # 获取list_box列表中的项目内容
    list_temp = list(lb.get(0, END))
    # 执行排序
    sorted_list = sorted(list_temp, reverse=reverse_bool)
    # 删除原来的listbox
    lb.delete(0, END)
    # 遍历排序好的列表
    for item in sorted_list:
        # 将排序好的item项目添加到listbox
        lb.insert(END, item)


def select_all():
    lb.select_set(0, END)


def deselect_all():
    lb.select_clear(0, END)


entry = Entry(window)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_add = Button(window, text="添加", width=10, command=item_add)
btn_add.grid(row=0, column=1, padx=5, sticky=W)

btn_delete = Button(window, text="删除", width=10, command=item_deleted)
btn_delete.grid(row=0, column=2, padx=5, pady=5, sticky=W)

lb = Listbox(window,selectmode=MULTIPLE)
lb.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=W + E)

scrollbar = Scrollbar(window)
scrollbar.grid(row=1, column=3, sticky=N + S)

lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

sort_type = Checkbutton(window, text="排序方式：按字母顺序(从大到小)", variable=is_checked_var)
sort_type.grid(row=2, column=0, padx=5, pady=5, sticky=W)

sort_button = Button(window, text="排序", width=10, command=item_sort)
sort_button.grid(row=2, column=1, padx=5, pady=5, sticky=W)

select_all_button = Button(window, text="全选", width=10, command=select_all)
select_all_button.grid(row=2, column=2, padx=5, pady=5, sticky=W)

deselect_all_button = Button(window, text="取消全选", width=10, command=deselect_all)
deselect_all_button.grid(row=2, column=3, padx=5, pady=5, sticky=W)

window.mainloop()
