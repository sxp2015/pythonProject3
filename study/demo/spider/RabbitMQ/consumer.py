import pika

# 定义队列名称
QUEUE_NAME = 'scrape'
# 连接RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 声明频道
channel = connection.channel()
# 声明队列
# channel.queue_declare(queue=QUEUE_NAME)
#
#
# def callback(ch, method, properties, body):
#     print(f'得到:{body.decode("utf-8")}')
#
#
# channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=callback)
# channel.start_consuming()

# 随用随取机制
while True:
    input('输入你想获取的内容：')
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        print(f'获取到的内容: {body.decode("utf-8")}')


