import requests, sys, webbrowser, bs4

print('搜索中... ...')
url = 'https://cn.bing.com/search?q=hello'
query_params = ''.join(sys.argv[1:])
res = requests.get(url + query_params)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.b_algo')

# 最少返回5条 Python的min函数是一个内置函数，用于返回一组数字或可迭代对象中的最小值
numOpen = min(5, len(link_elems))

for items in range(numOpen):
    urlToOpen = link_elems[items].select('a')[0]['href']
    print('urlToOpen', str(urlToOpen))
    webbrowser.open(urlToOpen)

# print('link_Elems_content', str(link_elems[0]))
