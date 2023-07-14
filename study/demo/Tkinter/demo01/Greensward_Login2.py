from tkinter import *
from PIL import Image, ImageTk

# 创建窗口对象
window = Tk()
window.title('郴州建活塑胶科技有限公司 用户登陆')

window.geometry('500x350')


def print_info():
    # 打印输入的账号和密码信息
    print(f"账号是: {entry_account.get()}")
    print(f"密码是: {entry_password.get()}")


def clear_input():
    entry_password.delete(0, END)
    entry_account.delete(0, END)


# 禁用窗口最大化功能
window.resizable(False, False)

wellcome_content = "欢迎进入郴州建活塑胶科技有限公司测试后台管理系统"

# 加载公司 Logo 图片
logo_file = Image.open('logo/logo-100x100.png')

# 缩放公司 Logo 图片
scale_init = 0.6
new_width = int(logo_file.width * scale_init)
new_height = int(logo_file.height * scale_init)
scaled_img = logo_file.resize((new_width, new_height), Image.LANCZOS)

# 将 PIL 图片对象转换为 Tkinter 图片对象
tk_img = ImageTk.PhotoImage(scaled_img)

# 创建标签显示公司 Logo 和欢迎信息
logo = Label(window, image=tk_img, text=wellcome_content, font="Helvetica 12 bold", compound=TOP, anchor=CENTER,
             width=500)
logo.grid(row=0, column=0, columnspan=2, padx=10, pady=30, sticky=N)

# 创建账号和密码的标签和输入框
login_frame = LabelFrame(window, text="用户登陆")
# login_frame.pack(padx=10, pady=5, ipadx=5, ipady=5)
login_frame.grid(padx=10, pady=5, ipadx=5, ipady=5)

label_account = Label(login_frame, text="账 号：")
entry_account = Entry(login_frame)
label_account.grid(row=0, column=0)
entry_account.grid(row=0, column=1)
entry_account.insert(0, "admin")  # 在账号输入框中显示初始值

label_password = Label(login_frame, text="密 码：")
entry_password = Entry(login_frame, show='*')
entry_password.insert(0, "admin")  # 在密码输入框中显示初始值
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)

# 创建登录和退出按钮
button_login = Button(login_frame, text="登 陆", command=print_info)
button_login.grid(row=2, column=0, padx=5, pady=5)

button_quit = Button(login_frame, text="退出", command=window.quit)
button_quit.grid(row=2, column=1, padx=5, pady=5)

# 创建清除输入的按钮
clear_input_button = Button(login_frame, text="清除输入", command=clear_input)
clear_input_button.grid(row=2, column=2, padx=5, pady=5)

# 进入主循环
window.mainloop()
