from tkinter import *

window = Tk()
window.title('sticky参数测试')

label_user_name = Label(window, text='用户名：', relief='raised')
label_user_name_input = Label(window, bg='yellow', width=20)
label_user_password = Label(window, text='用户密码：', relief='raised')
label_user_password_input = Label(window, bg='aqua', width=20)

# sticky 参数(对齐方式)的可能值 N/S/W/E 也可以组合使用。
# sticky=N+S:可以拉长高度让控件在顶端和底端对齐。
# sticky=W+E:可以拉长宽度让控件在左边和右边对齐。
# sticky=N+S+E:可以拉长高度让控件在顶端和底端对齐，同时切齐右边。
# sticky=N+S+W:可以拉长高度让控件在顶端和底端对齐，同时切齐左边
# sticky=N+S+W+E:可以拉长高度让控件在顶端和底端对齐，同时切齐左右边。

label_user_name.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)
label_user_name_input.grid(row=0, column=1, padx=5, pady=5)
label_user_password.grid(row=1, column=0, padx=5, pady=5)
label_user_password_input.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
