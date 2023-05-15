import aiohttp
import asyncio
import time


# 定义初始时间
start = time.time()


# 定义异步函数get，通过类型标注指定参数类型和返回值类型，参数为url: str，返回值为aiohttp.ClientResponse类型
async def get(url: str) -> aiohttp.ClientResponse:
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


# 定义异步函数request_site，获取指定url的响应结果，通过类型标注指定返回值类型，返回值为None
async def request_site() -> None:
    url = 'https://www.baidu.com'
    print('等待响应:', url)

    # 调用异步函数get获取响应结果
    response = await get(url)

    # 打印获取到的响应结果信息
    print(f'从{url}获取响应结果:', response)


# 创建任务列表
tasks = [asyncio.ensure_future(request_site()) for _ in range(10)]

# 获取事件循环对象loop
loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

# 运行事件循环，执行协程任务
loop.run_until_complete(asyncio.wait(tasks))

# 计算程序运行时间
end = time.time()
print('程序运行耗时:', end - start)
