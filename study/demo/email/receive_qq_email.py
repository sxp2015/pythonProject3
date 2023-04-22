import imaplib
import email
import os
import chardet

# 邮箱账号和授权码
email_address = "240746804@qq.com"
email_auth_code = "e*********d"

# 连接 QQ 邮箱的 IMAP 服务器
imap_server = "imap.qq.com"
imap_port = 993
imap = imaplib.IMAP4_SSL(imap_server, imap_port)

# 登录邮箱
# 使用授权码登录邮箱
imap.login(email_address, email_auth_code)

# 选择收件箱
imap.select('INBOX')

# 搜索收件箱中所有未读邮件的编号
_, message_numbers = imap.search(None, "UNSEEN")

# 遍历所有未读邮件的编号
for num in message_numbers[0].split():
    # 获取邮件
    _, message_data = imap.fetch(num, "(RFC822)")
    message = email.message_from_bytes(message_data[0][1])

    # 获取邮件主题和发件人信息
    subject = email.header.decode_header(message.get("Subject"))[0][0]
    sender = email.utils.parseaddr(message.get("From"))[1]

    # 遍历邮件的所有部分，查找文本内容和附件
    for part in message.walk():
        # 如果是文本部分
        if part.get_content_type() == "text/plain":
            # 获取文本内容
            text = part.get_payload(decode=True)
            # 自动检测编码格式
            encoding = chardet.detect(text)["encoding"]
            # 使用相应的编码格式解码
            text = text.decode(encoding, errors="ignore")
            # 打印文本内容
            print(f"邮件主题：{subject}")
            print(f"发件人：{sender}")
            print(f"文本内容：{text}")
            # 将文本内容保存到本地文件
            with open(f"{subject.decode(encoding)}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            # 如果是附件部分，可以进行保存操作
        elif part.get_content_type().startswith("application"):
            filename = part.get_filename()
            with open(filename, "wb") as f:
                f.write(part.get_payload(decode=True))

# 关闭邮箱连接
imap.close()
imap.logout()
