# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Scrapy-Splash 的安装 https://cuiqingcai.com/31044.html
import scrapy


class ScrapysplashdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    tags = scrapy.Field()
    score = scrapy.Field()
    cover = scrapy.Field()
    price = scrapy.Field()

