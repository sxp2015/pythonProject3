import queue, threading, time, random

buffer_size = 10

q = queue.Queue()


def producer():
    while True:
        if not q.full():
            item = random.randint(1, 100)
            q.put(item)  # 放入库存
            print(f'【生产者】生产了一个数据,【存入】%2s: queue size:%s' % (item, q.qsize()), end='\n')
            time.sleep(2)


def consumer():
    while True:
        if not q.empty():
            item = q.get()  # 取出库存
            print(f'【消费者】消费了一个数据,【取出】%2s: queue size:%s' % (item, q.qsize()))
            time.sleep(2)


p = threading.Thread(name='producer', target=producer)  # 建立producer线程
c = threading.Thread(name='consumer', target=consumer)  # 建立consumer线程
p.start()
time.sleep(2)
c.start()
time.sleep(2)
