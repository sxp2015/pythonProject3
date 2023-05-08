import csv
import pandas as pd

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

data = [{"name": "Bob", "gender": "male", "birthday": "1992-10-18"},
        {"name": "Selina", "gender": "female", "birthday": "1995-10-18"},
        {"name": "张三", "gender": "男", "birthday": "1990年12月11日"},
        {'name': '1004', 'gender': '小李', 'birthday': 23},
        {'name': '1005', 'gender': '小何', 'birthday': 28},
        {'name': '1006', 'gender': '小王', 'birthday': 29}]

# 使用pandas 来保存csv文件
df = pd.DataFrame(data)
df.to_csv('csvfile3.csv', index=False)

# 使用pandas 来读取csv文件
df = pd.read_csv('csvfile.csv')
data_values = df.values.tolist()
print('values ==', data_values)