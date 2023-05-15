#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-15 21:10
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : test_semaphore.py
# @IDE     : PyCharm
import asyncio
import aiohttp

# 定义并发量
CONCURRENCY = 5

# 定义网址
URL = 'https://www.baidu.com'

# 控制并发量
semaphore = asyncio.Semaphore(CONCURRENCY)


# 定义异步函数scrape_api
async def scrape_api(session):
    # 每次请求前先获得一个信号量，防止并发过大，服务器拒绝连接。
    async with semaphore:
        # 输出正在请求的URL
        print('scraping url:', URL)
        # 发起请求，并等待响应结果
        async with session.get(URL) as response:
            # 等待1秒，模拟人工操作，防止过于频繁的请求被服务器封锁。
            await asyncio.sleep(1)
            # 返回响应文本内容
            return await response.text()


# 定义主函数
async def main():
    # 创建一个新的会话对象
    async with aiohttp.ClientSession() as session:
        # 定义一万个任务，每个任务都是异步调用scrape_api函数
        scrape_index_tasks = [asyncio.ensure_future(scrape_api(session)) for _ in range(10000)]
        # 等待所有任务并发执行，并返回所有任务的结果
        result = await asyncio.gather(*scrape_index_tasks)
    return result


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        results = loop.run_until_complete(main())
    finally:
        loop.close()

"""
在main方法里，我们声明了10000个task，将其传递给gather 方法运行。倘若不加以限制，
那这10000个task会被同时执行，并发数量相当大。
但有了信号量的控制之后，同时运行的task数量最大会被控制在5个，
这样就能给aiohttp 限制速度了。
"""
