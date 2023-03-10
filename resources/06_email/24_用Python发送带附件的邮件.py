# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

host_server = 'smtp.sina.com'
sender_sina = 'your_email@sina.com'
pwd = 'your_pwd'

sender_sina_mail = 'your_email@sina.com'
receiver = 'others_email@sina.com'
mail_title = '这是标题'
mail_content = '这是正文'
msg = MIMEMultipart()
msg['Subject'] = Header(mail_title, 'utf-8')
msg['From'] = sender_sina_mail
msg['To'] = Header('mail_title', 'utf-8')
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
# 添加附件
attachment = MIMEApplication(open('student.xls', 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename='student.xls')
msg.attach(attachment)
try:
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_sina, pwd)
    smtp.sendmail(sender_sina_mail, receiver, msg.as_string())
    smtp.quit()
    print('success')
except smtplib.SMTPException:
    print('error')
