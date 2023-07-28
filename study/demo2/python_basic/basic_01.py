nums = [1, 2, 3, 4, 5, 6]

del nums[0:6:2]

print('nums=', nums)

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        # end=' '是print()函数的一个参数，用于指定在打印结束后要添加到输出末尾的字符，默认为换行符\n
        # 通过设置end=' '，print()函数在输出完每个乘法结果后会添加一个空格字符，使得下一个乘法结果能够紧跟在后面，实现乘法表格的效果。
        # 如果没有设置end参数或将其设置为默认值\n，则输出的每个乘法结果将占据独立的一行。
        # %-3d 保持字段宽度为3对齐方式为左对齐
        print("%d * %d = %-3d" % (i, j, result), end=' ')
    print()

seq1 = ['name', 'age', 'sex']
# 列表转字典，没有赋值，默认为空值
list_dict1 = dict.fromkeys(seq1)
print('字典1', list_dict1)
# 列表转字典，有值，则每个Key，都赋一个值
list_dict2 = dict.fromkeys(seq1, 'hello world')
print('字典2', list_dict2)
# 列表转元组，没有赋值，默认为空值
seq2 = ('name', 'age', 'sex')
tup_dict1 = dict.fromkeys(seq2)
print('字典3', tup_dict1)
# 列表转元组，有值，则每个Key，都赋一个值
tup_dict2 = dict.fromkeys(seq2, 'Green')
print('字典4', tup_dict2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A.intersection(B)
print("对称差集，就是不属于两个交集的值 :", A ^ B)
# A.union(B)
print("并集，两个集合去重后的所有元素:", A | B)

# 属于 A 集合元素，同时不属于 B 集合则可以使用差集 (A-B)。 # A.difference(B)
print("并集，两个集合去重后的所有元素:", A - B)
print("并集，两个集合去重后的所有元素:", B - A)

