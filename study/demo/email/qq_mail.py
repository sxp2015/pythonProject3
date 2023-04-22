import imaplib
import email
from email.header import decode_header

# 登录邮箱并选择收件箱
mail = imaplib.IMAP4_SSL('imap.qq.com')
mail.login('240746804@qq.com', 'exvisatltfymbhbd')
mail.select('inbox')

# 打开txt文件，准备写入
with open('邮件内容.html', 'w', encoding='utf-8') as f:
    # 搜索收件箱中的邮件
    status, data = mail.search(None, 'ALL')
    mail_ids = data[0].split()

    # 读取每个邮件的内容
    for mail_id in mail_ids:
        status, data = mail.fetch(mail_id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        # 解析邮件主题和发件人
        subject = decode_header(msg['Subject'])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode('utf-8')
        sender = decode_header(msg['From'])[0][0]
        if isinstance(sender, bytes):
            sender = sender.decode('utf-8')

        # 如果邮件中有多个部分，则递归获取
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass

                # 如果邮件中包含html内容，则写入txt文件
                if content_type == "text/html" and "attachment" not in content_disposition:
                    f.write('Subject: {}\n'.format(subject))
                    f.write('From: {}\n'.format(sender))
                    f.write('Body: \n{}\n'.format(body))

        # 如果邮件只有一部分，则获取内容
        else:
            body = msg.get_payload(decode=True).decode()
            f.write('Subject: {}\n'.format(subject))
            f.write('From: {}\n'.format(sender))
            f.write('Body: \n{}\n'.format(body))

# 关闭邮箱连接
mail.close()
mail.logout()