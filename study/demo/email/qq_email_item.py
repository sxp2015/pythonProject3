import imaplib  # 加载imaplib库，用于连接邮件服务器并获取邮件
import email  # 加载email库，用于解析邮件内容和元数据
import re  # 加载re库，用于替换文件名中的非法字符
from email.header import decode_header  # 加载decode_header函数，用于解码邮件主题和发件人
import os  # 加载os库，用于操作文件系统
import get_email_attachment


# 登录邮箱并选择收件箱
mail = imaplib.IMAP4_SSL('imap.qq.com')  # 连接QQ邮箱的IMAP服务器。通过SSL保障安全连接
mail.login('240746804@qq.com', 'exvisatltfymbhbd')  # 使用账号和授权码登录QQ邮箱
mail.select('inbox')  # 选择收件箱
# mail.select('信用卡账单')  # 选择收件箱

# 获取最新5封邮件的uid
status, data = mail.search(None, 'ALL')  # 搜索收件箱，返回所有邮件的uid列表
mail_ids = data[0].split()  # 将uid列表转换为字符串，并在逗号处分割字符串为单个的uid
latest_mail_ids = mail_ids[-10:]  # 获取最新的5封邮件的uid

# 循环读取每个邮件的内容
for mail_id in latest_mail_ids:
    status, data = mail.fetch(mail_id, '(RFC822)')  # 获取指定uid的邮件内容和元数据
    msg = email.message_from_bytes(data[0][1])  # 解析邮件内容

    # 解析邮件主题和发件人
    subject = decode_header(msg['Subject'])[0][0]  # 解码邮件主题并取出第一个元素
    if isinstance(subject, bytes):
        subject = subject.decode('utf-8')  # 如果subject是bytes类型，就将其解码为utf-8编码的字符串
    sender = decode_header(msg['From'])[0][0]  # 解码发件人并取出第一个元素
    if isinstance(sender, bytes):
        try:
            sender = sender.decode('utf-8')
        except UnicodeDecodeError:
            sender = sender.decode('gbk', 'ignore')  # 使用gbk编码进行解码，并忽略无法解码的字符

    # 如果邮件中有多个部分，则递归获取
    if msg.is_multipart():
        for part in msg.walk():  # 遍历邮件中的所有部分
            content_type = part.get_content_type()  # 获取部分的内容类型
            content_disposition = str(part.get("Content-Disposition"))  # 获取部分的Content-Disposition字段
            try:
                # 对html内容进行解码操作
                if "text/html" in content_type:  # 如果部分内容是html文本
                    body = part.get_payload(decode=True).decode()  # 获取body内容，并使用decode方法将其解码为字符串
                    # 替换文件名中的非法字符
                    filename = re.sub(r'[\\/:*?"<>|]', '_', '{}_{}.html'.format(sender, subject))  # 替换文件名中的非法字符
                    with open(filename, 'w', encoding='utf-8') as f:  # 打开文件并以utf-8编码写入
                        f.write(body)  # 写入HTML正文内容
                        print('已保存文件：{}'.format(filename))  # 输出文件名

                elif "attachment" in content_disposition:  # 如果部分内容是附件
                    filename = decode_header(part.get_filename())[0][0]  # 获取附件文件名并解码
                    if isinstance(filename, bytes):
                        filename = filename.decode('utf-8')  # 如果filename是bytes类型，就将其解码为utf-8编码的字符串
                    filename = re.sub(r'[\\/:*?"<>|]', '_', filename)  # 替换文件名中的非法字符
                    filepath = os.path.join(os.getcwd(), filename)  # 构造文件路径
                    with open(filepath, 'wb') as f:  # 打开并以二进制写入模式写入附件内容
                        f.write(part.get_payload(decode=True))
                        print('已保存附件：{}'.format(filename))  # 输出文件名

            except:
                pass

    # 如果邮件只有一部分，则获取内容
    else:
        body = msg.get_payload(decode=True).decode()  # 获取邮件正文
        # 替换文件名中的非法字符
        filename = re.sub(r'[\\/:*?"<>|]', '_', '{}_{}.html'.format(sender, subject))  # 替换文件名中的非法字符
        with open(filename, 'w', encoding='utf-8') as f:  # 打开文件并以utf-8编码写入
            f.write(body)  # 写入HTML正文内容
            print('已保存文件：{}'.format(filename))  # 输出文件名

# 关闭邮箱连接
mail.close()  # 关闭选择的邮箱
mail.logout()  # 注销邮箱账号

"""
这个程序的开发流程如下：
1. 首先确定需求，即从邮箱中获取最新的邮件并解析其正文，将其保存为HTML文件。
2. 了解相关的Python库和API，确定需要使用imaplib、email、re和os库，以及QQ邮箱的IMAP API。
3. 编写代码连接QQ邮箱的IMAP服务器，登录QQ邮箱，并选择收件箱。
4. 获取最新的5封邮件的uid，以便后续读取每个邮件的内容。
5. 循环读取每个邮件的内容，解析邮件主题和发件人，并判断邮件是否有多个部分。如果有多个部分，则递归获取每个部分的内容；否则直接获取邮件的内容。
6. 对邮件中的HTML内容进行解码操作，并替换文件名中的非法字符。
7. 将HTML正文内容写入相应的HTML文件中，并输出文件名。
8. 关闭QQ邮箱的IMAP连接和注销邮箱账号。

总体来说，这个程序的开发流程包括了以下几个步骤：需求分析、API和库的选用、代码编写、调试和测试。最终实现了从QQ邮箱中获取邮件并解析其正文，将其保存为HTML文件的功能。
"""