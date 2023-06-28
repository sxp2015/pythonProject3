import scrapy
from scrapy import Request
from ..items import PipelineDemoItem


class Ssr1Spider(scrapy.Spider):
    name = "ssr1"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]
    max_page = 10

    def start_requests(self):
        for i in range(1, self.max_page + 1):
            url = f'{self.start_urls[0]}/page/{i}'
            yield Request(url, callback=self.parse_index)

    def parse_index(self, response):
        for item in response.css('.item'):
            href = item.css('.name::attr(href)').get()
            url = response.urljoin(href)
            yield Request(url=url, callback=self.parse_detail)
            # print('Response:', response)

    def parse_detail(self, response):
        item = PipelineDemoItem()
        item['name'] = response.xpath('//div[contains(@class,"item")]//h2/text()').get()
        item['categories'] = response.xpath('//button[contains(@class,"category")]//span/text()').getall()
        item['score'] = response.css('.score::text').re_first('[\d\.]+')
        item['drama'] = response.css('.drama p::text').get().strip()
        item['directors'] = []
        directors = response.xpath('//div[contains(@class,"directors")]//div[contains(@class,"director")]')

        for director in directors:
            # print('director:', director)
            director_image = director.xpath('.//img[@class="image"]/@src').get()
            director_name = director.xpath('.//p[contains(@class,"name")]/text()').get()
            item['directors'].append({'image': director_image, 'name': director_name})
        item['actors'] = []
        actors = response.css('.actors .actor')
        for actor in actors:
            actor_image = actor.css('.actor .image::attr(src)').get()
            actor_name = actor.css('.actor .name::text').get()
            item['actors'].append({'image': actor_image, 'name': actor_name})
        yield item
