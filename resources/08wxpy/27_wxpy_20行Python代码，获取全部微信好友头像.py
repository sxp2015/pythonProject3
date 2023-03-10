# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


from wxpy import *
import os,sys

# 初始化机器人，扫码登陆微信，适用于Windows系统
bot = Bot()
# # Linux系统，执行登陆请调用下面的这句
# bot = Bot(console_qr=2, cache_path="botoo.pkl"
# 获取当前路径信息
image_dir = os.getcwd()+'\\' + "FriendImgs\\"
# 如果保存头像的FriendImgs目录不存在就创建一个
if not os.path.exists(image_dir):
    os.mkdir(image_dir)
os.popen('explorer ' + image_dir)
my_friends = bot.friends(update=True)
# 获取好友头像信息并存储在FriendImgs目录中
n = 0
for friend in my_friends:
    print(friend)
    image_name = image_dir + str(n) + '.jpg'
    friend.get_avatar(image_name)
    n = n + 1