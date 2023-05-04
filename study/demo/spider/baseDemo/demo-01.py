import requests, re, logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = 'https://ssr1.scrape.center/'
TOTAL_PAGE = 10
logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s:-%(message)s')


# 列表页
def scrape_page(url):
    logging.info('scraping ... s%', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code: s% while scraping s%', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping s%', url, exc_info=True)


# 详情页
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


#
def parse_index(html):
    pattern = re.compile('<a(.*?)href="(.*?)"(.*?)class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        logging.info('detail urls %s', list(detail_urls))


if __name__ == '__main__':
    main()

"""
在 for 循环中使用 yield 是一种生成器函数的用法。

生成器函数是一种特殊的函数，它可以在运行时暂停执行并返回一个值，然后在需要时再次从暂停的地方继续执行。生成器函数是通过 yield 语句实现这种暂停和继续执行的机制的。

当我们在 for 循环中使用生成器函数时，每次迭代都会执行生成器函数，并获取该函数返回的下一个值。当函数使用 yield 语句时，它会暂停执行并返回一个值，然后等待下一次迭代继续执行。这样就可以逐步产生一个序列而不必一次性将所有值都加载到内存中。

下面是一个简单的示例代码，演示了如何在 for 循环中使用 yield：

python
def generate_numbers(start, end):
    for i in range(start, end):
        yield i

for num in generate_numbers(1, 10):
    print(num)
"""
