# 定义一个异步方法获取网站的访问状态
import asyncio
from typing import Coroutine

import requests


async def request_site():
    url = 'https://cn.bing.com'
    status = requests.get(url)
    return status


# 调用execute函数并获取协程对象

# 任务列表
tasks = [asyncio.ensure_future(request_site()) for _ in range(5)]
print('Task List:', tasks)

# 创建事件循环对象
loop = asyncio.get_event_loop()
# 执行事件循环
loop.run_until_complete(asyncio.wait(tasks))
"""
在Python3.7及以后的版本中，我们可以使用asyncio.run(main())代替最后的启动操作，
不需要显示声明事件循环，run 方法内部会自动启动一个事件循环。但这里为了兼容更多的Python版本，
依然显式声明了事件循环。
"""
# 遍历结果
for task in tasks:
    print('Task 结果:', task.result())
