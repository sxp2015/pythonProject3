import office

# word转PDF
# word_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\resources\\02word\\012_Word_word转pdf\\test.docx'
# office.word.docx2pdf(path=word_file_path)

# 批量重命名文件
# rename_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_file\\'
# office.file.replace4filename(path=rename_file_path, del_content='test11.docx', replace_content='test13.docx')

# 批量重命名文件(夹)
# rename_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_doc'
# office.file.replace4filename(path=rename_doc_path, del_content='rename2', replace_content='rename3')

# PPT转PDF
# ppt_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\ppt\\'
# office.ppt.ppt2pdf(path=ppt_doc_path)

# 批量假数据 详细字段 https://mp.weixin.qq.com/s/xVwEjXu58WovgSi4ZTtVQw
# office.excel.fake2excel(columns=['name_female', 'name_male', 'phone_number', 'ssn',
#                                  'company', 'company_email', 'pystr', 'country', 'province', 'city_suffix',
#                                  'street_address', 'address'], rows=20)

# 合并多张Excel工作表到一个工作簿
# excel_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\excel'
# office.excel.merge2excel(dir_path=excel_doc_path, output_file='mege2.xlsx')


# PDF加水印
# pdf_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\pdf\\静夜思.pdf'
# office.pdf.add_watermark_by_parameters(pdf_file=pdf_path, mark_str='水印文字')


# 生成词云 就是哪个字符出现的最多，这个字符显示的字号越大，形成一张图片(功能过期)
# txt_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\txt\\1.txt'
# office.image.txt2wordcloud(filename=txt_file_path, color='red', result_file='res.png')

# 多个Excel关联查询(target_dir 搜索的目录)
# excel_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\excel'
# office.excel.find_excel_data(search_key='李想', target_dir=excel_doc_path)

# pdf转word
# pdf_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\pdf\\2.pdf'
# office.pdf.pdf2docx(file_path=pdf_file_path, output_path=pdf_doc_path)

# 图片加水印
# img_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\img\\111.jpg'
# office.image.add_watermark(file=img_file_path, mark='添加图片水印')

# 根据内容查找文件（所有文件在一个目录下，word是搜索正文内容部分，excel是搜索精准列名，不是包含和模糊搜索，PPT也是文字部分内容）
# 注意路径的写法，双反斜杠，还是单反斜杠，如果是单的，前面要加个r,  r 代表 raw 原始数据
# search_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\search_by_content'
# search_path2 = r'C:\Users\admin\PycharmProjects\pythonProject1\study\demo\search_by_content'
# office.file.search_by_content(search_path=search_path2, content='中医')

# 下载图片
url = 'https://www.baidu.com/img/pcdoodle_2a77789e1a67227122be09c5be16fe46.png'
office.image.down4img(url=url)


