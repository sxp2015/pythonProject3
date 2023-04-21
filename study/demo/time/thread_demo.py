import threading, time

print('程序开始！')


def take_nap():
    time.sleep(3)
    print('停三秒，线程被唤醒了')


threadObj = threading.Thread(target=take_nap)
threadObj.start()

print('程序结束！')
