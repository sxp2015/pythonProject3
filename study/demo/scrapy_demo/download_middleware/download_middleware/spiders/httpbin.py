import scrapy


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org/get"]

    def parse(self, response):
        Response_Text = response.text
        print('Response Text:', Response_Text)
