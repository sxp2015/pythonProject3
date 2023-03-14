import pyinputplus as pyip

#  blank=True,允许输入时有空格 limit=3,尝试输入几次 timeout=5,输入超时时间/秒 default='N/A'报错时默认值
# res = pyip.inputNum('请输入1-8的任意数字：', min=1, max=8, blank=True, limit=3, timeout=5, default='N/A')
#
# print('res = ', res)


# help(pyip.inputChoice)

# 使用自定义函数
def add_up_to_ten(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('所有数字求和不等于10,  等于%s.' % (sum(numbersList)))
    return int(numbers)


# 计算结果
res = pyip.inputCustom(add_up_to_ten)

# 输出结果
print(f'计算结果：输入的数{res}，求和等于10')
