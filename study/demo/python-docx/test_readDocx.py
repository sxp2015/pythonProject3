import readDocx

docx_file_path = r'C:\Users\admin\PycharmProjects\pythonProject3\study\docx\test\房屋买卖协议.docx'

print('获取到的文件内容', readDocx.get_text(docx_file_path))
