# 导入需要用到的Python库
import json

from selenium import webdriver  # 用于模拟浏览器操作
from selenium.common.exceptions import TimeoutException  # 用于处理超时异常
from selenium.webdriver.common.by import By  # 用于指定元素的查找方式
from selenium.webdriver.support import expected_conditions as EC  # 用于指定等待条件
from selenium.webdriver.support.wait import WebDriverWait  # 用于等待元素加载完成
from urllib.parse import urljoin  # 用于处理URL链接
import logging  # 用于输出日志
from os import makedirs
from os.path import exists

RESULTS_DIR = './results'

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 配置日志输出格式和级别
logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s:%(message)s')

# 定义全局变量
INDEX_URL = 'https://spa2.scrape.center/page/{page}'  # 列表页的URL地址
TIME_OUT = 10  # 操作超时时间
TOTAL_PAGE = 10  # 总共爬取多少页

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 初始化浏览器对象和等待对象
browser = webdriver.Chrome(options=options)  # 使用Chrome浏览器进行操作
wait = WebDriverWait(browser, TIME_OUT)


# 定义函数：抓取某个页面
def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)  # 输出日志：开始抓取指定URL的页面
    try:
        browser.get(url)  # 打开指定URL的页面
        wait.until(condition(locator))  # 等待页面中指定的元素出现
    except TimeoutException:  # 如果等待超时，则捕获异常并输出日志
        logging.error('error occurred while scraping %s', url, exc_info=True)


# 定义函数：抓取某个列表页
def scrape_index(page):
    url = INDEX_URL.format(page=page)  # 构造当前页的URL地址
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


# 定义函数：解析某个列表页
def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')  # 查找所有电影名称元素
    for element in elements:
        href = element.get_attribute('href')  # 获取当前电影链接的href属性值
        yield urljoin(INDEX_URL, href)  # 将相对链接转换为完整链接并返回


# 定义函数：抓取某个详情页
def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.TAG_NAME, 'h2'))


# 定义函数：解析某个详情页
def parse_detail():
    url = browser.current_url  # 获取当前页面的URL地址
    name = browser.find_element(By.TAG_NAME, 'h2').text  # 获取电影名称
    categories = [element.text for element in
                  browser.find_elements(By.CSS_SELECTOR, '.categories button span')]  # 获取电影类别
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')  # 获取电影封面图链接
    score = browser.find_element(By.CLASS_NAME, 'score').text  # 获取电影评分
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text  # 获取电影剧情简介

    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data_path, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# 定义整个爬虫的主函数
def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)  # 抓取当前页的内容
            detail_urls = parse_index()  # 解析当前页中所有详情页的链接
            logging.info('details urls %s', list(detail_urls))  # 输出日志：当前页中所有详情页的链接
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)  # 输出日志：开始抓取某个详情页
                scrape_detail(detail_url)  # 抓取当前详情页的内容
                detail_data = parse_detail()  # 解析当前详情页的内容
                logging.info('detail data %s', detail_data)  # 输出日志：当前详情页的内容
                save_data(detail_data)
    finally:
        browser.close()  # 关闭浏览器对象


# 判断当前是否为入口文件，并开始运行爬虫
if __name__ == "__main__":
    main()
