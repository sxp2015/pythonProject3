import scrapy
from ..items import ScrapytutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            item = ScrapytutorialItem()
            item["text"] = quote.css("span.text::text").get()  # 提取名言文本
            item["author"] = quote.css("small.author::text").get()  # 提取作者
            item["tags"] = quote.css("div.tags a.tag::text").getall()  # 提取标签

            # 写入文件
            with open("quotes.txt", "a", encoding="utf-8") as file:
                file.write(f"名言：{item['text']}\n")  # 写入名言
                file.write(f"作者：{item['author']}\n")  # 写入作者
                file.write(f"标签：{', '.join(item['tags'])}\n")  # 写入标签
                file.write("========================\n")

            yield item  # 返回Item对象
        next_page = response.css(".pager .next a::attr(href)").get()  # 提取下一页链接
        next_url = response.urljoin(next_page)  # 构造完整的下一页URL
        yield scrapy.Request(next_url, callback=self.parse)  # 发起下一页的请求，并指定回调函数为parse

        # 与以下方法同样的效果
        # yield {
        #     "text": quote.css("span.text::text").extract_first(),
        #     "author": quote.css("small.author::text").extract_first(),
        #     "tags": quote.css("div.tags a.tag::text").extract(),
        # }

        # text = quote.css("span.text::text").get()
        # author = quote.css("small.author::text").get()
        # tags = quote.css("div.tags a.tag::text").getall()
        #
        # # 输出到控制台
        # print("名言：", text)
        # print("作者：", author)
        # print("标签：", tags)
        # print("========================")
        #
