import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('Canvas绘画')
# window.geometry('600x400')
canvas_frame = Frame(window)
canvas_frame.pack(fill=BOTH, expand=True)
canvas_frame.bind('<<Configure>>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

canvas = Canvas(canvas_frame, width=1920, height=1080, background='lightblue')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

canvas.create_line(10, 30, 500, 30)
canvas.create_line(20, 40, 500, 40, width=5)
canvas.create_line(30, 50, 500, 50, width=15, fill='lightyellow')
canvas.create_line(40, 80, 500, 80, dash=(15, 15, 5, 5))

canvas.create_line(80, 120, 500, 120, width=20, joinstyle=ROUND)

canvas.create_line(80, 170, 500, 170, width=20, stipple="gray25")
canvas.create_line(80, 220, 500, 220, width=20, stipple="gray50")
canvas.create_line(80, 270, 500, 270, width=20, stipple="questhead")
canvas.create_line(80, 320, 500, 320, width=20, stipple="info")

canvas.create_rectangle(80, 370, 500, 470, outline='red', width=10)
canvas.create_rectangle(580, 420, 1000, 570, fill='yellow', outline='black', width=10)
# 绘制弧形 style 参数分别是 ARC(圆形)、CHORD（半圆）、PIESLICE（扇形）
canvas.create_arc(580, 380, 1080, 80, start=0, extent=359, style=ARC, fill='yellow', outline='black', width=10)

# 绘制圆或椭圆
canvas.create_oval(750, 200, 1000, 300, fill='aqua', outline='black', width=10)

# 绘制多边形

canvas.create_polygon(50, 620, 450, 620, 230, 700, fill='green', outline='black', width=5)
canvas.create_polygon(70, 720, 550, 720, 280, 750, 190, 820, fill='orange', outline='black', width=5)

# 绘制文字
canvas.create_text(770, 20, text='hello world', fill='black', font=('Arial', 20))

# 给画布添加滚动条
yscrollbar = Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=yscrollbar.set)

window.mainloop()
