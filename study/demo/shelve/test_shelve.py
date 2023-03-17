import shelve

# 利用shelve模块来保存数据是将变量保存到文件的最佳方式

shelveFile = shelve.open('mydata')
cats = ['Cat1', 'Cat2', 'Cat3']
shelveFile['cats'] = cats


print('type', type(shelveFile))

print('shelveFile = ', shelveFile['cats'])

# 返回类似列表的值，而不是真正列表，所以应该将它们传递
# 给list()函数来取得列表的形式

print('keys = ', list(shelveFile.keys()))
print('values = ', list(shelveFile.values()))

shelveFile.close()
