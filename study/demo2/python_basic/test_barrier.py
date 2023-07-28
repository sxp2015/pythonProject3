import random
import threading
import time


def player():
    name = threading.currentThread().getName()
    time.sleep(random.randint(2, 5))
    print('%s 抵达栅栏时间 %s' % (name, time.ctime()))
    barrier.wait()


barrier = threading.Barrier(4)
print('比赛开始..')

threads = []
for i in range(4):
    t = threading.Thread(target=player, args=(barrier,))
    threads.append(t)
    t.start()

for j in threads:
    j.join()

print('所有选手均已抵达栅栏')
# barrier.wait()  # 主线程等待所有子线程完成
#
# print('比赛结束..')
