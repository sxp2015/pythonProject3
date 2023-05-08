import csv

with open('csvfile.csv', 'a+', encoding='utf-8') as csvfile:
    # delimiter参数，是以什么符号分隔列，下面是空格
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['工号', '姓名', '年龄'])
    writer.writerow(['1001', '张三', '18'])
    writer.writerow(['1002', '李四', '19'])
    writer.writerow(['1003', '王五', '20'])

with open('csvfile2.csv', 'a+', encoding='utf-8') as csvfile2:
    fieldnames = ['工号', '姓名', '年龄']
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'工号': '1004', '姓名': '小李', '年龄': 23})
    writer.writerow({'工号': '1005', '姓名': '小何', '年龄': 28})
    writer.writerow({'工号': '1006', '姓名': '小王', '年龄': 29})
