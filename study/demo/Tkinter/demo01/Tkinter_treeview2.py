import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title('树状结构视图案例2')
window.geometry('600x400')

asia = {"中国": "北京", "日本": "东京", "泰国": "曼谷", "韩国": "首尔"}
europe = {"英国": "伦敦", "法国": "巴黎", "德国": "柏林", "挪威": "奥斯陆"}

# 建立treeview
tree = Treeview(window, columns=('capital', ))
# 建立图标栏 和标题
tree.heading('#0', text='国家') # 图标栏
tree.heading('capital', text='首都')
# 建立ID
id_asia = tree.insert('', index=END, text='亚洲')
id_europe = tree.insert('', index=END, text='欧洲')

# 建立id_asia 和 id_europe的底层内容
for key in asia.keys():
    tree.insert(id_asia, index=END, text=key, values=asia[key])
for key in europe.keys():
    tree.insert(id_europe, index=END, text=key, values=europe[key])

tree.pack()

window.mainloop()
