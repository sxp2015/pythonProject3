import office

word_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\resources\\02word\\012_Word_word转pdf\\test.docx'
rename_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_file\\'
rename_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\demo\\rename_doc'
ppt_doc_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\ppt\\'
excel_merge_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject1\\study\\excel'
# word转PDF
# office.word.docx2pdf(path=word_doc_path)

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
office.excel.merge2excel(dir_path=excel_merge_path, output_file='mege2.xlsx')
