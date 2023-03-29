import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')


# 编写了一个函数以计算一个数的阶乘。在数学上，4 的阶乘是1 × 2 × 3 × 4，
# 即24。7的阶乘是1 × 2 × 3 × 4 × 5 × 6 × 7，即5040。
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1  # 这里不能定义为0，因为0乘任何数，都是0

    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    logging.debug('End of factorial(%s%%)' % n)
    return total


print(factorial(8))
logging.debug('End of program')
