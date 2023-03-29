ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
# ages.reverse() 取消注释，则断言不成立
print("ages ==", ages)
assert ages[0] <= ages[-1]  # assert判断右方条件表达式是否成立，为True则执行下一步，否则，抛出异常
print('assert...')
