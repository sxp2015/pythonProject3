import scrapy
from scrapy import Request
from scrapy.http import FormRequest, JsonRequest


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org/get"]
    # start_urls = ["https://www.httpbin.org/post"]
    # 定义请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.142.86 Safari/537.36 '
    }
    # 定义cookies
    cookies = {'name': 'germey', 'age': 26}

    # 定义要传递的数据
    # data = {'name': 'germey', 'age': '26'}

    def start_requests(self):
        for offset in range(5):
            get_url = self.start_urls[0] + f'?offset={offset}'
            yield Request(url=get_url, headers=self.headers, cookies=self.cookies, callback=self.parse,
                          meta={'offset': offset})

    # def start_requests(self):
    #     yield FormRequest(url=self.start_urls[0], headers=self.headers, cookies=self.cookies, callback=self.parse,
    #                       formdata=self.data)
    #     yield JsonRequest(url=self.start_urls[0], headers=self.headers, cookies=self.cookies, callback=self.parse,
    #                       formdata=self.data)

    def parse(self, response):
        print('response.text:', response.text)
        print('response.url:', response.url)
        print('response.status:', response.status)
        print('response.headers:', response.headers)
        print('response.meta:', response.meta)
        print('response.request:', response.request)
