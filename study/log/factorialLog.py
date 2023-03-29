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


"""
使用日志消息的好处在于，你可以在程序中想加多少
就加多少，稍后只要加入一次logging.disable (logging. CRITICAL)调用就可以禁
止日志，不像print()需逐条清除。logging模块使得显示和隐藏日志消息之间的切换变
得很容易。
"""