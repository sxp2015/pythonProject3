import random, requests
from pathlib import Path

# 从网络请求数据
# url = 'http://apis.juhe.cn/fapigw/globalarea/areas?key=15de6af29786008b8a0b8eeaf3b23279&country=%E4%B8%AD%E5%9B%BD'
# area_list = requests.get(url).content.decode('utf-8')
# fileObj = open(Path('area_list.txt'), 'w')
# fileObj.write('area_list = ' + area_list + '\n')

# 从本地读取
area_content = open(Path('area_list.txt'), 'r').readlines()
area_list = list(area_content)

print('area_list', area_list)
print('area_list_len', len(area_list))

for area in area_list:
    print('area', area)

# 遍历城市
# for area in range(area_list):
#     print('area = ', area)

# print("area_list", area_list)

# for area in area_list:
#     # res = str(area).encode('utf-8')
#     print("area = ", area.result)

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate
