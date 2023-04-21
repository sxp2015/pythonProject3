import time


def calc_prod():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
prod = calc_prod()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
# round()函数将按照指定的精度四舍五入一个浮点数。
# 第二个参数，指明需要传入保留的小数位数
print('Took %s seconds to calculate.' % round((endTime - startTime), 2))

if __name__ == "__main__":
    calc_prod()
