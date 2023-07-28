import time, threading

semaphore = threading.BoundedSemaphore(3)


def func():
    if semaphore.acquire():
        print(threading.currentThread().getName() + '正在执行', end='\n')
        print('working ...', end='\n')
        time.sleep(2)
        semaphore.release()
        print(threading.currentThread().getName() + '执行完毕', end='\n')


for i in range(10):
    t = threading.Thread(target=func)
    t.start()
