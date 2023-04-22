import threading, time

print('程序开始！')


# 在程序的所有线程终止之前，Python程序不会终止
def take_nap():
    time.sleep(3)
    print('停三秒，线程被唤醒了')


# 也可以向线程传递参数 Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
# kwargs={'sep': ' & '})

threadObj = threading.Thread(target=take_nap)
threadObj.start()

print('程序结束！')
