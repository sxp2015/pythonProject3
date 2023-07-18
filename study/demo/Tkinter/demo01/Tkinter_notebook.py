from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title('多选项卡案例')

notebook = Notebook(window)

style = Style()
style.configure('Custom.TLabelframe', background='lightpink')
style.configure('TLabelframe', background='lightyellow')
style.configure('TFrame', background='lightgreen')

frame1 = Frame(width=120, height=150, style="TFrame")
lab1 = Label(frame1, text="第一个控件")
lab1.pack(fill=BOTH, expand=True, padx=10, pady=10)

frame2 = Frame(width=120, style='Custom.TLabelframe')
lab2 = Label(frame2, text="第二个控件")
lab2.pack(fill=BOTH, expand=True, padx=10, pady=10)

frame3 = Frame(width=120, style="TLabelframe")
lab3 = Label(frame3, text="第三件控件")
lab3.pack(fill=BOTH, expand=True, padx=10, pady=10)

notebook.add(frame1, text="选项卡1")
notebook.add(frame2, text="选项卡2")
notebook.add(frame3, text="选项卡3")

notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

window.mainloop()
