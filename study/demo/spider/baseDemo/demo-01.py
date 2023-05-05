import logging, re, json, os, requests
from typing import List, Dict
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 2
RESULT_DIR: str = './result'

"""创建存放文件的文件夹"""
os.path.exists(RESULT_DIR) or os.makedirs(RESULT_DIR)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')


# 爬取页面
def scrape_page(url: str) -> str:
    """
    发送 HTTP GET 请求，并返回响应的 HTML 文本
    """
    logging.info('正在爬取... %s', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('请求 %s 时返回了无效的状态码: %s', url, response.status_code)
    except requests.RequestException as e:
        logging.error('请求 %s 时发生了错误: %s', url, str(e))


def scrape_index(page: int) -> str:
    """
    爬取给定 index 页面的 HTML 文本
    """
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html: str) -> List[str]:
    """
    从 index 页面的 HTML 文本中解析出详情页的 URL，并返回详情页 URL 列表
    """
    soup = BeautifulSoup(html, 'html.parser')
    detail_urls = [urljoin(BASE_URL, a['href']) for a in soup.select('a.name[href]')]
    logging.info('获取到 %d 个详情页 URL', len(detail_urls))
    return detail_urls


def scrape_detail(url: str) -> str:
    """
    爬取给定详情页的 HTML 文本
    """
    return scrape_page(url)


def parse_detail(html: str) -> Dict[str, str]:
    """
    从详情页的 HTML 文本中解析出电影/电视剧信息，并返回字典类型的数据
    """
    soup = BeautifulSoup(html, 'html.parser')
    cover = soup.select_one('.item .cover')['src'] if soup.select_one('.item .cover') else None
    name = soup.select_one('h2').text.strip() if soup.select_one('h2') else None
    categories = [span.text.strip() for span in soup.select('.categories button span')] if soup.select(
        '.categories button span') else []
    published_at = re.search(r'(\d{4}-\d{2}-\d{2})\s?上映', html).group(1) if re.search(r'(\d{4}-\d{2}-\d{2})\s?上映',
                                                                                      html) else None
    drama = soup.select_one('.drama p').text.strip() if soup.select_one('.drama p') else None
    score = float(soup.select_one('.score').text.strip()) if soup.select_one('.score') else None

    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


def save_data(data: dict) -> None:
    # 从 data 字典中获取 name 字段值
    name: str = data.get('name')
    # 拼接数据文件路径
    data_path: str = os.path.join(RESULT_DIR, f'{name}.json')
    # 将 data 数据以 JSON 格式写入到数据文件中
    with open(data_path, 'w', encoding='utf-8') as fp:
        # ensure_ascii=False 表示输出中文字符不进行 Unicode 编码
        # indent=2 表示以缩进形式对 JSON 格式进行排版，便于阅读
        json.dump(data, fp, ensure_ascii=False, indent=2)


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        if not index_html:
            continue
        try:
            detail_urls = parse_index(index_html)
            logging.info('获取到 %d 个详情页 URL: %s', len(detail_urls), detail_urls)

            for detail_url in detail_urls:
                detail_html = scrape_detail(detail_url)
                data = parse_detail(detail_html)
                logging.info('获取到电影/电视剧数据: %s', data)
                logging.info('保存数据到Json文件...')
                save_data(data)
                logging.info('数据保存成功')

        except Exception as e:
            logging.error('解析第 %d 页数据时发生错误: %s', page, str(e))


if __name__ == '__main__':
    main()

"""
使用 BeautifulSoup 库解析 HTML：将字符串类型的 HTML 文本转换成 BeautifulSoup 对象，方便根据 HTML 标签、CSS 选择器等方式进行数据的解析。

统一使用类型标注：在函数参数、返回值、变量等处添加类型标注，增加代码的可读性和稳定性。

优化正则表达式：使用原生的字符串字面量来编写正则表达式，避免反斜杠需要转义的问题。另外，在正则表达式中使用非贪婪匹配（.*?）可以提高匹配效率。

优化解析详情页数据的代码：使用 CSS 选择器来获取标签，使代码更加简洁、易读。同时，使用 BeautifulSoup 提供的方法来获取标签的属性值，避免手写正则表达式，代码更加健壮。

strip() 方法是 Python 中字符串对象的内置方法，它的作用是删除字符串开头或结尾的空格或指定字符
"""
