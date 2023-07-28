import PyPDF2

# 打开 PDF 文档
pdf_file = open('input.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 打开名字文本文件
names_file = open('names.txt', 'r', encoding='utf-8')
names = names_file.readlines()

# 确保名字的数量与页数相同
# if len(names) != len(pdf_reader.pages):
#     print('名字的数量与页数不一致！')
#     exit()

# 逐页保存为单独的 PDF 文档
for i, page in enumerate(pdf_reader.pages):
    # 创建一个新的 PDF writer
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)

    # 生成新的文件名
    current_name = names[i].strip()
    new_filename = f'绩效评估_上级对下级评价_{current_name}_{i}.pdf'

    # 将对应的名字作为文件名进行保存
    with open(new_filename, 'wb') as output_file:
        pdf_writer.write(output_file)
        print(f'已保存：{new_filename} - 姓名：{current_name}')

# 关闭文件
pdf_file.close()
names_file.close()
