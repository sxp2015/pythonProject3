import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random

# 爱情感悟文本，随机选择一段
love_quotes = [
    "爱情不是一种占有，而是一种给予。——卡勒德·纪伯伦",
    "爱情，是一种甜美的负担。——卡尔·拉格斐",
    "爱情就像一场旅行，不会因为目的地的改变而失去精彩。——克莱尔·博伊尔",
    "爱情是一束烈火，两颗心融为一体，化作永恒。——特里·摩根",
    "爱情是一种信任，是一种承诺。——张爱玲",
    "爱情是一种磨合，也是一种成长。——普希金",
    "爱情不是占有，而是欣赏。——卢梭",
    "爱情是一种珍贵的礼物，是一种无私的付出。——乔治·桑",
    "爱情，是一个不断打磨的镜子，能让我们看到自己的缺点和不足。——雪莱",
    "爱情不是避难所，而是一座战场。——卢泰拉",
    "爱情，是一道充满暖意的阳光。——莎士比亚",
    "爱情是一种宝藏，需要我们用心去挖掘和发掘。——佚名"
]

love_quote = random.choice(love_quotes)

sender_email = "240746804@qq.com"  # 发件人邮箱
sender_password = "exvisatltfymbhbd"  # 发件人邮箱授权码
receiver_email = "ssxxpp2015@163.com"  # 收件人邮箱地址

message = MIMEText(f'亲爱的，\n\n{love_quote}\n\n邮件正文', 'plain', 'utf-8')  # 邮件正文内容
message['From'] = formataddr(("发件人昵称", sender_email))  # 发件人昵称和邮箱地址
message['To'] = formataddr(("收件人昵称", receiver_email))  # 收件人昵称和邮箱地址
message['Subject'] = "邮件标题"  # 邮件标题

smtp_obj = None  # 初始化变量

try:
    smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 连接 QQ 邮箱的 SMTP 服务器，端口为 465
    smtp_obj.login(sender_email, sender_password)  # 登录发件人邮箱
    smtp_obj.sendmail(sender_email, [receiver_email], message.as_string())  # 发送邮件
    print("邮件发送成功！")
except Exception as e:
    print("邮件发送失败！错误信息：", e)
finally:
    if smtp_obj is not None:
        smtp_obj.quit()  # 退出 SMTP 服务器连接
