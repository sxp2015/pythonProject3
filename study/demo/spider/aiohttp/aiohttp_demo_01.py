import aiohttp
import asyncio
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient

# 定义常量
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'

# 获取客户端、数据库、连接器
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# 初始化日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - $(levelname)s: %(message)s')

# 定义常量
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE: int = 18
PAGE_NUMBER: int = 5
CONCURRENCY: int = 5

# 创建一个信号量，控制并发数量
semaphore = asyncio.Semaphore(CONCURRENCY)


# 定义异步函数scrape_api，通过类型标注指定参数类型和返回值类型，参数为session: aiohttp.ClientSession，url: str，返回值类型为dict
async def scrape_api(session: aiohttp.ClientSession, url: str) -> dict:
    # 每次请求前先获得一个信号量，防止并发过大，服务器拒绝连接。
    async with semaphore:
        try:
            # 记录日志，输出正在爬取的URL
            logging.info('正在爬取: %s', url)

            # 发起HTTP请求
            async with session.get(url) as response:
                # 解析响应结果为json格式并返回
                return await response.json()
        except aiohttp.ClientError:
            # 发生异常时，记录异常信息到日志中
            logging.error('爬取 %s 时出错', url, exc_info=True)


# 定义异步函数scrape_index，通过类型标注指定参数类型和返回值类型，参数为session: aiohttp.ClientSession，page: int，返回值类型为dict
async def scrape_index(session: aiohttp.ClientSession, page: int) -> dict:
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    # 调用异步函数scrape_api获取响应结果并返回
    return await scrape_api(session, url)


# 定义保存数据到数据库的方法
async def save_data(data):
    logging.info('save data %s', data)
    if data:
        # upsert=True 参数表示如果找不到匹配的文档，就插入一条新数据，默认为 False
        return await collection.update_one({'id': data.get('id')}, {'$set': data}, upsert=True)


# 定义爬取详情页的方法
async def scrape_detail(session, book_id):
    url = DETAIL_URL.format(id=book_id)
    data = await scrape_api(session, url=url)
    await save_data(data)


# 定义异步函数main，通过类型标注指定返回值类型为None
async def main() -> None:
    # 创建一个HTTP请求会话对象
    async with aiohttp.ClientSession() as session:
        # 创建任务列表，调用scrape_index函数获取指定页码的图书信息
        scrape_index_tasks = [asyncio.ensure_future(scrape_index(session, page)) for page in range(1, PAGE_NUMBER + 1)]

        # 等待所有异步协程任务完成
        results = await asyncio.gather(*scrape_index_tasks)

        # 输出获取到的图书信息结果，采用json格式化，并设置ensure_ascii=False保留非ASCII字符，indent设置为2进行缩进
        logging.info('获取到的图书信息结果: %s,', json.dumps(results, ensure_ascii=False, indent=2))

        # 定义一个数组变量保存返回的每个id
        ids = []
        for index_data in results:
            if not index_data:
                continue
            for item in index_data.get('results'):
                ids.append(item.get('id'))

        # 爬取详情页
        scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(session, book_id)) for book_id in ids]
        await asyncio.wait(scrape_detail_tasks)
        # 关闭HTTP请求会话对象
        await session.close()


if __name__ == '__main__':
    # 获取事件循环对象loop
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    # 运行事件循环，执行异步协程任务
    loop.run_until_complete(main())
