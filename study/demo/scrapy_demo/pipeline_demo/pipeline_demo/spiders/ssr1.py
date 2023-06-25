import scrapy
from scrapy import Request


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
        print('Response:', response)
