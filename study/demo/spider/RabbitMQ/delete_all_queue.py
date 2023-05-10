import pika


def delete_all_queues():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # 获取所有队列的名称
    queue_list = channel.queue_declare('', passive=True)
    queue_names = [queue.name for queue in queue_list]

    # 删除所有队列
    for queue_name in queue_names:
        channel.queue_delete(queue=queue_name)
        print(f"Queue '{queue_name}' deleted.")

    connection.close()


if __name__ == '__main__':
    delete_all_queues()
