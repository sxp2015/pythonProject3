import time  # 导入时间模块
from tkinter import *  # 导入 tkinter 库的所有模块
from tkinter import messagebox  # 导入 tkinter 的 messagebox 模块
from tkinter.font import *
from tkinter.ttk import *

window = Tk()  # 创建一个窗口实例
window.title('选择字体类型和大小的案例')  # 设置窗口标题
window.geometry('400x300')  # 设置窗口大小


# 改变字体的方法
def change_font(event):
    f = Font(family=var_font.get())
    text_01.config(font=f)


def change_weight(event):
    f = Font(weight=var_weight.get())
    text_01.config(font=f)


def size_selected(event):
    f = Font(size=var_font_size.get())
    text_01.config(font=f)
    # 以下方式，可以选择指定文字后设置字体大小
    # text_01.tag_config(SEL, font=f)


def selected_text():
    try:
        sel_text = text_01.get(SEL_FIRST, SEL_LAST)  # 选择文本
        # 显示选择的文本
        text_row = str(text_01.index(SEL_FIRST)).split('.')[0]
        text_col = str(text_01.index(SEL_LAST)).split('.')[-1]
        messagebox.showinfo("提示", f'选择的文本：{sel_text},第{text_row}行，最后一个字的索引：{text_col}')
    except TclError:
        messagebox.showinfo('提示', '没有选中任何文本')


# 建立工具栏
toolbar = Frame(window, relief=RAISED, borderwidth=1)  # 创建一个工具栏实例，设置宽度和高度
toolbar.pack(side=TOP, fill=X)  # 工具栏的布局

# 建立字体选项
var_font = StringVar()  # 定义一个字体变量
font_family = ('宋体', 'Arial', '黑体', 'Times', 'Courier', '楷体', 'Console')  # 定义一个字体列表
var_font.set(font_family[0])  # 设置字体变量

# 建立字体粗细列表
var_weight = StringVar()
weight_list = ("normal", "bold")  # 定义一个字体粗细列表
var_weight.set(weight_list[0])  # 设置字体粗细变量

# 创建一个字体选项菜单
option_menu_family = OptionMenu(toolbar, var_font, *font_family, command=change_font)  # 创建一个选项菜单实例
option_menu_family.pack(side=LEFT, padx=3)  # 选项菜单的布局

# 建立粗细选项菜单
option_menu_weight = OptionMenu(toolbar, var_weight, *weight_list, command=change_weight)
option_menu_weight.pack(side=LEFT, padx=3)

# 字体大小列表
var_font_size = IntVar()
size = Combobox(toolbar, textvariable=var_font_size)
size_family = [x for x in range(8, 40, 2)]  # 定义一个字体大小列表
size["values"] = size_family  # 设置字体大小变量
size.current(0)
size.bind("<<ComboboxSelected>>", size_selected)
size.pack(side=LEFT, padx=3)

# 输出选择文字的索引
btn_selected_text = Button(toolbar, text='显示选择文字的索引', command=selected_text)
btn_selected_text.pack(side=LEFT, padx=3)

# 显示的文字
word_01 = """1.Download Microsoft Translator app on iOS or Android and start a conversation.
2.Share the conversation code with other participants, who can join using the Translator app or website.
3.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
4.Share the conversation code with other participants, who can join using the Translator app or website.
5.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
6.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
"""  # 定义一个长文本字符串
text_01 = Text(window, width=30, height=5, wrap="none")  # 创建一个文本框实例，设置宽度和高度
text_01.insert(INSERT, word_01)  # 在文本框中插入文本
# 插入文字同时设置Tab,同时设置样式
text_01.insert(END, "这是一段最后插入的文本，设置为标签Last_Tag,可以居中和设置下划线，等相关样式", "Last_Tag")
text_01.tag_config('Last_Tag', foreground='red', underline=True, background='yellow', justify=CENTER)

text_01.pack(fill=BOTH, expand=True, padx=2, pady=2, side=RIGHT)  # 文本框的布局
text_01.focus_get()

window.mainloop()
