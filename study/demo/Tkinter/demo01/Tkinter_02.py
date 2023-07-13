# 导入 tkinter 模块
from tkinter import *

# 定义一个全局计数器变量
counter = 0


# 定义一个函数用于运行计数器
def run_counter(digit):
    # 定义内部函数用于执行计数
    def counting():
        # 使用 global 关键字声明全局变量
        global counter
        # 计数器加1
        counter += 1
        # 更新标签的文本内容
        digit.config(text=str(counter))
        # 每隔一秒调用 counting 函数
        digit.after(1000, counting)

    # 调用 counting 函数开始计数
    counting()


# 创建根窗口
container = Tk()

# 设置窗口标题
container.title('内容自动加1')

# 创建标签，设置背景、前景颜色、高度、宽度和字体样式,
# cursor='heart' 鼠标经过悬浮时，显示心形鼠标
digit = Label(container, bg='yellow', fg='blue', height=3, width=10, font='Helvetica 20 bold', cursor='heart')

# 将标签添加到窗口中的合适位置
digit.pack()

# 输出所有可传的参数
for key in digit.keys():
    print('args:', key + '\n')

# 运行计数器函数，传入标签作为参数
run_counter(digit)


# 定义个按钮关闭对话框
Button(container, text="关闭计时", command=container.destroy).pack(padx=5)

# 进入 tkinter 的主循环，等待事件的发生
container.mainloop()
