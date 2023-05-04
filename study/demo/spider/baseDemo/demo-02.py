import requests, re, logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')


# 列表页
def scrape_page(url):
    logging.info('scraping ... %s', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code: %s while scraping %s', response.status_code, url)
    except requests.RequestException as e:
        logging.error('error occurred while scraping %s: %s', url, str(e))


# 详情页
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    pattern = re.compile('<a.*?class="name".*?href="(.*?)".*?>')
    items = re.findall(pattern, html)
    detail_urls = [urljoin(BASE_URL, item) for item in items]
    logging.info('get %d detail urls', len(detail_urls))
    return detail_urls


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    cover_pattern = re.compile('class ="item.*?" <img.*? src=(.*?)')


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        if not index_html:
            continue
        try:
            detail_urls = parse_index(index_html)
            logging.info('detail urls %s', detail_urls)
        except Exception as e:
            logging.error('Error occurred while parsing page %d: %s', page, str(e))


if __name__ == '__main__':
    main()
