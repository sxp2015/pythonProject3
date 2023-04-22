
def get_mail_content(part):
    """
    获取邮件正文
    """
    content_charset = part.get_charset()  # 获取当前部分的字符集
    if part.is_multipart():  # 判断当前部分是否为多个部分
        for sub_part in part.get_payload():
            get_mail_content(sub_part)  # 递归获取每个子部分的内容
    else:
        content_type = part.get_content_type()  # 获取当前部分的MIME类型
        if content_type == 'text/plain' or content_type == 'application/pdf' or content_type == 'application/zip':
            try:
                content = part.get_payload(decode=True).decode(content_charset)
            except AttributeError:
                content = part.get_payload(decode=True)

            # 根据正文类型，生成不同的文件名
            if content_type == 'text/plain':
                filename = '__邮件正文.txt'
            elif content_type == 'application/pdf':
                filename = '__邮件正文.pdf'
            else:
                filename = '__邮件正文.zip'

            # 将正文保存到本地文件
            with open(filename, 'wb') as f:
                f.write(content)
            print('已保存文件：{}'.format(filename))