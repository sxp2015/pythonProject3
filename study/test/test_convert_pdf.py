import office

word_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\resources\\02word\\012_Word_word转pdf\\test.docx'
rename_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_file\\'
rename_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_doc'
ppt_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\ppt\\'
excel_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\excel'
txt_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\resources\\10txt\\684-三十年临证经验集.txt'
pdf_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\pdf\\2.pdf'
pdf_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\pdf\\'
img_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\img\\111.jpg'
# word转PDF
# office.word.docx2pdf(path=word_file_path)

# 批量重命名文件
# office.file.replace4filename(path=rename_file_path, del_content='test11.docx', replace_content='test13.docx')

# 批量重命名文件(夹)
# office.file.replace4filename(path=rename_doc_path, del_content='rename2', replace_content='rename3')

# PPT转PDF
# office.ppt.ppt2pdf(path=ppt_doc_path)

# 批量假数据 详细字段 https://mp.weixin.qq.com/s/xVwEjXu58WovgSi4ZTtVQw
# office.excel.fake2excel(columns=['name_female', 'name_male', 'phone_number', 'ssn',
#                                  'company', 'company_email', 'pystr', 'country', 'province', 'city_suffix',
#                                  'street_address', 'address'], rows=20)

# 合并多张Excel工作表到一个工作簿
# office.excel.merge2excel(dir_path=excel_doc_path, output_file='mege2.xlsx')


# PDF加水印
# pdf_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\pdf\\静夜思.pdf'
# office.pdf.add_watermark_by_parameters(pdf_file=pdf_path, mark_str='水印文字')


# 生成词云 就是哪个字符出现的最多，这个字符显示的字号越大，形成一张图片(功能过期)
# office.image.txt2wordcloud(filename=txt_file_path, color='red', result_file='res.png')

# 多个Excel关联查询(target_dir 搜索的目录)
# office.excel.find_excel_data(search_key='李想', target_dir=excel_doc_path)

# pdf转word
# office.pdf.pdf2docx(file_path=pdf_file_path, output_path=pdf_doc_path)

# 图片加水印
office.image.add_watermark(file=img_file_path, mark='添加图片水印')
