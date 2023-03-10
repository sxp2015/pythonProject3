# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


# pip install wxpy
from wxpy import *

# 初始化一个机器人对象
# cache_path缓存路径，给定值为第一次登录生成的缓存文件路径
bot = Bot()
# 获取好友列表(包括自己)
my_friends = bot.friends(update=False)
'''
stats_text 函数：帮助我们简单统计微信好友基本信息
简单的统计结果的文本    
:param total: 总体数量    
:param sex: 性别分布    
:param top_provinces: 省份分布    
:param top_cities: 城市分布    
:return: 统计结果文本
'''
print(my_friends.stats_text())
