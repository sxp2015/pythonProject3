import random
from pathlib import Path
import numpy as np

# 从网络请求数据
# url = 'http://apis.juhe.cn/fapigw/globalarea/areas?key=15de6af29786008b8a0b8eeaf3b23279&country=%E4%B8%AD%E5%9B%BD'
# area_list = requests.get(url).content.decode('utf-8')
# fileObj = open(Path('area_list.txt') 'w')
# fileObj.write(area_list + '\n')

# 从本地读取
capitals = {'湖南省': '长沙市', '广东省': '广州市', '江西省': '南昌市',
            '湖北省': '武汉市', '河南省': '郑州市', '河北省': '石家庄市'}

for quizNum in range(35):
    # 定义测试和答案文件
    quizFile = open(f'题目{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'答案{quizNum + 1}.txt', 'w')
    # 定义测试卷头部信息
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
