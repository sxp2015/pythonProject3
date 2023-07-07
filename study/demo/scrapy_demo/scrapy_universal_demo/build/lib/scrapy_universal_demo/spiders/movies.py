import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyUniversalDemoItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Identity, Compose


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_output = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)


class MoviesSpider(CrawlSpider):
    name = "movies"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]

    rules = (
        Rule(LinkExtractor(restrict_css='.item .name'), callback="parse_detail", follow=True),
        Rule(LinkExtractor(restrict_css='.next'), follow=True),
    )

    def parse_item(self, response):
        item = ScrapyUniversalDemoItem()
        item["name"] = response.css('.item h2::text').get()
        item["cover"] = response.css('.cover::attr(src)').get()
        item["categories"] = response.css('.categories button span::text').getall()
        item["published_at"] = response.css('.info span::text').re_first('(\d{4}-\d{2}-\d{2})\s?上映')
        item["drama"] = response.xpath('//div[contains(@class, "drama")]/p/text()').get().strip()
        item["score"] = response.xpath('//p[contains(@class, "score")]/text()').get().strip()
        # print('【URL】:', response.url)
        yield item
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_detail(self, response):
        loader = MovieItemLoader(item=ScrapyUniversalDemoItem(), response=response)
        loader.add_css('categories', '.categories button span::text')
        loader.add_css('name', '.item h2::text')
        loader.add_css('cover', '.cover::attr(src)')
        loader.add_css('published_at', '.info span::text', re='(\d{4}-\d{2}-\d{2})\s?上映')
        loader.add_xpath('drama', '//div[contains(@class, "drama")]/p/text()')
        loader.add_xpath('score', '//p[contains(@class, "score")]/text()')
        yield loader.load_item()

