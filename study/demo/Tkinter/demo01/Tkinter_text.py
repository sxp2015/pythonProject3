import time  # 导入时间模块
from tkinter import *  # 导入 tkinter 库的所有模块
from tkinter import messagebox  # 导入 tkinter 的 messagebox 模块

window = Tk()  # 创建一个窗口实例
window.title('文字区域案例')  # 设置窗口标题
window.geometry('400x300')  # 设置窗口大小

word_01 = """
1.Download Microsoft Translator app on iOS or Android and start a conversation.
2.Share the conversation code with other participants, who can join using the Translator app or website.
3.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
4.Share the conversation code with other participants, who can join using the Translator app or website.
5.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
6.Speak or type in your language to communicate with other participants in the conversation. Other participants will see your messages in their own language.
"""  # 定义一个长文本字符串

# text_01 = Text(window, width=30, height=5)  # 创建一个文本框实例，设置宽度和高度
# text_01.insert(END, "Hello Tkinter")  # 在文本框中插入文本
# text_01.insert(INSERT, '\n鼠标右键，复制内容' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 在光标位置插入文本和当前时间
# text_01.insert(INSERT, "\n Take me to your heart.")  # 在光标位置插入文本
# text_01.pack(side=TOP, anchor=NW)  # 文本框的布局

# *********************************************************************************#

# wrap="none" 不换行，X轴才会出现滚动条
text_02 = Text(window, width=80, height=5, wrap="none", bg="lightyellow")  # 创建一个文本框实例，设置宽度、高度和换行方式

yscrollbar = Scrollbar(window, command=text_02.yview)  # 创建一个垂直滚动条实例，绑定文本框的 y 轴滚动事件
xscrollbar = Scrollbar(window, command=text_02.xview, orient=HORIZONTAL)  # 创建一个水平滚动条实例，绑定文本框的 x 轴滚动事件

yscrollbar.pack(side=RIGHT, fill=Y)  # 将垂直滚动条放置在窗口的右侧
xscrollbar.pack(side=BOTTOM, fill=X)  # 将水平滚动条放置在窗口的底部

text_02.config(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  # 设置文本框的滚动命令

text_02.insert(END, word_01)  # 在文本框中插入长文本字符串
text_02.pack()  # 文本框的布局

window.mainloop()  # 运行窗口的主循环
