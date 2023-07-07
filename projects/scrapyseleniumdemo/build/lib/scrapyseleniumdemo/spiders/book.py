import scrapy, re
from gerapy_selenium import SeleniumRequest

from ..items import ScrapyseleniumdemoItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["spa5.scrape.center"]
    start_urls = ["https://spa5.scrape.center"]

    def start_requests(self):
        start_url = f'{self.start_urls[0]}/page/1'
        #  yield scrapy.Request(url=start_url, callback=self.parse_index)
        yield SeleniumRequest(url=start_url, callback=self.parse_index, wait_for='.item .name')

    def parse_index(self, response):
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').get()
            detail_url = response.urljoin(href)
            # 以下两个方法都可以
            # yield scrapy.Request(url=detail_url, callback=self.parse_detail, priority=2)
            yield response.follow(url=detail_url, callback=self.parse_detail, priority=2)

        # 使用 re.findall() 一次性提取所有页码
        # 这个方法是一次性拿到所有列表页，再逐个获取详情页（推荐此方法）
        page_nums = re.findall(r'page/(\d+)', response.url)
        if not page_nums:
            return
        max_page_num = max(map(int, page_nums))
        next_page_num = max_page_num + 1
        next_url = f'{self.start_urls[0]}/page/{next_page_num}'
        yield response.follow(next_url, callback=self.parse_index)

        # 这个方法是先获取一本书的列表页再拿详情页，需要打开两次浏览器（不推荐）
        # match = re.search(r'page/(\d+)', response.url)
        # if not match:
        # page_num = int(match.group(1)) + 1
        # next_url = f'{self.start_urls[0]}/page/{page_num}'
        # yield scrapy.Request(url=next_url, callback=self.parse_index)

    def parse_detail(self, response):
        name = response.css('.name::text').get()
        tags = response.css('.tags button span::text').getall()
        score = response.css('.score::text').get()
        cover = response.css('.cover img::attr(src)').get()
        price = response.css('.price span::text').get()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        item = ScrapyseleniumdemoItem(name=name, tags=tags, score=score, cover=cover, price=price)
        yield item
