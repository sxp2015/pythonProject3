import pika, requests, pickle

# 定义消息优先级(可选)
MAX_PRIORITY = 100

# 定义队列名称
QUEUE_NAME = 'scrape_queue'

# 连接RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 声明频道
channel = connection.channel()
session = requests.Session()


def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {response.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')


while True:
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        request = pickle.loads(bytes(body))
        print(f'Get {request}')
        scrape(request)
