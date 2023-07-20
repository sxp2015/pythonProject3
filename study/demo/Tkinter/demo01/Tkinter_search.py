import time  # 导入时间模块
from tkinter import *  # 导入 tkinter 库的所有模块
from tkinter import messagebox  # 导入 tkinter 的 messagebox 模块
from tkinter.font import *  # 导入 tkinter 的字体模块
from tkinter.ttk import *  # 导入 tkinter 的 ttk 模块

window = Tk()  # 创建一个窗口实例
window.title('搜索文字案例')  # 设置窗口标题
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


def search():
    # 删除卷标，不删除卷标定义
    text.tag_remove("found", "1.0", END)
    # 设置搜索起始位置
    start = "1.0"
    # 获取输入框中的搜索关键字
    key = entry.get()
    # 如果没有输入
    if not len(key.strip()):
        return
    while True:
        # 执行搜索
        pos = text.search(key, start, END)
        if not pos:
            break
        # 设置卷标
        text.tag_add("found", pos, "%s+%dc" % (pos, len(key)))
        # 更新搜索起始位置
        start = "%s+%dc" % (pos, len(key))


"""
text.tag_add("found", pos, "%s+%dc" % (pos, len(key)))：tag_add() 是 Text 类的一个方法，用于给指定的区域添加标签。
它接受三个参数：标签名称、起始位置和结束位置。

"found"：这是要添加的标签名称，即我们自定义的 "found" 标签。

pos：这是搜索到的匹配项的起始位置，即关键字在文本框中的出现位置。

"%s+%dc" % (pos, len(key))：这是设置标签的结束位置。%s 是格式化字符串中的占位符，表示将会被 pos 的值替代。+%dc 的形式表示从起始位置
 pos 处向后偏移 len(key) 个字符的位置作为结束位置。
 
"""

# 建立Text undo=True 是否能恢复或撤消
text = Text(window, undo=True, font="console 14")
text.grid(row=1, column=0, padx=5, columnspan=2, pady=5, sticky=W + E + S + N)
text.insert(END, story)
text.tag_config("found", background="yellow", font="Arial 20 bold")

# 搜索输入框
entry = Entry(window)
entry.grid(row=0, column=0, padx=5, sticky=W + E)
entry.focus()

# 查找按钮
search_btn = Button(window, text='查找', command=search)
search_btn.grid(row=0, column=1, padx=5, sticky=W + E)

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

window.mainloop()
