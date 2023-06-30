import random

import scrapy, re
from ..items import ScrapysplashdemoItem
import logging
from gerapy_pyppeteer import PyppeteerRequest
from scrapy import Request, Spider


class Book2Spider(scrapy.Spider):
    name = "book2"
    allowed_domains = ["spa5.scrape.center"]
    start_urls = ["https://spa5.scrape.center"]

    def start_requests(self):
        start_url = f'{self.start_urls[0]}/page/1'
        # yield scrapy.Request(url=start_url, callback=self.parse_index)
        yield PyppeteerRequest(url=start_url, callback=self.parse_index, wait_for='.item .name',
                               screenshot={'type': 'png', 'fullPage': True})

    def parse_index(self, response):
        """
        提取书和下一页
        :param response:
        :return:
        """


        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').get()
            detail_url = response.urljoin(href)
            # yield response.follow(url=detail_url, callback=self.parse_detail, priority=2)
            yield PyppeteerRequest(url=detail_url, callback=self.parse_detail, priority=2, wait_for='.item .name')
        page_nums = re.findall(r'page/(\d+)', response.url)
        if not page_nums:
            return
        max_page_num = max(map(int, page_nums))
        next_page_num = max_page_num + 1
        next_url = f'{self.start_urls[0]}/page/{next_page_num}'
        # yield response.follow(next_url, callback=self.parse_index)

        # with open(f'screenshot-{random.randint(1000, 9999)}.png', 'wb') as f:
        #     f.write(response.meta['screenshot'].getbuffer())

        yield PyppeteerRequest(url=next_url, callback=self.parse_index, wait_for='.item .name')

    def parse_detail(self, response):
        name = response.css('.name::text').get()
        tags = response.css('.tags button span::text').getall()
        score = response.css('.score::text').get()
        cover = response.css('.cover img::attr(src)').get()
        price = response.css('.price span::text').get()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        item = ScrapysplashdemoItem(name=name, tags=tags, score=score, cover=cover, price=price)
        yield item
