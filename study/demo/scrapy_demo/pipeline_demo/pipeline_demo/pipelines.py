# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import PipelineDemoItem
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class PipelineDemoPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):  # MongoDBPipeline类
    def __init__(self, mongo_uri, mongo_db):  # 初始化方法，接收MongoDB的URI和数据库名称
        self.mongo_uri = mongo_uri  # 保存MongoDB的URI
        self.mongo_db = mongo_db  # 保存数据库名称

    @classmethod
    def from_crawler(cls, crawler):  # 类方法，从爬虫配置中获取MongoDB的URI和数据库名称
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):  # 在爬虫启动时连接MongoDB
        self.client = pymongo.MongoClient(self.mongo_uri)  # 创建MongoDB客户端
        self.db = self.client[self.mongo_db]  # 获取数据库实例

    def close_spider(self, spider):  # 在爬虫关闭时断开MongoDB连接
        self.client.close()  # 关闭MongoDB客户端连接

    def process_item(self, item, spider):  # 处理item的方法
        name = item.__class__.__name__  # 获取item的类名
        self.db[name].update_one({'name': item['name']}, {'$set': dict(item)}, True)  # 将item插入到对应的集合中
        return item  # 返回item


# 内置的ImagesPipeline 会默认读取Item的image urls字段并认为它是列表形式，接着遍历该
# 字段后取出每个URL进行图片下载
# "Forbidden by robots.txt" 是一个错误提示信息，通常在您尝试访问某些网站页面时出现。
# 这意味着该网站的网站管理员已经通过 robots.txt 文件阻止了搜索引擎爬虫或机器人访问某些页面或目录。
# robots.txt 是一个标准文件，用于告知搜索引擎爬虫和机器人哪些页面可以被访问，哪些页面应该被忽略。
# 如果网站管理员将某些页面列为禁止访问，那么当搜索引擎爬虫或机器人请求访问这些页面时，它们会被拒绝访问，
# 并显示 "Forbidden by robots.txt" 的错误提示信息。这是一个常见的安全措施，用于保护网站的敏感信息，
# 或防止搜索引擎爬虫或机器人访问不必要的页面

class ImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        movie = request.meta['movie']
        file_type = request.meta['type']
        name = request.meta['name']
        file_name = f'{movie}/{file_type}/{name}.jpg'
        return file_name

    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Image Downloaded Failed Item contains no images")
        # item['image_paths'] = image_paths
        # print('【image_paths】：', item['image_paths'])
        return item

    def get_media_requests(self, item, info):
        for director in item['directors']:
            director_name = director['name']
            director_image = director['image']
            # print('director_image', director_image, 'director_name', director_name)
            yield Request(director_image, meta={'movie': item['name'], 'type': 'director', 'name': director_name})

        for actor in item['actors']:
            actor_name = actor['name']
            actor_image = actor['image']
            # print('actor_image', actor_image, 'actor_name', actor_name)
            yield Request(actor_image, meta={'movie': item['name'], 'type': 'actor', 'name': actor_name})
