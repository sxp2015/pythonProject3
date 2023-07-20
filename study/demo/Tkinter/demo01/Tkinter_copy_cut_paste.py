import time  # 导入时间模块
from tkinter import *  # 导入 tkinter 库的所有模块
from tkinter import messagebox  # 导入 tkinter 的 messagebox 模块
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.font import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *

from PIL import Image,ImageTk

window = Tk()  # 创建一个窗口实例
window.title('复制剪切粘贴的案例')  # 设置窗口标题
window.geometry('400x300')  # 设置窗口大小

story = """Once upon a time, in a quaint little village nestled among rolling hills, there lived a young girl named 
Lily. She had a sparkle in her eyes and a heart filled with curiosity. Lily loved exploring the woods near her home, 
where she would spend hours discovering hidden treasures and observing nature. One sunny morning, while venturing 
deeper into the forest than ever before, Lily stumbled upon a mysterious old book. Its weathered pages were filled 
with enchanting tales and captivating illustrations. Filled with excitement, Lily decided to take the book home and 
uncover its secrets. As she delved into the stories, Lily found herself whisked away on incredible adventures. She 
traveled to faraway lands, met mythical creatures, and befriended extraordinary characters. Each page turned into a 
gateway to a world brimming with magic and wonder. 
Lily's imagination soared as she read under the soft glow of moonlight, completely captivated by the tales. The book 
became her cherished companion, accompanying her on countless imaginary journeys. Through the stories, Lily learned 
valuable lessons about bravery, friendship, and the power of dreams. Years passed, and Lily grew older, but her love 
for storytelling never waned. Inspired by the magical book, she became a renowned writer, creating her own stories 
that touched the hearts of readers around the world. Lily's stories carried the same sense of wonder and enchantment 
that she had discovered in the forest that fateful day. And so, the little girl who found an old book in the woods 
transformed into a beloved storyteller, spreading the joy of imagination to all who read her words. Her stories 
continue to inspire generations, reminding us all of the beauty that lies within our own hearts and the limitless 
possibilities that exist in the world around us. """

# 建立Text undo=True 是否能恢复或撤消
text = Text(window, undo=True)
text.pack(fill=X, padx=5, pady=5, side=TOP)
text.insert(END, story)

# 带滚动条的文本控件
scroll_text = ScrolledText(window, undo=True)
scroll_text.pack(fill=X, padx=5, pady=5, side=BOTTOM)
scroll_text.insert(END, story)


# 复制文字的方法
def copy_text():
    # try:
    #     # 复制前，先清除剪切板
    #     text.clipboard_clear()
    #     copied_text = text.get(SEL_FIRST, SEL_LAST)
    #     text.clipboard_append(copied_text)
    # except TclError:
    #     messagebox.showinfo('提示', '没有选取文字')
    # 虚拟方法 效果相同
    text.event_generate('<<Copy>>')


# 粘贴文字的方法
def paste_text():
    # try:
    #     # 读取剪切板的内容
    #     copied_text = text.selection_get(selection='CLIPBOARD')
    #     # 插入剪切板的内容
    #     text.insert(INSERT, copied_text)
    # except TclError:
    #     messagebox.showinfo('提示', '剪切板无数据')

    # 虚拟方法 效果相同
    text.event_generate('<<Paste>>')


# 剪切文字方法
def cut_text():
    # # 复制选取文字
    # copy_text()
    # # 删除选取的文字
    # text.delete(SEL_FIRST, SEL_LAST)

    # 虚拟方法 效果相同
    text.event_generate('<<Cut>>')


# 弹出窗口鼠标右键菜单的方法
def show_popup(event):
    popup_menu.post(event.x_root, event.y_root)


# 撤消修改的方法
def text_undo_method():
    text.edit_undo()


# 重复执行的方法
def text_redo_method():
    text.edit_redo()


# 保存文件
def save_file():
    text_content = text.get(1.0, END)
    file_name = "story.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text_content)
        window.title(file_name)


# 另存为文件
def save_as_file():
    text_content = text.get(1.0, END)
    file_name = asksaveasfilename(defaultextension='.txt')
    if not file_name:
        return
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text_content)
        window.title(file_name)


def new_file():
    text.delete(1.0, END)
    window.title('新建文件')


def open_file():
    file_name = askopenfilename()
    if not file_name:
        return
    with open(file_name, 'r', encoding='utf-8') as f:
        # 先删除Text控件中的内容
        text.delete(1.0, END)
        # 再插入内容
        text.insert(1.0, f.read())
        window.title(file_name)


# 定义总菜单栏
menubar = Menu(window)
# 定义弹出菜单
popup_menu = Menu(menubar, tearoff=0)
# 定义文件菜单
file_menu = Menu(menubar, tearoff=0)

# 关联菜单
menubar.add_cascade(label='文件(F)', menu=file_menu)
menubar.add_cascade(label='编辑(E)', menu=popup_menu)

# 编辑菜单的功能
popup_menu.add_command(label='复制', command=copy_text)
popup_menu.add_command(label='粘贴', command=paste_text)
popup_menu.add_command(label='剪切', command=cut_text)
popup_menu.add_command(label='撤消', command=text_undo_method)
popup_menu.add_command(label='重复一次', command=text_redo_method)

# 文件菜单的功能
file_menu.add_command(label='新建', command=new_file)
file_menu.add_command(label='打开文件', command=open_file)
file_menu.add_command(label='保存', command=save_file)
file_menu.add_command(label='另保存', command=save_as_file)
file_menu.add_command(label='退出', command=window.destroy)

img = Image.open('logo/logo-100x100.png')
img_tk = ImageTk.PhotoImage(img)
# 添加图像
text.image_create(END, image=img_tk)

window.bind("<Button-3>", show_popup)
window.config(menu=menubar)

window.mainloop()
