#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-10 21:34
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : ajax_demo2.py
# @IDE     : PyCharm
# !/usr/bin/python3
# coding:utf-8
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved
#
# @Time    : 2023-05-10 20:01
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : scrape_ajax.py
# @IDE     : PyCharm
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

LIMIT = 10

TOTAL_PAGE = 10


def scrape_api(url):
    """
    获取API数据
    :param url: API URL地址
    :return: 返回API响应的JSON格式数据
    """
    logging.info('正在抓取数据 %s....', url)
    try:
        response = requests.get(url, verify='./scrape.center.crt')
        if response.status_code == 200:
            print('response == ', response.text)
            return response.json()
        logging.error('抓取 %s 失败，状态码：%s', url, response.status_code)

    except requests.RequestException as e:
        logging.error('抓取 %s 失败，错误信息：%s', url, e)


def scrape_index(page):
    """
    获取索引页数据
    :param page: 索引页页码
    :return: 返回索引页响应的JSON格式数据
    """
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


def scrape_detail(id):
    """
    获取电影详情页数据
    :param id: 电影ID
    :return: 返回电影详情页响应的JSON格式数据
    """
    url = DETAIL_URL.format(id=id)
    data = scrape_api(url)
    if data:
        return data.get('data')


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        if index_data is None:
            continue
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            print('获取成功：', detail_data)


if __name__ == "__main__":
    main()
