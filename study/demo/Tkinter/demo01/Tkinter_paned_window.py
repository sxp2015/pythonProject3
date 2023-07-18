from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title('控件面板案例')

# window.geometry("480x320")

pw = PanedWindow(window, orient=HORIZONTAL)


style = Style()
style.configure('Custom.TLabelframe', background='lightpink')
style.configure('TLabelframe', background='lightyellow')
style.configure('TFrame', background='lightgreen')

lab1 = LabelFrame(pw, text="第一个控件", width=120, height=150, style="TFrame")
pw.add(lab1, weight=1)
lab2 = LabelFrame(pw, text="第二个控件", width=120, style='Custom.TLabelframe')
pw.add(lab2, weight=1)
lab3 = LabelFrame(pw, text="第三个控件", width=120, style="TLabelframe")
pw.add(lab3, weight=1)

##
entry = Entry(pw, background='yellow')
pw.add(entry)

scale = Scale(pw, orient=HORIZONTAL)
pw.add(scale)


pw.pack(fill=BOTH, expand=True, padx=10, pady=10)


window.mainloop()
