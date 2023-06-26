# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import PipelineDemoItem


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
