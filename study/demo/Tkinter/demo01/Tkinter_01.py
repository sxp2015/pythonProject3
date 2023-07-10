import tkinter
from tkinter import *
from PIL import Image, ImageTk

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

# 创建一个Label标签 bg 背景色  fg 前景色  anchor九宫格位置 ,anchor='nw' (默认上下左右居中，参数
# nw (North West) 西北方向
# ne (North East) 东北方向
# w (West) 正西方向
# sw (South West) 西南方向
# center  居中方向
# se) (South East) 东南方向
# anchor 的参数设置也可以使用内建大写常数，例如，nw 使用 NW、n使用N  width=30,height=5, anchor=S
# wraplength = 40 文字长度达到40个像素后换行
# compound='left' 图像bitmap与文字text的位置关系
# relief 轮廓边框凹凸效果:flat（无效果）,groove（平面）,raised(凸出来),ridge,solid,sunken（凹进去）
# padx/pady文字与控件的横纵内边距
# PhotoImage 可以直接打开PNG,GIF图片
png_image = PhotoImage(file='./images/north_gate.png')
# 如果是JPG图像格式，需要借助Pillow库的Image和ImageTk
jpg_image = Image.open('./images/north_gate.jpg')
jpg_image_tk = ImageTk.PhotoImage(jpg_image)
# bitmap 参数和 image 参数不能共存
label = Label(container, text='郴州建活塑胶科技有限公司', bg='#ffffff', fg='#087360', bitmap='warning', font='Helvetic 14 bold',
              compound='left', relief='sunken', padx=10, pady=5, image=jpg_image_tk)

#  这样写也可以
#  Label(container, text='郴州建活塑胶科技有限公司', bg='#ffffff', fg='#087360',anchor='nw').pack()

# 包装窗口的Widget 控件和定位窗口的对象
label.pack()

# 输出版本号
print('version', tkinter.TkVersion)

# mainloop()方法，放在最后一行，可以让程序继续执行，同时进入等待与处理窗口事件，
# 单击窗口右上方的“关闭”按钮，此程序才会结束。
container.mainloop()
