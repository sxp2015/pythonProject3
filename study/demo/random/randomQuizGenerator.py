import random, requests
from pathlib import Path
import numpy as np

# 从网络请求数据
# url = 'http://apis.juhe.cn/fapigw/globalarea/areas?key=15de6af29786008b8a0b8eeaf3b23279&country=%E4%B8%AD%E5%9B%BD'
# area_list = requests.get(url).content.decode('utf-8')
# fileObj = open(Path('area_list.txt'), 'w')
# fileObj.write(area_list + '\n')

# 从本地读取
area_content = open(Path('area_list.txt'), 'r').readlines()
# 数据类型转换
area_str = str(area_content)

# 数据切片
sub_start_index = area_str.find('[{')
sub_end_index = area_str.find('}]')
data_content = area_str[sub_start_index + 1: sub_end_index+1]

if data_content.endswith('}'):
    c = data_content.split('},')
    print("c == ", c)
    newArr = []
    for i in c:
        newItem = i + '}'
        newArr.append(newItem)
        print("newItem == ", newItem)

    # print('newArr', newArr)
    print('newArr_length', len(newArr))
# print('content==', data_content)
# print('area_arr==', area_arr)
