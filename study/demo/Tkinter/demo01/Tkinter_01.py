import tkinter
from tkinter import *

# 创建根窗口
container = tkinter.Tk()

# 设置标题
container.title('郴州建活塑胶科技有限公司')
# 设置指定尺寸
# container.geometry("800x600")

# 全屏显示
# container.attributes('-fullscreen', True)

# 程序框架尺寸
width = 800
height = 500

# 获取屏幕的宽度和高度
screen_width = container.winfo_screenwidth()
screen_height = container.winfo_screenheight()

# 左上角X轴居中
align_x = int(screen_width / 2 - width / 2)
# 左上角Y轴居中
align_y = int(screen_height / 2 - height / 2)

# 设置窗口大小和位置
# width x height 已说明是窗口的宽和高，width 与 height  用x分隔。
# “+x”表示x 是窗口左边距离屏幕左边的距离，
# 如果是“-x”则表示x是窗口右边距离屏幕右边的距离。“+y”表示y
# 是窗口上边距离屏幕上边的距离，如果是“-y”则表示y 是窗口下边距离屏幕下边的距离。
container.geometry(f"{width}x{height}+{align_x}+{align_y}")

# 设置背景颜色
container.config(bg='#087360')

# 设置LOGO图标
container.iconbitmap("logo/logo.ico")


# 创建一个Label标签
label = Label(container, text='郴州建活塑胶科技有限公司', bg='#ffffff', fg='#087360',anchor='nw')

label.pack()

# 输出版本号
print('version', tkinter.TkVersion)

# mainloop()方法，放在最后一行，可以让程序继续执行，同时进入等待与处理窗口事件，
# 单击窗口右上方的“关闭”按钮，此程序才会结束。
container.mainloop()
