import pika, requests, pickle

# 定义消息优先级(可选)
MAX_PRIORITY = 100
# 队列总量
TOTAL = 10

# 定义队列名称
QUEUE_NAME = 'scrape_queue'

# 连接RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 声明频道
channel = connection.channel()
# 声明队列
channel.queue_declare(queue=QUEUE_NAME, durable=True)
# 遍历

for i in range(1, TOTAL + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, properties=pika.BasicProperties(delivery_mode=2),
                          body=pickle.dumps(request))
    print(f'Put request of {url}')
