
import pika

# 定义队列名称
QUEUE_NAME = 'scrape'
# 连接RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 声明频道
channel = connection.channel()

# 定义消息优先级(可选)
MAX_PRIORITY = 100

# 设置队列参数，包括优先级和自动删除
queue_arguments = {
    'x-max-priority': MAX_PRIORITY,  # x-max-priority 优先级的最大值为100，即优先级范围为0~100。
    'x-message-ttl': 100000,  # x-message-ttl 消息的存活时间为100秒。
    'x-expires': 300000  # x-expires：队列的生存时间为300秒。
}

# 发布消息队列
# channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=b'hello world!')


# 随用随取机制
while True:
    # 获取用户输入的内容和优先级
    user_input = input('输入你要发送的内容（格式：内容 优先级别）: ').split()
    if len(user_input) != 2:
        print('输入格式错误，请重新输入！')
        continue
    data, priority = user_input
    try:
        # 如果队列已经存在，则不会创建新队列，而是使用已经存在的队列，并更新队列的参数。
        # 在声明队列时指定durable为True，即可开启持久化存储，这样即使RabbitMQ服务器宕机，队列也不会丢失实现如下:
        channel.queue_declare(queue=QUEUE_NAME, durable=True, arguments=queue_arguments)

        # 发送消息到队列
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME,
                              body=data.encode('utf-8'),
                              # 添加消息的时候需要指定BasicProperties 对象的delivery_mode为2
                              properties=pika.BasicProperties(priority=int(priority), delivery_mode=2))
        print(f'消息已发送：{data}')
    except RuntimeError:
        print('发送消息失败！')

# 关闭连接
connection.close()

"""
`queue_declare`方法中的`arguments`参数是一个字典，用于指定队列的一些额外参数。这些参数可以用于控制队列的行为、性能和安全性等方面。以下是一些常用的参数及其说明：

- `x-message-ttl`：指定消息的存活时间，单位为毫秒。当消息在队列中等待的时间超过此值时，消息将被删除。如果队列中已经存在某个消息，而该消息的存活时间已经过期，则该消息将在队列中保留，直到被消费者消费。

- `x-expires`：指定队列的生存时间，单位为毫秒。当队列在指定的时间内未被使用时，队列将被自动删除。如果队列在某个时间点已经被声明，但在该时间点后未被使用，则该队列将在指定的时间后被自动删除。

- `x-max-length`：指定队列中允许存储的最大消息数量。当队列中的消息数量超过此值时，新的消息将被拒绝并返回给生产者。如果将此参数设置为0或负数，则表示队列中的消息数量不受限制。

- `x-max-length-bytes`：指定队列中允许存储的最大消息总大小，单位为字节。当队列中的消息总大小超过此值时，新的消息将被拒绝并返回给生产者。如果将此参数设置为0或负数，则表示队列中的消息总大小不受限制。

- `x-max-priority`：指定队列支持的最大优先级数。当消息发送到队列时，可以指定消息的优先级。如果队列的优先级数为N，则优先级范围为0~N-1。默认情况下，队列的优先级数为0，即不支持优先级。如果将此参数设置为正整数，则表示队列支持指定数量的优先级。

- `x-dead-letter-exchange`：指定死信队列的交换机名称。当队列中的消息被拒绝、过期或达到最大重试次数时，这些消息将被发送到死信队列。如果将此参数设置为某个交换机名称，则表示该交换机将接收死信消息。

- `x-dead-letter-routing-key`：指定死信队列的路由键。当消息被发送到死信队列时，可以使用该路由键将死信消息路由到指定的队列中。

这些参数可以在队列声明时指定，也可以在队列已经存在的情况下使用`queue_bind`方法进行绑定。使用这些参数可以对队列的行为进行精细控制，提高队列的性能和安全性。
"""
