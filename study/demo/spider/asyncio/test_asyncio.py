import asyncio
from typing import Coroutine
import requests


# 定义协程函数execute，并通过类型标注指定参数类型和返回值类型，参数x为int类型


async def execute(x: int) -> int:
    print('Number:', x)
    return x


# 定义一个异步方法获取网站的访问状态
async def request_site(url):
    status = requests.get(url)
    return status


# 定义一个回调函数，打印任务执行结果
def callback(task_obj):
    print('callback 任务结果：', task_obj.result())


# 调用execute函数并获取协程对象
coroutine: Coroutine = execute(100)
coroutine2: Coroutine = execute(200)
coroutine_request: Coroutine = request_site('https://cn.bing.com')

print('Coroutine:', coroutine)
print('调用协程对象之后')

# 获取事件循环对象loop
loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
loop_request: asyncio.AbstractEventLoop = asyncio.get_event_loop()

# 创建任务对象task，将协程对象作为参数传入
task: asyncio.Task = loop.create_task(coroutine)

# 定义task对象还有另外一种方式就是直接调用asyncio包的ensure future方法，返回结果也是task对象
task2: asyncio.Task = asyncio.ensure_future(coroutine2)

# 访问网站的任务
task_request: asyncio.Task = asyncio.ensure_future(coroutine_request)
task_request.add_done_callback(callback)
loop_request.run_until_complete(task_request)

print('Task:', task)
print('Task2:', task2)
print('Task_request:', task_request)

"""
task,它是对协程对象的进一步封装比协程对象多了运行状态例如running、finished等，
我们可以利用这些状态获取协程对象的执行情况。
"""

# 运行事件循环，执行协程任务
loop.run_until_complete(task)

# 打印任务结果和任务对象信息
print('任务结果:', task.result())
print('任务对象:', task)
print('调用事件循环之后')
