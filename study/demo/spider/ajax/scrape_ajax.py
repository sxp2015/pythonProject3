#!/usr/bin/python3
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
import pymongo

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

LIMIT = 10

TOTAL_PAGE = 3


def scrape_api(url):
    logging.info('scraping .. %s....', url)
    try:
        response = requests.get(url, verify='./scrape.center.crt')
        if response.status_code == 200:
            print('response == ', response.text)
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)

    except requests.RequestException:
        logging.error('error occurred while scrape %s ', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


MONGODB_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGODB_NAME = 'movies'
MONGODB_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)

db = client['movies']

collection = db['movies']


def sava_data(data):
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        if index_data is None:
            continue
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            sava_data(detail_data)
            logging.info('detail data saved successfully %s', detail_data)


if __name__ == "__main__":
    main()
