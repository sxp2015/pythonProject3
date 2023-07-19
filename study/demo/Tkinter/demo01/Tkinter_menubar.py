import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('菜单栏案例')
window.geometry('600x400')


# 打开文件
def open_file():
    messagebox.showinfo('提示', '打开文件')


# 询问是否真的需要退出
def confirm_exit():
    if messagebox.askokcancel('退出', '确定要退出吗?'):
        window.quit()
        window.destroy()


# 保存文件
def save_file():
    if messagebox.showinfo('提示', '保存文件！'):
        pass


# 另存为文件
def save_as_file():
    if messagebox.showinfo('提示', '文件另存为成功！'):
        pass


# 查找方法
def find_content():
    messagebox.showinfo('提示', '查找内容')


# 查找文档内容
def find_content_by_doc():
    messagebox.showinfo('提示', '查找文档内的所有内容')


# 查找目录内容
def find_content_by_dir():
    messagebox.showinfo('提示', '指定目录下的内所有内容')


# 替换内容
def replace_content():
    messagebox.showinfo('提示', '替换内容')


# 复制内容
def copy_content():
    messagebox.showinfo('提示', f'鼠标右键，复制内容{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')


# 粘贴内容
def paste_content():
    messagebox.showinfo('提示', f'鼠标右键 粘贴内容{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')


# 顶层菜单
menubar = Menu(window)

# 创建文件菜单
file_menu = Menu(menubar, tearoff=0)  # tearoff=1 会产生虚拟分隔线
# 帮助菜单
help_menu = Menu(menubar, tearoff=0)
# 编辑菜单
edit_menu = Menu(menubar, tearoff=False)
# 在编辑菜单中，创建一个【查找】子菜单
search_menu = Menu(edit_menu, tearoff=0)
# 顶层菜单关联下级的文件级联菜单
menubar.add_cascade(label='文件(F)', menu=file_menu, underline=3)
menubar.add_cascade(label='编辑(E)', menu=edit_menu, underline=3)
menubar.add_cascade(label='帮助(H)', menu=help_menu, underline=3)
# 级联菜单添加命令菜单
file_menu.add_command(label='打开', command=open_file, underline=3, accelerator='Ctrl+O')
file_menu.add_command(label='保存', command=save_file, accelerator='Ctrl+S')
file_menu.add_command(label='另存为', command=save_as_file, accelerator='Ctrl+Shift+S')

# 添加子菜单
edit_menu.add_command(label='查找', command=find_content, accelerator='Ctrl+F')
edit_menu.add_command(label='替换', command=replace_content, accelerator='Ctrl+R')

# 这里要指定上一级菜单是谁 menu=search_menu，而上一级菜单，是根据顶级菜单，再次构造实例出来的
# 添加级联菜单【查找】
edit_menu.add_cascade(label='查找方式', menu=search_menu)
search_menu.add_command(label='全文查找', command=find_content_by_doc)
search_menu.add_command(label='目录查找', command=find_content_by_dir)

help_menu.add_command(label='查看帮助')
help_menu.add_command(label='关于软件')

# 鼠标右键菜单
popup_menu = Menu(window, tearoff=0)
popup_menu.add_command(label='查看帮助')
popup_menu.add_command(label='复制', command=copy_content)
popup_menu.add_command(label='粘贴', command=paste_content)

# 设置联菜单的分隔线
file_menu.add_separator()
# 级联菜单添加命令菜单
file_menu.add_command(label='退出', command=confirm_exit)

# 将顶层菜单配置到窗口
window.config(menu=menubar)
# 配置绑定快捷键事件
window.bind('<Control-o>', lambda event: open_file())
window.bind('<Control-s>', lambda event: save_file())
window.bind('<Control-Shift-s>', lambda event: save_as_file())
window.bind('<Button-3>', lambda event: popup_menu.tk_popup(event.x_root, event.y_root))
# 绑定鼠标右键弹出菜单到窗口


# 运行程序
window.mainloop()
